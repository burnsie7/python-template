import os

import coloredlogs
import json
import logging
import pprint
import sys
from dotenv import load_dotenv

from datetime import datetime
from helpers.WidgetHelper import WidgetHelper
from src.const import REQUIRED_VARS

# TODO: wrap logger
# FILE_LOCATION = "helpers.WidgetHelper"
# wrapped_logger(level, FILE_LOCATION, utils.format_message(functionName, msg, data))


#  Example data
WIDGET_HOLDER = {
    "title": "Widget Holder",
    "description": "I hold widgets",
    "widgets": [
        {
            "id": 1,
            "title": "The First Widget",
            "definition": {
                "type": "cog",
                "requests": [
                    {
                        "queries": [
                            {
                                "data_source": "sql",
                                "query": "SELECT cogs " "FROM " "parts;"
                            }
                        ]
                    }
                ],
            },
        },
        {
            "id": 2,
            "title": "The Second Widget",
            "definition": {
                "type": "action",
                "query": '"Hello World"',
                "columns": [
                    "department",
                    "service"
                ],
                "data_source": "file",
                "indexes": [],
                "sort": {
                    "column": "time"
                },
            },
        },
    ],
}

NOT_WIDGET_HOLDER = ["i", "am", "a", "list"]

class AppClass:
    def __init__(self):
        self.initializer()

    def initializer(self, dry_run=True):
        """
        Initialise the Template class with the proper env variable
        either loaded from the default .env.

        :param dry_run: Whether or not this should have no consequences or not

        """
        logger.debug("Launching initialize")

        # Default to True
        if os.getenv("DRY_RUN", default=dry_run) == "False":
            self.dry_run = False
            logger.warning("Dry run mode is not activated, operations WILL HAVE consequences")
        else:
            self.dry_run = True
            logger.info("Dry run mode is activated, all operations will have NO consequences")

    def init_widget_helper(self, name, data):
        """
        Inits Helper
        """
        logger.debug("init widget")
        self.widget_helper = WidgetHelper(name, data)

    def use_widget_helper(self):
        """
        Use Helper
        """
        return self.widget_helper.use()

    def __del__(self):
        logger.info("Destructor called")


def validate_required_vars():
    """Validate that the required env vars are present"""
    is_valid = True
    for v in REQUIRED_VARS:
        temp = os.getenv(v, None)
        if temp is None:
            logger.warn("Missing required var: {}".format(v))
            is_valid = False
    return is_valid


if __name__ == "__main__":

    ## Loads the .env file for work happening locally
    ## If no env file are found we rely on env variables passed directly

    date_now = str(datetime.now().strftime("%Y-%m-%d---%H:%M"))

    logger = logging.getLogger("app_logger")
    coloredlogs.install(fmt="%(levelname)s %(message)s", level="DEBUG", logger=logger)
    logger.info("{} - Starting application".format(date_now))

    dotenv_path_local = os.path.join(os.path.dirname(__file__), "../../.env")

    if os.path.isfile(dotenv_path_local):
        logger.info("Local env file found")
        load_dotenv(dotenv_path_local)
    else:
        logger.warning("No local env file found, fall back on global env variable")

    if validate_required_vars():
        logger.info("All required vars exist.")
    else:
        logger.warn("Please confirm all required env vars exist")
        exit(0)

    ## Initialize AppClass
    app = AppClass()

    name = "my_widget_helper"
    app.init_widget_helper(name, WIDGET_HOLDER)

    # Get and Set
    logger.info(app.widget_helper.name)
    app.widget_helper.name = "new_widget_helper"
    logger.info(app.widget_helper.name)

    # Set queries inside class
    app.widget_helper.flatten_queries_from_widgets()
    logger.info(app.widget_helper.queries)

    exit(0)
