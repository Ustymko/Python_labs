from university import University


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
