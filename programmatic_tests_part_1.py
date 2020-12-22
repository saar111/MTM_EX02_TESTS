import os

import eventManager


def runYoungStudentsWithInputName(input_file_name, k):
    input_file_path = "./inputs/{}".format(input_file_name)
    output_file_path = "./outputs/{}".format(input_file_name)
    return eventManager.printYoungestStudents(input_file_path, output_file_path, k)

def runCorrectAgeAvgWithInputName(input_file_name, semester):
    input_file_path = "./inputs/{}".format(input_file_name)
    return eventManager.correctAgeAvg(input_file_path, semester)

class Tests(object):
    @staticmethod
    def testYoungStudentsNegativeKReturnsMinus1():
        input_file_name = "3.1.2.1_young_students_negative_k.txt"
        output_file_path = "./outputs/{}".format(input_file_name)

        assert runYoungStudentsWithInputName(input_file_name, -1) == -1
        assert not os.path.exists(output_file_path), "File should not be created for negative k"

        assert runYoungStudentsWithInputName(input_file_name, 0) == -1
        assert not os.path.exists(output_file_path), "File should not be created for negative k"

    @staticmethod
    def testYoungStudentsBasicUsageReturnsCorrectNumber():
        input_file_name = "3.1.2.1_young_students_basic_1_k_3.txt"
        assert runYoungStudentsWithInputName(input_file_name, 3) == 3

        input_file_name = "3.1.2.1_young_students_basic_2_k_4.txt"
        assert runYoungStudentsWithInputName(input_file_name, 4) == 2
        assert runYoungStudentsWithInputName(input_file_name, 3) == 2
        assert runYoungStudentsWithInputName(input_file_name, 2) == 2
        assert runYoungStudentsWithInputName(input_file_name, 8) == 2
        assert runYoungStudentsWithInputName(input_file_name, 1) == 1

    @staticmethod
    def testYoungStudentsNoYoungestReturns0():
        input_file_name = "3.1.2.1_young_students_no_students_valid_k_1.txt"
        assert runYoungStudentsWithInputName(input_file_name, 1) == 0

    @staticmethod
    def testYoungStudentsManyWrongStudentsAndGenerallyShit():
        input_file_name = "3.1.2.1_young_students_many_wrong_students_and_generally_shit_k_100000.txt"
        assert runYoungStudentsWithInputName(input_file_name, 10000) == 20
        assert runYoungStudentsWithInputName(input_file_name, 17) == 17
        assert runYoungStudentsWithInputName(input_file_name, 10) == 10

    @staticmethod
    def testCorrectAgeAvgBasicUsage():
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_basic_1.txt", 1) == (20 + 23) / 2.0
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_basic_1.txt", 2) == (19 + 17) / 2.0
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_basic_1.txt", 3) == 18
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_basic_1.txt", 4) == 16

    @staticmethod
    def testCorrectAgeAvgSemestersWithNoStudentsReturns0():
        input_ = "3.1.2.2_correct_avg_basic_1.txt"
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_basic_1.txt", 5) == 0
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_basic_1.txt", 6) == 0
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_basic_1.txt", 9) == 0

    @staticmethod
    def testCorrectAgeAvgInvalidSemesterReturnsMinus1():
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_basic_1.txt", -1) == -1
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_basic_1.txt", 0) == -1
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_basic_1.txt", -6) == -1

    @staticmethod
    def testCorrectAgeAvgMegaShitstormTest():
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 1) == 37.285714285714285, runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 1)
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 2) == 18, runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 2)
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 3) == 31, runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 3)
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 4) == 19.333333333333332, runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 4)
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 5) == 18, runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 5)
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 6) == 0, runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 6)
        assert runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 15) == 20, runCorrectAgeAvgWithInputName("3.1.2.2_correct_avg_shitstorm_test.txt", 15)





TESTS = method_list = [getattr(Tests, func) for func in dir(Tests) if
                       callable(getattr(Tests, func)) and not func.startswith("__")]
