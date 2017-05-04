{% for mabbrev in mabbrev_list %}
class {{mabbrev}}(Message):
  
    {% for abbrev, Type in abb_type_list if ((Type == "uint8_t" ) or (Type == "int8_t") or (Type == 'int16_t') or (Type == 'uint16_t') or (Type == 'int32_t') or (Type == 'uint32_t') or (Type == 'int64_t') or (Type == 'fp32_t') or (Type == 'fp64_t')) -%}
    self.{{abbrev}} = 0
    {% endfor -%}
    	
   	{%- for abbrev, Type in abb_type_list if ((Type != "uint8_t" ) and (Type != "int8_t") and (Type != 'int16_t') and (Type != 'uint16_t') and (Type != 'int32_t') and (Type != 'uint32_t') and (Type != 'int64_t') and (Type != 'fp32_t') and (Type != 'fp64_t')) -%}
	self.{{abbrev}} = ""
    {% endfor %}	
    {% for abbrev, Type in abb_type_list -%}
    def get_{{abbrev}}(self):
        return self.{{abbrev}}

    {% endfor -%}

    {% for abbrev, Type in abb_type_list -%}
    def set_{{abbrev}}(self,new):
        self.{{abbrev}} = new
        
    {% endfor -%}
    def get_abbrev(self):
        return "{{mabbrev}}"

    def clone(self):
        return deepcopy(self) 
        
    def serialize(self):
     	#return 
{% endfor %}
