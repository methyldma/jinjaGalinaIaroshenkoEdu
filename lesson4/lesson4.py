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

environment = Environment(loader=FileSystemLoader("templates/"))
results_template = environment.get_template("lesson4_template.html")

result_filename = "lesson4/student_results.html"

context = {"students": students,
           "test_name": test_name,
           "max_score": max_score,
}

with open(result_filename, mode="w", encoding="utf-8") as results:
    results.write(results_template.render(context))
    print(f"...wrote {result_filename}")