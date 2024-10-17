import jinja2

enviroment = jinja2.Environment()
template = enviroment.from_string("Hello {{name}}!")

print(template.render(name = "World"))