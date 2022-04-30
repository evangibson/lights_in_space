from support import geo
from support import configure
import os
import datetime
import random
import json
import timeit
import multiprocessing

#%% Static variables

continuation_lock = True

# Load or create configuration
config_local = configure.helper(os.path.join("config", "static.json"))

# max x and y value for coordinate place. Minimum is zero
max_coor_value = float(config_local.config['max_coor_value'])

# Lowest number of circles allowed in each plane
num_circle_min = int(config_local.config['num_circle_min'])

# Highest number of allowed circles
num_circles_max = int(config_local.config['num_circle_max'])

# Lowest circle radius
radius_min = float(config_local.config['circle_min_radius'])

# minimum x value
min_x_ = 0 + radius_min

# minimum y value
min_y_ = 0 + radius_min

# num of points in planes
mc_points = int(config_local.config['checks_per_plane'])

# Number of scenarios to generate
num_planes = int(config_local.config['num_planes_per_file'])

# For multiprocessing
cores_use = int(config_local.config['cores_use'])

# machine's outfile
outfile_hier = str(config_local.config['outfile_directory'])

#%% Define assistant functions
def create_circle(max_x,
                  max_y,
                  min_x,
                  min_y,
                  min_radius):
    """Attempts to create a circle matching the given parameters"""

    # To generate floats between range, use uniform
    redu_x = random.uniform(min_x, max_x)
    redu_y = random.uniform(min_y, max_y)

    # Produce a random radius (cannot make circle touch or exceed edges of plane)
    # Assume min is 0

    # In other words, we are finding the x and y distances to the edge of the plane (4 values)
    x_up = max_x - redu_x
    x_down = max_x - x_up  # can be derived by getting the opposite side of the line from our center axis
    y_up = max_y - redu_y
    y_down = max_y - y_up  # We determine minimums at zero

    # This is the largest number the radius can be
    radius_max = min([x_up, x_down, y_up, y_down])

    # Convert the number back to a float
    radius = random.uniform(min_radius, radius_max)

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
def main(core_use):


    # Area of the overall fenced area
    area_fence = max_coor_value**2 # Area of a square

    # Create a plane container object
    plane_dict = dict()

    # Do loop for plane generation
    for c in range(num_planes):

        # Naming convention for planes
        plane_name = "plane_{}".format(str(c))

        # Determine how many circles exist in this plane
        temp_num_cirs = random.randint(num_circle_min, num_circles_max)

        # Placeholder for circle generation
        cir_null = 0

        # List of circles in plane
        circles_list = []
        while temp_num_cirs > cir_null:
            cir_null += 1
            # generate a random circle within boundaries established in config
            circle_temp = create_circle(max_coor_value,
                                        max_coor_value,
                                        min_x_,
                                        min_y_,
                                        radius_min)

            # Add an interpretted dictionary to the list
            circles_list.append({"x": circle_temp[0],
                                 "y": circle_temp[1],
                                 "r": circle_temp[2]})

        # Compute area for circles on the plane
        temp_area = monte_carlo_plane(circles_list,
                                      mc_points,
                                      max_coor_value - radius_min,
                                      max_coor_value - radius_min,
                                      min_x_,
                                      min_y_)

        # Add list and area to plane dictionary
        plane_dict.update({plane_name: {"plane": circles_list, "area": temp_area}})

    # Store timestamp info as string, also save core in use
    timing = dict({"year": datetime.datetime.now().year,
                   "day": datetime.datetime.now().day,
                   "month": datetime.datetime.now().month,
                   "hour": datetime.datetime.now().hour,
                   "minute": datetime.datetime.now().minute,
                   "core": core_use})

    date_string = "{year}_{day}_{month}_{hour}_{minute}_{core}".format(**timing)

    # store config and run info within dictionary
    plane_dict.update({"config": config_local.config})
    plane_dict.update({"timestamp": date_string})

    # Declare filename for output
    outfile = os.path.join(outfile_hier, "{}.json".format(date_string))

    if os.path.isfile(outfile):
        # Read file as json
        with open(outfile, "w") as f:
            # At this point, we only create the file
            json_temp = json.dumps(plane_dict, indent=4)
            f.write(json_temp)
            f.close()

    else:
        os.makedirs(os.path.dirname(outfile), exist_ok=True)
        with open(outfile, "w") as f:
            # At this point, we only create the file
            json_temp = json.dumps(plane_dict, indent=4)
            f.write(json_temp)
            f.close()

#%% Execute main

if __name__ == "__main__":
    tic = timeit.default_timer()
    iteration_count = 0

    # Locks the script to run until interupted
    while continuation_lock:
        iteration_count += 1
        pool = multiprocessing.Pool()
        pool.map(main, range(0, cores_use))
        pool.close()
        toc = timeit.default_timer()

        sys.stdout.write("\033[K")  # Cursor up one line
        print("Elapsed time: {}  Current Iteration: {}".format((toc - tic), iteration_count), end="\r")

