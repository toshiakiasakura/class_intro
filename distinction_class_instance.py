"""This module illustrates the difference between
class and instance variables. 
"""

class Test():
    class_str = "Hello world"
    class_list = ["a1"]

    def __init__(self):
        self.inst_str= "dog"
        self.inst_list= ["a2"]

if __name__ == "__main__": 
    # see the behavior of class variables.
    print("##### Class variables of string behavior ####\n")

    ob1 = Test() 
    ob2 = Test() 
    ob3 = Test() 

    ob1.class_str = "Good night"
    print("# Set ob1.class_str as Good night")
    print(f"ob1.class_str: {ob1.class_str}")
    print(f"ob2.class_str: {ob2.class_str}") 
    print(f"ob3.class_str: {ob3.class_str}") 
    print()
    Test.class_str = "Good morning"
    print("# Set class variable as Good morning")
    print(f"ob1.class_str: {ob1.class_str}")
    print(f"ob2.class_str: {ob2.class_str}") 
    print(f"ob3.class_str: {ob3.class_str}") 
    print()
    
    s = """-> This result indicates, set same variable to the class instance 
means overiding the class variable with instance variable. 
That is, if we change class variable, instance variable do not change thereafter.
"""
    print(s)
    

    print("##### Class variables of list behavior ####\n")
    
    ob1 = Test() 
    ob2 = Test() 
    ob3 = Test() 

    ob1.class_list.append("a2")
    ob2.class_list.append("a3") 

    print("# Append a2 to object 1, append a3 to object 2")
    print(f"ob1.class_list: {ob1.class_list}")
    print(f"ob2.class_list: {ob2.class_list}") 
    print(f"ob3.class_list: {ob3.class_list}") 
    print()



