# Считыватель новых учеников и добавления их в общее хранилище
class Students:

    def __init__(self):
        self.s_name = input("New student name: ")
        self.s_age = input("New student age: ")
        self.s_mark = input("New student age: ")

    def new_student(self):
        f = open("student_counter.txt", "a+")
        f.write("Created new student {} and its age is {}, average mark is {}!\r\n".format(self.s_name, self.s_age,
                                                                                           self.s_mark))
        f.write("%s - %s years - %s points\r\n" % (self.s_name, self.s_age, self.s_mark))
        f.close()


def student_showing():
    f = open("student_counter.txt", "r")
    print(f.read())
    f.close()


def student_removing():
    print("Not possible with this, but soon I should do this!")


user_inp = (int(input('''What you wanna do? 
1 - see students 
2 - add new student 
3 - remove student? 
----> ''')))

if user_inp == 1:
    student_showing()

elif user_inp == 2:
    new_student = Students()
    new_student.new_student()
    while True:
        response = input("Would you want to add new student?(y/n): ")
        if response == "y" or response == "Y":
            new_student = Students()
            new_student.new_student()
        elif response == "n" or response == "N":
            break

    print("\nAll you new students in file \"student_counter\", you can see!")

elif user_inp == 3:
    student_removing()
