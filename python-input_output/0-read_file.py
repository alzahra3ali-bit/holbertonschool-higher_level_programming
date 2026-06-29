#!/usr/bin/python3
""defind function that Open file""
def read_file(filename=""):
    ""read And Print the file""
    with open(zahra,"r", encoding="UTF8") as f:
      print(f.read(), end="")
