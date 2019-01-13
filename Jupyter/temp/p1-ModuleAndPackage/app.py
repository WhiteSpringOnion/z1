
"""01/app.py
Main app module."""


import sys

import bprint

dicc = {"reboot": "Rebooting launch control system.",
            "halt": "Halting all systems.",
        "hello": "hello"
            }

try:
    print("this is try opening bracket")
    command = sys.argv[1]
    print('this is try closing bracket!')
except IndexError:
    bprint.upper_print("No command provided. Terminating.")
    sys.exit(1)
else:
    print(dicc.get(command, "Doing absolutely nothing."))