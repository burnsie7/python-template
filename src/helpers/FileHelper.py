import logging
import json
import os
import pprint

from os.path import join, dirname

from src.utils import create_message

logger = logging.getLogger("app_logger")


class FileHelper:
    def __init__(self):
        """Read data from a file, perform some actions, write data to file"""

    def get_relative_file_path(self, file_dir, file_name):
        file_path = None
        relative_file_path = None
        if file_dir.endswith("/"):
            file_path = file_dir + file_name
        else:
            file_path = file_dir + "/" + file_name
        relative_file_path = os.path.join(os.path.dirname(__file__), file_path)
        if os.path.isfile(relative_file_path):
            return relative_file_path
        logger.error("Invalid file path: {}".format(relative_file_path))
        return None

    def read_json_file(self):
        """Read JSON from file. ENV VARS existence is validated by app"

        Return: JSON object
        """
        input_dir = os.getenv("INPUT_DIR", None)
        input_file = os.getenv("INPUT_FILE", None)
        input_path = self.get_relative_file_path(input_dir, input_file)
        with open(input_path, "rt") as json_file:
            json_data = json.load(json_file)
        return json_data

    def write_json_file(self, json_data):
        """Write JSON to file. ENV VARS existence is validated by app"

        Return: Path to file
        """
        output_dir = os.getenv("output_DIR", None)
        output_file = os.getenv("output_FILE", None)
        output_path = self.get_relative_file_path(output_dir, output_file)
        with open(output_path, "wt") as output:
            json.dump(json_data, output, sort_keys=True, indent=4, separators=(",", ": "))

    def __del__(self):
        logger.info("Destructor called")
