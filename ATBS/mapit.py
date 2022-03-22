# Author: Tracy Vierra
# Date Created: 3/22/2022
# Date Modified: 3/22/2022

# Description: mapit takes the address you pass and opens it in Google Maps.

# Usage:

import webbrowser, sys, pyperclip

sys.argv
# check if command line arguments were passed.
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

