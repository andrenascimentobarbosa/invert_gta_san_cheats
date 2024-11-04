#!/usr/bin/python3

import sys
import traceback


def invert(input_str):
    temp = input_str.replace('1', 'TEMP')
    temp = temp.replace('2', '1')
    result = temp.replace('TEMP', '2')
    
    return result


if __name__ == '__main__':
    try:    
        file = sys.argv[1]

        with open(file, 'r+') as f:
            origin_data = f.read()
            str_data = str(origin_data)
            print(invert(str_data))
    except IndexError:
        print('Usage: ./script.py <file.txt>\n')
