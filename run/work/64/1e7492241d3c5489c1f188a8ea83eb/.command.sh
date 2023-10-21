#!/bin/bash -ue
bedtools intersect -a Sample9.breakends.bed.filtered -b chr21_AsiSI_sites.t2t.bed -wa > Sample9.breakends.bed.filtered.intersected
