from xml.etree import ElementTree

class serial_message:
    def __init__(self):
        with open('imc.xml', 'rt') as f:
            self.tree = ElementTree.parse(f)
            self.serial = ""
            self.form_list = []

    def parse_message(self):
        for node in self.tree.iter('message'):            
            self.parse_field(node)
            self.get_serial()
            self.form_list = []            
           
    def parse_field(self, message_node):
        for field_node in message_node.iter('field'):
            #print "\n"
            type = field_node.attrib.get('type')
                        
            if type is not None:
                print "\ttype: " + type
                form = self.format(type)
                self.form_list.append(form)             
                   
    def get_serial(self):
        self.serial = self.serial.join(self.form_list)
        print self.serial

    def format(self, type):
        if(type == 'int8_t'):
            return 'b'
        elif(type == 'uint8_t'):
            return 'B'
        elif(type == 'int16_t'):
            return 'h'
        elif(type == 'uint16_t'):
            return 'H'
        elif(type == 'int32_t'):
            return 'i'
        elif(type == 'uint32_t'):
            return 'I'
        elif(type == 'int64_t'):
            return 'q'
        elif(type == 'fp32_t'):
            return 'f'
        elif(type == 'fp64_t'):
            return 'd'
        else:
            return "?"
        
ms = serial_message()
ms.parse_message()

