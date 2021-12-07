# WiPL_Conv
Converter from WiPL to SimRadar formats

## Description

Convert data from ascii human-readable file output by WiPL to a binary format readable by SimRadar.
Both programs have data in spherical co-ordinates on a domain of phi = 0 to 360 and theta = -90 to 90 and have complex values for E_phi & E_theta, and absolute values for RCS and RCS_db, so no numerical conversion is carried out.

Assumption is made that input file has a 3 character file extension

The SimRadar binary files are very position dependent for the field, and so a change in the layout of the input file will result in errors in the output file being incorrect

## Usage

WiPLconv <input_filename> -o <output_path> -d <debug_flag>

Arguments:
    input    - [REQUIRED] Positional argument.
               The filename of the input ra1 format WiPL file, including the path to that file if
               not in the running directory

    --outdir - [OPTIONAL] Flagged argument
    -o         Path to the output directory. Will attempt to create the directory if it doesn't exist
               Default to the directory containing the input file

    --debug  - [OPTIONAL] Flagged argument
    -d         Flag for debug behaviour. If true rcs file will be converted back to human readable
               text file to check for validation against the input file.


Included in this repo is a test program which can be used to convert a file back from SimRadar to human-readable WiPL again for file verification.

Author: Christopher Symonds
Date Created: 18 June 2021
Institution: CEMAC, University of Leeds
Contact: c.c.symonds@leeds.ac.uk
Credit: wipl_radiation_output_reader function written by R. Neely III, NCAS
