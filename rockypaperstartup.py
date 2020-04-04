from runpy import run_path as r
from sys import exit as e
try:
    while True:
        r(file_path="rockypaper.py")
except (KeyboardInterrupt, EOFError): #if ^C or ^D
    e("Successfully exited rockyPaper.")
except: #any other error
    print("An unknown error occured.")
