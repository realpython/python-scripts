### WIP

import sys
import os
import getopt
import csv

"""
    Splits a CSV file into multiple pieces based on command line arguments.

    Arguments:
        `-h`: help file of usage of the script  
        `-i`: input file name 
        `-o`: output file, A %s-style template for the numbered output files.
        `-r`: row limit to split 
        `-c`: A %s-style template for the numbered output files.

    Default settings:
        `output_path` is the current directory
        `keep_headers` is on (headers will be kept)
        `delimeter` is ,

    Example usage:
        # split by every 10000 rows
        >> python 12_csv_split.py -i input.csv -o rownumber -r 10000   
        # split by unique items in column 0 
        >> python 12_csv_split.py -i input.csv -o userid -c 0   
        # access help
        >> python 12_csv_split.py -h for help 
    
"""

def main(argv):

    argument_dict = grab_command_line_arguments(argv)
    parse_file(argument_dict)


def grab_command_line_arguments(argv):

    # global variables
    inputfile = ''
    outputfile = ''
    rowlimit = ''
    columnindex = ''  
    argument_dict = {} 

    # grab arguments
    opts, args = getopt.getopt(argv,"hi:o:r:c:",["ifile=","ofile=","rowlimit=","columnindex="])

    # end if no arguments provided
    if not opts:
        print "No options provided. Try again. Use `-h` for help."
        sys.exit()

    # grab arguments
    for opt, arg in opts:
        if opt == '-h':
            print 'csvsplit.py -i <inputfile> -r <row limit> -c <column index> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-r", "--rowlimit"):
            rowlimit = arg
        elif opt in ("-c", "--columnindex"):
            columnindex = arg

    # Output arguments
    print "\nArguments:"
    if inputfile:
        argument_dict["input_file"] = inputfile
        print "Input file is '{}'".format(inputfile)
    else:
        "Please enter an input file."
    if outputfile:
        argument_dict["output_file"] = outputfile
        print "Output file is '{}'".format(outputfile)
    else:
        print "Please enter an output file."
    if rowlimit:
        argument_dict["rowlimit"] = rowlimit
        print "Rowlimit is '{}'".format(rowlimit)
    if columnindex:
        argument_dict["columnindex"] = columnindex
        print "Columnindex is '{}'".format(columnindex) 
    if rowlimit and columnindex:
        print "Please use either a rowlimit or columnlimit, not both."
        sys.exit()
    if not rowlimit or columnindex:
        print "Please enter either a rowlimit or columnlimit."
        sys.exit()

    # to do - check to make sure file, rowlimit, and columnlimit exist
    print argument_dict
    return argument_dict


def parse_file(argument_dict):

    #split csv file by certain rownumber 
    if argument_dict["rowlimit"]:           
        rowlimit = int(argument_dict["rowlimit"])
        output_name_file = "{}.csv".format(argument_dict["output_file"])
        output_path='.'
        keep_headers=True
        delimiter=','
        filehandler = open(argument_dict["input_file"],'r')
        reader = csv.reader(filehandler, delimiter=delimiter)
        current_piece = 1
        current_out_path = os.path.join(
            output_path,
            output_name_file
        )
        current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
        current_limit = rowlimit
        if keep_headers:
            headers = reader.next()
            current_out_writer.writerow(headers)
        for i, row in enumerate(reader):
            if i + 1 > current_limit:
                current_piece += 1
                current_limit = rowlimit * current_piece
                current_out_path = os.path.join(
                    output_path,
                    output_name_file
                )
            current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)

# elif columnindex:               #split csv file accrording to unique values of certain column,it's like filter only certain item in excel 
# itemlist = []
# columnindex = int(columnindex)
# output_name_template= outputfile+'_%s.csv'
# output_path='.'
# keep_headers=True
# delimiter=','
# filehandler = open(inputfile,'r')
# reader = csv.reader(filehandler, delimiter=delimiter)
# if keep_headers:
#   headers = reader.next()

# for i, row in enumerate(reader):

#   current_out_path = os.path.join(
#        output_path,
#        output_name_template  % row[columnindex] )
#   if row[columnindex] not in itemlist:
#      try:
#          current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
#      except IOError:
#          continue
#      else:
#          itemlist.append(row[columnindex])
#          if keep_headers:
#              current_out_writer.writerow(headers)
#          current_out_writer.writerow(row)
#   else:
#      current_out_writer = csv.writer(open(current_out_path, 'a'), delimiter=delimiter)
#      current_out_writer.writerow(row)
# print 'totally %i unique items in column %i \n' % (len(itemlist),columnindex)
# else:
# print "oops, please check instruction of script by >>./csvsplit.py -h"


if __name__ == "__main__":
   main(sys.argv[1:])