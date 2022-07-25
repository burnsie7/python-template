class ListFlattener:
    """Recursively flatten lists while preventing additive lists or endless recursion"""

    def __init__(self):
        self.__flat_list = []

    def __recursively_flatten_list(self, obj):
        if type(obj) is list:
            for o in obj:
                self.__recursively_flatten_list(o)
        else:
            self.__flat_list.append(obj)

    def flatten_list_of_lists(self, obj):
        self.__flat_list = []
        self.__recursively_flatten_list(obj)
        return self.__flat_list


def recursively_find_matches(obj, matches):
    matched = []
    if type(obj) is list:
        for o in obj:
            if type(o) is list or type(o) is dict:
                matched += recursively_find_matches(o, matches)
    elif type(obj) is dict:
        for k, v in obj.items():
            if k in matches:
                matched.append(v)
            elif type(v) is list or type(v) is dict:
                matched += recursively_find_matches(v, matches)
    else:
        print("Unexpected object type: {}".format(object))
    return matched


def format_message(self, level, *args):
    msg = level.upper() + ": "
    for arg in args:
        msg += " - {}".format(arg)
    return msg
