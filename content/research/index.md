+++
title = "Research"
description = "Ongoing research projects in the Cohen Lab"
+++
# Research

## Gene Regulatory Genomics

{% section() %}

What is the contribution of non-protein coding genetic variation to human disease? Genetic mapping studies tell us that non-coding DNA harbors the majority of variation that contributes to disease, but, we have virtually no ability to identify the specific disease-causing nucleotides in non-coding DNA. In protein-coding DNA the genetic code helps us interpret the likely effects of sequence changes, but we have no corresponding “non-coding code” for the 98% of the genome that does not code for protein. Does a non-coding code exist that might help us identify and understand disease causing variants?

Possibly.

A common hypothesis is that the majority of non-coding disease variants lie in enhancers, which are short DNA sequences that influence the transcription of nearby genes. Enhancers are in turn comprised of binding sites for transcription factors and other sequences that influence the shape and accessibility of DNA. While it is unlikely that a simple DNA code exists to explain the activity of enhancers the arrangements of binding sites and sequence features in enhancers often conform to certain physical constraints. Based on these observations we hypothesize that enhancers are subject to a “*cis*-regulatory grammar”, which governs the functional consequences of arrangements of transcription factor binding sites in the genome. The goal of our lab is to identify and formalize the “rules” that might comprise a non-coding DNA grammar. Such rules would be powerful new agents for interpreting disease causing genetic variation by allowing us to identify new enhancers in non-coding DNA and to predict the effects of sequence variation on existing enhancers

How can we identify the rules that might comprise a *cis*-regulatory grammar? We base our approach on a simple historical fact. Namely, that the genetic code was cracked by synthetic biologists. Starting with Marshall Nirenberg and Heinrich Matthaei in 1961 investigators began constructing artificial RNAs and recording the resulting polypeptides that were produced.  From these data the genetic code was deduced. In a modern twist of this idea we leverage advances in highly parallel DNA synthesis technologies to synthesize and measure they activity of tens of thousands of designer artificial enhancers. These artificial enhancers are comprised of combinations of transcription factor binding sites, nucleosome positioning signals, and DNA shape determining sequences. Using techniques from machine learning and statistical thermodynamics we deduce the rules that govern the activities of enhancers.

With these approaches our ultimate goal is to produce formal, quantitative models that accurately predict the effects of DNA sequence changes on gene regulation. Such models will be invaluable tools for identifying the particular causal variants in a large number of disease-associated genomic regions.

Our efforts are focused on several projects:

1) *Massively parallel assays of cis-regulatory elements.* We are developing a suite of experimental technologies to design, construct, and assay tens of thousands of reporter genes in a single experiment.

2) *Thermodynamic models of cis-regulation.* We are exploring the use of concepts from statistical physics as a formal way to model how interactions between transcription factors and DNA lead to specific patterns of gene expression.

3) *Stochastic models of cis-regulation.* We are investigating how stochastic fluctuations in gene expression can inform on the mechanism enhancers use to activate gene expression.

4) *Determinants of cell type specific gene expression.* We are interested in identifying the specific DNA features that “program” the genome to express certain genes in particular cell types. We are working in a variety of cell types including embryonic stem cells, lymhoblastoid cell lines, and neuronal cell lines in the brains of live mice.

5) *Determinants of specificity in mammalian genomes.* A key question is how the cell distinguishes groups of transcription factor binding sites that make up real enhancers from spurious collections of biding sites. Here we leverage our ability to design thousands of artificial enhancers to unravel the sequence features adjacent to functional versus non-functional instances of transcription factor binding sites.

6) *The relationship of genetic variation in cis-regulation to natural phenotypic variation between individuals.* Ultimately we care about the effect of variation in gene regulation on the phenotypes of organisms. To this end we are mapping and identifying cis-regulatory variation that affects cellular phenotypes in yeast, and we are attempting to identify the causal variants in regions identified in human genetic mapping studies.

{% end %}
