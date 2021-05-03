import timeit
import sys

tic = timeit.default_timer()


with open("Z://data_share/coordinates/100_100_01_coordinates_b.csv", "w") as c:
    # Write header
    row = "{},{}\n".format("x","y")
    c.write(row)
    for x in range(10000):
        for y in range(10000):
            row = "{},{}\n".format(x*0.01, y*0.01)  # DO
            c.write(row)
            print("Progress: {},{}".format(x*0.01, y*0.01), end="\r")
            sys.stdout.write("\033[K")  # Cursor up one line


toc = timeit.default_timer()
print("Elapsed time: {}".format(toc-tic))