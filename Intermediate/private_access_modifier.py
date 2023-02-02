class Student:
    #public:
    # std_id = 283
    # std_name = "abc"
    # std_course = "Python"
    # you can see that these are the data members that are declared initialized with public access, now just give any of the variable one double underscore it will become a private
    #privateaccessmodifier:
    __std_id = 283
    __std_name = "abc"
    __std_course = "Python"

    # Step 3
    def show_std_info(self):
        print(self.__std_id)
        print(self.__std_name)
        print(self.__std_course)
    #steo 3 ended

#We will not be able to access this above private thing below as this is private. The private access modifier data members functions can be accessed in a same class or in that class in which they are declare
class Xyz(Student):
    def show(self):
        # print(self.__std_id) # attribute error will be displayed here
        # To solve above attribute error we will go to step 3 as commented
        print(self.show_std_info)

obj = Xyz()
obj.show()