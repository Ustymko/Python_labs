class University:
    """
    University class
    """

    def __init__(self, university_name: str) -> None:
        """
        Initializes university object
        :param university_name:
        """
        self._university_name = university_name

    def __str__(self) -> str:
        return f"university {self._university_name}. "


class Institute(University):
    """
    Institute class, inherits University
    """

    def __init__(self, university_name: str, abbreviation: str, branch: str) -> None:
        """
        Initializes group object
        """
        super().__init__(university_name)
        self._abbreviation = abbreviation
        self._branch = branch

    def __str__(self) -> str:
        return f"{self._abbreviation} institute which is teaching students {self._branch} in " + super().__str__()

    # def get_all_institutes(self):
    #     super().get_all_institutes()


class Group(Institute):
    """
    Group class, inherits Institute class
    """

    def __init__(self, university_name: str, institute_abbreviation: str, branch: str,
                 group_name_and_number: str) -> None:
        """
        Initializes Group object
        :param university_name:
        :param institute_abbreviation:
        :param branch:
        """
        super().__init__(university_name, institute_abbreviation, branch)
        self._name_and_number = group_name_and_number

    def __str__(self) -> str:
        return f"{self._name_and_number} group of " + super().__str__()


class Student(Group):
    """
    Student class, inherits Group class
    """

    def __init__(self, university_name: str, institute_abbreviation: str, branch: str,
                 group_name_and_number: str, full_name: str) -> None:
        """
        Initializes Student object
        :param university_name:
        :param institute_abbreviation:
        :param branch:
        :param group_name_and_number:
        :param full_name:
        """
        super().__init__(university_name, institute_abbreviation, branch, group_name_and_number)
        self._full_name = full_name

    def __str__(self) -> str:
        return f"{self._full_name} is student of " + super().__str__()

    def how_is_the_student(self) -> str:
        return "Check it using progress object"


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


class Progress(Student):
    """
    Progress class, inherits Student class
    """
    def __init__(self, university_name: str, institute_abbreviation: str, branch: str, group_name_and_number: str,
                 full_name: str, middle_mark: float):
        """
        Initializes Progress object
        :param university_name:
        :param institute_abbreviation:
        :param branch:
        :param group_name_and_number:
        :param full_name:
        :param middle_mark:
        """
        super().__init__(university_name, institute_abbreviation, branch, group_name_and_number, full_name)
        self.__middle_mark = middle_mark

    def __str__(self) -> str:
        return super().__str__() + f"His middle mark is {self.__middle_mark}."

    def how_is_the_student(self) -> str:
        if self.__middle_mark == 5:
            return "Unbelievable student!"
        if 4 <= self.__middle_mark < 5:
            return "Very nice student!"
        if 3 <= self.__middle_mark < 4:
            return "Normal student"
        if 2 < self.__middle_mark < 3:
            return "This student must try better!"
        if self.__middle_mark <= 2:
            return "This student is doing really bad :("


def main():
    politech = University("LPNU")
    print(politech)
    ikta = Institute("LPNU", "IKTA", "computer science")
    print(ikta)
    iot11 = Group("LPNU", "IKTA", "computer science", "IoT-11")
    print(iot11)
    student1 = Student("LPNU", "IKTA", "computer science", "IoT-11", "Taras Pavlovych")
    print(student1)
    student1.how_is_the_student()
    dict1 = {"Monday": ("math", "prog"), "Tuesday": ("phys", "math"), "Wednesday": ("prog", "chill")}
    schedule1 = Schedule("LPNU", "IKTA", "computer science", "IoT-11", dict1)
    print(schedule1)
    progress = Progress("LPNU", "IKTA", "computer science", "IoT-11", "Taras Pavlovych", 5)
    print(progress)
    print(progress.how_is_the_student())


if __name__ == "__main__":
    main()
