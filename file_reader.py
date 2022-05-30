#!/bin/python
#Shayna Mallett
#Originally completed: ASU Fall 2021 - CSE 598 
#Published open source: https://github.com/ShaynaMallett/Debugging_DNA

#Import libraries 
from pathlib import Path, PurePath

def get_input_file(file_name):
    #Find the input file in the same directory as the script
    path = Path(__file__).parent.absolute()
    return PurePath(path, file_name)

def read_string(file_name):
    #Read the DNA string 
    file = get_input_file(file_name)
    dna = ''
    with open(file, 'r') as data:
        dna = data.readline()
        data.close
    return dna
