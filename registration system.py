class Student :
    def __init__(self, id, name, roll_no, department):
        self.id=id
        self.name=name
        self.rollno=roll_no
        self.department=department

    def get_name(self):
        print(f'Name        | {self.name}')

    def get_rollno(self):
        print(f'Roll no     | {self.rollno}')

    def get_depart(self):
        print(f'Department  | {self.department}')


class Registerion_system:
    
    students = []

    def add_student(self):
        while True:
            id=(input('Enter student id           | '))
            try:
                id = int(id)
                break
            except ValueError:
                print('Invalid id ! you need to enter a numerical value')

        while True:
            name=input('Enter student name         | ').upper()
            try:
                name = str(name)
                break
            except TypeError:
                print('Invalid name ! Name should be entered in alphabets ')

        roll=input('Enter student roll number  | ').upper()
        depart=input('Enter student department   | ').upper()
        self.students.append(Student(
            id=id, name=name, roll_no=roll, department=depart
        )) 
        print()
        print('student added successfully')
        print()

    def view_student_detail(self):
        id=int(input('Enter id : '))
        for student in self.students:
            if student.id == id:
                print()
                student.myname()
                student.myrollno()
                student.mydepart()
                print()
                return
            else:
                print('id not found ! Enter a new id : ')

        print('id not found ! Enter a new id : ')
            

    def delete_student(self):
        id=int(input('Enter id : '))
        for i, student in enumerate(self.students):
            if student.id == id: 
                del self.students[i]
                print(f'Student with id {id} has been deleted successfully ')
                print()
                return
            else:
                print('Invalid id ! Try again')
            
        print('Invalid id ! Try again')
            

    def print(self):
        print('||| PRESS 1 TO REGISTER A STUDENT         ||| ')
        print('||| PRESS 2 TO TO VIEW STUDENTS DETAIL    ||| ')
        print('||| PRESS 3 TO DELETE A STUDENT           ||| ')
        print('||| PRESS 4 TO EXIT THE PROGRAM           ||| ')
        print()

        self.x=int(input())

        if self.x == 1:
            self.add_student()
            self.print()

        elif self.x == 2:
            self.view_student_detail()
            self.print()
        
        elif self.x == 3:
            self.delete_student()
            self.print()
        
        elif self.x == 4:
            print('you have exited successfully !')

        else:
            print('Invalid input ! Enter again ')
            print()
            self.print()

obj=Registerion_system()
obj.print()