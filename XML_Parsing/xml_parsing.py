from bs4 import BeautifulSoup
import parser
import xml.etree.ElementTree as ET
import os
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files))

my_file = open("Test_Files/famous_quotes.xml", encoding="utf-8")

my_text = my_file.read()


my_xml = BeautifulSoup(my_text, "xml")