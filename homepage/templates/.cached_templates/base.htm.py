# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492566029.0057137
_enable_loop = True
_template_filename = 'C:/Users/Kristin/Desktop/mycookbook/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['bannerArea', 'mainContent']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def mainContent():
            return render_mainContent(context._locals(__M_locals))
        def bannerArea():
            return render_bannerArea(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n\n        <title>homepage</title>\n\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n\n        <link href="https://fonts.googleapis.com/css?family=Nobile|Open+Sans" rel="stylesheet">\n\n        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\n\n\n\n')
        __M_writer('        ')
        __M_writer(str( django_mako_plus.link_css(self) ))
        __M_writer('\n\n    </head>\n    <body>\n\n      <nav>\n        <div id="branding"><a href="/homepage/index/">\n          <img id="logo" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/SmallLightTeal.png" /></a>\n          <h2 id="header-content">My Cookbook</h2>\n        </div>\n        <ul id="nav-links">\n          <a href="/homepage/newRecipe/"><li id="submit-tab"><h4>Submit New Recipe</h4></li></a>\n          <li><h4>|</h4></li>\n          <a href="/homepage/search/"><li id="search-tab"><h4>Search</h4></li></a>\n          <li><h4>|</h4></li>\n          <a href="/homepage/browse/"><li id="browse-tab"><h4>Browse by Meal</h4></li></a>\n        </ul>\n      </nav>\n\n      <div id="banner-area">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bannerArea'):
            context['self'].bannerArea(**pageargs)
        

        __M_writer('\n      </div>\n\n      <div id="main-content">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainContent'):
            context['self'].mainContent(**pageargs)
        

        __M_writer('\n      </div>\n\n      <div id="footer">\n        <h4>K Goodman Web Solutions, LLC | 2017</h4>\n        <p>Enjoy this site? Check out some of my other work <a href="www.kgoodmanwebsolutions.com">here</a>!</p>\n      </div>\n\n')
        __M_writer('      ')
        __M_writer(str( django_mako_plus.link_js(self) ))
        __M_writer('\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bannerArea(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bannerArea():
            return render_bannerArea(context)
        __M_writer = context.writer()
        __M_writer('\n\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def mainContent():
            return render_mainContent(context)
        __M_writer = context.writer()
        __M_writer('\n\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Kristin/Desktop/mycookbook/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"17": 0, "28": 2, "29": 10, "30": 20, "31": 20, "32": 20, "33": 27, "34": 27, "39": 42, "44": 48, "45": 57, "46": 57, "47": 57, "53": 40, "59": 40, "65": 46, "71": 46, "77": 71}}
__M_END_METADATA
"""
