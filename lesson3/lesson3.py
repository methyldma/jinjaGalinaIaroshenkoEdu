from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name = "Python Challenge"

students = [
    {"name": "Олег", "score": 100},
    {"name": "Жанна", "score": 87},
    {"name": "Таня", "score": 97},
    {"name": "Сергей", "score": 45},
    {"name": "Екатерина", "score": 35}
]

environment = Environment(loader=FileSystemLoader('templates/'))
template = environment.get_template('lesson3_template.txt')

for student in students:
    filename = f"lesson3/message_{student['name'].lower()}.txt"

    content = template.render(student, max_score=max_score, test_name=test_name)

    with open(filename, mode='w', encoding='utf-8') as massege:
        massege.write(content)
        print(f"...wrote {filename}")

