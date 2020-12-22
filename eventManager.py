#### IMPORTS ####
# import event_manager as EM


#### PART 1 ####

ID_INDEX = 0
NAME_INDEX = 1
AGE_INDEX = 2
BIRTH_YEAR_INDEX = 3
SEMESTER_INDEX = 4

CURRENT_YEAR = 2020


# Filters a file of students' subscription to specific event:
#   orig_file_path: The path to the unfiltered subscription file
#   filtered_file_path: The path to the new filtered file
def fileCorrect(orig_file_path: str, filtered_file_path: str):
    with open(orig_file_path) as in_file:
        entries = createAndNormalizeEntries(in_file.read())

    with open(filtered_file_path, "w") as out_file:
        out_file.write(stringifyEntries(entries))


def stripExcessSpaces(string: str) -> str:
    string = string.strip()
    string = ' '.join(string.split())
    return string


def isEntryLegal(entry: list) -> bool:
    if len(entry[ID_INDEX]) != 8 or entry[ID_INDEX][0] == '0':
        return False
    if not "".join(entry[NAME_INDEX].split(" ")).isalpha():
        return False
    if not (16 <= int(entry[AGE_INDEX]) <= 120):
        return False
    if not CURRENT_YEAR - int(entry[BIRTH_YEAR_INDEX]) == int(entry[AGE_INDEX]):
        return False
    if not int(entry[SEMESTER_INDEX]) >= 1:
        return False

    return True


def removeIllegalEntries(entries: list):
    for entry in list(entries):
        if not isEntryLegal(entry):
            entries.remove(entry)


def removeDuplicates(entries: list):
    entries.reverse()
    seen_ids = {}
    for entry in list(entries):
        current_id = entry[ID_INDEX]
        if seen_ids.get(current_id):
            entries.remove(entry)

        seen_ids[current_id] = True


def createAndNormalizeEntries(file_data: str) -> list:
    entries = []
    for raw_row_data in file_data.splitlines():
        row_data_fields = raw_row_data.split(",")
        row_data_fields = list(map(stripExcessSpaces, row_data_fields))
        entries.append(row_data_fields)

    removeIllegalEntries(entries)
    removeDuplicates(entries)
    entries.sort(key=lambda row_data: int(row_data[ID_INDEX]))
    return entries


def stringifyEntries(entries: list) -> str:
    entries_str = ""
    for entry in entries:
        entries_str += ", ".join(entry) + '\n'

    return entries_str


# Writes the names of the K youngest students which subscribed
# to the event correctly.
#   in_file_path: The path to the unfiltered subscription file
#   out_file_path: file path of the output file
def printYoungestStudents(in_file_path: str, out_file_path: str, k: int) -> int:
    if k <= 0:
        return -1

    with open(in_file_path) as in_file:
        entries = createAndNormalizeEntries(in_file.read())
        entries.sort(key=lambda entry: int(entry[AGE_INDEX]))

    # TODO: no students empty or new line?
    output_string = ""
    for entry in entries[:k]:
        output_string += entry[NAME_INDEX] + "\n"

    with open(out_file_path, "w") as out_file:
        out_file.write(output_string)


# Calculates the avg age for a given semester
#   in_file_path: The path to the unfiltered subscription file
#   out_file_path: The path to the new filtered file
#   retuns the avg, else error codes defined.
def correctAgeAvg(in_file_path: str, semester: int) -> float:
    if semester <= 0:
        return -1

    with open(in_file_path) as in_file:
        entries = createAndNormalizeEntries(in_file.read())

    semester_entries = list(filter(lambda entry: int(entry[SEMESTER_INDEX]) == semester, entries))
    if len(semester_entries) == 0:
        return 0

    avg = 0.0
    for semester_entry in semester_entries:
        avg += int(semester_entry[AGE_INDEX])

    return avg / len(semester_entries)


#### PART 2 ####
# Use SWIG :)
# print the events in the list "events" using the functions from hw1
#   events: list of dictionaries
#   file_path: file path of the output file
def printEventsList(events: list,
                    file_path: str):  # em, event_names: list, event_id_list: list, day: int, month: int, year: int):
    pass
    pass
    pass
    # TODO


def testPrintEventsList(file_path: str):
    events_lists = [{"name": "New Year's Eve", "id": 1, "date": EM.dateCreate(30, 12, 2020)}, \
                    {"name": "annual Rock & Metal party", "id": 2, "date": EM.dateCreate(21, 4, 2021)}, \
                    {"name": "Improv", "id": 3, "date": EM.dateCreate(13, 3, 2021)}, \
                    {"name": "Student Festival", "id": 4, "date": EM.dateCreate(13, 5, 2021)}, ]
    em = printEventsList(events_lists, file_path)
    for event in events_lists:
        EM.dateDestroy(event["date"])
    EM.destroyEventManager(em)


#### Main ####
# feel free to add more tests and change that section. 
# sys.argv - list of the arguments passed to the python script
if __name__ == "__main__":
    import sys

    fileCorrect(sys.argv[1], "out.txt")
    printYoungestStudents(sys.argv[1], "out2.txt", 3)
    print(correctAgeAvg(sys.argv[1], 2))

    # if len(sys.argv) > 1:
    #     testPrintEventsList(sys.argv[1])
