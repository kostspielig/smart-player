
from distutils.core import setup
import py2exe,sys,os

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
    if os.path.basename(pathname).lower() in ("wsock32.dll", "user32.dll", "advapi32.dll", "shell32.dll", "kernel32.dll", "ntdll.dll", "shlwapi.dll", "msvcrt.dll", "ws2_32.dll", "gdi32.dll", "rpcrt4.dll", "secur32.dll", "ws2help.dll"):
        return 0
    return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL

setup(
    windows=[
        {'script': 'main.py'
         }],
    options={
        "py2exe":{
            "unbuffered": True,
            "optimize": 2,
            "bundle_files":1
            }
        },
    zipfile=None
    )
