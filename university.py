class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = 0

    def find_average_grade(self):
        s = 0
        n = 0
        for course in self.grades:
            s += sum(self.grades[course])
            n += len(self.grades[course])
        self.average_grade = s/n
  
    def __str__(self):
        return 'Имя: {}\nФамилия: {}\nСредняя оценка за лекции: {}'.format(self.name, self.surname, self.average_grade)

    def __eq__(self, other):
        if self.average_grade == other.average_grade:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.average_grade < other.average_grade:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.average_grade > other.average_grade:
            return True
        else:
            return False

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return 'Имя: {}\nФамилия: {}'.format(self.name, self.surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student):
            if course in student.courses_in_progress or course in student.finished_courses:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0

    def find_average_grade(self):
        s = 0
        n = 0
        for course in self.grades:
            s += sum(self.grades[course])
            n += len(self.grades[course])
        self.average_grade = s/n
    
    def __str__(self):
        return 'Имя: {}\nФамилия: {}\nСредняя оценка за домашние задания: {}\nКурсы в процессе изучения: {}\nЗавершенные курсы: {}'.format(self.name, self.surname, self.average_grade, ', '.join(self.courses_in_progress),', '.join(self.finished_courses))

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
          
    def __eq__(self, other):
        if self.average_grade == other.average_grade:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.average_grade < other.average_grade:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.average_grade > other.average_grade:
            return True
        else:
            return False
      

def average_stud(students, course):
    s = 0
    n = 0
    for stud in students:
        if course in stud.grades:
            s += sum(stud.grades[course])
            n += len(stud.grades[course])
    if n == 0:
        return 0
    else:
        return s/n

def average_lect(lectors, course):
    s = 0
    n = 0
    for lect in lectors:
        if course in lect.grades:
            s += sum(lect.grades[course])
            n += len(lect.grades[course])
    if n == 0:
        return 0
    else:
        return s/n

s = []
l = []
lect1 = Lecturer('Roman','Sidorov')
lect1.courses_attached += ['Java']
lect1.courses_attached += ['Python']

lect2 = Lecturer("Tell me your name","And I'll say who are you")
lect2.courses_attached += ['SQL']

stud1 = Student('Olaf', 'Smith', 'male')
stud1.courses_in_progress += ['Python']
stud1.finished_courses += ['Java']
stud1.rate_lec(lect1, 'Java', 8)
stud1.rate_lec(lect1, 'Python', 10)

stud2 = Student('Jessica', 'Ivanova', 'male')
stud2.courses_in_progress += ['Python']
stud2.finished_courses += ['Java']
stud2.finished_courses += ['SQL']
stud2.rate_lec(lect1, 'Java', 9)
stud2.rate_lec(lect2, 'SQL', 8.5)

review1 = Reviewer('Vlad','Just')
review1.rate_hw(stud1, 'Java', 10)
review1.rate_hw(stud1, 'Python', 5)
review1.rate_hw(stud2, 'Java', 7)
review1.rate_hw(stud2, 'SQL', 1)
review1.rate_hw(stud2, 'Python', 9.5)

review2 = Reviewer('Leona','Dianova')
review2.rate_hw(stud1, 'Java', 7)
review2.rate_hw(stud1, 'Python', 6)
review2.rate_hw(stud2, 'Java', 9)
review2.rate_hw(stud2, 'SQL', 10)
review2.rate_hw(stud2, 'Python', 4.5)

lect1.find_average_grade()
lect2.find_average_grade()

print("1 лектор")
print(lect1)
print()
print("2 лектор")
print(lect2)
print()

if lect1 > lect2:
    print("{} {} лучше по средней оценке, чем {} {}".format(lect1.name,lect1.surname,lect2.name,lect2.surname))
elif lect1 < lect2:
    print("{} {} лучше по средней оценке, чем {} {}".format(lect2.name,lect2.surname,lect1.name,lect1.surname))
else:
    print("Средная оценка у лектора {} {} совпадает со средней оценкой лектора {} {}".format(lect1.name,lect1.surname,lect2.name,lect2.surname))
print()

stud1.find_average_grade()
stud2.find_average_grade()

print("1 студент")
print(stud1)
print()
print("2 студент")
print(stud2) 
print()

if stud1 > stud2:
    print("{} {} лучше по средней оценке, чем {} {}".format(stud1.name,stud1.surname,stud2.name,stud2.surname))
elif stud1 < stud2:
    print("{} {} лучше по средней оценке, чем {} {}".format(stud2.name,stud2.surname,stud1.name,stud1.surname))
else:
    print("Средная оценка у студента {} {} совпадает со средней оценкой студента {} {}".format(stud1.name,stud1.surname,stud2.name,stud2.surname))
print()

s.append(stud1)
s.append(stud2)
l.append(lect1)
l.append(lect2)

print("Средняя оценка за курс Python среди всех студентов -",average_stud(s,'Python'))
print("Средняя оценка за лекции на курсе Python среди всех лекторов -",average_lect(s,'Python'))
print("Средняя оценка за курс Java среди всех студентов -",average_stud(s,'Java'))
print("Средняя оценка за лекции на курсе Java среди всех лекторов -",average_lect(s,'Java'))
print("Средняя оценка за курс SQL среди всех студентов -",average_stud(s,'SQL'))
print("Средняя оценка за лекции на курсе SQL среди всех лекторов -",average_lect(s,'SQL'))
