    {% for mabbrev,  m_id in mabbrev_mid_list -%}
    if (name == '{{mabbrev}}'):
        return {{mabbrev}}()
    {% endfor -%}
