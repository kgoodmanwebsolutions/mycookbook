# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492573087.2037368
_enable_loop = True
_template_filename = 'C:/Users/Kristin/Desktop/mycookbook/homepage/templates/newRecipe.directions.html'
_template_uri = 'newRecipe.directions.html'
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
        directionsForm = context.get('directionsForm', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        ingredient_array = context.get('ingredient_array', UNDEFINED)
        cook_time = context.get('cook_time', UNDEFINED)
        def mainContent():
            return render_mainContent(context._locals(__M_locals))
        recipe_name = context.get('recipe_name', UNDEFINED)
        source = context.get('source', UNDEFINED)
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
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n  New Recipe - Step 3 | My Cookbook\r\n')
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
        directionsForm = context.get('directionsForm', UNDEFINED)
        ingredient_array = context.get('ingredient_array', UNDEFINED)
        cook_time = context.get('cook_time', UNDEFINED)
        def mainContent():
            return render_mainContent(context)
        recipe_name = context.get('recipe_name', UNDEFINED)
        source = context.get('source', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content container">\r\n    <h1>Submit New Recipe - Step 3</h1>\r\n\r\n    <h4><strong>Recipe Name:</strong> ')
        __M_writer(str( recipe_name ))
        __M_writer('</h4>\r\n    <h4><strong>Total Cook Time:</strong> ')
        __M_writer(str( cook_time ))
        __M_writer('</h4>\r\n    <h4><strong>Source:</strong> ')
        __M_writer(str( source ))
        __M_writer('</h4>\r\n    <hr>\r\n\r\n')
        if ingredient_array:
            __M_writer('      <h3>Ingredients</h3>\r\n')
            for item in ingredient_array:
                __M_writer('        <h4>')
                __M_writer(str( item[0] ))
                __M_writer(' ')
                __M_writer(str( item[1] ))
                __M_writer(' ')
                __M_writer(str( item[2] ))
                __M_writer('</h4>\r\n')
        __M_writer('\r\n    <hr>\r\n\r\n    <form method="POST" action="/homepage/newRecipe.submit/">\r\n')
        for field in directionsForm:
            __M_writer('        <div class="form-field-div">\r\n          <h3 class="form-label">')
            __M_writer(str( field.label_tag() ))
            __M_writer('</h3>\r\n          ')
            __M_writer(str( field ))
            __M_writer('\r\n        </div>\r\n')
        __M_writer('      <input class="btn btn-info btn-lg" type="submit" value="Finish" />\r\n    </form>\r\n\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Kristin/Desktop/mycookbook/homepage/templates/newRecipe.directions.html", "uri": "newRecipe.directions.html", "source_encoding": "utf-8", "line_map": {"28": 0, "44": 1, "49": 5, "54": 9, "59": 40, "65": 3, "71": 3, "77": 7, "83": 7, "89": 11, "100": 11, "101": 15, "102": 15, "103": 16, "104": 16, "105": 17, "106": 17, "107": 20, "108": 21, "109": 22, "110": 23, "111": 23, "112": 23, "113": 23, "114": 23, "115": 23, "116": 23, "117": 26, "118": 30, "119": 31, "120": 32, "121": 32, "122": 33, "123": 33, "124": 36, "130": 124}}
__M_END_METADATA
"""
