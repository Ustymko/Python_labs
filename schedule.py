from group import Group


class Schedule(Group):
    """
    Schedule class, inherits Group class
    """

    def __init__(self, university_name: str, institute_abbreviation: str, branch: str,
                 group_name_and_number: str, lessons_on_each_day: dict):
        """
        Initializes Schedule object
        :param university_name:
        :param institute_abbreviation:
        :param branch:
        :param group_name_and_number:
        :param lessons_on_each_day:
        """
        super().__init__(university_name, institute_abbreviation, branch, group_name_and_number)
        self.__lessons_on_each_day = lessons_on_each_day

    def __str__(self) -> str:
        schedule = ""
        for x in self.__lessons_on_each_day.keys():
            schedule += x + ": "
            for i in self.__lessons_on_each_day.get(x):
                schedule += str(i) + ", "
            schedule_string_list = list(schedule)
            schedule_string_list[len(schedule) - 2] = ";"
            schedule = "".join(schedule_string_list)
        schedule_string_list = list(schedule)
        schedule_string_list[len(schedule) - 2] = "."
        schedule = "".join(schedule_string_list)
        return f"Here you can see the schedule of " + super().__str__() + schedule
