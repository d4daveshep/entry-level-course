import os
from os import path

directory_to_create ="test_directory/inner_directory"
if not path.exists(directory_to_create):
    os.mkdir(directory_to_create)
os.chdir("test_directory")
print(os.getcwd())
print(os.listdir())
os.rmdir("inner_directory")
print(os.listdir())
