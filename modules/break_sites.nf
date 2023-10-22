process FILTER_Q30 {
  tag "q30_filtering"
  label "small"

  publishDir "${params.resultsDir}", pattern: '*', mode: 'copy'

  input:
  path sample

  output:
  path "*"

  script:
  """
  filter_q30.py $sample -o ${sample}.filtered > ${sample}.counts
  """
}

process INTERSECT {
  tag "intersect_q30_files"
  label "samll"

  publishDir "${params.resultsDir}", pattern: '*', mode: 'copy'

  input:
  path filtered  // will have 2 files [0]=counts [1]=filtered, want filtered //TODO how to name
  path intersect_file

  output:
  path "*"

  script:
  """
  bedtools intersect -a ${filtered[1]} -b ${intersect_file} -wa > ${filtered[1]}.intersected
  """
}

process NORMALISED {
  tag "normalise"
  "label small"

  publishDir "${params.resultsDir}", pattern: '*', mode: 'copy'

  input:
  path sample
  path intersected

  output:
  path "*"

  script:
  """
  normalised_counts.sh $sample ${sample}.filtered.intersected
  """
}


process NEATEN {
  tag "neaten"

  publishDir "${params.resultsDir}", pattern: '*', mode: 'copy'

  input:
  val header
  path normalised

  output:
  path "*"

  script:
  """
  { echo -e "${header}"; sort -t' ' -k1.1 ${normalised}; } > results.txt
  """
}

process PLOT {
  tag "plot"

  publishDir "${params.resultsDir}", pattern: '*', mode: 'copy'

  input:
  path results

  output:
  path "*"

  script:
  """
  plot_samples_normalised_counts_rounded.py $results
  """
}
