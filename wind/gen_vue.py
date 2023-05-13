import csv
from wind_predictor import pred_file
from wind_predictor import distance


screen_width = 1920
screen_height = 980
px_per_deg_lon = int(screen_width / 360)
px_per_deg_lat = int(screen_height / 180)


def generate_vue_components() -> list:
    with open(pred_file) as f:
        reader = csv.reader(f, delimiter=",")
        rows = [row for row in reader]

        components = "["
        for r in range(1, len(rows)):
            row = rows[r]
            
            id = row[0]
            n = int(row[1])
            lati = float(row[2])
            loni = float(row[3])
            latf = float(row[4])
            lonf = float(row[5])

            xi = int(loni + 180) * px_per_deg_lon
            yi = int(-lati + 90) * px_per_deg_lat
            xf = int(lonf + 180) * px_per_deg_lon
            yf = int(-latf + 90) * px_per_deg_lat

            s = int(max(n, 10) / 2)

            components += "{" + \
                f"id:\"{id}\"," + \
			    f"n:\"{n}\"," + \
			    f"lat:\"{'%.4f' % lati}\"," + \
			    f"lon:\"{'%.4f' % loni}\"," + \
			    f"x:\"{xi}px\"," + \
			    f"y:\"{yi}px\"," + \
			    f"x7:\"{xf}px\"," + \
			    f"y7:\"{yf}px\"," + \
			    f"s:\"{s}px\"" + \
                "}"

            if (r < len(rows) - 1):
                components += ","

        components += "]"
        return components


if (__name__ == "__main__"):
    components = generate_vue_components()
    print(components)
