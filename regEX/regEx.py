import re

str = "1, Hemlal Dulal,+977-9898989889, dulal@gmail.com,+977-9860606162,"

# matched = re.search("[0-9]{10,10}", str)
matched = re.findall(
    "\+[0-9]{3,3}-[0-9]{10,10}", str
)  #! number of matched pattern in a list

print(matched)
