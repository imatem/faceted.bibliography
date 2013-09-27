<!DOCTYPE html>
<html>
  <head>
    <title>
      Tutorialsavvy.com : Bottle framework template demo
    </title>
    
  </head>
  <body>
  %import modules.interface as interface
  %from sets import Set
  %set_empty = Set([])
  %interface_principal = interface.interface(set_empty,"researchers.txt","archivo.bib")
  %interface_principal.ini_listas() 
  %list_c = interface_principal.list_citation 
  %list_r = interface_principal.list_reference 
  %interface_citation  = interface.interface(list_c,"researchers.txt","archivo.bib")
  %interface_reference = interface.interface(list_r,"researchers.txt","archivo.bib")
  %interface_citation.ini_listas()
  %interface_reference.ini_listas()
  %list_author= sorted(interface_principal.list_author )
  %list_type=sorted(interface_principal.list_type)
  %list_year = sorted(interface_principal.list_year)
  %list_journal = sorted(interface_principal.list_journal)
  %list_collaborator = sorted(interface_principal.list_collaborator)
  %list_objs = sorted(interface_principal.list_objs)
  %lista =list
  %list_string_obj = interface_principal.return_list_objs()
 
  {{lista}}
  <br>
  {{list}}
  <br><br>
  {{list_author}}<br>
  {{list_type}}<br>
  {{list_journal}}<br>
  {{list_year}}<br>
  {{list_collaborator}}<br>
  <br><br>
  {{list_objs}}
  <br><br>
  %for item in list_string_obj:
      {{item}} <br><br>
   <br><br>
  </body>
</html>
