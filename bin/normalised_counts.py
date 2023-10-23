#!/usr/bin/env python3

import argparse
import os
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = round((end_time - start_time), 5)  # round to 5 decimals
        print(f"{func.__name__} executed in approx.: {execution_time} seconds.")
        return result
    return wrapper

def get_sample_name(file_path):
    filename = os.path.basename(file_path)
    return filename.split(".")[0]

def count_lines(file_path):
    with open(file_path) as file:
        return sum(1 for line in file)


def round_to_nearest_half(normalised_counts):
    if normalised_counts == 0:
        rounded = 0
    else:
        rounded = int(normalised_counts + 0.5)
        if rounded < 0.5:
            rounded = 0.5
    return round(rounded, 1)

@timing_decorator
def main(args):
    raw_counts_file = args.raw_counts
    intercept_counts_file = args.intercept_counts

    # Check if the input files exist
    if not (os.path.exists(raw_counts_file) and os.path.exists(intercept_counts_file)):
        print("One or both of the input files do not exist.")
        return

    # Extract the part before the first dot to create the sample name
    sample_name = get_sample_name(raw_counts_file)

    # Count the lines in the first file and store the count in a variable
    count_raw = count_lines(raw_counts_file)

    # Count the lines in the second file and store the count in a variable
    count_intercept = count_lines(intercept_counts_file)

    # Divide the first count by 1000
    count_raw_1000 = count_raw / 1000.0

    # Divide the second count by the value of the first count
    normalised_counts = (count_intercept / count_raw_1000)

    # Round the normalised counts to the nearest integer
    #int_normalised_counts = int(round(normalised_counts, 3))
    int_normalised_counts = round_to_nearest_half(normalised_counts)

    # Create a new file (e.g., counts.txt) with headers and all counts
    with open(sample_name + ".counts.txt", "w") as output_file:
        output_file.write(f"{sample_name}\t{count_raw}\t{count_intercept}\t{count_raw_1000:.3f}\t{normalised_counts:.3f}\t{int_normalised_counts}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process raw and intercept counts files.")
    parser.add_argument("raw_counts", help="Path to the raw counts file")
    parser.add_argument("intercept_counts", help="Path to the intercept counts file")
    args = parser.parse_args()
    main(args)