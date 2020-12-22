import os

import eventManager

class Tests(object):
    @staticmethod
    def testYoungStudentsNegativeKReturnsMinus1():
        input_file_name = "3.1.2.1_young_students_negative_k.txt"
        input_file_path = "./inputs/{}".format(input_file_name)
        output_file_path = "./outputs/{}".format(input_file_name)

        assert eventManager.printYoungestStudents(input_file_path, output_file_path, -1) == -1
        assert not os.path.exists(output_file_path), "File should not be created for negative k"


TESTS = method_list = [getattr(Tests, func) for func in dir(Tests) if
                       callable(getattr(Tests, func)) and not func.startswith("__")]
