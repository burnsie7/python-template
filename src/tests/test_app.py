from helpers.WidgetHelper import WidgetHelper

"""Note on pytest and imports:
   1. Include an __init__.py file in the tests directory.
   2. pytests will walk up the file system until it finds
      a directory that does not have __init__.py
   3. This is the root directory for imports

"""


# Confirm the WidgetHelper returns the name given
def test_widget_name():
    widget_helper = WidgetHelper("carl", {})
    assert (widget_helper.name) == "carl"


# Confirm the WidgetHelper returns the name given
def test_widget_data_type():
    widget_helper = WidgetHelper("carl", {})
    assert (type(widget_helper.widgets)) is dict
    return
