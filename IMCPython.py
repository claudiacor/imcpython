#!/usr/bin/env/python
from jinja2 import Environment, FileSystemLoader
import os
from xml.etree import ElementTree


class IMCPython:    
    def __init__(self):
        with open('imc.xml', 'rt') as f:
            self.tree = ElementTree.parse(f)
        self.abbrev_lista = []
        self.mabbrev_lista = []
        self.type_lista = []
        self.abb_type = []
        self.THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        self.j2_env = Environment(loader=FileSystemLoader(self.THIS_DIR), trim_blocks = True)
        self.out = ""
        self.serial = ""
        self.form_list = []
            
    def parse_message(self):
        for node in self.tree.iter('message'):
            m_id = node.attrib.get('id')
            m_name = node.attrib.get('name')
            m_abbrev = node.attrib.get('abbrev')
            m_source = node.attrib.get('source')
            self.parse_field(node)
            self.get_serial()
            if m_abbrev is not None:
                self.mabbrev_lista.append(m_abbrev)
           
            aux = self.j2_env.get_template('Template.py').render(abb_type_form_list = self.abb_type_form, mabbrev_list = self.mabbrev_lista)
            self.out += aux
            self.out += "\n"
            self.form_list = [] 
            self.abbrev_lista = []
            self.mabbrev_lista = []  
                       
           #criar tuplo com o abbrev e o tipo 
                               
    def parse_field(self, message_node):
        for field_node in message_node.iter('field'):
            name = field_node.attrib.get('name')
            self.abbrev = field_node.attrib.get('abbrev')
            type = field_node.attrib.get('type')
            unit = field_node.attrib.get('unit')
            
            if self.abbrev is not None:
                self.abbrev_lista.append(self.abbrev)
                
            if type is not None:
            	print "\ttype: " + type
            	form = self.format(type)
                self.form_list.append(form)   
                self.type_lista.append(type)
            	
       	self.abb_type_form = zip(self.abbrev_lista,self.type_lista,self.form_list)

    def get_serial(self):
    	self.serial = self.serial.join(self.form_list)
        print self.serial
        
    def format(self, type):
        if(type == 'int8_t'):
            return '\'b\''
        elif(type == 'uint8_t'):
            return '\'B\''
        elif(type == 'int16_t'):
            return '\'h\''
        elif(type == 'uint16_t'):
            return '\'H\''
        elif(type == 'int32_t'):
            return '\'i\''
        elif(type == 'uint32_t'):
            return '\'I\''
        elif(type == 'int64_t'):
            return '\'q\''
        elif(type == 'fp32_t'):
            return '\'f\''
        elif(type == 'fp64_t'):
            return '\'d\''
        elif(type == 'plaintext'):
            #o len tem que ser do q esta dentro da variavel
            return "str(len(self." + self.abbrev + ")) + \'s\'"
        else:
            return "?"
        
nw = IMCPython()
nw.parse_message()

with open('src_generated/Definitions.py','wb') as f:
    f.write('import struct\n')
with open("src_generated/Definitions.py", "ab") as f:
    f.write("from copy import deepcopy\n")
with open("src_generated/Definitions.py", "ab") as f:
    f.write(nw.out.encode('latin-1'))

    #copiar o message.py para o src_generated
with open('Message.py','rb') as ms:
    data = ms.read()
    with open('src_generated/Message.py','wb') as m:
        m.write(data)
