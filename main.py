#! /usr/bin/python3

import pandas as pd
import re

PATH = "./data-sets/Train.csv"

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

ds = pd.read_csv(PATH)
text = ds["text"][17]

print (cleanhtml(text))