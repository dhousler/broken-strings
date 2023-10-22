# Discussion
Points for discussion and consideration.

## Nextflow - break_sites workflow
### Workflow
1. Currently step 3 of the workflow will pull in all the intersected files.
`NORMALISED(sample_ch, INTERSECT.out.collect())` using the closure collect() method.
This isn't ideal, and there must be a simpler way to do this, using an alternative.
Some form of file matching on the Sample name or an alternative closure.
__This is a case of balance time to find correct code vs results__
In this case files are small not a problem, but for larger files and increased processing tim 
this would become a limitation and would need an alternative solution.

### Input files
- There are little checks on these, better checks could be added to check delimitation etc.
  By writing an initial check file step, but as these have been pre-processed it can be assumed the output has been created programmatically, hence little error.
### Output files
- These could be named better in the workflow and specific naming conventions rather than just collection all files.
- _This is something that could be worked on._
### Docker
- All modules are set to run in the docker container
  - to run outside of docker 
    - set enabled=false in configs/docker.config
- These run slower if run using docker as memory and cpu have been set very low.
-Docker has been used purely to show how this can be set-up, as wasn't asked for in the assignment.

### Results
#### q30 filtered
- This was slightly ambigious in the question whether this sould be >=30 or >30
  Decision was to use >= 30
- Two files are produced as output, the filtered file, and an additional counts file.
  - this is used for checking results
  - and to show how to work with multiple results as input into the next step of the workflow
- I have added within the code how to use a 
  - generator
  - list comprehension was not used due to the addition of the counts
#### results in results folder
- could work smarter here and be specific about exact files to move
- currently all outputs are moved here

## Plot
- This has been added to the workflow in addition
- List comprehensions have been used here.
- probably could look at moving code into a main but as a plot will suffice
- could work on naming
- decision was made to order the samples at this final step
  - e.g., Sample1, Sample10, Sample2 --> Sample1, Sample2, Sample3
  - this is done at this step to prevent any errors.
  - samples are also clustered so that controls and results are grouped together. 
## Miscellaneous
### Parallel processing
- I believe this is what Nextflow is doing, as this takes in the channels and there is no looping with the Python code
- The parallelisation is dependent on cpus and can be further parallelised in cloud. 
- _I could look into this in more detail._
### Improvements
- Addition of logging at various points:
  - for the python scripts
  - in the workflow
- Addition of tests (test driven development)
### Licensing
- As this is not for commercial use licensing is not a factor but should always be a consideration.
### Notes
This code has been run externally in a miniconda environment 
and within the docker container as per provided build.



