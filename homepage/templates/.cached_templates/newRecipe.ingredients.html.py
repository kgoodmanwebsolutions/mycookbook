# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492572974.121332
_enable_loop = True
_template_filename = 'C:/Users/Kristin/Desktop/mycookbook/homepage/templates/newRecipe.ingredients.html'
_template_uri = 'newRecipe.ingredients.html'
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
        addIngredientForm = context.get('addIngredientForm', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        ingredient_array = context.get('ingredient_array', UNDEFINED)
        cook_time = context.get('cook_time', UNDEFINED)
        createIngredientForm = context.get('createIngredientForm', UNDEFINED)
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
        __M_writer('\r\n  New Recipe - Step 2 | My Cookbook\r\n')
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
        addIngredientForm = context.get('addIngredientForm', UNDEFINED)
        ingredient_array = context.get('ingredient_array', UNDEFINED)
        cook_time = context.get('cook_time', UNDEFINED)
        createIngredientForm = context.get('createIngredientForm', UNDEFINED)
        def mainContent():
            return render_mainContent(context)
        recipe_name = context.get('recipe_name', UNDEFINED)
        source = context.get('source', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content container">\r\n    <h1>Submit New Recipe - Step 2</h1>\r\n\r\n    <h4>Recipe Name: ')
        __M_writer(str( recipe_name ))
        __M_writer('</h4>\r\n    <h4>Total Cook Time: ')
        __M_writer(str( cook_time ))
        __M_writer('</h4>\r\n    <h4>Source: ')
        __M_writer(str( source ))
        __M_writer('</h4>\r\n\r\n    <form method="POST" action="/homepage/newRecipe.ingredients/">\r\n      <table id="ing-table">\r\n        <tr>\r\n')
        for field in addIngredientForm:
            if field.name == 'measurement':
                __M_writer('              <th class="form-label"><h4>')
                __M_writer(str( field.label_tag() ))
                __M_writer(' <a href="#" data-toggle="modal" data-target="#helpModal"><span class="glyphicon glyphicon-question-sign"></span></a></h4>\r\n              </th>\r\n')
            else:
                __M_writer('              <th class="form-label"><h4>')
                __M_writer(str( field.label_tag() ))
                __M_writer('</h4></th>\r\n')
        __M_writer('        </tr>\r\n')
        if ingredient_array:
            for item in ingredient_array:
                __M_writer('          <tr>\r\n            <td><h5>')
                __M_writer(str( item[0] ))
                __M_writer('</h5></td>\r\n            <td><h5>')
                __M_writer(str( item[1] ))
                __M_writer('</h5></td>\r\n            <td><h5>')
                __M_writer(str( item[2] ))
                __M_writer('</h5></td>\r\n          </tr>\r\n')
        __M_writer('        <tr class="form-field-div">\r\n')
        for field in addIngredientForm:
            if field.name == 'ingredient':
                __M_writer('              <td><nobr>')
                __M_writer(str( field ))
                __M_writer(' <input class="btn btn-primary" type="submit" value="Add" name="addIngredient"/></nobr></td>\r\n')
            else:
                __M_writer('              <td>')
                __M_writer(str( field ))
                __M_writer('</td>\r\n')
        __M_writer('        </tr>\r\n    </table>\r\n    <br>\r\n    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal">Create New Ingredient</button>\r\n    <br><br><br>\r\n\r\n    <a class="btn btn-info btn-lg" href="/homepage/newRecipe.directions/">Done Adding Ingredients</a>\r\n\r\n    <div id="myModal" class="modal fade" role="dialog">\r\n      <div class="modal-dialog">\r\n        <div class="modal-content">\r\n          <div class="modal-header">\r\n            <button type="button" class="close" data-dismiss="modal">&times;</button>\r\n            <h4 class="modal-title">Create New Ingredient</h4>\r\n          </div>\r\n          <div class="modal-body">\r\n            <form method="POST" action="/homepage/newRecipe.ingredients/">\r\n')
        for field in createIngredientForm:
            __M_writer('                <div class="form-field-div">\r\n                  <h4 class="form-label">')
            __M_writer(str( field.label_tag() ))
            __M_writer('</h4>\r\n                  ')
            __M_writer(str( field ))
            __M_writer('\r\n                </div>\r\n')
        __M_writer('              <input class="btn btn-primary" type="submit" value="Create" name="createIngredient"/>\r\n            </form>\r\n          </div>\r\n          <div class="modal-footer">\r\n            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n\r\n    <div id="helpModal" class="modal fade" role="dialog">\r\n      <div class="modal-dialog">\r\n        <div class="modal-content">\r\n          <div class="modal-header">\r\n            <button type="button" class="close" data-dismiss="modal">&times;</button>\r\n            <h4 class="modal-title">Measurement Conversion</h4>\r\n          </div>\r\n          <div class="modal-body">\r\n            <table id="measure-table">\r\n              <tr>\r\n                <th>Fraction</th>\r\n                <th>Decimal</th>\r\n              </tr>\r\n              <tr>\r\n                <td>1/8</td>\r\n                <td>0.125</td>\r\n              </tr>\r\n              <tr>\r\n                <td>1/4</td>\r\n                <td>0.25</td>\r\n              </tr>\r\n              <tr>\r\n                <td>1/3</td>\r\n                <td>0.333</td>\r\n              </tr>\r\n              <tr>\r\n                <td>3/8</td>\r\n                <td>0.375</td>\r\n              </tr>\r\n              <tr>\r\n                <td>1/2</td>\r\n                <td>0.5</td>\r\n              </tr>\r\n              <tr>\r\n                <td>5/8</td>\r\n                <td>0.625</td>\r\n              </tr>\r\n              <tr>\r\n                <td>2/3</td>\r\n                <td>0.667</td>\r\n              </tr>\r\n              <tr>\r\n                <td>3/4</td>\r\n                <td>0.75</td>\r\n              </tr>\r\n              <tr>\r\n                <td>7/8</td>\r\n                <td>0.875</td>\r\n              </tr>\r\n            </table>\r\n          </div>\r\n          <div class="modal-footer">\r\n            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Kristin/Desktop/mycookbook/homepage/templates/newRecipe.ingredients.html", "uri": "newRecipe.ingredients.html", "source_encoding": "utf-8", "line_map": {"28": 0, "45": 1, "50": 5, "55": 9, "60": 140, "66": 3, "72": 3, "78": 7, "84": 7, "90": 11, "102": 11, "103": 15, "104": 15, "105": 16, "106": 16, "107": 17, "108": 17, "109": 22, "110": 23, "111": 24, "112": 24, "113": 24, "114": 26, "115": 27, "116": 27, "117": 27, "118": 30, "119": 31, "120": 32, "121": 33, "122": 34, "123": 34, "124": 35, "125": 35, "126": 36, "127": 36, "128": 40, "129": 41, "130": 42, "131": 43, "132": 43, "133": 43, "134": 44, "135": 45, "136": 45, "137": 45, "138": 48, "139": 65, "140": 66, "141": 67, "142": 67, "143": 68, "144": 68, "145": 71, "151": 145}}
__M_END_METADATA
"""
