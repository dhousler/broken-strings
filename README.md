# broken-strings - Assignment

## Workflow manager
### Nextflow
nextflow version 23.10.0.5889
##### Installation
+ see `/docs/Installation_guidelines.md` for full instructions.

### Running the workflow
The workflow is called 'break-sites'

1. Once the git repository has been pulled, in the project directory,
   make a 'run' directory and cd into this dir. 
   This will compartmentalise results
   ```commandline
   mkdir run
   cd run
   ```
2. From the 'run' directory, **USAGE**:
   ```commandline
   nextflow run ../main.nf
   ```
3. This will produce a work directory and a dated results directory with all output files.
   ``` 
   CON-MP2C0C8L:~/scripts/broken-strings/run$ nextflow run ../main.nf
   N E X T F L O W  ~  version 23.10.0
   Launching `../main.nf` [jovial_fermi] DSL2 - revision: c8f5bde496
   executor >  local (49)
   [0c/64671b] process > break_sites:FILTER_Q30 (q30_filtering)      [100%] 16 of 16 ✔
   [48/d75667] process > break_sites:INTERSECT (intersect_q30_files) [100%] 16 of 16 ✔
   [c9/6894a8] process > break_sites:NORMALISED (normalise)          [100%] 16 of 16 ✔
   [95/7d4565] process > break_sites:NEATEN (neaten)                 [100%] 1 of 1 ✔

   CON-MP2C0C8L:~/scripts/broken-strings/run$ ls
   results_2023-10-22-15:44:07  work
   ```
4. Results
   ```commandline

   dalebridges@CON-MP2C0C8L:~/scripts/broken-strings/run$ ls results_2023-10-22-16\:46\:46/
   Plot-DBS_normalised_count_results.html       Sample13.breakends.bed.counts                Sample2.breakends.bed.filtered              Sample6.breakends.bed.filtered.intersected
   Sample1.breakends.bed.counts                 Sample13.breakends.bed.filtered              Sample2.breakends.bed.filtered.intersected  Sample6.counts.txt
   Sample1.breakends.bed.filtered               Sample13.breakends.bed.filtered.intersected  Sample2.counts.txt                          Sample7.breakends.bed.counts
   Sample1.breakends.bed.filtered.intersected   Sample13.counts.txt                          Sample3.breakends.bed.counts                Sample7.breakends.bed.filtered
   Sample1.counts.txt                           Sample14.breakends.bed.counts                Sample3.breakends.bed.filtered              Sample7.breakends.bed.filtered.intersected
   Sample10.breakends.bed.counts                Sample14.breakends.bed.filtered              Sample3.breakends.bed.filtered.intersected  Sample7.counts.txt
   Sample10.breakends.bed.filtered              Sample14.breakends.bed.filtered.intersected  Sample3.counts.txt                          Sample8.breakends.bed.counts
   Sample10.breakends.bed.filtered.intersected  Sample14.counts.txt                          Sample4.breakends.bed.counts                Sample8.breakends.bed.filtered
   Sample10.counts.txt                          Sample15.breakends.bed.counts                Sample4.breakends.bed.filtered              Sample8.breakends.bed.filtered.intersected
   Sample11.breakends.bed.counts                Sample15.breakends.bed.filtered              Sample4.breakends.bed.filtered.intersected  Sample8.counts.txt
   Sample11.breakends.bed.filtered              Sample15.breakends.bed.filtered.intersected  Sample4.counts.txt                          Sample9.breakends.bed.counts
   Sample11.breakends.bed.filtered.intersected  Sample15.counts.txt                          Sample5.breakends.bed.counts                Sample9.breakends.bed.filtered
   Sample11.counts.txt                          Sample16.breakends.bed.counts                Sample5.breakends.bed.filtered              Sample9.breakends.bed.filtered.intersected
   Sample12.breakends.bed.counts                Sample16.breakends.bed.filtered              Sample5.breakends.bed.filtered.intersected  Sample9.counts.txt
   Sample12.breakends.bed.filtered              Sample16.breakends.bed.filtered.intersected  Sample5.counts.txt                          all.counts.txt
   Sample12.breakends.bed.filtered.intersected  Sample16.counts.txt                          Sample6.breakends.bed.counts                results.txt
   Sample12.counts.txt                          Sample2.breakends.bed.counts                 Sample6.breakends.bed.filtered
   ```
   + `Sample#.breakends.bed.counts` the original raw files
   + `Sample#.counts.txt` there are the individual counts that are collected by collectFile directive in 'main.nf'
   + `Sample#.breakends.bed.filtered` q30 filtered files
   + `Sample#.breakends.bed.filtered.intersected` is the intersected results with the chr21_AsiSI_sites.t2t.bed file 
   + `all.counts.txt` is the combination results Sample#.counts.txt results
   + `results.txt` is all.counts.txt with an additional header and simple ordering, it is the final file that is used for plotting
   + `Plot-DBS_normalised_count_results.html` produces the plot of normalised counts rounded to the nearest1.
      Unless the number falls below 0.5 then this is captured as uncertain and coloured blue. 

### Code - in-house
Each of the module code in the `bin` folder can be run independently 
#### filter_q30.py
Usage:  
```commandline
python3 filter_q30.py {sample}.breakends.bed -o ${sample}.filtered > ${sample}.counts
```
#### normalised_counts.py 
Usage:  
```commandline
bash normalised_counts.sh {sample_name}.breakends.bed {sample_name}.breakends.bed.filtered.intersected
```
#### plot_samples_normalised_counts_rounded.py
+ see 'plot/README.md' for additional details.
Usage:
```commandline
python3 plot_samples_normalised_counts_rounded.py
```

### 3rd party tools
+ see `bedtools` below for installation
Usage:
+ https://bedtools.readthedocs.io/en/latest/content/quick-start.html#use-bedtools

## Directory
### files
`.gitignore` files and folder to ignore e.g., run folder.
`main.nf` runs the workflow
`nextflow.config` sets the paramaters, processes etc. for workflow execution
- links to all files in the `configs` directory.
`README.md` this file.

### bin
- in-house developed scripts
### breaks
- all raw sample bed files
- chr21 intersect file
### configs
configs for additional nextflow settings as called by 'nextflow.config'
### docker
files for building docker container
### docs
Answers to questions, Discussion points, Installation_guidelines and some troubleshooting.
### modules
The main module file with all of the workflow processes to run.
This calls the script and tool commands.
(The Brain!)
### plot
the plot details for running independently and the final result.

## Additional dependencies, tested versions
NOTE: 
- All dependencies have been built into the docker file in the docker folder.
- If running independent of docker set `docker enabled=false` in the `configs/docker.config` file
- bedtools will need to be installed within the local environment
- Plotly will need to be installed for Python3 to run the plots

#### OS
ubuntu:20.04  

#### python3
python 3.8.10
**requirements:**
argparse
plotly==5.17.0  

#### bedtools
```commandline
sudo apt-get install bedtools
```
##### Installation
+ see `/docs/Installation_guidelines.md` for full instructions.

#### Docker
`Docker version 20.10.21, build 20.10.21-0ubuntu1~20.04.1`
##### Installation
+ see `/docs/Installation_guidelines.md` for full instructions.

## Miscellaneous
+ See `docs/Troubleshooting.md` for common errors and solutions





