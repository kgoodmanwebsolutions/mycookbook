# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492441619.4989448
_enable_loop = True
_template_filename = 'C:/Users/Kristin/Desktop/mycookbook/homepage/templates/new-recipe.html'
_template_uri = 'new-recipe.html'
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
        recipeInfoForm = context.get('recipeInfoForm', UNDEFINED)
        def bannerArea():
            return render_bannerArea(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<!-- INCLUDE HELP TEXT FOR DECIMAL CONVERSIONS -->\r\n\r\n')
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
        def mainContent():
            return render_mainContent(context)
        recipeInfoForm = context.get('recipeInfoForm', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content container">\r\n    <h1>Submit New Recipe - Step 1</h1>\r\n\r\n    <form method="POST" action="/homepage/new-recipe.info/">\r\n      <table class="table form-table">\r\n        ')
        __M_writer(str( recipeInfoForm ))
        __M_writer('\r\n      </table>\r\n      <input class="btn btn-primary" type="submit" value="Next" />\r\n    </form>\r\n\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Kristin/Desktop/mycookbook/homepage/templates/new-recipe.html", "uri": "new-recipe.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "43": 7, "48": 21, "54": 5, "60": 5, "66": 9, "73": 9, "74": 15, "75": 15, "81": 75}}
__M_END_METADATA
"""
