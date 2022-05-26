from student import Student


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
