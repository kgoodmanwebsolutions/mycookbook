# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492572795.3805008
_enable_loop = True
_template_filename = 'C:/Users/Kristin/Desktop/mycookbook/homepage/templates/details.html'
_template_uri = 'details.html'
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
        def title():
            return render_title(context._locals(__M_locals))
        ingredients = context.get('ingredients', UNDEFINED)
        recipe = context.get('recipe', UNDEFINED)
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
        recipe = context.get('recipe', UNDEFINED)
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n  ')
        __M_writer(str( recipe.recipe_name ))
        __M_writer(' | My Cookbook\r\n')
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
        ingredients = context.get('ingredients', UNDEFINED)
        recipe = context.get('recipe', UNDEFINED)
        def mainContent():
            return render_mainContent(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="content container">\r\n      <h2>')
        __M_writer(str( recipe.recipe_name ))
        __M_writer('</h2>\r\n      <h4>Total Cook Time: ')
        __M_writer(str( recipe.cook_time ))
        __M_writer('</h4>\r\n\r\n      <hr>\r\n\r\n      <h4>Ingredients:</h4>\r\n      <ul id="ingredient-list">\r\n')
        for item in ingredients:
            if item.unit == "(No Units)":
                __M_writer('            <li>')
                __M_writer(str( item.measurement ))
                __M_writer(' - ')
                __M_writer(str( item.ingredient.ingredient_text ))
                __M_writer('</li>\r\n')
            else:
                __M_writer('            <li>')
                __M_writer(str( item.measurement ))
                __M_writer(' ')
                __M_writer(str( item.unit ))
                __M_writer(' - ')
                __M_writer(str( item.ingredient.ingredient_text ))
                __M_writer('</li>\r\n')
        __M_writer('      </ul>\r\n\r\n      <br>\r\n\r\n      <h4>Directions:</h4>\r\n      <p id="recipe-directions">')
        __M_writer(str( recipe.directions ))
        __M_writer('</p>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Kristin/Desktop/mycookbook/homepage/templates/details.html", "uri": "details.html", "source_encoding": "utf-8", "line_map": {"28": 0, "41": 1, "46": 5, "51": 9, "56": 34, "62": 3, "69": 3, "70": 4, "71": 4, "77": 7, "83": 7, "89": 11, "97": 11, "98": 13, "99": 13, "100": 14, "101": 14, "102": 20, "103": 21, "104": 22, "105": 22, "106": 22, "107": 22, "108": 22, "109": 23, "110": 24, "111": 24, "112": 24, "113": 24, "114": 24, "115": 24, "116": 24, "117": 27, "118": 32, "119": 32, "125": 119}}
__M_END_METADATA
"""
