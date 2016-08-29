roles = ["Postgraduate", "Undergraduate"]
staff_type = ["Temporary", "Permanent"]
studies = ["Introduction to data science","IOT","Introduction to Python", "Introduction to databases"]
student = [["Postgraduate","Jane","Smith","Thomsons","0000"],["UNDERGRADUATE", "John", "Jay", "Larson", 1123]]

class School:
    def __init__(self, rank, firstname, secondname, lastname, rolenumber):
        self.rank = rank
        self.firstname = firstname
        self.secondname = secondname
        self.lastname = lastname
        self.rolenumber = rolenumber

    def student(self):
        if student_class() == "Postgraduate" and self.rolenumber ==0000:
            return student[0]
        return False
    def student_class(self):
        if self.rank ==roles[1]:
            return roles[:2]
        return roles[2:]
mySchool = School("Postgraduate")
print mySchool.student
