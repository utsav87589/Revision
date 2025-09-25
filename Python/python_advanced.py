
#-----------------------------------------------------Python week 2----------------------------------

#--------------------------------------Lists----------------------------

### Lists in python are represented by [] brackets and they are
### dynamic in nature i.e, elements can be added or removed
### aloowed duplicates and ordered

# my_list = ['Developer', 21, True]
# my_list.append('Dairies')

# print(my_list)

#---------------------------------Tuples-------------------------

### Tuples are represnted by () brackets, they allow duplicates and
### elements can not be added or removed after creation

# my_tuple = ('Developer', 'Developer', 22, 44, False, True, True)

# print(my_tuple)
# print(my_tuple.index('Developer'))

#--------------------------------Sets--------------------------------

### sets are represnted by {} brackets and they are
### unordered, don't allow the duplicates and
### elements can be added and removed in them

# my_set = {1, 1, 1, 2, 'Dev', 'Dev', True, 55, 'a'}
# my_set.add('The developer')

# for i in range(0, 5) :
#     print(my_set)

#---------------------------------Dictonaries--------------------------

### Dictionaires are the represented by {} brackets but they are
### key, value pairs, and they are ordered in some version of python, 
### no duplicates are allowed

# my_dict = {
#     'name' : 'Developer',
#     'age' : 21,
#     'car' : 'Mustang',
#     'loves programming' : True,
#     'age' : 21
# }

# print(my_dict)

# my_dict['age'] = 20

# print(my_dict)
# print(my_dict)


#--------------------------------------List comprehension----------------------------

### it is a better and optimized way to write the lists
### syntax is something like this ==> my_list = [expression : expression if the condition is True]

# new_list = [x*2 for x in range(0, 100) if x > 90]

# print(new_list)

# base_list = [1, -1, 3, -4, 6, 8, -12]
# new_list = [x*x for x in base_list if x < 0]

# print(base_list)
# print(new_list)


#---------------------------------------OOPS in Python-------------------------------------

### OOPS : object orinted programming is a way of represting the real world objects in python

### Objects : everything in python is basically an object, similar to the real world objects, in python objects have their own 
### significane and properties

### Classes :  Classes are a way or a blueprint, that is used to create the objects

# ### in the example below car is a general template for different types of cars

# class Car :
#     def __init__(self, year, make, model, color) : 
#         self.year = year
#         self.make = make
#         self.model = model
#         self.color = color

#     def run(self) : 
#         print(f"I have a {self.year} {self.make} {self.model} in {self.color}")

# my_car = Car(2025, 'Ford', 'Mustang 5.0 Convertible', 'Red')
# my_car_2 = Car(2026, 'Chevrolet', 'Tahoe RST', 'Silver')


# print(my_car.run())
# print(my_car_2.run())
# print(my_car_2.color)
# print(my_car.make)


#--------------------------------------------variable scope in python--------------------------

### global variable : which is defined outside of a method like class or a function or a loop and can be used anywhere
### local variable : defined inside a loop, function or a class and cannot be used outside of that

# a = int(input('Enter a number : '))

# def add(x, y) : 
#     b = 15
#     c = a+b+y
    
#     print(b)
#     print(c)

# add(a, 10)
# print(a)
# print(b)



#---------------------------------------------------Inheritance----------------------------------

### Like other programming languages, in python also inheritance is way for the 
### child class the inherent the properties of the parent class
### There are multiple types of inheritance on python like single, mutlilevel, multiple inheritance

# class Car :
#     def __init__(self, details) : 
#         self.details = details

#     def run(self) : 
#         print(f"the car is {self.details}")

# class Truck : 
#     def __init__(self, details) : 
#         self.details = details

#     def carry(self) : 
#         print(f"the truck {self.details}")

# class Airplane(Car, Truck) : 
#     def __init__(self, details):
#         super().__init__(details)

#     def both(self) : 
#         print({self.details})

# car = Car('2025 Mustang 5.0 runs super fast')
# truck = Truck('2026 VOLVO VNL can carry upto 80000lbs')

# airplane = Airplane('beoing 777F')

# print(airplane.run())
# print(airplane.carry())


#------------------------------------------Polymorphism------------------------------------

### polymorphism in python refers to the ability of an object to take many forms

### polymorphism can also be used in form of duck typing as well, where it says if it looks like and behave like
### other then it's also other

# class Animal : 
#     def speak(self) : 
#         print("Animal speaks")

# class Cat(Animal) : 
#     def speak(self) : 
#         print("meow meow")

# class Dog(Animal) : 
#     def speak(self) : 
#         print("woof woof !")

# def make_animal_speak(animal) : 
#     animal.speak()

# cat = Cat()
# dog  = Dog()

# make_animal_speak(cat)
# make_animal_speak(dog)
