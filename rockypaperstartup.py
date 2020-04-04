from runpy import run_path as r
from sys import exit as e
try:
    while True:
        r(path_name="rockypaper.py")
except (KeyboardInterrupt, EOFError): #if ^C or ^D
    e("\nSuccessfully exited rockyPaper.")
except: #any other error
    e("An unknown error occured :/")
