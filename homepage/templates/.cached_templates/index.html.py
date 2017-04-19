# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492441754.2786167
_enable_loop = True
_template_filename = 'C:/Users/Kristin/Desktop/mycookbook/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['bannerArea', 'mainContent']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def mainContent():
            return render_mainContent(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def bannerArea():
            return render_bannerArea(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bannerArea'):
            context['self'].bannerArea(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainContent'):
            context['self'].mainContent(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bannerArea(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def bannerArea():
            return render_bannerArea(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="container">\n    <img id="banner-img" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/camaje-cooking-7.jpg" />\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def mainContent():
            return render_mainContent(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content container">\n        <h1>Welcome!</h1>\n        <h4>I have created this site to collect recipes that my family and I enjoy.\n          Meal planning has always been a struggle for me, especially since I have\n          recipes in so many places and mediums. This is a centralized location where\n          I can collect the recipes we enjoy without all the clutter of a hard copy.</h4>\n    </div>\n\n    <div class="container" id="tiles">\n      <div class="row">\n        <a href="/homepage/browse/" class="tile-link">\n          <div class="col-sm-4 tile">\n            <h2>Browse by Meal</h2>\n            <hr>\n            <p>Need some meal ideas? Browse recipes by meal on this page.</p>\n          </div>\n        </a>\n        <a href="/homepage/search/" class="tile-link">\n          <div class="col-sm-4 tile">\n            <h2>Search</h2>\n            <hr>\n            <p>Have some ingredients that need to be used soon? Search recipes based\n            on ingredients you have on hand.</p>\n          </div>\n        </a>\n        <a href="/homepage/newRecipe/" class="tile-link">\n          <div class="col-sm-4 tile">\n            <h2>Submit New Recipe</h2>\n            <hr>\n            <p>Help us by submitting recipes you have enjoyed so others can enjoy them as well!</p>\n          </div>\n        </a>\n      </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Kristin/Desktop/mycookbook/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "43": 7, "48": 44, "54": 3, "61": 3, "62": 5, "63": 5, "69": 9, "75": 9, "81": 75}}
__M_END_METADATA
"""
