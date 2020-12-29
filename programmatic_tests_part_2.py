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

        em = eventManager.printEventsList(events_lists, "./outputs/3.2.2_test_3.txt")
        EM.emTick(em, 1)
        em = eventManager.printEventsList(events_lists, "./outputs/3.2.2_test_3.txt")

        for event in events_lists:
            EM.dateDestroy(event["date"])
        EM.destroyEventManager(em)


        input_name = "3.2.2_test_3.txt"
        assert_test(filecmp.cmp("./outputs/3.2.2_test_3.txt", "./expected_outputs/3.2.2_test_3.txt"), True,
                    "\nExpected: <a href='/ex02/staging/{STAGING_ID}/expected_outputs/" + input_name + "'>expected_" + input_name + "</a>, but got instead: <a href='/ex02/staging/{STAGING_ID}/outputs/" + input_name + "'>{}</a>".format(
                        input_name))


TESTS = method_list = [getattr(Tests, func) for func in dir(Tests) if
                       callable(getattr(Tests, func)) and not func.startswith("__")]
