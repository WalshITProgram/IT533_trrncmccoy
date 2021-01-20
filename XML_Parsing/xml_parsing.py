from bs4 import BeautifulSoup


my_file = open("Test_Files/famous_quotes.xml", encoding="utf=8")

my_text = my_file.read()

my_xml = BeautifulSoup(my_text, "lxml")
