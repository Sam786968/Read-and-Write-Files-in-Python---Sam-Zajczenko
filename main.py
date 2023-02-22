# File Objects
# Introduction to moving and creating txt files with python.
# This will allows us to have human variable interaction.

# f = open("test.txt","r")
# print(f.readlines())
# f.close()

# with open("test.txt","r") as f:
#   f_contents = f.readline()
#   print(f_contents, end="")

#   f_contents = f.readline()
#   print(f_contents, end="")

# employee_file = open("employees.txt","r")
# for employee in employee_file.readlines():
#   print(employee)
# employee_file.close()

# To append, create, and write documents.
# with open('readme.txt', 'w') as f:
#   f.write('readme')
# with open('readme.txt', 'w') as f:
#   f.write('I dont care.')
# with open('readme.txt', 'a') as f:
#   f.write('I dont care. 2') 

# Create a file through python code.
# Get it to accept user input.
# To append to the content.

# First Way
# with open('new_file.txt','w') as f:
#   f.write()
# user_input = input("How was your day? ")
# with open('new_file.txt','a') as f: 
#   f.write(user_input)

# Second Way
# with open('user.txt', 'a') as f:
#   input = ("How was your day? ")
#   f.write(input)

# --- Second Group of Work ---
# import urllib
# import json

import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Best-Sellers-Books/zgbs/books"
headers = {
  'user_agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

books = soup.find_all()