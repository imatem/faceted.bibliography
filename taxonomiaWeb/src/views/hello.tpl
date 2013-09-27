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
  %list_empty = Set([])
  %interface_principal = interface.interface(list_empty,"researchers.txt","archivo.bib")
  %interface_principal.ini_listas()
  %list_c = interface_principal.list_citation 
  %list_r = interface_principal.list_reference 
  %interface_citation  = interface.interface(list_c,"researchers.txt","archivo.bib")
  %interface_reference = interface.interface(list_r,"researchers.txt","archivo.bib")
  %interface_citation.ini_listas()
  %interface_reference.ini_listas()
  %list_author= interface_principal.list_author 
  %list_type=interface_principal.list_type
  %list_year = interface_principal.list_year
  %list_journal = interface_principal.list_journal
  %list_collaborator = interface_principal.list_collaborator
  %
  <br>
 
  
  
  </body>
</html>
