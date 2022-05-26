from group import Group


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
