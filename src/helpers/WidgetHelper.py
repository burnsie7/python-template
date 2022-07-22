import logging
import json
import os
import pprint

from os.path import join, dirname

logger = logging.getLogger("app_logger")


class WidgetHelper:
    def __init__(self, name, widgets):
        self.name = name
        self.widgets = widgets

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

    def flatten_queries_from_widgets(self):
        self.queries = self.recursively_find_queries(self.widgets)

    def __del__(self):
        logger.info("Destructor called")

