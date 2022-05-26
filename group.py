from institute import Institute


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
