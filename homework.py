class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def average(self, course):
        for name, val in self.grades.items():
            average = sum(val) / len(val)
        return average
    
    def __str__(self):
        for name, val in self.grades.items():
            average = sum(val) / len(val)
        text = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {average} \
            \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return text

    def __lt__(self, other):
        for name, val in self.grades.items():
            average = sum(val) / len(val)
        return self.average() < other.average()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] 
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average(self, course):
        for name, val in self.grades.items():
            average = sum(val) / len(val)
        return average

    def __str__(self):
        for name, val in self.grades.items():
            average = sum(val) / len(val)
        text = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {average}'
        return text

    def __lt__(self, other):
        for name, val in self.grades.items():
            average = sum(val) / len(val)
        return self.average() < other.average()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        text = f'Имя: {self.name} \nФамилия: {self.surname}'
        return text
           
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def avr_rate(course, list):
    for l in list:
        for c in course:
            avr = l.average(course) / len(list)
    return avr


# some_student = Student('Ruoy', 'Eman', 'your_gender')
# some_student.courses_in_progress += ['Python', 'C++']
 
# cool_mentor = Reviewer('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(some_student, 'Python', 9)
# cool_mentor.rate_hw(some_student, 'Python', 10)
# cool_mentor.rate_hw(some_student, 'Python', 10)
 
# print(some_student.grades)

# some_lecturer = Lecturer('Some', 'Buddy')
# some_lecturer.courses_attached += ['Python']

# some_student.rate_hw(some_lecturer, 'Python', 9)
# some_student.rate_hw(some_lecturer, 'Python', 9)
# some_student.rate_hw(some_lecturer, 'Python', 9)

# some_reviewer = Reviewer('Some', 'Buddy')

# print(some_lecturer.grades)

# print(some_reviewer)
# print(some_lecturer)
# print(some_student)