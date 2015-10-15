import sys
import os
import csv
import argparse

"""

Splits a CSV file into multiple files based on command line arguments.

    Arguments:

    `-h`: help file of usage of the script
    `-i`: input file name
    `-o`: output file name
    `-r`: row limit to split

    Default settings:

    `output_path` is the current directory
    headers are displayed on each split file
    the default delimeter is a comma

    Example usage:

    ```
    # split csv by every 100 rows
    >> python csv_split.py -i input.csv -o output -r 100
    ```

"""


def get_arguments():
    """Grab user supplied arguments using the argparse library."""

    # Use arparse to get command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", required=True,
                        help="csv input file (with extension)", type=str)
    parser.add_argument("-o", "--output_file", required=True,
                        help="csv output file (without extension)", type=str)
    parser.add_argument("-r", "--row_limit", required=True,
                        help="row limit to split csv at", type=int)
    args = parser.parse_args()

    # Check if the input_file exits
    is_valid_file(parser, args.input_file)

    # Check if the input_file is valid
    is_valid_csv(parser, args.input_file, args.row_limit)

    return args.input_file, args.output_file, args.row_limit


def is_valid_file(parser, file_name):
    """Ensure that the input_file exists."""
    if not os.path.exists(file_name):
        parser.error("The file '{}' does not exist!".format(file_name))
        sys.exit(1)


def is_valid_csv(parser, file_name, row_limit):
    """
    Ensure that the # of rows in the input_file
    is greater than the row_limit.
    """
    row_count = 0
    for row in csv.reader(open(file_name)):
        row_count += 1
    # Note: You could also use a generator expression
    # and the sum() function to count the rows:
    # row_count = sum(1 for row in csv.reader(open(file_name)))
    if row_limit > row_count:
        parser.error(
            "The 'row_count' of '{}' is > the number of rows in '{}'!"
            .format(row_limit, file_name)
        )
        sys.exit(1)


def parse_file(arguments):
    """
    Splits the CSV into multiple files or chunks based on the row_limit.
    Then create new CSV files.
    """
    input_file = arguments[0]
    output_file = arguments[1]
    row_limit = arguments[2]
    output_path = '.'  # Current directory

    # Read CSV, split into list of lists
    with open(input_file, 'r') as input_csv:
        datareader = csv.reader(input_csv)
        all_rows = []
        for row in datareader:
            all_rows.append(row)

        # Remove header
        header = all_rows.pop(0)

        # Split list of list into chunks
        current_chunk = 1
        for i in range(0, len(all_rows), row_limit):  # Loop through list
            chunk = all_rows[i:i + row_limit]  # Create single chunk

            current_output = os.path.join(  # Create new output file
                output_path,
                "{}-{}.csv".format(output_file, current_chunk)
            )

            # Add header
            chunk.insert(0, header)

            # Write chunk to output file
            with open(current_output, 'w') as output_csv:
                writer = csv.writer(output_csv)
                writer = writer.writerows(chunk)

            # Output info
            print("")
            print("Chunk # {}:".format(current_chunk))
            print("Filepath: {}".format(current_output))
            print("# of rows: {}".format(len(chunk)))

            # Create new chunk
            current_chunk += 1


if __name__ == "__main__":
    arguments = get_arguments()
    parse_file(arguments)
