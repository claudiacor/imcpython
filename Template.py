{% for mabbrev in mabbrev_list %}
class {{mabbrev}}(Message):
   	
{% if abb_type_form_list|length != 0 %}
    def __init__(self):
{% endif %}
    {% for abbrev, Type, Format in abb_type_form_list -%}
    {% if ((Type == "uint8_t" ) or (Type == "int8_t") or (Type == 'int16_t') or (Type == 'uint16_t') or (Type == 'int32_t') or (Type == 'uint32_t') or (Type == 'int64_t') or (Type == 'fp32_t') or (Type == 'fp64_t')) %}
    self.{{abbrev}} = 0
    {% elif Type == 'plaintext' %}
    self.{{abbrev}} = ""
    {% elif (Type == 'rawdata' or Type == 'message-list') %}
    self.{{abbrev}} = []
    {% elif (Type == 'message') %}
    self.{{abbrev}} = None
    {% endif -%}
    {% endfor %}
    	
    {% for abbrev, Type, Format in abb_type_form_list -%}
    def get_{{abbrev}}(self):
        return self.{{abbrev}}

    {% endfor -%}

    {% for abbrev, Type, Format in abb_type_form_list -%}
    def set_{{abbrev}}(self,new):
        self.{{abbrev}} = new
        
    {% endfor -%}
    def get_abbrev(self):
        return "{{mabbrev}}"

    def clone(self):
        return deepcopy(self) 
        
    #def serialize(self):
     	#return 
     	
{% if abb_type_form_list|length != 0 %}
    def serializeFields(self, buffer, offset = DUNE_IMC_CONST_HEADER_SIZE):
    {% for abbrev, Type, Format in abb_type_form_list if Type is not none -%}
   	{% if Type == 'rawdata' or Type == 'plaintext' %}
    nbytes = len(self.{{abbrev}})
	struct.pack_into('<H' + str(nbytes) + {{Format}},buffer,offset, nbytes, self.{{abbrev}})
        offset += struct.calcsize('<' + str(nbytes) + {{Format}})
	{% else %}
	struct.pack_into('<' + {{Format}},buffer,offset, self.{{abbrev}})
    	offset += struct.calcsize('<' + {{Format}})
    {% endif %}  
    {% endfor %}

    def deserializeFields(self, buffer, offset = DUNE_IMC_CONST_HEADER_SIZE):
    {% for abbrev, Type, Format in abb_type_form_list if Type is not none -%}
    {% if Type == 'rawdata' or Type == 'plaintext' %}
    Nbytes = struct.unpack_from('<H',buffer,offset)
    	offset += struct.calcsize('<H')
    	self.{{abbrev}} = struct.unpack_from('<' + str(Nbytes) + {{Format}},buffer,offset)
        offset += struct.calcsize('<' + str(Nbytes) + {{Format}})
    {% else %}
    self.{{abbrev}} = struct.unpack_from('<' + {{Format}},buffer,offset)
        offset += struct.calcsize('<' + {{Format}})
    {% endif %} 
    {% endfor %}
{% endif %}
{% endfor %}


