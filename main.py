#! /usr/bin/python3

import pandas as pd
import numpy as np
import re

PATH = "./data-sets/Train.csv"

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

if __name__ == '__main__':
    db = pd.read_csv(PATH)
    
    comments = [comment for comment in db["text"]]
    labels = [lable for lable in db["label"]]
    print (labels[0])
    print (comments[16])
    print ("---------------------------------")
    print(cleanhtml(comments[16]))