import pyperclip


"""
pip3 install pyperclip
    # Pyperclip is a cross-platform Python module 
    # for copy and paste clipboard functions.
     
Need some dependence:
    sudo apt-get install xsel to install the xsel utility.
    sudo apt-get install xclip to install the xclip utility.
"""

# does not return anything!
pyperclip.copy("This line will be copied to clipboard")


b = pyperclip.paste()
print(b)
print(type(b))


def convert_text(text):
    return " ".join(text.split())


s = convert_text(b)
print(s)
print(type(s))

