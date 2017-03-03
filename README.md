# rjscssmin-plugin

A wrapper around [rjsmin](http://opensource.perlig.de/rjsmin/) and [rcssmin](http://opensource.perlig.de/rcssmin/) to easily use them. Best used with templating engine such as jinja2.

## What it does

Given the list of files(js or css), minify and aggreate the files in the given order and return as a one big chunk. This enables the user to return one minified chunk of html file with all css and js in it.

### Install

Just download the snippet and put in the working directory or

```
pip install git+https://github.com/bosukh/rjscssmin-plugin
```

### Prerequisites

The snippet requires that you give it a local path to static resources. In there, it assumes that you will have javascript files in "js" folder and css files in "css" folder. You should also give url path for static resources for local environment.

Local path is used to read the files and minify them.
Url path is used to add link or script tag in development environment to ease debugging.

Initialize it by the following. mode can be either local or deploy.

```python
from rjscssmin_plugin import minified_files

minified = minified_files(static_path='static', local_path = 'app/static', mode='deploy') # or mode='local' in development environment
app.jinja_env.globals['minified'] = minified # assuming jinja2 is being used.
```

### How it's used

Suppose I have the following file structure.
```
- main.py
- app
  - templates
    - example.html
  - static
    - js
      - auth.js
      - account.js
      - base.js
    - css
      - base.css
      - normalize.css
      - framework.css
```
example.html would look like the following.
```html
<html>
  <head>
    <title>This is title</title>
    {{minified.include_css('normalize.css', 'framework.css', 'base.css')|safe}}
  </head>
  <body>
    Hello world
  </body>
  {{ minified.include_js('base.js', 'auth.js') | safe}}
</html>
```
When mode is not set to be anything other than "local", then first place will be filled with minified css, aggregated in order, enclosed in style tag. Second place will be filled with minified javascript, aggregated in order, enclosed in script tag.

If mode is set to be local, it will result in the following, which will ease debugging.
```html
<html>
  <head>
    <title>This is title</title>
    <link rel="stylesheet" type="text/css" href="/static/css/normalize.css">
    <link rel="stylesheet" type="text/css" href="/static/css/framework.css">
    <link rel="stylesheet" type="text/css" href="/static/css/base.css">
  </head>
  <body>
    Hello world
  </body>
    <script src="/static/js/base.js"></script>
    <script src="/static/js/auth.js"></script>
</html>
```

### htmlmin wrapper
If you want to minify html as well, you can wrap your handler like the following.
This will use [htmlmin](https://pypi.python.org/pypi/htmlmin/) to minify the response of the handler.

```python
from rjscssmin_plugin import minify_html

@app.route('/example', methods=['GET', 'POST']) # suppose you are using Flask
@minify_html
def example():
    return render_template("example.html")

```
