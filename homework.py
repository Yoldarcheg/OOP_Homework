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

    def average_a(self):
        for val in self.grades.values():
            average = sum(val) / len(val)
            return average

    def average_l(self, course):
        for course in self.grades.keys():
            average = sum(self.grades[course]) / len(self.grades[course])
            return average
    
    def __str__(self):
        text = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_a()} \
            \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return text

    def __lt__(self, other):
        return self.average_a() < other.average_a()

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

    def average_a(self):
        for val in self.grades.values():
            average = sum(val) / len(val)
            return average

    def average_l(self, course):
        for course in self.grades.keys():
            average = sum(self.grades[course]) / len(self.grades[course])
            return average

    def __str__(self):
        for name, val in self.grades.items():
            average = sum(val) / len(val)
        text = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_a()}'
        return text

    def __lt__(self, other):
        return self.average_a() < other.average_a()


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
            avr = l.average_l(course) / len(list)
    return avr

student_1 = Student('Алдар', 'Зандраев', 'М')
student_1.courses_in_progress += ['Python', 'C++']
student_1.finished_courses += ['Git']

student_2 = Student('Александр', 'Козиков', 'М')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['C++']

lecturer_1 = Lecturer('Евгений', 'Лебедев')
lecturer_1.courses_attached += ['Python']
 
lecturer_2 = Lecturer('Виктор', 'Цой')
lecturer_2.courses_attached += ['Python']

reviewer_1 = Reviewer('Лариса', 'Степановна')
reviewer_1.courses_attached += ['Python']
 
reviewer_2 = Reviewer('Ольга', 'Кузнецова')
reviewer_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_1, 'Python', 7)

reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 10)

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Python', 8)

student_2.rate_hw(lecturer_2, 'Python', 7)
student_2.rate_hw(lecturer_2, 'Python', 6)
student_2.rate_hw(lecturer_2, 'Python', 5)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]

print(student_1)
print(lecturer_1)
print(reviewer_1)
print(lecturer_1 > lecturer_2)
print(student_1 > student_2)
print(avr_rate('Python', student_list))
print(avr_rate('Python', lecturer_list))