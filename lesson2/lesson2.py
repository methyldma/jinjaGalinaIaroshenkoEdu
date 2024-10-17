from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name = "Python Challenge"

students = [
    {"name": "Олег", "score": 100},
    {"name": "Жанна", "score": 87},
    {"name": "Таня", "score": 97}
]

enviroment = Environment(loader=FileSystemLoader("templates/"))
template = enviroment.get_template("lesson2_template.txt")

for student in students:
    filename = f"lesson2/message_{student['name'].lower()}.txt"

    content = template.render(student, max_score=max_score, test_name=test_name)

    with open(filename, mode='w', encoding='utf-8') as massege:
        massege.write(content)
        print(f"...wrote {filename}")