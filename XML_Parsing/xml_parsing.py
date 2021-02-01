from bs4 import BeautifulSoup
from xml.dom.minidom import parse
import parser
import re
import xml.etree.ElementTree as ET
import os
'''
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files))
'''

my_file = open("Test_Files/famous_quotes.xml", encoding="utf-8")

my_text = my_file.read()
for (index, character) in enumerate(my_text):
    try:
        encoder = character.encode("ascii")
    except:
        print(index, character, ord(character))
        if ord(character) == 8221:
            my_text = my_text.replace(character, "")


my_xml = BeautifulSoup(my_file, "xml")

my_qoutes = my_xml.find_all("qoute")

for qoute in my_qoutes:
    print(qoute.person.get_test())
    print("said" + qoute.qoute.get_text())
for (index, character) in enumerate(my_text):
    try:
        encoder = character.encode("ascii")
    except:
        print(index, character, ord(character))
        if ord(character) == 8221:
            my_text = my_text.replace(character, "")



