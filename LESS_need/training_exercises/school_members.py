class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Join new school member - {}".format(self.name))

    def tell(self):
        print('Name:"{}" - Age:"{}"'.format(self.name, self.age))

class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Created new Teacher - {})'.format(name))

    def tell(self):
        SchoolMember.tell(self)
        print("Joined teacher {} earns approximately {}$".format(self.name, self.salary))

class Student(SchoolMember):

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("(Created new Student - {})".format(name))

    def tell(self):
        SchoolMember.tell(self)
        print("New student {} have a {} average mark".format(self.name, self.marks))

T = Teacher("Michail", 38, 7500)
S = Student("Daniel", 18, 3.9)

print()

T.tell()
S.tell()

