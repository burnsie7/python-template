def format_message(self, level, *args):
    msg = level.upper() + ": "
    for arg in args:
        msg += " - {}".format(arg)
    return msg
