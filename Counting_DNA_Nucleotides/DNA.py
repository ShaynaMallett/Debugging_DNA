#!/bin/python
#Shayna Mallett
#Originally completed: ASU Fall 2021 - CSE 598 
#Published open source: https://github.com/ShaynaMallett/Debugging_DNA

#Import libraries 
from collections import defaultdict
from pathlib import Path
from file_reader import read_string 

'''Main function for Counting DNA Nucleotides'''
def main():
    #Read in the file 
    dna = read_string('rosalind_dna.txt')

    #Initialize dictionary of nucleotide counts 
    #Note: Use a dictionary to hash nucleotides rather than using if/else gates
    nucleotides = defaultdict(int)

    #Iterate the string once
    #Note: Don't use built in functions to count each number independently. 
    #      That would iterate the string each time rather than just once.
    for n in dna:
        nucleotides[n] += 1  

    #Print solution (dictionary is case sensitive)  
    #Sample Output:20 12 17 21                
    print(nucleotides['A'] , " " , nucleotides['C'] , " " , nucleotides['G'] , " " , nucleotides['T'])        

'''Call main function at start of program'''    
if __name__ == '__main__':
    main()
