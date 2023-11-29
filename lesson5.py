####################### OOP #######################


class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def hello(self):
        return f"Hello, I'm {self.name} {self.surname}!"
    
person_1 = Person('Sancho', 'Poncho')
# print(person_1.hello())


class Tester(Person):
    def __init__(self, name, surname, framework):
        super().__init__(name, surname)
        self.framework = framework
    
    def test(self):
        return f"{self.hello()} and I'm testing with {self.framework}"
    
tester_1 = Tester('Soso', 'Gogidze', 'pytest')
print(tester_1.test())
