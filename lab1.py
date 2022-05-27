from abc import ABC, abstractmethod
from typing import List
import datetime


class Progress:
    """
    Progress class
    """

    def __init__(self, this_term_middle_mark: float, zno_entrance_mark: float):
        """
        Initializes Progress object
        :param middle_mark:
        """
        self._this_term_middle_mark = this_term_middle_mark
        self._zno_entrance_mark = zno_entrance_mark

    def __str__(self) -> str:
        return f"This term: {self._this_term_middle_mark}, ZNO: {self._zno_entrance_mark}"


class Person(ABC):
    """
    Abstract Person class, inherits ABC library
    """

    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name

    def __str__(self) -> str:
        return f"{self._last_name} {self._first_name}"

    @abstractmethod
    def get_full_name(self) -> str:
        return self._first_name + " " + self._last_name


class Student(Person):
    """
    Student class, inherits Person class
    """

    def __init__(self, first_name: str, last_name: str, year_of_graduation: int, progress: Progress):
        super().__init__(first_name, last_name)
        self._year_of_graduation = year_of_graduation
        self._progress = progress

    def __str__(self) -> str:
        return super().__str__() + f", graduated in {self._year_of_graduation}, marks: " + self._progress.__str__()

    def get_full_name(self) -> str:
        return super().get_full_name()


class Instructor(Person):
    """
    Instructor class, inherits Person class
    """

    def __init__(self, first_name: str, last_name: str, science_degree: str):
        super().__init__(first_name, last_name)
        self._science_degree = science_degree

    def __str__(self):
        return super().__str__() + f" with {self._science_degree}"

    def get_full_name(self) -> str:
        return super().get_full_name()


class Lead(Instructor):
    """
    Class Lead, inherits Instructor class
    """

    def __init__(self, first_name: str, last_name: str, science_degree: str, started_at_position: datetime):
        super().__init__(first_name, last_name, science_degree)
        self.__started_at_position = started_at_position

    def __str__(self):
        return super().__str__() + f" started at {self.__started_at_position}"

    def get_full_name(self) -> str:
        return super().get_full_name()


class Institution(ABC):
    """
    Abstract Institution class, inherits ABC library
    """
    def __init__(self, name: str, people_amount: int):
        self._name = name
        self._people_amount = people_amount

    def __str__(self) -> str:
        return f"{self._name} includes {self._people_amount} people"

    @abstractmethod
    def print_how_massive_it_is(self):
        if self._people_amount > 1000:
            print("Giant!")
        if 500 < self._people_amount < 1000:
            print("Very big")
        if 100 < self._people_amount <= 500:
            print("Not so big actually")
        if 0 < self._people_amount <= 100:
            print("Normal size")


class Schedule:
    """
    Schedule class
    """

    def __init__(self, lessons_on_each_day: dict):
        """
        Initializes Schedule object
        :param lessons_on_each_day:
        """
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
        return schedule


class InstitutionWithPeople(Institution, ABC):
    """
    Abstract InstitutionWithPeople class, inherits Institution class and ABC library
    """
    def __init__(self, name: str, people_amount: int):
        super().__init__(name, people_amount)

    @abstractmethod
    def add_new_member(self, new_member: Person):
        super()._people_amount += 1


class InstitutionWithInstitutions(Institution, ABC):
    """
    Abstract InstitutionWithInstitutions class, inherits Institution class and ABC library
    """
    def __init__(self, name: str, people_amount: int):
        super().__init__(name, people_amount)

    @abstractmethod
    def add_new_institution(self, new_institution: Institution):
        super()._people_amount += 1


class Group(InstitutionWithPeople, Institution):
    """
    Group class, inherits InstitutionWithPeople and Institution classes
    """

    def __init__(self, name: str, people_amount: int, schedule: Schedule, monitor: Student, students: List[Student]):
        super().__init__(name, people_amount)
        self._schedule = schedule
        self._monitor = monitor
        self._students = students

    def __str__(self) -> str:
        return super().__str__() + f", monitor is " + self._monitor.get_full_name()

    def print_how_massive_it_is(self):
        super().print_how_massive_it_is()

    def get_schedule(self):
        return self._schedule.__str__()

    def add_new_member(self, new_student: Student):
        super().add_new_member(new_student)
        self._students.append(new_student)


class Department(InstitutionWithPeople, Institution):
    """
    Department class, inherits InstitutionWithInstitutions and Institution classes
    """

    def __init__(self, name: str, people_amount: int, address: str, instructors: List[Instructor]):
        super().__init__(name, people_amount)
        self._address = address
        self._instructors = instructors

    def __str__(self):
        return f"Address: {self._address} " + super().__str__()

    def print_how_massive_it_is(self):
        super().print_how_massive_it_is()

    def add_new_member(self, new_instructor: Instructor):
        super().add_new_member(new_instructor)
        self._instructors.append(new_instructor)


class Faculty(InstitutionWithInstitutions, Institution):
    """
    Institute class, inherits InstitutionWithInstitutions and Institution classes
    """

    def __init__(self, name: str, people_amount: int, branch: str, groups: List[Group], dean: Lead):
        super().__init__(name, people_amount)
        self._branch = branch
        self._groups = groups
        self._dean = dean

    def __str__(self) -> str:
        return f"{self._branch}, " + super().__str__()

    def print_how_massive_it_is(self):
        super().print_how_massive_it_is()

    def get_all_groups_in_str(self) -> str:
        all_groups = ""
        for x in self._groups:
            all_groups += x.__str__() + "\n"
        return all_groups

    def add_new_institution(self, new_institution: Group):
        self._groups.append(new_institution)


class University(InstitutionWithInstitutions, Institution):
    """
    University class, inherits InstitutionWithInstitutions and Institution classes
    """

    def __init__(self, name: str, people_amount: int, rector: Lead, faculties: List[Faculty]) -> None:
        super().__init__(name, people_amount)
        self._rector = rector
        self._faculties = faculties

    def __str__(self) -> str:
        return f"Rector: {self._rector.get_full_name()}, " + super().__str__()

    def print_how_massive_it_is(self):
        super().print_how_massive_it_is()

    def get_all_faculties_in_str(self) -> str:
        all_faculties = ""
        for x in self._faculties:
            all_faculties += x.__str__()
        return all_faculties

    def add_new_institution(self, new_institution: Faculty):
        self._faculties.append(new_institution)


def main():
    progress_1 = Progress(5, 200)
    student_1 = Student("Taras", "Petryko", 2021, progress_1)
    progress_2 = Progress(4.5, 185)
    student_2 = Student("Vasyl", "Minalo", 2021, progress_2)
    progress_3 = Progress(3, 155)
    student_3 = Student("Stepan", "Andriiv", 2021, progress_3)
    progress_4 = Progress(3.2, 189)
    student_4 = Student("Andrii", "Stepaniv", 2021, progress_4)
    iot11_lessons = {"Mon": ("math", "phys"), "Tue": ("prog", "math"), "Wed": ("discrete", "prog")}
    schedule_iot11 = Schedule(iot11_lessons)
    iot12_lessons = {"Mon": ("math", "phys"), "Tue": ("math", "discrete"), "Wed": ("math", "prog")}
    schedule_iot12 = Schedule(iot12_lessons)
    group_iot_11 = Group("iot-11", 27, schedule_iot11, student_1, [student_1, student_2, student_3, student_4])
    group_iot_12 = Group("iot-12", 27, schedule_iot12, student_2, [student_1, student_2, student_3, student_4])
    rector_politechnic = Lead("Yuriy", "Bobalo", "professor", datetime.datetime(2007, 5, 3))
    prog_teacher = Instructor("Zenoviy", "Veres", "professor")
    math_teacher = Instructor("Zinoviy", "Nytrebych", "professor")
    ikta_dean = Lead("Mikiychuk", "Mykola", "doctor", datetime.datetime(2010, 1, 1))
    ikta = Faculty("IKTA", 500, "computers", [group_iot_11, group_iot_12], ikta_dean)
    some_department = Department("Kafedra name", 20, "Bandery 25", [prog_teacher, math_teacher])
    politechnic = University("LPNU", 50000, rector_politechnic, [ikta])
    ikta.print_how_massive_it_is()
    print(ikta.get_all_groups_in_str())
    print(group_iot_11.get_schedule())


if __name__ == "__main__":
    main()
