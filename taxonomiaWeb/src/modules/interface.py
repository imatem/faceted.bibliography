'''
Created on 27/08/2013

@author: Alejandra
'''
import arbol
import sys
import re
from sets import Set


class interface(object):
    '''
    classdocs
    '''
    def __init__(self,lista_objs,filenameAuthors,filenameBib):
        self.tree = arbol.arbol()
        
        if lista_objs.__len__()> 0:
            self.tree.building_tree(lista_objs,filenameAuthors)
        else:
            self.tree.construir_arbol(filenameAuthors,filenameBib)
        #objetos resultantes
        self.list_objs = Set([])
        # los objetos de cada concepto -- la extension de los conceptos seleccionados
        self.list_ext_author  = Set([])
        self.list_ext_journal = Set([])
        self.list_ext_type = Set([])
        self.list_ext_year = Set([])
        self.list_ext_collaborator = Set([])
        # los conceptos validos
        
        self.list_val_author = Set([])
        self.list_val_journal = Set([])
        self.list_val_type = Set([])
        self.list_val_year = Set([])
        self.list_val_collaborator = Set([])
        #lista de conceptos
        self.list_author = Set([])
        self.list_journal = Set([])
        self.list_type = Set([])
        self.list_year = Set([])
        self.list_collaborator = Set([])
        
        self.list_reference = Set([]) #lista de objetos referencia de todos las publicaciones validas
        self.list_citation = Set([]) #lista de objetos citas de todas las publicaciones validas
        
    def ini_listas(self):
        
                
        self.list_ext_author = self.tree.extension("author")
        self.list_objs = self.list_ext_author
        
        self.list_ext_collaborator = self.tree.extension("collaborator")
        self.list_objs = self.list_objs.union(self.list_ext_collaborator)
        
        self.list_ext_type = self.tree.extension("type")
        self.list_objs = self.list_objs.union(self.list_ext_type)
        
        self.list_ext_year = self.tree.extension("year")
        self.list_objs = self.list_objs.union(self.list_ext_year)
        
        self.list_ext_journal = self.tree.extension("journal")
        self.list_objs = self.list_objs.union(self.list_ext_journal)
        
        self.list_val_author = self.tree.valido("author", self.list_ext_author)
        self.list_val_collaborator = self.tree.valido("collaborator", self.list_ext_collaborator)
        self.list_val_type = self.tree.valido("type", self.list_ext_type)
        self.list_val_year = self.tree.valido("year", self.list_ext_year)
        self.list_val_journal = self.tree.valido("journal", self.list_ext_journal)

        self.list_author = self.list_val_author
        self.list_type = self.list_val_type
        self.list_year = self.list_val_year
        self.list_journal = self.list_val_journal
        self.list_collaborator = self.list_val_collaborator

        list_c = Set([])
        list_r = Set([])
        for item in self.list_objs:
            obj = self.tree.G.node[item]['data']
            list_c = list_c.union(obj.citation)  #union de listas
            list_r = list_r.union(obj.reference)
        self.list_citation = self.tree.get_objects_list(list_c)
        self.list_reference = self.tree.get_objects_list(list_r)
        
        
    def get_list_objects(self,list_input):
        
        if list_input.__len__()>0:
            self.calculo_concepto_author(list_input)
            self.calculo_concepto_journal(list_input)
            self.calculo_concepto_type(list_input)
            self.calculo_concepto_year(list_input)
            self.calculo_concepto_collaborator(list_input)
            
            for item in list_input:
                if item in self.list_year:
                    self.list_objs = self.list_objs.intersection(self.list_ext_year)
                 
                elif item in self.list_type:
                    self.list_objs = self.list_objs.intersection(self.list_ext_type)
                
                elif item in self.list_author:
                    self.list_objs = self.list_objs.intersection(self.list_ext_author)
                    
                elif item in self.list_collaborator:
                    self.list_objs = self.list_objs.intersection(self.list_ext_collaborator)

                elif item in self.list_journal:
                    self.list_objs = self.list_objs.intersection(self.list_ext_journal)
            
            self.list_val_author = sorted(self.tree.valido("author", self.list_objs))
            self.list_val_type = sorted(self.tree.valido("type", self.list_objs))
            self.list_val_journal = sorted(self.tree.valido("journal", self.list_objs))
            self.list_val_year = sorted(self.tree.valido("year", self.list_objs))
            self.list_val_collaborator = sorted(self.tree.valido("collaborator", self.list_objs))
            list_c = Set([])
            list_r = Set([])
            for item in self.list_objs:
                obj = self.tree.G.node[item]['data']
                list_c = list_c.union(obj.citation)  #union de listas
                list_r = list_r.union(obj.reference)
            
            #de la lista de objetos obtengo las citas y referencias que son IDs
            self.list_citation = self.tree.get_objects_list(list_c) #obtengo los objetos con los IDs pasados
            self.list_reference = self.tree.get_objects_list(list_r)
        else:
            self.ini_listas()
            

    def calculo_concepto_author(self,list_input):
        if list_input.intersection(self.list_author).__len__()>0:
            list_aux = Set([])
            for item in list_input:
                if item in self.list_author:
                    list_aux = self.tree.extension(item).union(list_aux)
                
            self.list_ext_author = list_aux
            self.list_objs = self.list_ext_author
            
    def calculo_concepto_collaborator(self,list_input):
        if list_input.intersection(self.list_collaborator).__len__()>0:
            list_aux = Set([])
            for item in list_input:
                if item in self.list_collaborator:
                    list_aux = self.tree.extension(item).union(list_aux)
                
            self.list_ext_collaborator = list_aux
            self.list_objs = self.list_ext_collaborator
            
    def calculo_concepto_year(self,list_input):
        if list_input.intersection(self.list_year).__len__()>0:
            list_aux = Set([])
            for item in list_input:
                if item in self.list_year:
                    list_aux = self.tree.extension(item).union(list_aux)
        
            self.list_ext_year = list_aux
            self.list_objs = self.list_ext_year
    def calculo_concepto_type(self,list_input):
        if list_input.intersection(self.list_type).__len__()>0:
            list_aux = Set([])
            for item in list_input:
                if item in self.list_type:
                    list_aux = self.tree.extension(item).union(list_aux)
        
            self.list_ext_type = list_aux
            self.list_objs = self.list_ext_type
        
    def calculo_concepto_journal(self,list_input):
        if list_input.intersection(self.list_journal).__len__()>0:
            list_aux = Set([])
            for item in list_input:
                if item in self.list_journal:
                    list_aux = self.tree.extension(item).union(list_aux)
        
            self.list_ext_journal = list_aux
            self.list_objs = self.list_ext_journal
            
            

    def print_list_objs(self):
        for item in self.list_objs:
            obj = self.tree.G.node[item]['data']
            print obj.idp, obj.type, obj.title,'\n', obj.author, obj.journal, obj.publisher, obj.year
            print "list citation ",sorted(obj.citation)
            print "list reference ",sorted(obj.reference), '\n\n'
            
        print "\n"
        
    def return_list_objs(self):
        list_string_obj = Set([])
        for item in self.list_objs:
            obj = self.tree.G.node[item]['data']
            
            cad1= obj.idp +', '+ obj.type +', ' + obj.title+', '
        
            cad2 = obj.journal +', '+  obj.publisher +', '+  obj.year  +', '
            cad3 = ', '.join(obj.author)
            cad4 = ', '.join(obj.citation)
            cad5= ', '.join(obj.reference)
            if cad4.__len__()>0:
                cadx=' Citedby: '+cad4 
            else:
                cadx = cad4
            if cad5.__len__()>0:
                cady=' References: '+cad5
            else:
                cady = cad5
            
            string = cad1 + cad3 + cad2 +cadx +cady
            list_string_obj.add(string)
            
        return list_string_obj
    