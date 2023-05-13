import os
import csv
import math
import random
import string
from wind_cleaner import csv_out_path


prediction_time = 604800 # seconds
random_trash_count = 100 # how many randomly placed trash should be added


wind_file = csv_out_path
trash_file = os.getcwd() + "/trash_origins.csv"
pred_file = os.getcwd() + f"/trash_predictions_{prediction_time}s.csv"


class WindVector:
    """
    Represents a two-dimensional wind vector

    @author Jonathan Uhler
    """

    
    def __init__(self, x: float, y: float):
        """
        Constructs a new {@code WindVector} object.

        @param x: float  the strength of the wind in the x direction (m/s).
        @param y: float  the strength of the wind in the y direction (m/s).
        """
        
        self.x = x
        self.y = y


    def __str__(self) -> str:
        """
        Returns a string representation of this {@code WindVector} object.

        @return a string representation of this {@code WindVector} object. The returned value
                is a scientific vector in the form "<x, y>"
        """
        return f"<{self.x} m/s, {self.y} m/s>"


class Trash:
    """
    Represents a piece of trash in the ocean.

    @author Jonathan Uhler
    """
    
    
    def __init__(self, ident: str, num: int, lat: float, lon: float):
        """
        Constructs a new {@code Trash} object.

        @param ident  the unique id for this trash.
        @param num    the number of pieces of trash in this pile.
        @param lat    the starting latitude of this trash [-90, 90).
        @param lon    the starting longitude of this trash [0, 360).
        """
        
        self.ident = ident
        self.num = num
        self.lati = lat
        self.loni = lon
        self.lat = lat
        self.lon = lon


    def update(self, wind: WindVector, delta_t: float) -> None:
        """
        Updates the position of this trash based on the current wind and a time interval.

        @param wind: WindVector  the closest wind vector to this trash (m/s).
        @param delta_t: float    the time to simulate for under the given wind (s).
        """
        
        m_per_lat = 111120
        m_per_lon = m_per_lat * math.cos(self.lat * (180 / math.pi))

        v_lat = wind.y
        v_lon = wind.x

        self.lat += v_lat * (1 / m_per_lat) * delta_t
        self.lon += v_lon * (1 / m_per_lon) * delta_t

        # Handle wrapping around the planet
        if (self.lon < 0):
            self.lon = 359.9
        if (self.lon >= 360):
            self.lon = 0

        if (self.lat <= -90):
            self.lat = -89.9
            if (self.lon >= 180):
                self.lon -= 180
            else:
                self.lon += 180
        if (self.lat >= 90):
            self.lat = 89.9
            if (self.lon >= 180):
                self.lon -= 180
            else:
                self.lon += 180
                


    def __str__(self):
        return f"{self.ident}: x{self.num} @ {self.lat}N {self.lon}E"


def distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculates the distance (in degrees) between two points of latitude and longitude.

    @param lat1  the latitude of the first point.
    @param lon1  the longitude of the first point.
    @param lat2  the latitude of the second point.
    @param lon2  the longitude of the second point.
    """
    
    return math.sqrt(math.pow((lat1 - lat2), 2) + math.pow((lon1 - lon2), 2))



def read_wind_data() -> list:
    with open(wind_file) as f:
        reader = csv.reader(f, delimiter=",")
        rows = [row for row in reader]

        # Cast numbers to floats
        wind_data: list = []
        for r in range(1, len(rows)):
            row = rows[r]
            row[0] = float(row[0])
            row[1] = float(row[1])
            row[2] = float(row[2])
            row[3] = float(row[3])

            wind_data.append(row)
        
        return wind_data


def read_trash_origins() -> list:
    with open(trash_file) as f:
        reader = csv.reader(f, delimiter=",")
        rows = [row for row in reader]

        # Cast numbers to floats
        trash_origins: list = []
        for r in range(1, len(rows)):
            row = rows[r]
            row[2] = float(row[2])
            row[3] = float(row[3])

            trash_origins.append(row)
            
        return trash_origins


def write_predictions(trash_list: list) -> None:
    trash_csv_list: list = [["id", "n", "lati", "loni", "latf", "lonf"]]

    for trash in trash_list:
        # subtract -180 since the NOAA stuff expected long to be [0, 360) and it should really be
        # [-180, 180)
        trash_csv_list.append([trash.ident, trash.num,
                               trash.lati, trash.loni - 180,
                               trash.lat, trash.lon - 180])
    
    with open(pred_file, "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(trash_csv_list)


wind_data: list = None
def nearest(lat: float, lon: float) -> WindVector:
    """
    Finds the nearest wind vector to the given position.

    @param lat: float  the lat (y) position to find the nearest wind vector to.
    @param lot: float  the lon (x) position to find the nearest wind vector to.

    @return the nearest wind vector to the given lat, lon position. If the given coordinates
            are too far from any wind position, the wind vector <0, 0> is returned. This may
            also be returned if the actual closest vector is <0, 0>
    """

    global wind_data
    if (wind_data == None):
        wind_data = read_wind_data()

    shortest_dist: float = 1000
    wind_x: float = 0
    wind_y: float = 0
    
    for row in wind_data:
        wind_lat: float = row[0]
        wind_lon: float = row[1]
        dist: float = distance(lat, lon, wind_lat, wind_lon)

        if (dist < shortest_dist):
            shortest_dist = dist
            wind_x = row[2]
            wind_y = row[3]
    
    return WindVector(wind_x, wind_y)


def main():
    trash_origins = read_trash_origins()
    trash_list: list = []

    # Add real world trash
    for origin in trash_origins:
        # +180 really hacky since this code (and NOAA wind stuff) expected longitude to be [0, 360)
        trash_list.append(Trash(origin[0], origin[1], origin[2], origin[3] + 180))

    # Add the random trash
    for i in range(random_trash_count):
        random_id = ''.join(random.choices(string.digits, k=6))
        random_num = random.choice([random.randint(5, 15)] * 4 + [random.randint(15, 100)])
        random_lat = random.uniform(-89.0, 89.0)
        random_lon = random.uniform(1.0, 359.0)
        trash_list.append(Trash(random_id, random_num, random_lat, random_lon))

    # Simulate
    time_interval: int = 300 # seconds
    iterations: int = int(prediction_time / time_interval)
    for i in range(iterations):
        if (i % 100 == 0):
            print(f"iteration {i}/{iterations} ({'%.2f' % (i/iterations*100)}%)")
        
        for trash in trash_list:
            wind: WindVector = nearest(trash.lat, trash.lon)
            trash.update(wind, time_interval)

    # Write results to file
    write_predictions(trash_list)


if (__name__ == "__main__"):
    main()
