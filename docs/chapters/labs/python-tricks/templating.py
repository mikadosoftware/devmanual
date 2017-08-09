from jinja2 import Template

template = Template('''
    <!DOCTYPE html>
            <head>
                    <title>search results</title>
                    <link rel="stylesheet" href="static/results.css">
            </head>
            <body>
                    {% for item in items %}
                            {% if len(item[0]) < 60 %}
                                    <p><a href="{{ item[1] }}">{{item[0]}}</a></p>
                            {% else %}
                                    <p><a href="{{ item[1] }}">{{item[0][40:]}}...</a></p>
                            {% endif %}
                    {% endfor %}
            </body>
    </html>''')

## somewhere later in the code...

template.render(items=links).encode('utf-8')
