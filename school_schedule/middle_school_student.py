from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, get_transportation=False):
        super().__init__(name, grade, classes)
        self.get_transportation = get_transportation

    def summary(self):
        student_summary = super().summary
        get_message = "gets" if self.get_transportation else "doesn't get"
        return (f"{student_summary}"
                f"{self.name} {get_message} transportation")
    
John = MiddleSchoolStudent("John", "7th", ["Art", "Science"])
print(John.summary())