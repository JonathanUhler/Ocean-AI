import csv
import os


# USER CONSTANTS
resolution = 10 # The resolution of the cleaned data, in degrees
csv_in_name = "uv_wind.csv"
csv_out_name = "wind_final.csv"
# end: USER CONSTANTS


# Include information about the files
csv_in_dir = os.getcwd()
csv_in_path = csv_in_dir + "/" + csv_in_name

csv_out_dir = os.getcwd()
csv_out_path = csv_out_dir + "/" + csv_out_name


# Read CSV data
def read() -> list:
    with open(csv_in_path) as f:
        reader = csv.reader(f, delimiter=",")
        data = [row for row in reader]
        return data


# Write CSV data
def write(data: list) -> None:
    with open(csv_out_path, "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(data)


# Prepare the arrays for read/write
data = read()
cleaned = [["lat", "lon", "x_wind", "y_wind"]]

# Clean the data
last_lat = -90 # The last recorded latitude
last_lon = 0 # The last recorded longitude

for row in data[1:]:
    # Gather data
    lat = row[2]
    lon = row[3]
    x_wind = row[4]
    y_wind = row[5]

    lat_f = float(lat)
    lon_f = float(lon)

    # Conditionally skip on the both the vertical (lat) and horizontal (lon) to create
    # an evenly distributed grid of {@code resolution*resolution} points. This first
    # condition of this statement is responsible for distributing the horizontal
    # points by {@code resolution}. The second statement checks if the data wrapped
    # to a new latitude (e.g. last_lon, which would be close to 359 is now greater
    # than the longitude of the new row, which would be close to 0). If this is true
    # and the latitude is too close to the previously added latitudes (< resolution),
    # then the latitudes can start being skipped.
    if (abs(lon_f - last_lon) < resolution or
        (last_lon > lon_f and abs(lat_f - last_lat) < resolution)):
        continue

    # Check if there is any wind data for this point
    if (len(x_wind) == 0 or len(y_wind) == 0):
        continue

    # Add data as a new row
    last_lat = lat_f
    last_lon = lon_f
    cleaned.append([lat, lon, x_wind, y_wind])


# Write cleaned data
write(cleaned)
