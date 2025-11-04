from jinja2 import Template
tpl = Template(request.form['template'])
result = tpl.render(user=current_user)
