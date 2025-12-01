# ============================================
#   USER CLASSES
# ============================================

class Person:
    """Base class for shared attributes."""
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return f"{self.first} {self.last}"


class Student(Person):
    def __init__(self, first, last, class_name):
        super().__init__(first, last)
        self.class_name = class_name


class Teacher(Person):
    def __init__(self, first, last, subject, classes):
        super().__init__(first, last)
        self.subject = subject
        self.classes = classes  # list


class HomeroomTeacher(Person):
    def __init__(self, first, last, class_name):
        super().__init__(first, last)
        self.class_name = class_name


# ============================================
#   SCHOOL CLASS (DATABASE + LOGIC)
# ============================================

class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.homeroom_teachers = []

    # ------------------- CREATE -------------------
    def create_menu(self):
        while True:
            print("\nCreate menu: student | teacher | homeroom teacher | end")
            choice = input("Choose: ").lower()

            if choice == "student":
                self.create_student()

            elif choice == "teacher":
                self.create_teacher()

            elif choice == "homeroom teacher":
                self.create_homeroom_teacher()

            elif choice == "end":
                return

            else:
                print("Invalid option.")

    def create_student(self):
        first = input("First name: ")
        last = input("Last name: ")
        class_name = input("Class (e.g., 3C): ")
        self.students.append(Student(first, last, class_name))
        print("Student created.")

    def create_teacher(self):
        first = input("First name: ")
        last = input("Last name: ")
        subject = input("Subject: ")

        print("Enter classes they teach (empty to finish):")
        classes = []
        while True:
            c = input("Class: ")
            if c == "":
                break
            classes.append(c)

        self.teachers.append(Teacher(first, last, subject, classes))
        print("Teacher created.")

    def create_homeroom_teacher(self):
        first = input("First name: ")
        last = input("Last name: ")
        class_name = input("Class they lead: ")

        self.homeroom_teachers.append(HomeroomTeacher(first, last, class_name))
        print("Homeroom teacher created.")

    # ------------------- MANAGE -------------------
    def manage_menu(self):
        while True:
            print("\nManage menu: class | student | teacher | homeroom teacher | end")
            choice = input("Choose: ").lower()

            if choice == "class":
                self.manage_class()

            elif choice == "student":
                self.manage_student()

            elif choice == "teacher":
                self.manage_teacher()

            elif choice == "homeroom teacher":
                self.manage_homeroom_teacher()

            elif choice == "end":
                return

            else:
                print("Invalid option.")

    # ---- Manage class ----
    def manage_class(self):
        class_name = input("Class: ")

        print("\nStudents:")
        for s in self.students:
            if s.class_name == class_name:
                print(s.full_name())

        print("\nHomeroom teacher:")
        found = False
        for h in self.homeroom_teachers:
            if h.class_name == class_name:
                print(h.full_name())
                found = True
        if not found:
            print("None")

# ---- Manage student ----
    def manage_student(self):
        first = input("First name: ")
        last = input("Last name: ")

        student = self.find_student(first, last)
        if student is None:
            print("Student not found.")
            return

        print("\nClass:", student.class_name)
        print("Teachers:")

        for t in self.teachers:
            if student.class_name in t.classes:
                print(f"{t.full_name()} — {t.subject}")

    # ---- Manage teacher ----
    def manage_teacher(self):
        first = input("First name: ")
        last = input("Last name: ")

        teacher = self.find_teacher(first, last)
        if teacher is None:
            print("Teacher not found.")
            return

        print("\nClasses taught:")
        for c in teacher.classes:
            print(c)

    # ---- Manage homeroom teacher ----
    def manage_homeroom_teacher(self):
        first = input("First name: ")
        last = input("Last name: ")

        ht = self.find_homeroom_teacher(first, last)
        if ht is None:
            print("Homeroom teacher not found.")
            return

        print("\nStudents in their class:")
        for s in self.students:
            if s.class_name == ht.class_name:
                print(s.full_name())

    # ------------------- HELPERS -------------------
    def find_student(self, first, last):
        for s in self.students:
            if s.first == first and s.last == last:
                return s
        return None

    def find_teacher(self, first, last):
        for t in self.teachers:
            if t.first == first and t.last == last:
                return t
        return None

    def find_homeroom_teacher(self, first, last):
        for h in self.homeroom_teachers:
            if h.first == first and h.last == last:
                return h
        return None


# ============================================
#   MAIN PROGRAM
# ============================================

def main():
    school = School()
    print("Commands: create | manage | end")

    while True:
        cmd = input("\nCommand: ").lower()

        if cmd == "create":
            school.create_menu()

        elif cmd == "manage":
            school.manage_menu()

        elif cmd == "end":
            print("Goodbye!")
            break

        else:
            print("Invalid command.")

main()
