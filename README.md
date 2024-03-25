# Murre24: Dialect Identification of Finnish Internet Forum Messages

Manually annotated dataset of Finnish varieties in the Suomi24, the largest Finnish internet forum, the id's of automatically annotated dialectal messages and the scripts used for classification and evaluation.

## Manual annotations
The manual annotations are located in the folder `S24`, with standard vs. non-standard Finnish data in one subfolder and the final dialect identification in the other subfolder. 
Messages are originally from the Suomi24 forum and must be attributed accordingly: https://www.kielipankki.fi/corpora/suomi24/.

## Additional training data
There are three additional datasets used for training:

### Murreviikko
The original data are presented here: https://github.com/Helsinki-NLP/murreviikko

### SKN
The original data is downloadable here: https://korp.csc.fi/download/SKN/skn-vrt/
Citation instructions: https://www.kielipankki.fi/viittaus/?key=skn-vrt&lang=en

### Finnish Wikipedia 2017
The original is downloadable here: https://www.kielipankki.fi/lexical-conceptual-resources/wikipedia-fi-2017/
Citation instructions: https://www.kielipankki.fi/viittaus/?key=wikipedia-fi-2017-src&lang=en

## Automatic annotation
The results of the automatic annotation are presented as message id's in the folder `dialect_annotations`. The original corpus is usable with an academic license in https://www.kielipankki.fi/corpora/suomi24/. You can ask for permissions of the original data and use the id's to search for the correct messages.

## Scripts
The scripts for classification and evaluation are presented in the folder `scripts`.

## Citation
Citation instructions will be added once the paper is published in the Proceedings.
