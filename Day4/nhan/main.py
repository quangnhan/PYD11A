class Human:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
    
    def say_hi(self):
        print(f"{self.__first_name} {self.__last_name} say hello world!")
    
    def get_first_name(self):
        return self.__first_name

class Student(Human):
    pass

class Worker(Human):
    pass

# human = Human("Vo", "Quang Nhan")
# human.say_hi()

student = Student("Vo", "Quang Nhan")
student.say_hi()
print(student.get_first_name())