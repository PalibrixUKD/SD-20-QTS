class person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return (f'Hello, I am {self.name} studying Quality and testing of software. '
                f'Here is my completed task about refactoring Python code')

class Student(person):

    def isStudent(self):
        return 'I am a student'


if __name__ == '__main__':
    student = Student(input('Enter your name: '))
    print(student)
    print(student.isStudent())
