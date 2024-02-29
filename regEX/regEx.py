import re

str = "1, Hemlal Dulal, dulal@gmail.com,9860606162"

matched = re.search("[0-9]{10,10}", str)
print(matched)
