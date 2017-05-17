{% for mabbrev in mabbrev_list %}
class {{mabbrev}}(Message):
  
    {% for abbrev, Type, Format in abb_type_form_list -%}
    {%-if ((Type == "uint8_t" ) or (Type == "int8_t") or (Type == 'int16_t') or (Type == 'uint16_t') or (Type == 'int32_t') or (Type == 'uint32_t') or (Type == 'int64_t') or (Type == 'fp32_t') or (Type == 'fp64_t')) -%}
    self.{{abbrev}} = 0
    {% elif Type == 'plaintext' -%}
    self.{{abbrev}} = ""
    {% elif (Type == 'rawdata' or Type == 'message-list') -%}
    self.{{abbrev}} = []
    {% elif (Type == 'message') -%}
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
        
    def serialize(self):
     	#return 

	{% if Type is not none -%}
	def serializeFields(self, buffer, offset = DUNE_IMC_CONST_HEADER_SIZE):
   		{% for abbrev, Type, Format in abb_type_form_list -%}    
	struct.pack_into('<' + {{Format}},buffer,offset, self.{{abbrev}})
   		{% endfor %}
  	{% endif -%}
{% endfor %}


