import os
import subprocess as sp

paths = {
    'notepad': "C:\\windows\\system32\\notepad.exe",
}

def open_camera():
    sp.run('start microsoft.windows.camera', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])

def open_cmd():
    os.system('start cmd')