#!/usr/bin/env python

from __future__ import annotations

import pathlib
import natsort

from jinja2 import Environment
from jinja2 import FileSystemLoader

# Define the URLs
urls = pathlib.Path("./").glob("*.html")
urls = natsort.natsorted([url.name for url in urls if not url.name == "index.html"])

# Load the Jinja2 template
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('index.html')

# Render the template with the URLs
output = template.render(urls=urls)

# Write the output to a new HTML file
with open('index.html', 'w') as f:
    f.write(output)
