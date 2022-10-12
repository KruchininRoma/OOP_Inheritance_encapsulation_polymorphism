class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        s = 0
        n = 0
        for course in self.grades:
            s += sum(self.grades[course])
            n += len(self.grades[course])
        if n == 0:
            return 'Имя: {}\nФамилия: {}\nСредняя оценка за лекции: {}'.format(self.name, self.surname, 0)
        else:
            return 'Имя: {}\nФамилия: {}\nСредняя оценка за лекции: {}'.format(self.name, self.surname, s/n)


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
        

    def __str__(self):
        s = 0
        n = 0
        for course in self.grades:
            s += sum(self.grades[course])
            n += len(self.grades[course])
        if n == 0:
            return 'Имя: {}\nФамилия: {}\nСредняя оценка за домашние задания: {}\nКурсы в процессе изучения: {}\nЗавершенные курсы: {}'.format(self.name, self.surname, 0, ', '.join(self.courses_in_progress),', '.join(self.finished_courses))
        else:
            return 'Имя: {}\nФамилия: {}\nСредняя оценка за домашние задания: {}\nКурсы в процессе изучения: {}\nЗавершенные курсы: {}'.format(self.name, self.surname, s/n, ', '.join(self.courses_in_progress),', '.join(self.finished_courses))

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_stud(students, course):
    s = 0
    n = 0
    for stud in students:
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

review2 = Reviewer('Leona','Dianova')
review2.rate_hw(stud1, 'Java', 7)
review2.rate_hw(stud1, 'Python', 6)
review2.rate_hw(stud2, 'Java', 9)
review2.rate_hw(stud2, 'SQL', 10)

print("1 лектор")
print(lect1)
print("2 лектор")
print(lect2)

print("1 студент")
print(stud1)
print("2 студент")
print(stud2) 

s.append(stud1)
s.append(stud2)
l.append(lect1)
l.append(lect2)

print("Средняя оценка за курс Python среди всех студентов -",average_stud(s,'Python'))

