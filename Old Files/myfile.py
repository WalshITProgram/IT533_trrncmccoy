from bs4 import BeautifulSoup
import xml
import os
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files))

with open('famous_qoutes.xml', 'r') as f:
    data = f.read()
Bs_data = BeautifulSoup(data, "xml") 
