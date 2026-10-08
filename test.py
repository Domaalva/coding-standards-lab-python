
# Reviewed under SE2 coding standards guidelines
"""Student Grade Management System."""


class Student:
    """Represent a student and manage their grades."""

    MIN_GRADE = 0
    MAX_GRADE = 100
    PASSING_GRADE = 60
    HONOR_GRADE = 90

    def __init__(self, student_id, name):
        """Initialize a student with a valid ID and name."""
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty.")

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grade(self, grade):
        """Add a valid numeric grade between 0 and 100."""
        if isinstance(grade, bool) or not isinstance(
            grade, (int, float)
        ):
            print("Error: Grade must be numeric.")
            return False

        if not self.MIN_GRADE <= grade <= self.MAX_GRADE:
            print("Error: Grade must be between 0 and 100.")
            return False

        self.grades.append(grade)
        self.update_status()
        return True

    def calculate_average(self):
        """Calculate the average of all student grades."""
        if not self.grades:
            return 0.0

        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Convert the average into a letter grade."""
        average = self.calculate_average()

        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def update_status(self):
        """Update pass/fail and honor roll status."""
        average = self.calculate_average()
        self.is_passed = average >= self.PASSING_GRADE
        self.honor = average >= self.HONOR_GRADE

    def remove_grade_by_index(self, index):
        """Remove a grade using its index."""
        if isinstance(index, bool) or not isinstance(index, int):
            print("Error: Index must be an integer.")
            return False

        if index < 0 or index >= len(self.grades):
            print("Error: Grade index is out of bounds.")
            return False

        removed_grade = self.grades.pop(index)
        self.update_status()
        print(f"Grade {removed_grade} removed successfully.")
        return True

    def remove_grade_by_value(self, grade):
        """Remove a grade using its value."""
        if grade not in self.grades:
            print("Error: Grade value was not found.")
            return False

        self.grades.remove(grade)
        self.update_status()
        print(f"Grade {grade} removed successfully.")
        return True

    def generate_report(self):
        """Display a formatted student summary report."""
        self.update_status()

        status = "Passed" if self.is_passed else "Failed"

        print("\n" + "=" * 40)
        print("STUDENT GRADE REPORT")
        print("=" * 40)
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Average Grade: {self.calculate_average():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")
        print(f"Pass/Fail Status: {status}")
        print(f"Honor Roll: {self.honor}")
        print("=" * 40)


def main():
    """Demonstrate the student grade management system."""
    print("STUDENT GRADE MANAGEMENT SYSTEM")

    try:
        student_one = Student("001", "Ana Garcia")
        student_two = Student("002", "Carlos Lopez")
        student_three = Student("003", "Maria Perez")

        # Add valid grades.
        student_one.add_grade(95)
        student_one.add_grade(92)
        student_one.add_grade(98)

        student_two.add_grade(75)
        student_two.add_grade(85)
        student_two.add_grade(80)

        student_three.add_grade(40)
        student_three.add_grade(55)
        student_three.add_grade(50)

        # Generate student reports.
        student_one.generate_report()
        student_two.generate_report()
        student_three.generate_report()

        # Test invalid grades.
        print("\nTESTING INVALID GRADES")
        student_one.add_grade("Fifty")
        student_one.add_grade(150)
        student_one.add_grade(-10)

        # Test grade removal by index.
        print("\nTESTING REMOVAL BY INDEX")
        student_two.remove_grade_by_index(1)
        student_two.generate_report()

        # Test grade removal by value.
        print("\nTESTING REMOVAL BY VALUE")
        student_one.remove_grade_by_value(92)
        student_one.generate_report()

        # Test invalid removals.
        print("\nTESTING INVALID REMOVALS")
        student_one.remove_grade_by_index(10)
        student_one.remove_grade_by_value(50)

        # Test invalid student information.
        print("\nTESTING INVALID STUDENT DATA")
        try:
            Student("", "Invalid Student")
        except ValueError as error:
            print(f"Error: {error}")

        try:
            Student("004", "")
        except ValueError as error:
            print(f"Error: {error}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
