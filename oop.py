class Bike:
    def start(self):
        print('Bike is starting')
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

okx = Bike()  # Create an instance of Bike
okx.set_name('Honda')  # Set the name of the bike
print(okx.get_name())  # Print the name of the bike




# class student:
#     def set_details(self, name, grade):
#         self.name = name
#         self.grade = grade
#     def display(self):
#         print(f'student name: {self.name}')
#         print(f'student grade: {self.grade}')

# stu1 = student()

# stu1.set_details('Haroon', 'A')

# stu1.display()