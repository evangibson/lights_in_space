from support import geo
from support import configure
import os
import datetime
import random



#%% Static variables

# Number of scenarios to generate
num_planes = 100

# Number of monte carlo random casting points
mc_points = 100000

#%% Define assiatant functions
def create_circle(max_x, max_y, float_precision_):
    """Attempts to create a circle matching the given parameters"""

    # Use a factor of float precision to create a random point within max and min params. MUST BE REDUCED BEFORE USE
    temp_x = random.randrange(1, stop=max_x * (10 ** float_precision_))
    temp_y = random.randrange(1, stop=max_y * (10 ** float_precision_))

    # Reduced the numbers to their appropriate values
    redu_x = temp_x / 10 ** float_precision_
    redu_y = temp_y / 10 ** float_precision_

    # Produce a random radius (cannot make circle touch or exceed edges of plane)
    # Assume min is 0

    # In other words, we are finding the x and y distances to the edge of the plane (4 values)
    x_up = max_x - redu_x
    x_down = max_x - x_up  # can be derived by getting the opposite side of the line from our center axis
    y_up = max_y - redu_y
    y_down = max_y - y_up # We determine minimums at zero

    # This is the largest number the radius can be
    radius_max = min([x_up, x_down, y_up, y_down])

    # The max radius has to be converted to an integer temporarily to use this random within range function
    radius_big = random.randrange(1, stop=int(round(radius_max * 10 ** float_precision_, 0)))

    # Convert the number back to a float
    radius = radius_big / 10 ** float_precision_

    return redu_x, redu_y, radius


def monte_carlo_plane(list_of_point_dicts, num_points, max_x, max_y, min_x, min_y):
    """Params:
    list_of_points_dicts - [{x:3, y:2, r:3}, {...}, ...]
    num_points - how many random points to cast within area
    total_area - the total area of the plane"""
    # Calculate total area of param box
    total_area = (max_x - min_x) * (max_y - min_y)

    # Will add value for each point within a circle
    running_sum = 0
    for n in range(num_points):
        # generate a random point within the allowable range
        mc_x = random.uniform(min_x, max_x)
        mc_y = random.uniform(min_y, max_y)

        # Check if random coordinate exists within ANY of the circles
        for p in list_of_point_dicts:
            #
            if geo.cir_test(p["x"], p["y"], mc_x, mc_y, p["r"]):
                running_sum += 1
                # Break so we do not double count whether a point occurs within area of venn diagram
                break

            else:
                pass
    # The proportion of hits v total
    prop_hits = running_sum / num_points

    return total_area * prop_hits



#%% Define main function
def main():
    # Load or create configuration
    config_local = configure.helper(os.path.join("config", "static.json"))

    # Decimal places for rounding functions
    float_precision = config_local.config["float_precision"]

    # max x and y value for coordinate place. Minimum is zero
    max_coor_value = config_local.config['max_coor_value']

    # Lowest number of circles allowed in each plane
    num_circle_min = config_local.config['num_circle_min']

    # Highest number of allowed circles
    num_circles_max = config_local.config['num_circles_max']

    # Area of the overall fenced area
    area_fence = max_coor_value**2 # Area of a square

    for c in range(num_planes):
        plane_dict = dict()




    # Store timestamp info as string
    timing = dict({"year": datetime.datetime.now().year,
                   "day": datetime.datetime.now().day,
                   "month": datetime.datetime.now().month,
                   "minute": datetime.datetime.now().minute})

    date_string = "{year}_{day}_{month}_{minute}".format(timing)

    # Declare filename for output
    outfile = os.path.join("data", "{}.json".format(date_string))

#%% Execute main

if __name__ == "__main__":
    main()

