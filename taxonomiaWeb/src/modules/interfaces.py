'''
Created on 17/09/2013

@author: Alejandra
'''
import interface
import sys
from sets import Set
class interfaces(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        list_empty = Set([])
        self.interface_principal = interface.interface(list_empty,"researchers.txt","archivo.bib")
        self.interface_principal.ini_listas()
        
        self.list_c = self.interface_principal.list_citation #objetos
        self.list_r = self.interface_principal.list_reference #objetos
        
        self.interface_citation = interface.interface(self.list_c,"researchers.txt","archivo.bib")
        self.interface_reference = interface.interface(self.list_r,"researchers.txt","archivo.bib")
        self.interface_citation.ini_listas()
        self.interface_reference.ini_listas()
        
    def interaction(self):
        list_input = Set([])
        list_input_citation = Set([])
        list_input_reference = Set([])
        count = 0
        while True:
            
            print "\nLista de objetos: ",self.interface_principal.list_objs.__len__()
            print self.interface_principal.list_objs
            
            print "\nLista de conceptos"
            if count == 0:
                print self.interface_principal.list_author
                print self.interface_principal.list_type
                print self.interface_principal.list_year
                print self.interface_principal.list_journal
                print self.interface_principal.list_collaborator
                
                print "\n\n Facetas de las citas \t Num objetos: ", self.interface_citation.list_objs.__len__()
                print self.interface_citation.list_year
                print self.interface_citation.list_type
                print self.interface_citation.list_objs
#                print "\n\n Facetas de las referencias"
#                print self.interface_reference.list_year
#                print self.interface_reference.list_type
                

            else:
                print self.interface_principal.list_author
                print self.interface_principal.list_val_author, "\n"
                print self.interface_principal.list_type
                print self.interface_principal.list_val_type, "\n"
                print self.interface_principal.list_year
                print self.interface_principal.list_val_year, "\n"
                print self.interface_principal.list_journal
                print self.interface_principal.list_val_journal, "\n"
                print self.interface_principal.list_collaborator
                print self.interface_principal.list_val_collaborator, "\n"
                print "\nLista de conceptos citas seleccionados: "
                print list_input_citation 
                print "\n\n Facetas de las citas", self.interface_citation.list_objs.__len__()
                print self.interface_citation.list_year
                print self.interface_citation.list_val_year
                print self.interface_citation.list_type
                print self.interface_citation.list_val_type
                print self.interface_citation.list_objs
                print "\nLista de conceptos citas seleccionados: "
                print list_input_citation 
#                print "\n\n Facetas de las referencias"                
#                print self.interface_reference.list_year
#                print self.interface_reference.list_val_year
#                print self.interface_reference.list_type
#                print self.interface_reference.list_val_type
                
                 
            
            print "\nLista de conceptos seleccionados: "
            print list_input

            sys.stdout.flush()
            focus = raw_input('\n>')
            focus_citation = raw_input('\n>')
            focus_reference = raw_input('\n>')
            if self.interface_principal.tree.G.has_node(focus): #focus action click
                if focus in  list_input:
                        list_input.remove(focus)
                else:
                        list_input.add(focus)
                self.interface_principal.get_list_objects(list_input)
                "Lista de objetos principal"
                self.interface_principal.print_list_objs()
            
                if self.list_c != self.interface_principal.list_citation:
                    self.list_c = self.interface_principal.list_citation
                    self.interface_citation.tree.building_tree(self.list_c,"researchers.txt")
                    list_input_citation.clear()
                    self.interface_citation.ini_listas()
                    self.interface_citation.get_list_objects(list_input_citation)


                if self.list_r != self.interface_principal.list_reference:
                    self.list_r = self.interface_principal.list_reference
                    self.interface_reference.tree.building_tree(self.list_r,"researchers.txt")
                    list_input_reference.clear()
                    self.interface_reference.ini_listas()
                    self.interface_reference.get_list_objects(list_input_reference)
                    

                count = count + 1
                
                
            if self.interface_citation.tree.G.has_node(focus_citation):                
                if focus_citation in list_input_citation:
                    list_input_citation.remove(focus_citation)
                else:
                    list_input_citation.add(focus_citation)
                "Lista de objetos citas"
                self.interface_citation.get_list_objects(list_input_citation)
                self.interface_citation.print_list_objs()
                count = count + 1
            
            if self.interface_reference.tree.G.has_node(focus_reference):                
                if focus_reference in list_input_reference:
                    list_input_reference.remove(focus_reference)
                else:
                    list_input_reference.add(focus_reference)
                "Lista de objetos referencias"
                self.interface_reference.get_list_objects(list_input_reference)
                self.interface_reference.print_list_objs()
                
                count = count + 1
