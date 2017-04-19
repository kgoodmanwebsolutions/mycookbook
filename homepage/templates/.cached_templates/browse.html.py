# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492572769.6577196
_enable_loop = True
_template_filename = 'C:/Users/Kristin/Desktop/mycookbook/homepage/templates/browse.html'
_template_uri = 'browse.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['title', 'bannerArea', 'mainContent']


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
        def bannerArea():
            return render_bannerArea(context._locals(__M_locals))
        currentMeal = context.get('currentMeal', UNDEFINED)
        recipes = context.get('recipes', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        mealFilter = context.get('mealFilter', UNDEFINED)
        meals = context.get('meals', UNDEFINED)
        def mainContent():
            return render_mainContent(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        currentMeal = context.get('currentMeal', UNDEFINED)
        def title():
            return render_title(context)
        mealFilter = context.get('mealFilter', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if mealFilter:
            __M_writer('    ')
            __M_writer(str( currentMeal ))
            __M_writer(' | My Cookbook\r\n')
        else:
            __M_writer('    Browse | My Cookbook\r\n')
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
        recipes = context.get('recipes', UNDEFINED)
        currentMeal = context.get('currentMeal', UNDEFINED)
        mealFilter = context.get('mealFilter', UNDEFINED)
        meals = context.get('meals', UNDEFINED)
        def mainContent():
            return render_mainContent(context)
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
{"filename": "C:/Users/Kristin/Desktop/mycookbook/homepage/templates/browse.html", "uri": "browse.html", "source_encoding": "utf-8", "line_map": {"28": 0, "43": 1, "48": 9, "53": 13, "58": 46, "64": 3, "72": 3, "73": 4, "74": 5, "75": 5, "76": 5, "77": 6, "78": 7, "84": 11, "90": 11, "96": 15, "106": 15, "107": 17, "108": 18, "109": 18, "110": 18, "111": 19, "112": 20, "113": 22, "114": 24, "115": 25, "116": 26, "117": 26, "118": 26, "119": 26, "120": 26, "121": 29, "122": 32, "123": 33, "124": 34, "125": 35, "126": 35, "127": 37, "128": 37, "129": 38, "130": 38, "131": 41, "132": 42, "133": 44, "139": 133}}
__M_END_METADATA
"""
