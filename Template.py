import struct
from copy import copy

{% for mabbrev in mabbrev_list %}
class {{mabbrev}}(Message):
    {% for abbrev in abbrev_list -%}
    def get_{{abbrev}}(self):
        print "{{abbrev}} - " + str(self.{{abbrev}})
        
    {% endfor %}

    {% for abbrev in abbrev_list -%}
    def set_{{abbrev}}(self,new):
        self.{{abbrev}} = new
        
    {% endfor -%}
    def get_name(self):
        return "{{mabbrev}}"

    def clone(self):
        return copy(self)

    
{% endfor %}
