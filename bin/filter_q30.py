#!/usr/bin/env python3

import time
import argparse
import os

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = round((end_time - start_time), 5)  # round to 5 decimals
        print(f"{func.__name__} executed in approx.: {execution_time} seconds.")
        return result
    return wrapper


def q30_filter(input_file):
    # This assumes a clean input file, would need a pre-file checker for tab delimited and correct #cols
    try:
        with open(input_file, 'r') as file:
            # Read the file line by line
            count = 0
            qcount = 0
            for line in file:  # list comprehension columns = [line.split("\t") for line in file]  # decision to count to not valid in this context
                # Process each line as needed
                columns = line.split("\t")
                count += 1

                try:
                    # Convert the second-to-last column to an integer
                    second_last_value = int(columns[-2])

                    # Check if the integer value is greater than or equal to 30
                    if second_last_value >= 30:
                        qcount += 1
                        yield line  # Generator

                except ValueError:
                    # Handle the case where conversion to an integer fails
                    pass

            print(f"Total reads: {count}")
            print(f"q30 filtered reads: {qcount}")

    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist.")

    except Exception as e:
        print(f"An error occurred: {e}")


@timing_decorator
def main(args):

    # Read the file and print or process the content
    file_content = args.infile

    ''' Apply Filer '''
    # Use the generator to filter and yield lines with integer second-to-last value >= 30
    filtered_lines = q30_filter(input_file=file_content)

    ''' Result to Output'''
    # check that the output file doesn't already exist as using append
    if os.path.exists(args.outfile):
        try:
            # Delete the file
            os.remove(args.outfile)
        except Exception as e:
            print(f"An error occurred while deleting the file: {e}")

    # Print the result
    for line in filtered_lines:

        try:
            with open(args.outfile, 'a') as output_file:
                # Write the line to the new outfile
                output_file.write(line)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':

    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Read the contents of a file")
    # Add a positional argument for the file path
    parser.add_argument("infile", metavar="file_path", type=str, help="Input file.")
    # Add optional arguments with abbreviations
    parser.add_argument("-o", "--outfile", type=str, help="Output file.")
    # Parse the command-line arguments
    args = parser.parse_args()
    main(args)

# TODO add logging instead of print
