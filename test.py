#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 18:38:59 2021

@author: chris
"""

from os import path, makedirs
import argparse
from sys import stderr, exit

class ArgumentsError(Exception):
    '''
    Exception raised when there is an error detected in the argument list.
    '''
    def __init__(self, msg):
        stderr.write('[FATAL ERROR] : %s' % msg )
        exit(9)

class FatalError(Exception):
    '''
    Exception raised when there is an error detected in the argument list.
    '''
    def __init__(self, msg):
        stderr.write('[FATAL ERROR] : %s' % msg )
        exit(9)

class FileError(Exception):
    '''
    Exception raised when contents of files are not as expected
    '''
    def __init__(self,msg):
        stderr.write('[FILE ERROR] : %s' % msg )
        exit(9)

def readargs():
    """
    Read input arguments if run as separate program

    Returns
    -------
    None.

    """


    parser = argparse.ArgumentParser(description=(
        'Convert data from WiPL format to binary SimRadar-compatible format.'
        ))

    parser.add_argument('input',
                        type=str,
                        help='[REQUIRED] File to be converted')
    parser.add_argument('--outdir', '-o',
                        type=str,
                        help='Output directory for rcs files, default as location of input file',
                        default='.')
    parser.add_argument('--debug', '-d',
                        type=str,
                        help=('[True/False] Flag for debug mode - writes file back out again in human readable'
                              +' format after conversion to allow validation of converted data'),
                        default='False')

    args = parser.parse_args()

    infile = args.input

    if not path.isfile(infile):
        raise ArgumentsError("Could not find file {}\n If file exists try again with absolute path rather than relative path")

    path_out = args.outdir
    
    if path_out == '.':
        inpath = path.split(infile)[0]
        if inpath != '':
            path_out = inpath

    if not path.exists(path_out):
        print('Directory to write rcs files to'
              + ' does not exist\nAttempting to create:')
        try:
            makedirs(path_out)
        except:
            raise FatalError('Could not create directory '+ path_out +'\n')
        else:
            print ("Success!\n")

    if path_out and not path.isdir(path_out):
        raise ArgumentsError(path_out + ' exists but is not a directory\n')
        
    debug_str = args.debug
    
    if debug_str.lower() == "true" or debug_str.lower() == "t":
        debug = True
    elif debug_str.lower() == "false" or debug_str.lower() == "f":
        debug = False
    else:
        raise ArgumentsError("Value for debug should be True/False. Value read was {}".format(debug_str))
    

    return (infile, path_out, debug)

def main():
    
    (filein, pathout, debug) = readargs()
    print (filein)
    print (pathout)
    print (debug)
    print (type(debug))
    
if __name__ == "__main__":
    main()