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
        self.THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        self.j2_env = Environment(loader=FileSystemLoader(self.THIS_DIR), trim_blocks = True)
        self.out = ""
            
    def parse_message(self):
        for node in self.tree.iter('message'):
            m_id = node.attrib.get('id')
            m_name = node.attrib.get('name')
            m_abbrev = node.attrib.get('abbrev')
            m_source = node.attrib.get('source')
            self.parse_field(node)
            if m_abbrev is not None:
                self.mabbrev_lista.append(m_abbrev)
           
            aux = self.j2_env.get_template('all.py').render(abbrev_list = self.abbrev_lista, mabbrev_list = self.mabbrev_lista)
            self.out += aux
            self.out += "\n"
            self.abbrev_lista = []
            self.mabbrev_lista = []            
                               
    def parse_field(self, message_node):
        for field_node in message_node.iter('field'):
            name = field_node.attrib.get('name')
            abbrev = field_node.attrib.get('abbrev')
            type = field_node.attrib.get('type')
            unit = field_node.attrib.get('unit')
            
            if abbrev is not None:
                self.abbrev_lista.append(abbrev)

nw = IMCPython()
nw.parse_message()

with open("new_file.py", "w") as f:
    f.write(nw.out.encode('latin-1'))
  
  
