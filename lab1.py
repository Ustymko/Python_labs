from university import University
from institute import Institute
from group import Group
from student import Student
from schedule import Schedule
from progress import Progress


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
