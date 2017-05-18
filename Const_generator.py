#!/usr/bin/env/python
from jinja2 import Environment, FileSystemLoader
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
j2_env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks = True)

new_version = input("New IMC version string: \n")
new_git_info = input("New Git repository information: \n")
new_const_md5 = input("New D5 sum of XML specification file: \n")
new_sync = input("New Synchronization number: \n")
new_sync_rev = input("New Reversed synchronization number: \n")
new_header_size = input("New Size of the header in bytes: \n")
new_footer_size = input("New Size of the footer in bytes: \n")
new_null_id = input("New Identification number of the null message: \n")
new_max_size = input("New Maximum message data size: \n")
new_unk_eid = input("New Unknown entity identifier: \n")
new_sys_eid = input("New System entity identifier: \n")


out = j2_env.get_template('Const_temp.py').render(version = new_version, git_info = new_git_info, const_md5 = new_const_md5, sync = new_sync, sync_rev = new_sync_rev, header_size = new_header_size, footer_size = new_footer_size, null_id = new_null_id, max_size = new_max_size, unk_eid = new_unk_eid, sys_eid = new_sys_eid)


print out
with open("Constantes.py", "w") as f:
    f.write(out.encode('latin-1'))
