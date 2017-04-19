# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492563403.9338272
_enable_loop = True
_template_filename = 'C:/Users/Kristin/Desktop/mycookbook/homepage/templates/browse.html'
_template_uri = 'browse.html'
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
        meals = context.get('meals', UNDEFINED)
        def mainContent():
            return render_mainContent(context._locals(__M_locals))
        recipes = context.get('recipes', UNDEFINED)
        currentMeal = context.get('currentMeal', UNDEFINED)
        mealFilter = context.get('mealFilter', UNDEFINED)
        def bannerArea():
            return render_bannerArea(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bannerArea'):
            context['self'].bannerArea(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainContent'):
            context['self'].mainContent(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bannerArea(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bannerArea():
            return render_bannerArea(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainContent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        meals = context.get('meals', UNDEFINED)
        def mainContent():
            return render_mainContent(context)
        recipes = context.get('recipes', UNDEFINED)
        currentMeal = context.get('currentMeal', UNDEFINED)
        mealFilter = context.get('mealFilter', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="content container">\r\n')
        if mealFilter:
            __M_writer('        <h1>Browse by Meal: ')
            __M_writer(str( currentMeal ))
            __M_writer('</h1>\r\n')
        else:
            __M_writer('        <h1>Browse by Meal</h1>\r\n')
        __M_writer('      <div id="meal-filter">\r\n        <h4><a href="/homepage/browse/">All Recipes</a></h4>\r\n')
        if meals:
            for item in meals:
                __M_writer('            <h4><a href="/homepage/browse/')
                __M_writer(str( item[1] ))
                __M_writer('/">')
                __M_writer(str( item[1] ))
                __M_writer('</a></h4>\r\n')
        __M_writer('      </div>\r\n\r\n      <div id="meal-tiles" class="container">\r\n')
        if recipes:
            for item in recipes:
                __M_writer('            <div class="tile meal">\r\n              <h3>')
                __M_writer(str( item.recipe_name ))
                __M_writer('</h3>\r\n              <hr>\r\n              <h4>Total Cook Time: ')
                __M_writer(str( item.cook_time ))
                __M_writer('</h4>\r\n              <p><a class="btn btn-default" href="/homepage/details/')
                __M_writer(str( item.id ))
                __M_writer('/">View Recipe &raquo;</a></p>\r\n            </div>\r\n')
        else:
            __M_writer('          <h3>No recipes currently available.</h3>\r\n')
        __M_writer('      </div>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Kristin/Desktop/mycookbook/homepage/templates/browse.html", "uri": "browse.html", "source_encoding": "utf-8", "line_map": {"28": 0, "41": 1, "46": 5, "51": 38, "57": 3, "63": 3, "69": 7, "79": 7, "80": 9, "81": 10, "82": 10, "83": 10, "84": 11, "85": 12, "86": 14, "87": 16, "88": 17, "89": 18, "90": 18, "91": 18, "92": 18, "93": 18, "94": 21, "95": 24, "96": 25, "97": 26, "98": 27, "99": 27, "100": 29, "101": 29, "102": 30, "103": 30, "104": 33, "105": 34, "106": 36, "112": 106}}
__M_END_METADATA
"""
