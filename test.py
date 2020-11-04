import re
import string
import pandas as pd

def cleanHtmlTags(text):
    mask = re.compile("<.*?>")
    text = re.sub(mask, "", text)
    return text

def cleanNumbers(text):
    mask = re.compile("[0-9]*")
    text = re.sub(mask, "", text)
    return text

def cleanPunctuations(text):
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub("[‘’“”…]", "", text)
    return text




text = '''

    <!DOCTYPE html>
    <html>
        <body>
            <h1> Hello, World! 123 <\h1>
            <>
            ali < mamad
            <img src="https://jakesh.org/sexy/bitches" styles={color:100;}/>
            <p> Jakesh this is a new line <br /> hmmm <br /> yeeeeeees</p>
        </body>
    </html>
'''

text = cleanHtmlTags(text)
print (text)
text = cleanNumbers(text)
print (text)
text = cleanPunctuations(text)
print (text)