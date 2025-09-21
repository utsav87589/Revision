
#-------------------------------------------Python : Week 3--------------------------------------

#----------------------------------Duck Typing---------------------------------------------

### Duck typing is a way to achieve polymorphism besides the inheritance
### the underlying idea is that if "it sounds like duck, it is duck"
### it means that as long as the object satisfies the minimum requirements then it doesn't
### need necessarily belong to that class

# class Animal : 
#     is_alive = True

# class Dog(Animal) : 
#     def speak(self) : 
#         print("WOOF!")

# class Cat(Animal) :
#     def speak(self) : 
#         print('MEOW!')

# class Car : 
#     is_alive = False

#     def speak(self) : 
#         print('BOOM BOOM')

# animals = [Cat(), Dog(), Car()]

# for animal in animals : 
#     animal.speak()
#     print(animal.is_alive)


#------------------------------------------------------Static methods----------------------------------------

### Static methods are the ones that belongs to the class rather than the objects from that class
### for example we don't need an object from that class to access those methods

# class Employee : 
#     def __init__(self,name, position):
#         self.name = name
#         self.position = position

#     def get_info(self) : 
#         return f"{self.name} :: {self.position}"
    
#     @staticmethod
#     def available_jobs(jobs) : 
#         aval_jobs = ['Driver', 'Developer', 'Editor']

#         return jobs in aval_jobs

# print(Employee.available_jobs('Security'))
# print(Employee.available_jobs('Dispatch'))
# print(Employee.available_jobs('Driver'))


#-------------------------------------------------File operations in python----------------------------------

### In python we have the options to read and modify the files
### there are many operations based on that like rading, writing, making a file, deleting a file
### We can read file like excel, plain text or csv or json file etc..

# path_1 = 'Week 3/text.txt'
# path_2 = 'Week 3/Final.csv'

# with open(path_1, 'r') as f :
#     print(f.read())

# with open(path_2, 'r', encoding = 'UTF-8') as f : 
#     print(f.read())

# with open(path_1, 'r+') as f :
#     lines = f.read()
#     new_lines = 'I almost finished the python, bro code is an amzing instructor'

#     lines += new_lines

#     f.write(lines)
#     f.truncate()

#     print(lines)


#-----------------------------------------------------Date and time in Python-------------------------------

### Date and time in python can be accessed through date and time model

# from datetime import date
# from datetime import datetime

# today = date.today()
# current_time = datetime.now()

# print(today)
# print(current_time)



#-----------------------------------------------------Multithreading in python----------------------------------

# import threading
# import time

# def task(name):
#     print(f"Thread {name}: Starting")
#     time.sleep(2)  # Simulate I/O-bound work
#     print(f"Thread {name}: Finishing")

# # Create thread objects
# thread1 = threading.Thread(target=task, args=("One",))
# thread2 = threading.Thread(target=task, args=("Two",))

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for both threads to complete
# thread1.join()
# thread2.join()

# print("Main thread: All threads finished")