# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

def count(students):
    students_count = {}
    for student in students:
        person = student.get('first_name')
        if person not in students_count:
            students_count[person] = 1
        else:
            students_count[person] += 1
    return students_count

students_count = count(students)
for person, cnt in students_count.items():
    print(f'{person}: {cnt}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]


students_count = count(students)

def most_popular(students):
    person = None
    most_popular = 0
    for name, number in students.items():
        if number > most_popular:
            most_popular = number
            person = name
    return person

print(f'Самое частое имя среди учеников: {most_popular(students_count)}')





# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for ind, school_class in enumerate(school_students):
    students_count = count(school_class)
    most_popular_name = most_popular(students_count)
    print(f'Самое популярное имя в классе {ind + 1}: {most_popular_name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a


school = [
    {'class': '2a', 'students': [{'first_name': 'Миша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


class Group():

    GROUPS = []

    def __init__(self, group_number):
        self.group = self.determine_group(group_number)
        self.students = []
        self.counter = {'М': 0, 'Ж': 0}

    def determine_group(self, group_number):
        return group_number

    def __repr__(self):
        return f'Класс {self.group}'

    @classmethod
    def add_gender_information(cls):
        for group in cls.GROUPS:
            for student in group.students:
                if student.gender == 'М':
                    group.counter['М'] += 1
                else:
                    group.counter['Ж'] += 1


class Person(Group):

    def __init__(self, name, group, gender):
        super().__init__(group)
        self.name = self.determine_name(name)
        self.gender = self.determine_gender(gender)

    def __repr__(self):
        return f'(Имя: {self.name}, пол:{self.gender} )'

    def determine_name(self, name):
        return name

    def determine_gender(self, gender):
        if gender:
            return 'М'
        else: 
            return 'Ж'


def get_classes(school):
    for group in school:
        grp = Group(group['class'])
        Group.GROUPS.append(grp)
        for student in group['students']:
            std = Person(student['first_name'], group['class'], is_male[student['first_name']])
            grp.students.append(std)


get_classes(school)
Group.add_gender_information()


girls_most = ['', 0]
boys_most = ['', 0]
for group in Group.GROUPS:
    boys = group.counter['М']
    girls = group.counter['Ж']
    print(f'Класс {group.group}: мальчиков {boys}, девочек {girls}')
    if boys > boys_most[1]:
        boys_most[0] = group
        boys_most[1] = boys
    if girls > girls_most[1]:
        girls_most[0] = group
        girls_most[1] = girls
print(f'Больше всего мальчиков в классе {boys_most[0].group}')
print(f'Больше всего девочек в классе {girls_most[0].group}')
