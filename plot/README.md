USAGE

1. copy the `results.txt` from the nextflow output results folder.
2. run
   ```
   python3 plot_samples_normalised_counts_rounded.py
   ```
3. The following will appear as not a tty. `ctl+c`  # this is likely a wsl issue.
   ```
   dalebridges@CON-MP2C0C8L:~/scripts/break_sites/plot$ ltcgetpgrp failed: Not a tty
   sStart : This command cannot be run due to the error: The system cannot find the file specified.
   At line:1 char:1
   + Start "/home/dalebridges/scripts/break_sites/plot/bar_chart_custom_co ...
   + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (:) [Start-Process], InvalidOperationException
    + FullyQualifiedErrorId : InvalidOperationException,Microsoft.PowerShell.Commands.StartProcessCommand
   ```
4. Use any web browser to open the `Plot-DBS_normalised_count_results.html` html named file.
   
