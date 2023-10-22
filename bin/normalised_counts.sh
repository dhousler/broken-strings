#!/bin/bash

# TODO make this smarter so that the files are placed the correct order, workflow manager should handle but could be explicit currently implicit

# Check if exactly two file arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <file1> <file2>"
    exit 1
fi

# Get the file paths from command line arguments
raw_counts_file="$1"
intercept_counts_file="$2"

# Check if the input files exist
if [ ! -e "$raw_counts_file" ] || [ ! -e "$intercept_counts_file" ]; then
    echo "One or both of the input files do not exist."
    exit 1
fi

# Use cut to extract the part before the first dot
sample_name=$(echo "$raw_counts_file" | cut -d. -f1)

# Count the lines in the first file and store the count in a variable
count_raw=$(wc -l $raw_counts_file | awk '{print $1}')

# Count the lines in the second file and store the count in a variable
count_intercept=$(wc -l $intercept_counts_file | awk '{print $1}')

# Divide the first count by 1000
count_raw_1000=$(echo "scale=3; $count_raw/1000" | bc) #$((count_raw / 1000))

# Divide the second count by the value of the first count
normalised_counts=$(echo "scale=3; ($count_intercept / $count_raw_1000) " | bc)

# Count to integer - round to nearest 1
#int_normalised_counts=$(echo "scale=0; ($count_intercept / $count_raw_1000) " | bc -l)
#int_normalised_counts=$(awk -v num="$normalised_counts" 'BEGIN { rounded = int(num + 0.5); printf("%.0f\n", rounded) }')
#int_normalised_counts=$(awk -v num="$normalised_counts" 'BEGIN { rounded = int(num + 0.5); if (rounded < 0.5) rounded = 0.5; printf("%.2f\n", rounded) }')
int_normalised_counts=$(awk -v num="$normalised_counts" 'BEGIN {
  if (num == 0) {
    rounded = 0;
  } else {
    rounded = int(num + 0.5);
    if (rounded < 0.5) rounded = 0.5;
  }
  printf("%.1f\n", rounded);
}')

# Create a new file (e.g., counts.txt) with headers and all counts
#echo -e "sample\traw_counts\tintercept_counts\traw_div_1000\tnormalised_counts\tint_normalised_count_int" > $sample_name.counts.txt # header removed for collation
echo -e "$sample_name\t$count_raw\t$count_intercept\t$count_raw_1000\t$normalised_counts\t$int_normalised_counts" >> $sample_name.counts.txt

