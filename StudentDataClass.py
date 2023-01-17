# Type in the dataclass code from the slides/video. You would have done this before class.

# Add one more field: gpa, a float.

# Write a main function to create some example Student objects with some example names, college_id and GPA values. 

# Verify you can read the name, college ID and GPA for an example student.  Verify when you print an example student, the GPA is included. 

# Add some comments in your code to compare the dataclass version to the "traditional" version.

class Student:
    def __init__(self, name, college_id, gpa):
        self.name = name
        self.college_id = college_id
        self.gpa = gpa # added in gpa field
        
    def __str__(self):
        return f'Student: {self.name}, College ID: {self.college_id}, GPA: {self.gpa}'
    
    def update_gpa(self, new_gpa): # this will update a students GPA
        self.gpa = new_gpa
    
def main():
    alice = Student('Alice', 'aa1234aa', 3.5)
    bob = Student('Bob', 'bb1234bb', 3.2)
    print(alice) # prints: Student: Alice, College ID: aa1234aa, GPA: 3.5
    print(bob) # prints: Student: Bob, College ID: bb1234bb, GPA: 3.2
    alice.update_gpa(4.0) # update Alice's GPA to 4.0
    print(alice) # prints: Student: Alice, College ID: aa1234aa, GPA: 4.0
    
if __name__ == "__main__":
    main()
