import re

def remove_pathernesses(string):
    return re.sub(r"\((.*?)\)", r"\1", string)

