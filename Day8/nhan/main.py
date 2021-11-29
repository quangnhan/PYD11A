class Human:
    def eat(self):
        pass

    def __kill(self):
        pass 

class Student(Human):
    def say(self):
        self.__kill()

student = Student()
student.say()