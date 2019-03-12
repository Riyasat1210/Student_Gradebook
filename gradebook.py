import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)
    
    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days 

    def __lt__(self, other):
        """return  true if self's name is lexicographically less than other's name, 
        and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's last name"""
        return self.name

class MITPerson(Person):
    nextIDNum = 0 

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIDNum
        MITPerson.nextIDNum += 1
    
    def getIdNum(self):
        return self.IdNum

    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)

class UG(MITPerson):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    
    def getClass(self):
        return self.year
    def speak(self, utterance):
        return MITPerson.speak(self, "Dude, " + utterance)

class Grad(MITPerson):
    pass

# def isStudent(obj):
#     return isinstance(obj, UG) or isinstance(obj, Grad)

def isStudent(obj):
    isStudent(isinstance(obj, Student))

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    def speak(self, utterance):
        return MITPerson.speak(self, "dude, " + utterance)

class Grad(Student):
    pass       
class TransferStudent(Student):
    pass

class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        new = 'In course ' + self.department + 'we say: '
        return MITPerson.speak(self, new + utterance)
    
    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)

class grades(object):
    """A mapping from students to a list of grades """
    def __init__(self):
        """Create empty grade book """
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    
    def addGrade(self, student, grade):
        """ Assumes: grade is float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')
    
    def getGrades(self, student):
        """Return a list of grades for student"""
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('student not in grade book')
    
    def allStudents(self):
        """ Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]

    def gradeReport(course):
        """Assumes: course if of type grades"""
        report = []
        for s in course.allStudents():
            tot = 0.0
            numGrades = 0
            for g in course.getGrades(s):
                tot += g
                numGrades += 1
            try:
                average = tot/numGrades
                report.append(str(s) + '\'s mean grade is ' + str(average))
            except ZeroDivisionError:
                report.append(str(s) + ' has no grades')
        return '\n'.join(report)






##*******************************************************************************##
# Testing of the above Program #

p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')

personList = [p1,p2,p3,p4,p5]

# print(p1)

for e in personList:
    print(e)

personList.sort()
print() # Gives an space

for e in personList:
    print(e)

# ****************************************************************************#


m3 = MITPerson('Mark Zuckerberg')
m3.setBirthday(5,14,84)
m2 = MITPerson('Drew Houston')
m2.setBirthday(3,4,83)
m1 = MITPerson('Bill Gates')
m1.setBirthday(10,28,55)
m4 = MITPerson('Andrew Gates')
m5 = MITPerson('Steve Wozniak')

MITPersonList = [m1, m2, m3]

print(m1)

print(m3.speak('hi there'))

for e in MITPersonList:
    print(e)

print()

MITPersonList.sort()

for e in MITPersonList:
    print(e)

