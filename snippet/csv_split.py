import sys
import os
import csv
import argparse

"""
Introduce:
    Cut a big file to many small files
    
Usage:
    -h: show help
    -i: input file name 
    -o: output filename 
    -r: row limit to split
    
Example:
    >>>python3 csv_split.py -i data.csv -o part -r 10
"""


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", required=True,
                        help="csv input filename (with extension)", type=str)
    parser.add_argument("-o", "--output_file", required=True,
                        help="csv output filename (without extension)", type=str)
    parser.add_argument("-r", "--row_limit", required=True,
                        help="how many rows of a csv", type=int)
    args = parser.parse_args()

    is_valid_file(parser, args.input_file)

    is_valid_csv(parser, args.input_file, args.row_limit)

    return args.input_file, args.output_file,args.row_limit


def is_valid_file(parser, file_name):
    if not os.path.exists(file_name):
        parser.error("File: '{} does not exists'".format(file_name))
        sys.exit(1)


def is_valid_csv(parser, filename, row_limit):
    row_count = 0
    for row in csv.reader(open(filename)):
        row_count += 1

    # or:  row_count = sum(1 for row in csv.reader(open(filename)))
    if row_limit > row_count:
        parser.error(
            "The row_limit exceeds csv contains lines"
        )
        sys.exit(1)

def parse_file(arguments):
    # split csv-file to multi-part

    input_file = arguments[0]
    output_file = arguments[1]
    row_limit = arguments[2]
    output_path = '.'

    with open(input_file, 'r') as input_csv:
        datareader = csv.reader(input_csv)
        all_rows = []
        for row in datareader:
            all_rows.append(row)

        header = all_rows.pop(0)

        # Attention! here is the core part...
        current_chunk = 1
        for i in range(0, len(all_rows), row_limit):
            chunk = all_rows[i: i+row_limit]  # create singe chunk

            current_output = os.path.join(
                output_path,
                "{}-{}.csv".format(output_file, current_chunk)
            )

            chunk.insert(0, header) # don't miss the header

            with open(current_output, 'w') as out_csv:
                writer = csv.writer(out_csv)
                writer = writer.writerows(chunk)


            print("Done!")
            print("Chunk {}: ".format(current_chunk))
            print("filepath: {}".format(current_output))
            print("rows: {}".format(len(chunk)))

            current_chunk += 1


if __name__ == '__main__':
    arguments = get_arguments()
    parse_file(arguments)














