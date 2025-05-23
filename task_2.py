from typing import Set, List, Optional

# Definition of the Teacher class
class Teacher:
    def __init__(self, first_name: str, last_name: str, age: int, email: str, can_teach_subjects: Set[str]):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects: Set[str] = set()

    def __repr__(self):
        return (f"{self.first_name} {self.last_name}, {self.age} years old, "
                f"email: {self.email} — teaches: {', '.join(self.assigned_subjects)}")


def create_schedule(subjects: Set[str], teachers: List[Teacher]) -> Optional[List[Teacher]]:
    """
    Greedily assigns teachers to subjects to cover all subjects,
    minimizing the number of involved teachers.
    Returns a list of those Teachers who are assigned at least one subject,
    or None if it is impossible to cover all subjects.
    """
    to_cover = set(subjects)
    schedule: List[Teacher] = []

    # Copy the list
    available = teachers.copy()

    while to_cover:
        best = None
        best_can = set()
        for t in available:
            can = t.can_teach_subjects & to_cover
            if not best or len(can) > len(best_can) or (len(can) == len(best_can) and t.age < best.age):
                best = t
                best_can = can

        # If no new subject can be covered — it is impossible to create a schedule
        if not best or not best_can:
            return None

        # Assign the found subjects to this teacher
        best.assigned_subjects = best_can.copy()
        to_cover -= best_can
        schedule.append(best)
        available.remove(best)

    return schedule


if __name__ == '__main__':

    subjects = {'Mathematics', 'Physics', 'Chemistry', 'Computer Science', 'Biology'}

    teachers = [
        Teacher("Oleksandr", "Ivanenko", 45, "o.ivanenko@example.com", {"Mathematics", "Physics"}),
        Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {"Chemistry"}),
        Teacher("Serhiy", "Kovalenko", 50, "s.kovalenko@example.com", {"Computer Science", "Mathematics"}),
        Teacher("Natalia", "Shevchenko", 29, "n.shevchenko@example.com", {"Biology", "Chemistry"}),
        Teacher("Dmytro", "Bondarenko", 35, "d.bondarenko@example.com", {"Physics", "Computer Science"}),
        Teacher("Olena", "Grytsenko", 42, "o.grytsenko@example.com", {"Biology"}),
    ]

    schedule = create_schedule(subjects, teachers)

    # Outputting the schedule
    if schedule:
        print("Class schedule:")
        for t in schedule:
            print(f"{t.first_name} {t.last_name}, {t.age} years old, email: {t.email}")
            print(f"   Teaches subjects: {', '.join(t.assigned_subjects)}\n")
    else:
        print("It is impossible to cover all subjects with the available teachers.")
