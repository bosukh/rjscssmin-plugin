import os
from htmlmin import minify as html_minify
from rcssmin import _make_cssmin as css_minify
from rjsmin import _make_jsmin as js_minify
from functools import wraps

def minify_html(handler):
    @wraps(handler)
    def decorated_function(*args, **kwargs):
       return html_minify(handler(*args, **kwargs))
    return decorated_function

def minify_css(string_obj):
    cssmin = css_minify(python_only=True)
    return cssmin(string_obj)

def minify_js(string_obj):
    jsmin = js_minify(python_only=True)
    return jsmin(string_obj)

class minified_files:
    def __init__(self, static_path, local_path, mode='local'):
        from codecs import open
        if static_path[0] != '/':
            static_path = '/' + static_path
        if local_path[0] == '/':
            local_path = local_path[1:]
        self.mode = mode.lower()
        self.local_path, self.static_path = os.path.relpath(local_path), static_path
        self.js, self.css= {}, {}
        for jsfile in os.listdir(self.local_path+'/js'):
            if len(jsfile.split('.')) == 2 and jsfile[-2:] == 'js':
                temp = open(self.local_path+'/js/' + jsfile, encoding="utf-8")
                self.js[jsfile] = temp.read()
        for cssfile in os.listdir(self.local_path+'/css'):
            if len(cssfile.split('.')) == 2 and cssfile[-3:] == 'css':
                temp = open(self.local_path+'/css/' + cssfile, encoding="utf-8")
                self.css[cssfile] = temp.read()

    def include_js(self, *args):
        if self.mode =='local':
            js = ['<script src="%s"></script>'%(self.static_path+'/js/'+arg) for arg in args]
            return '\n'.join(js)
        stored = self.js.get(str(args))
        if stored:
            return stored
        js = ""
        for arg in args:
            js += self.js.get(arg, '')
        js = '<script type="text/javascript">%s</script>'%minify_js(js)
        self.js[str(args)] = js
        return js

    def include_css(self, *args):
        if self.mode =='local':
            css = ['<link rel="stylesheet" type="text/css" href="%s">'%(self.static_path+'/css/'+arg) for arg in args]
            return '\n'.join(css)
        stored = self.css.get(str(args))
        if stored:
            return stored
        css = ""
        for arg in args:
            css += self.css.get(arg, '')
        css = '<style media="screen">%s</style>'%minify_css(css)
        self.css[str(args)] = css
        return css
