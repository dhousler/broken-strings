#!/bin/bash -ue
{ echo -e "sample	raw_counts	intercept_counts	raw_div_1000	normalised_counts	normalised_count_rounded"; sort -t' ' -k1.1 all.counts.txt; } > results.txt
