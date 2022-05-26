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
