import argparse
import os, sys
import shutil

parser = argparse.ArgumentParser(description='parse for relevant information')
parser.add_argument('input', help='Name of the file to input')
parser.add_argument('--output', help='Name of the file to output', default='output.txt')
args = parser.parse_args()

inputf = open(args.input, 'r')
outputf = open(args.output, 'w')

def determine_amount_of_leading_tabs(string):
    if(string):
        if(string[0] == '\t'):
            return determine_amount_of_leading_tabs(string[1:len(string)]) + 1
        else:
            return 0
    else:
        return 0
        
def prepend_tabs(string, amount):
    for x in range(0, amount):
        string += '\t'
    return string
    
input_line = inputf.readline()
counter = 1
leading_tabs = 0
prev_tabs = 0
converted = ''

while(input_line):
    prev_tabs = leading_tabs
    leading_tabs = determine_amount_of_leading_tabs(input_line)
    if(leading_tabs > prev_tabs):
        converted = prepend_tabs(converted, prev_tabs)
        converted += ('\\begin{itemize}\n')
        converted = prepend_tabs(converted, leading_tabs)
        converted += ('\\item{')
        converted += (input_line[leading_tabs : len(input_line) - 1]) # -1 to cut off the newline
        converted += ('}\n')
        
    elif(leading_tabs < prev_tabs):
        for x in range(0, prev_tabs - leading_tabs): #close all the previous itemize blocks
            converted = prepend_tabs(converted, prev_tabs - 1 - x) 
            converted += ('\\end{itemize}\n')
            
        converted = prepend_tabs(converted, leading_tabs)
        converted += (input_line[leading_tabs : len(input_line)])
        
    elif(leading_tabs == prev_tabs & leading_tabs > 0):
        converted = prepend_tabs(converted, leading_tabs)
        converted += ('\\item{')
        converted += (input_line[leading_tabs : len(input_line) - 1])
        converted += ('}\n')
    
    else:
       converted += (input_line[leading_tabs : len(input_line)]) 
        
    input_line = inputf.readline()
    
outputf.write(converted)

"""
    if(input_line[0] == '\t'):
        print('gotem in line', counter)
    input_line = inputf.readline()
    counter = counter + 1
"""