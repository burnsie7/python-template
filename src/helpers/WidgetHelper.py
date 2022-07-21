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


class WidgetHelper:
    def __init__(self, name, widgets):
        """Handle widget data"""
        self._name = name
        self.widgets = widgets
        # Q: Do we set queries to something here?
        # self.queries = None or []?

    # Q: When to make something a property vs. an attribute
    @property
    def name(self):
        print("getter method called")
        return self._name
       
    @name.setter
    def name(self, new_name):
        print("setter method called")
        self._name = new_name

    def recursively_find_queries(self, obj):
        queries = []
        if type(obj) is list:
            for o in obj:
                if type(o) is list or type(o) is dict:
                    queries += self.recursively_find_queries(o)
        elif type(obj) is dict:
            for k, v in obj.items():
                if type(v) is list or type(v) is dict:
                    queries += self.recursively_find_queries(v)
                else:
                    if k.lower() == "query":
                        queries.append(v)
        return queries

    def set_queries_inside_class(self):
        self.queries = self.recursively_find_queries(self.widgets)

    def clear_queries_inside_class(self):
        self.queries = None

    def get_widgets(self):
        return self.widgets

    def return_queries_outside_class(self, widgets):
        queries = self.recursively_find_queries(widgets)
        return queries
    
    def get_queries(self):
        return self.queries

    def set_queries(self, queries):
        self.queries = queries

    def __del__(self):
        print("Destructor called")
