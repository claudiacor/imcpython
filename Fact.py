    {% for mabbrev,  m_id in mabbrev_mid_list -%}
    if id == '{{mabbrev}}' or id == '{{m_id}}':
        return {{mabbrev}}()
    {% endfor -%}
