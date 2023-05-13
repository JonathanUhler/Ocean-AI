import os
import csv
import math
from wind_cull import csv_out_path


wind_file = csv_out_path
trash_file = os.getcwd() + "/trash_origins.csv"
pred_file = os.getcwd() + "/trash_paths.csv"


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
    
    
    def __init__(self, ident: str, lat: float, lon: float):
        """
        Constructs a new {@code Trash} object.

        @param ident  the unique id for this trash.
        @param lat    the starting latitude of this trash.
        @param lon    the starting longitude of this trash.
        """
        
        self.ident = ident
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


    def __str__(self):
        return f"{self.ident}: {self.lat}N {self.lon}E"


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
            row[1] = float(row[1])
            row[2] = float(row[2])

            trash_origins.append(row)
            
        return trash_origins


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
    for origin in trash_origins:
        trash_list.append(Trash(origin[0], origin[1], origin[2]))

    time_interval: float = 300 # seconds
    iterations: int = 100
    for i in range(iterations):
        for trash in trash_list:
            wind: WindVector = nearest(trash.lat, trash.lon)
            trash.update(wind, time_interval)

    for trash in trash_list:
        print(trash)


if (__name__ == "__main__"):
    main()
