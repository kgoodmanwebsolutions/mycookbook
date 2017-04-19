# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492614235.4891093
_enable_loop = True
_template_filename = 'C:/Users/Kristin/Desktop/mycookbook/homepage/templates/search.html'
_template_uri = 'search.html'
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
        def mainContent():
            return render_mainContent(context._locals(__M_locals))
        searchform = context.get('searchform', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def bannerArea():
            return render_bannerArea(context._locals(__M_locals))
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
        __M_writer('\r\n  Search | My Cookbook\r\n')
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
        searchform = context.get('searchform', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class="content container">\r\n      <h1>Search</h1>\r\n      <h4>Select ingredients from the list you want to search for. If an\r\n        ingredient isn\'t listed, there are no recipes currently with that\r\n        ingredient.\r\n      </h4>\r\n      <hr>\r\n      <form method="GET" action="/homepage/search.search/">\r\n        <div id="search-form">\r\n')
        for field in searchform:
            __M_writer('            <div class="form-field-div">\r\n              <h4 class="form-label">')
            __M_writer(str( field.label_tag() ))
            __M_writer('</h4>\r\n              <div class="checkboxes">\r\n                ')
            __M_writer(str( field ))
            __M_writer('\r\n              </div>\r\n            </div>\r\n')
        __M_writer('        </div>\r\n        <input class="btn btn-info btn-lg" class="search-btn" type="submit" value="Search" />\r\n      </form>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Kristin/Desktop/mycookbook/homepage/templates/search.html", "uri": "search.html", "source_encoding": "utf-8", "line_map": {"28": 0, "40": 1, "45": 5, "50": 9, "55": 33, "61": 3, "67": 3, "73": 7, "79": 7, "85": 11, "92": 11, "93": 21, "94": 22, "95": 23, "96": 23, "97": 25, "98": 25, "99": 29, "105": 99}}
__M_END_METADATA
"""
