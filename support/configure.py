# Configures parameters for data generation and subsequent experiments

import os
import sys
import json

# Static variables (can be replaced by standing data dictionaries)

# List of default configuration variables
config_variables = ["float_precision",
                    "max_coor_value",
                    "num_circle_min",
                    "num_circle_max",
                    "checks_per_plane",
                    "circle_min_radius",
                    "circle_max_radius"]

# Define functions

def config_ask(default_message = True,
               config_args = config_variables):
    """Formats user command line input for configuration details"""
    if default_message:
        print("Enter configuration parameters for the following variables... ")
        config_dictionary = dict()
        for v in config_args:
            config_dictionary.update({v:input("{}: ".format(v))})

        return config_dictionary
    else:
        print(default_message)
        config_dictionary = dict()
        for v in config_args:
            config_dictionary.update({v:input("{}: ".format(v))})

        return config_dictionary
# Define configuration helper class

class helper:
    """Points to configuration file that helps bound experiment parameters without the need for continuous variable waterfalling"""
    def __init__(self, json_path):
        """Will create config file if proposed config does not already exist"""
        self.config_path = json_path
        # Check if configuration file exists, else create
        if os.path.isfile(self.config_path):
            # Read file as json
            with open(self.config_path, "r") as f:
                # The config will is interpreted as a python dict
                self.config = json.load(f)
                f.close()

        else:
            os.makedirs(os.path.dirname(self.config_path), exist_ok = True)
            with open(self.config_path, "w") as f:
                # Create formatted dictionary for configuration
                self.config = config_ask()
                # At this point, we only create the file
                json_temp = json.dumps(self.config, indent=4)
                f.write(json_temp)
                f.close()
