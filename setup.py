from distutils.core import setup
import py2exe

setup(version="0.1",
      license="GPL V3",
      scripts=['main.py'],
      console=['main.py'],
      options={"py2exe": {"bundle_files": 1}},
      zipfile=None
)
