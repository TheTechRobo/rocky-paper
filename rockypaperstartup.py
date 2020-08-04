from runpy import run_path as r
from sys import exit as e
try:
    choice = input("Select an option:\n    1 - Command-line version\n    2 - Graphical version\n>:")
except KeyboardInterrupt:
    print("\rExited.")
except EOFError:
    print("Task failed successfully.")
if choice == "1":
    path = "rockypaper.py"
elif choice == "2":
    path = "rockypapergui.py"
else:
    print("Defaulting to command-line edition.")
    path = "rockypaper.py"
try:
    while True:
        r(path_name=path)
except (KeyboardInterrupt, EOFError): #if ^C
    e("\nSuccessfully exited rockyPaper.")
except Exception as ename: #any other error
    e("\nAn unknown error occured (%s) :/" % ename)
