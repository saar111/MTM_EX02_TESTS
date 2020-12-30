import eventManager
import event_manager as EM
import filecmp


def assert_test(received_value, expected_value, error_message=None):
    if error_message == None:
        error_message = "(Wrong value was: {})".format(received_value)

    assert received_value == expected_value, error_message


class Tests(object):
    @staticmethod
    def testSegelProvidedTest():
        events_lists = [{"name": "New Year's Eve", "id": 1, "date": EM.dateCreate(30, 12, 2020)}, \
                        {"name": "annual Rock & Metal party", "id": 2, "date": EM.dateCreate(21, 4, 2021)}, \
                        {"name": "Improv", "id": 3, "date": EM.dateCreate(13, 3, 2021)}, \
                        {"name": "Student Festival", "id": 4, "date": EM.dateCreate(13, 5, 2021)}, ]
        em = eventManager.printEventsList(events_lists, "./outputs/3.2.2_test_1.txt")
        for event in events_lists:
            EM.dateDestroy(event["date"])
        EM.destroyEventManager(em)

        input_name = "3.2.2_test_1.txt"
        assert_test(filecmp.cmp("./outputs/3.2.2_test_1.txt", "./expected_outputs/3.2.2_test_1.txt"), True,
                    "\nExpected: <a href='/ex02/staging/{STAGING_ID}/expected_outputs/" + input_name + "'>expected_" + input_name + "</a>, but got instead: <a href='/ex02/staging/{STAGING_ID}/outputs/" + input_name + "'>{}</a>".format(
                        input_name))

    @staticmethod
    def testsPrintEventsListFunctionsWith2SameEarliestDates():
        events_lists = [{"name": "New Year's Eve", "id": 1, "date": EM.dateCreate(30, 12, 2020)}, \
                        {"name": "annual Rock & Metal party", "id": 2, "date": EM.dateCreate(21, 4, 2021)}, \
                        {"name": "Improv", "id": 3, "date": EM.dateCreate(13, 3, 2009)}, \
                        {"name": "Student Festival", "id": 4, "date": EM.dateCreate(13, 3, 2009)}]
        em = eventManager.printEventsList(events_lists, "./outputs/3.2.2_test_2.txt")
        for event in events_lists:
            EM.dateDestroy(event["date"])
        EM.destroyEventManager(em)

        input_name = "3.2.2_test_2.txt"
        assert_test(filecmp.cmp("./outputs/3.2.2_test_2.txt", "./expected_outputs/3.2.2_test_2.txt"), True,
                    "\nExpected: <a href='/ex02/staging/{STAGING_ID}/expected_outputs/" + input_name + "'>expected_" + input_name + "</a>, but got instead: <a href='/ex02/staging/{STAGING_ID}/outputs/" + input_name + "'>{}</a>".format(
                        input_name))

    @staticmethod
    def testPrintEventListFindsEarliestDateCorrectly():
        events_lists = [{"name": "Event1", "id": 1, "date": EM.dateCreate(1, 1, 2000)},
                        {"name": "Event6", "id": 6, "date": EM.dateCreate(6, 1, 2003)},
                        {"name": "Event4", "id": 4, "date": EM.dateCreate(4, 1, 2000)},
                        {"name": "Event5", "id": 5, "date": EM.dateCreate(5, 1, 1998)},
                        {"name": "Event3", "id": 3, "date": EM.dateCreate(3, 1, 2000)},
                        {"name": "Event2", "id": 2, "date": EM.dateCreate(2, 1, 2000)}]

        em = eventManager.printEventsList(events_lists, "./outputs/3.2.2_test_3_STUB.txt")
        EM.emTick(em, 1)
        EM.emPrintAllEvents(em, "./outputs/3.2.2_test_3.txt")

        for event in events_lists:
            EM.dateDestroy(event["date"])
        EM.destroyEventManager(em)

        input_name = "3.2.2_test_3.txt"
        assert_test(filecmp.cmp("./outputs/3.2.2_test_3.txt", "./expected_outputs/3.2.2_test_3.txt"), True,
                    "\nExpected: <a href='/ex02/staging/{STAGING_ID}/expected_outputs/" + input_name + "'>expected_" + input_name + "</a>, but got instead: <a href='/ex02/staging/{STAGING_ID}/outputs/" + input_name + "'>{}</a>".format(
                        input_name))
        @staticmethod
    def testPrintBigEventList():
        events_lists = [{"name": "Event1", "id": 1, "date": EM.dateCreate(1, 1, 2020)},
                        {"name": "Event6", "id": 6, "date": EM.dateCreate(6, 1, 2020)},
                        {"name": "Event4", "id": 4, "date": EM.dateCreate(4, 1, 2020)},
                        {"name": "Event5", "id": 5, "date": EM.dateCreate(5, 1, 1920)},
                        {"name": "Event3", "id": 3, "date": EM.dateCreate(6, 1, 1998)},
                        {"name": "Event2", "id": 2, "date": EM.dateCreate(2, 12, 2001)},
                        {"name": "Event7", "id": 7, "date": EM.dateCreate(3, 1, 1998)},
                        {"name": "Event8", "id": 8, "date": EM.dateCreate(4, 1, 1998)},
                        {"name": "Matam (shit)", "id": 9, "date": EM.dateCreate(19, 2, 2020)},
                        {"name": "Event10", "id": 10, "date": EM.dateCreate(2, 1, 1920)},
                        {"name": "Event11", "id": 11, "date": EM.dateCreate(3, 1, 1920)},
                        {"name": "Event12", "id": 12, "date": EM.dateCreate(4, 1, 1920)},
                        {"name": "Event13", "id": 13, "date": EM.dateCreate(5, 1, 1920)},
                        {"name": "Event14", "id": 14, "date": EM.dateCreate(6, 1, 1920)},
                        {"name": "Event15", "id": 15, "date": EM.dateCreate(7, 1, 1920)},
                        {"name": "Event16", "id": 16, "date": EM.dateCreate(8, 1, 1920)},
                        {"name": "Event17", "id": 17, "date": EM.dateCreate(9, 1, 1920)},
                        {"name": "Event18", "id": 18, "date": EM.dateCreate(11, 1, 1920)},
                        {"name": "SpanishFlu (corona ? yes please)", "id": 19, "date": EM.dateCreate(30, 12, 1919)},
                        {"name": "WW3", "id": 20, "date": EM.dateCreate(30, 12, 1919)},
                        {"name": "WW4? damn son", "id": 21, "date": EM.dateCreate(29, 12, 1919)}]

        em = eventManager.printEventsList(events_lists, "./outputs/3.2.2_test_4.txt")

        for event in events_lists:
            EM.dateDestroy(event["date"])
        EM.destroyEventManager(em)

        input_name = "3.2.2_test_4.txt"

        assert_test(filecmp.cmp("./outputs/3.2.2_test_4.txt", "./expected_outputs/3.2.2_test_4.txt"), True,
                    "\nExpected: <a href='/ex02/staging/{STAGING_ID}/expected_outputs/" + input_name + "'>expected_" + input_name + "</a>, but got instead: <a href='/ex02/staging/{STAGING_ID}/outputs/" + input_name + "'>{}</a>".format(
                        input_name))



TESTS = method_list = [getattr(Tests, func) for func in dir(Tests) if
                       callable(getattr(Tests, func)) and not func.startswith("__")]
