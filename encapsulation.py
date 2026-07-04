class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print("the marks is: ",self.marks)
    

s1=student("kiran",34)
print(f"Name is: {s1.name}")
s1.display()
    
