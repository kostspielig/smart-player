from distutils.core import setup
import py2exe

setup(version="0.1",
      license="GPL V3",
      scripts=['x50608460.py'],
      console=['x50608460.py'],
      options={"py2exe": {"bundle_files": 1}},
      zipfile=None
)
