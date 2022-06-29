import markdown

file = open("README.md", encoding="unicode_escape")
text = file.read()
html = markdown.markdown(text, extensions=['tables'])
file.close()

with open('app/templates/readme.html.jinja', 'w') as file:
    file.write("{% extends 'base.html.jinja' %}\n{% block content %}")
    file.write(html)
    file.write("{% endblock %}")