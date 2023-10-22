# Troubleshooting

## permissions
```commandline
Command error:
  .command.sh: line 2: /home/dalebridges/scripts/broken-strings/bin/plot_samples_normalised_counts_rounded.py: Permission denied
_Solution:_
```
Set the correct permissions on the file in the `/bin` directory
```commandline
chmod 755 {file_name}
```

## windows line endings
- compatability with line endings when developing in windows and moving to linux
```commandline
/home/dalebridges/scripts/broken-strings/bin/plot_samples_normalised_counts_rounded.py: line 3: $'\r': command not found
```
_Solution:_
- Use dos2linux conversion
```commandline
sudo apt-install dos2linux
dos2linux {file_for_conversion}
```

## Shebang missing
Similar error to above, if binary file is missing the shebang header then this could cause run issue.  
_Solution:_  
Add the shebang  

### Adding the program to the script
If the program name e.g., `python3` or `bash` is added to the script line in a module's process  
then nextflow will fail.   
Any script in the `bin` folder does not need to be called by the program as long as the shebang is available  
_Solution:_  
Remove the program name.