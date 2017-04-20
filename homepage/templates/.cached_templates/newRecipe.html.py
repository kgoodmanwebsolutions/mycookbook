# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492710763.7781
_enable_loop = True
_template_filename = 'C:/Users/Kristin/Desktop/mycookbook/homepage/templates/newRecipe.html'
_template_uri = 'newRecipe.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['bannerArea', 'mainContent', 'title']


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
        recipeInfoForm = context.get('recipeInfoForm', UNDEFINED)
        def bannerArea():
            return render_bannerArea(context._locals(__M_locals))
        def mainContent():
            return render_mainContent(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
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
        recipeInfoForm = context.get('recipeInfoForm', UNDEFINED)
        def mainContent():
            return render_mainContent(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content container">\r\n    <h1>Submit New Recipe - Step 1</h1>\r\n\r\n    <form method="POST" action="/homepage/newRecipe.info/">\r\n')
        for field in recipeInfoForm:
            if field.name == 'meals':
                __M_writer('        <h4 class="form-label">')
                __M_writer(str( field.label_tag() ))
                __M_writer('</h4>\r\n          <div class="form-field-div checkboxes meals">\r\n            ')
                __M_writer(str( field ))
                __M_writer('\r\n          </div>\r\n')
            else:
                __M_writer('          <div class="form-field-div">\r\n            <h4 class="form-label">')
                __M_writer(str( field.label_tag() ))
                __M_writer('</h4>\r\n            ')
                __M_writer(str( field ))
                __M_writer('\r\n          </div>\r\n')
        __M_writer('      <input class="btn btn-info btn-lg" type="submit" value="Next" />\r\n    </form>\r\n\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n  New Recipe - Step 1 | My Cookbook\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Kristin/Desktop/mycookbook/homepage/templates/newRecipe.html", "source_encoding": "utf-8", "line_map": {"67": 7, "73": 11, "80": 11, "81": 16, "82": 17, "83": 18, "84": 18, "85": 18, "86": 20, "87": 20, "88": 22, "89": 23, "90": 24, "91": 24, "92": 25, "93": 25, "94": 29, "100": 3, "40": 1, "28": 0, "106": 3, "45": 5, "112": 106, "50": 9, "55": 33, "61": 7}, "uri": "newRecipe.html"}
__M_END_METADATA
"""
