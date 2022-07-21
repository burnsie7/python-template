import logging
import json
import os
import pprint

from os.path import join, dirname

from src.utils import create_message

FILE_LOCATION = "subdir.ClassDef"

logger = logging.getLogger("app_logger")


def logDebug(functionName, msg, data):
    logger.debug("DEBUG: {}.{} - {} - {}".format(FILE_LOCATION, functionName, msg, data))


def logInfo(functionName, msg, data):
    logger.info("INFO: {}.{} - {} - {}".format(FILE_LOCATION, functionName, msg, data))


def logWarn(functionName, msg, data):
    logger.info("Warn: {}.{} - {} - {}".format(FILE_LOCATION, functionName, msg, data))


def logError(functionName, msg, data):
    logger.error("ERROR: {}.{} - {} - {}".format(FILE_LOCATION, functionName, msg, data))


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
        logError("get_relative_file_path", "Invalid file path", relative_file_path)
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
        print("Destructor called")
