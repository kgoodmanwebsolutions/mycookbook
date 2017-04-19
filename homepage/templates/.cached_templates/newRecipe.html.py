# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492572929.2694588
_enable_loop = True
_template_filename = 'C:/Users/Kristin/Desktop/mycookbook/homepage/templates/newRecipe.html'
_template_uri = 'newRecipe.html'
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
        recipeInfoForm = context.get('recipeInfoForm', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
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
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n  New Recipe - Step 1 | My Cookbook\r\n')
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
            __M_writer('        <div class="form-field-div checkboxes">\r\n          <h4 class="form-label">')
            __M_writer(str( field.label_tag() ))
            __M_writer('</h4>\r\n          ')
            __M_writer(str( field ))
            __M_writer('\r\n        </div>\r\n')
        __M_writer('      <input class="btn btn-info btn-lg" type="submit" value="Next" />\r\n    </form>\r\n\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Kristin/Desktop/mycookbook/homepage/templates/newRecipe.html", "uri": "newRecipe.html", "source_encoding": "utf-8", "line_map": {"28": 0, "40": 1, "45": 5, "50": 9, "55": 26, "61": 3, "67": 3, "73": 7, "79": 7, "85": 11, "92": 11, "93": 16, "94": 17, "95": 18, "96": 18, "97": 19, "98": 19, "99": 22, "105": 99}}
__M_END_METADATA
"""
