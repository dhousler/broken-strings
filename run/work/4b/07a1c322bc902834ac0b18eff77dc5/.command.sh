#!/bin/bash -ue
bedtools intersect -a Sample4.breakends.bed.filtered -b chr21_AsiSI_sites.t2t.bed -wa > Sample4.breakends.bed.filtered.intersected
