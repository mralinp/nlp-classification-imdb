#! /usr/bin/python3

import pandas as pd

db = {}
db["trainDataset"] = pd.read_csv("./data-sets/Train.csv")
db["testDataset"] = pd.read_csv("./data-sets/Test.csv")
db["validDataset"] = pd.read_csv("./data-sets/Valid.csv")

import re
import string

def cleanHtmlTags(text):
    mask = re.compile("<.*?>")
    text = re.sub(mask, "", text)
    return text

for dataset in db.values():
    dataset.
    for example in dataset:
        print (type(example))
