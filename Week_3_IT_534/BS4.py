from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
"""
Import Packages:
* PIL
* bs4
Create Variable to open file
Create function to open file 
Encode yext with ascii
"""

my_file = open("text_files/employee_data.xml", encoding= "utf-8")
my_text = my_file.read()
encoded_string = my_text.encode("ascii", "ignore")
decode_string = encoded_string.decode()
"""
Call Instance for for BeautifulSoup 
Inside parameters:
* Decode String
* XML
"""
my_xml = BeautifulSoup(decode_string, "xml")
"""
Create a 4 variables:
Profile Pic
Title 
Phone
Name
Add 4 varaibles to their own list 
"""

my_profiles = my_xml.find_all("profile_pic")
my_titles = my_xml.find_all("title")
my_phone_numbers = my_xml.find_all("phone")
my_names = my_xml.find_all("emp_name")
names = []
phone_numbers = []
profile_pics = []
titles = []
"""
Create four loop that iterate through variable 
"""
for name in my_names:
    names.append(name.get_text())
for title in my_titles:
    titles.append(title.get_text())
for phone_number in my_phone_numbers:
    phone_numbers.append(phone_number.get_text())
for my_profile in my_profiles:
    profile_pics.append(my_profile.get_text())

"""
Create a loop that enumerates through names and add text and font photos
Save photos to images/outputfiles
"""

for counter, value in enumerate(names):
    my_image = Image.open("images/" + profile_pics[counter])
    draw_text = ImageDraw.Draw(my_image)
    font = ImageFont.truetype("fonts/Syne-Regular.otf")
    draw_text.text((0,0), names[counter] + "\n" + titles[counter] + "\n" + phone_numbers[counter] + "\n", (255, 0, 0) , font)
    my_image.save("images/output_files/" + profile_pics[counter])




