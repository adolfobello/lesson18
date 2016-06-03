"""
import os

BASE_DIR = os.path.abspath(__file__)
print( BASE_DIR )
#/Users/adolfobello/dja1.9.6-pyt3.5/lesson_django18_src/pruebas.py

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print( BASE_DIR )
#/Users/adolfobello/dja1.9.6-pyt3.5/lesson_django18_src

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print( BASE_DIR )
#/Users/adolfobello/dja1.9.6-pyt3.5

print( os.path.join(BASE_DIR, "newsletter", "templates") )
"""
