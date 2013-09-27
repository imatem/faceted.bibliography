#coding: utf-8
from bottle import route, error, post, get, run, static_file, abort, redirect, response, request, template, SimpleTemplate
import modules.interface as interface
from sets import Set

@route('/')
@route('/index.html') 
@route('/index.html/')
def index():
    set_empty = Set([])
    interface_principal = interface.interface(set_empty,"researchers.txt","archivo.bib")
    interface_principal.ini_listas()
    
    list_c = interface_principal.list_citation 
    list_r = interface_principal.list_reference 
    interface_citation  = interface.interface(list_c,"researchers.txt","archivo.bib")
    interface_reference = interface.interface(list_r,"researchers.txt","archivo.bib")
    interface_citation.ini_listas()
    interface_reference.ini_listas()
    list_author= interface_principal.list_author 
    list_type=interface_principal.list_type
    list_year = interface_principal.list_year
    list_journal = interface_principal.list_journal
    list_collaborator = interface_principal.list_collaborator
    
    
    string =''
    for item in interface_principal.list_type:
        string = string + item + "</br>"
    string = "flower"
    list_a = interface_principal.list_year
    i=0
    list_objs = sorted(interface_principal.list_objs)
    tpl= template('temp', list=list_a) 
    return tpl
 
@route('/myapp/favourite/')
@route('/myapp/favourite/<item>')
def favourite(item):
    return template('favourite_template', item=item)


@route('/myapp/apphello')
@route('/myapp/apphello/')
def apphello():
    #tpl= template('hello {{name}}!', name='world')
    tpl= template('hello')
    return tpl
    
@route('/raise_error')
def raise_error():
    abort(404, "error...")
 
@route('/redirect')
def redirect_to_index():
    redirect('/index')
 
@route('/ajax')
def ajax_response():
    return {'dictionary': 'you will see ajax response right? Content-Type will be "application/json"'}
 
@error(404)
def error404(error):
    return '404 error !!!!!'
 
@get('/upload')
def upload_view():
    return """
        <form action="/upload" method="post" enctype="multipart/form-data">
          <input type="submit" name="test" value="boton 1" />
        </form>
        """    
        
 
@post('/upload')
def do_upload():
    test = request.forms.get('test')
    #if name is not None and data is not None:
    #    raw = data.file.read() # small files =.=
    #    filename = data.filename
    #    return "Hello s! You uploaded s (d bytes)."  (name, filename, len(raw))
    if test is  not None:
        return template('hello')
    else:
        redirect('/upload')
    #return "You missed a field."
 
run(host='localhost', port=8000, reloader=True)
