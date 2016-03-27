"""
Render a quick Jinja2 template.
Thanks Danny - http://pydanny.com/jinja2-quick-load-function.html

Example:

>>> from jinja_quick_load import render_from_template
>>> data = {
...     "date": "June 12, 2014",
...     "items": ["oranges", "bananas", "steak", "milk"]
... }
>>> render_from_template(".", "shopping_list.html", **data)

"""


from jinja2 import FileSystemLoader, Environment


def render_from_template(directory, template_name, **kwargs):
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)
