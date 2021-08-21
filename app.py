from base import app
from jinja2 import Environment
from jinjaMarkdown.markdownExtension import markdownExtension

app.jinja_env.add_extension(markdownExtension)