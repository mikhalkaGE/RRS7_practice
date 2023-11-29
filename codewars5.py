# https://www.codewars.com/kata/5121303128ef4b495f000001 --- Refactored Greeting --- DONE
# TODO: This method needs to be called multiple times for the same person (my_name).
# It would be nice if we didnt have to always pass in my_name every time we needed to great someone.

# class Person():
#     def __init__(self, my_name):
#         self.name = my_name
    
#     def get_my_name(self):
#         return self.name
    
#     def greet(self, your_name):
#         return "Hello %s, my name is %s" % (your_name, self.get_my_name())
    
# joe = Person('Joe')
# print(joe.greet('Kate')) # should return 'Hello Kate, my name is Joe'
# print(joe.name)          # should == 'Joe'







# https://www.codewars.com/kata/5956d127a817c7c51b000026 --- These are not my grades! (Revamped !) --- DONE

# class Student:

#     def __init__(self, first_name, last_name, grades=[]):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grades = grades.copy()
    
#     def add_grade(self, grade):
#         self.grades.append(grade)
    
#     def get_average(self):
#         return sum(self.grades) / len(self.grades)
    
# someStudent = Student('Matthew', 'Connor')
# someOtherStudent = Student('Chloe', 'Madison')
# someStudent.add_grade(98)
# someOtherStudent.add_grade(77)
# print(someStudent.grades == [98]) # Evaluates to True
# print(someOtherStudent.grades == [77]) # Evaluates to True







# https://www.codewars.com/kata/513f887e484edf3eb3000001 --- Person Class Bug --- DONE

# class Person():

#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'

# person = Person('Yukihiro', 'Matsumoto', 47)
# print(person.full_name)
# print(person.age)






# https://www.codewars.com/kata/53f1015fa9fe02cbda00111a --- Color Ghost --- DONE

# import random
# class Ghost():
#     def __init__(self):
#         self.color = random.choice(['red', 'white', 'yellow', 'purple'])

# ghost = Ghost()
# print(ghost.color)







# https://www.codewars.com/kata/55c1d030da313ed05100005d --- Building Spheres --- DONE

# import math

# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
        
#     def get_radius(self):
#         return self.radius
    
#     def get_mass(self):
#         return self.mass
    
#     def get_volume(self):
#         return round((4/3)*math.pi*(self.radius)**3, 5)
    
#     def get_surface_area(self):
#         return round(4*math.pi*(self.radius)**2, 5)
    
#     def get_density(self):
#         return round(self.mass/self.get_volume(), 5)
    
# ball = Sphere(2,50)
# print(ball.get_radius())
# print(ball.get_mass())
# print(ball.get_volume())
# print(ball.get_surface_area())
# print(ball.get_density())






# https://www.codewars.com/kata/55b75fcf67e558d3750000a3 --- Building blocks --- DONE

# class Block:
#     def __init__(self, objects):
#         self.w = objects[0]
#         self.l = objects[1]
#         self.h = objects[2]

#         self.v = self.w*self.l*self.h
#         self.s_a = 2*((self.l*self.w)+(self.l*self.h)+(self.w*self.h))
        
#     def get_width(self):
#         return self.w
#     def get_length(self):
#         return self.l
#     def get_height(self):
#         return self.h
#     def get_volume(self):
#         return self.v
#     def get_surface_area(self):
#         return self.s_a
    
# b = Block([2,4,6])
# print(b.get_width())
# print(b.get_length())
# print(b.get_height())
# print(b.get_volume())
# print(b.get_surface_area())






# https://www.codewars.com/kata/632408defa1507004aa4f2b5 --- Double value every next call --- CHITTED

# class Class:
#     value = 1
#     @staticmethod
#     def get_number():
#         new_value = Class.value
#         Class.value *=2
#         return new_value

# print(Class.get_number())
# print(Class.get_number())
# print(Class.get_number())
# print(Class.get_number())
# print(Class.get_number())






# https://www.codewars.com/kata/54fe05c4762e2e3047000add --- OOP: Object Oriented Piracy --- DONE

# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#     def is_worth_it(self):
#         return self.draft-self.crew*1.5 > 20
        
# boat = Ship(15, 10)
# print(boat.is_worth_it())






# https://www.codewars.com/kata/5882b052bdeafec15e0000e6 --- Thinkful - Object Drills: Quarks --- CHITTED

# class Quark(object):

#     _COLOR = frozenset(["red", "blue", "green"])
#     _FLAVOR = frozenset(['up', 'down', 'strange', 'charm', 'top', 'bottom'])
      
#     def __init__(self, color, flavor):
#         if color in self._COLOR:
#             self.color = color
#         else:
#             raise ValueError(f'{color} color is not allowed!')
#         if flavor in self._FLAVOR:
#             self.flavor = flavor
#         else:
#             raise ValueError(f'{flavor} flavor is not allowed!')
#         self.baryon_number = 1/3

#     def interact(self, second_quark):
#         self.color, second_quark.color = second_quark.color, self.color

# q1 = Quark('red', 'up')
# q2 = Quark('blue', 'down')
# print(q1.color)
# print(q2.color)
# print('EXCHANGE:')
# q1.interact(q2)
# print(q1.color)
# print(q2.color)






# https://www.codewars.com/kata/571d2e9eeed4a150d30011e7 --- Competitive eating scoreboard --- CHITTED

# lst = [{"name": "Habanero Hillary", "chickenwings": 5 , "hamburgers": 17, "hotdogs": 11},{"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]
# def scoreboard(who_ate_what):
#     result_list = []
#     for person in who_ate_what:

#         chickenwings = person.get('chickenwings', 0)
#         hamburgers = person.get('hamburgers', 0)
#         hotdogs = person.get('hotdogs', 0)

#         score = chickenwings*5 + hamburgers*3 + hotdogs*2
#         person_result = {"name": person['name'], "score": score}
#         result_list.append(person_result)

#     sorted_result = sorted(result_list, key=lambda x: (-x["score"], x["name"]))
#     return sorted_result

# print(scoreboard([{"name": "Habanero Hillary", "chickenwings": 5 , "hamburgers": 17, "hotdogs": 11},{"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]))
# print(scoreboard([]))







# https://www.codewars.com/kata/55ddcef532f8678af1000006 --- 



# https://www.codewars.com/kata/pythons-dynamic-classes-number-1 --- CHITTED

# def class_name_changer(cls, new_name) :
#     if not new_name[0].isupper() or not new_name.isalnum():
#         raise NameError('Invalid class name!')
#     cls.__name__ = new_name







# https://www.codewars.com/kata/563f879ecbb8fcab31000041 --- CHITTED

# def factory(x):
#     def arr_f(my_arr):
#         new_arr = []               # return [i*x for i in my_arr]
#         for i in my_arr:
#             new_arr.append(i*x)
#         return new_arr
#     return arr_f

# # Example usage:
# multiply_by_2 = factory(2)
# result = multiply_by_2([1, 2, 3, 4])
# print(result)  # Output: [2, 4, 6, 8]

# multiply_by_3 = factory(3)
# result = multiply_by_3([5, 6, 7, 8])
# print(result)  # Output: [15, 18, 21, 24]






# https://www.codewars.com/kata/5c79c07b4ba1e100097f4e1a --- 








# https://www.codewars.com/kata/64c766dd16982000173d5ba1
#  *
# https://www.codewars.com/kata/557d9e4d155e2dbf050000aa
# https://www.codewars.com/kata/5d774cfde98179002a7cb3c8
