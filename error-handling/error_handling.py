def handle_error_by_throwing_exception():
    try:
        1 / 0
    except ZeroDivisionError:
        raise Exception("You can't divide by zero, dummy!")


def handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    except ValueError:
        return None


def handle_error_by_returning_tuple(input_data):
    try:
        raise ValueError
    except ValueError:
        isdigit = input_data.isdigit()
        return isdigit, int(input_data) if isdigit else 0


def filelike_objects_are_closed_on_exception(filelike_object):
    with filelike_object:
        filelike_object.do_something()
