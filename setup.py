#! python3

import os
import sys

current_script = os.path.abspath(os.path.join(os.getcwd(), __file__))
current_dir = os.path.dirname(current_script)
modules_dir = os.path.join(current_dir, 'src', 'modules')
tests_dir = os.path.join(current_dir, 'src', 'tests')

path = ''
path_key = 'PYTHONPATH'

if path_key in os.environ:
    path = os.environ[path_key]

if modules_dir not in path.split(os.pathsep):
    addition = modules_dir

    if len(path) > 0:
        path = path + os.pathsep + addition
    else:
        path = addition

    command = 'setx -m ' + path_key + ' "' + path + '"'

    os.system(command)
