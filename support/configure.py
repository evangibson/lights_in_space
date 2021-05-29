# Configures parameters for data generation and subsequent experiments

import os
import sys

# Define functions


# Define configuration helper class

class helper:
    """Points to configuration file that helps bound experiment parameters without the need for continuous variable waterfalling"""
    def __init__(self, json_path):
        """Will create config file if proposed config does not already exist"""
        self.config_path = json_path
        # Check if configuration file exists, else create
        if os.path.isfile(self.config_path):
            # Read file as json
            print("FIX")

        else:
            os.makedirs(os.path.dirname(self.config_path), exist_ok = True)
            with open(self.config_path, "w") as f:
                f.write("TEMP")
                f.close()
