
def assert_test(received_value, expected_value, error_message):
    pass

class Tests(object):
    @staticmethod
    def a():
        pass

TESTS = method_list = [getattr(Tests, func) for func in dir(Tests) if
                       callable(getattr(Tests, func)) and not func.startswith("__")]
