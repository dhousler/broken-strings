#!/usr/bin/env nextflow
nextflow.enable.dsl = 2

/*
 * Author: Dale Bridges <dalehousler@yahoo.co.uk>
 *
 */

// Inputs
//params.sample = "$baseDir/data/*.bed"  //see nextflow.config
sample_ch = Channel.fromPath( params.sample, checkIfExists: true )
intersect_file = params.asisi_file
header = params.header


//Import modules
include { FILTER_Q30 } from './modules/break_sites.nf'
include { INTERSECT } from './modules/break_sites.nf'
include { NORMALISED } from './modules/break_sites.nf'
include { NEATEN } from './modules/break_sites.nf'
include { PLOT } from './modules/break_sites.nf'

//workflow break_sites {
//  result_ch = FILTER_Q30(sample_ch)
//  result_ch.view { it }
//}

workflow break_sites {
  FILTER_Q30(sample_ch)
  INTERSECT(FILTER_Q30.out, intersect_file)
  NORMALISED(sample_ch, INTERSECT.out.collect())  // there must be a simpler way to do this without adding all files
  NEATEN(header, NORMALISED.out.collectFile(name:"all.counts.txt", storeDir:params.resultsDir)) //header for file in params, collect all counts files and collate.
  PLOT(NEATEN.out)
}

workflow {
  break_sites()
}
