# file to contain settings used by multiple scripts

import utils.file_utils as utils
import socket

# Ouputs Structure:
# ouputs - version1 - all - method 1 - results.txt
#       |          |      - method 2 - results.txt
#       |           - species1
#       |
#        - version2

ALLOWEDVERSIONS = [
    "2017_10-seq-sim",
    "2017_10-string",
    "2017_10-seq-sim-string",
    "2017_10-seq-sim-14",
    "2017_10-seq-sim-x5-string-14",
    "2017_10-seq-sim-x5-string",
    "2017_10-string-14",
    # This is a new version with 14 new species
    "2018_02-seq-sim",
    ]

SEQ_SIM_NETWORKS = {
    "2017_10-seq-sim": "inputs/protein-similarity/2017-10-08-shiv-similarity-network-uniprot.txt",
    "2017_10-seq-sim-14": "inputs/protein-similarity/2017-10-08-shiv-similarity-network-uniprot.txt",
    "2017_10-seq-sim-string": "inputs/protein-similarity/2017-10-08-shiv-similarity-network-uniprot.txt",
    "2017_10-seq-sim-x5-string-14": "inputs/protein-similarity/2017-10-08-shiv-similarity-network-uniprot.txt",
    "2017_10-seq-sim-x5-string": "inputs/protein-similarity/2017-10-08-shiv-similarity-network-uniprot.txt",
    # TODO
    "2018_02-seq-sim": "TODO",
    }

NETWORK_VERSION_INPUTS = {
    "2017_10-seq-sim": ['SEQ_SIM'],
    "2017_10-seq-sim-14": ['SEQ_SIM'],
    "2017_10-seq-sim-string": ['SEQ_SIM', 'STRING'],
    "2017_10-seq-sim-x5-string-14": ['SEQ_SIM', 'STRING'],
    "2017_10-seq-sim-x5-string": ['SEQ_SIM', 'STRING'],
    "2017_10-string": ['STRING'],
    "2017_10-string-14": ['STRING'],
    "2018_02-seq-sim": ['SEQ_SIM'],
    }


VERSION_SELECTED_STRAINS = {
    "2017_10-seq-sim": 'inputs/selected-strains.txt',
    "2017_10-seq-sim-string": 'inputs/selected-strains.txt',
    "2017_10-seq-sim-x5-string": 'inputs/selected-strains.txt',
    "2017_10-string": 'inputs/selected-strains.txt',
    "2017_10-seq-sim-14": 'inputs/selected-strains-14.txt',
    "2017_10-seq-sim-x5-string-14": 'inputs/selected-strains-14.txt',
    "2017_10-string-14": 'inputs/selected-strains-14.txt',
    "2018_02-seq-sim": "inputs/selected-strains/2018_02-strains-14.txt",
}
SELECTED_STRAINS = "inputs/selected-strains.txt"

ALGORITHM_OPTIONS = {
    "local-ova": "--ova local",
    "local-ovn": "--ovn local",
    #"fun-flow-ova": "--ova functional-flow",
    "fun-flow-ovn": "--ovn functional-flow",
    "sinksource-ova": "--ova sinksource",
    "sinksource-ovn": "--ovn sinksource",
    "genemania-ova": "--ova genemania",
}

#STRING_NETWORKS = {
#    "2017_10-string": ""
#    "2017_10-seq-sim-string": ""
#    }
# STRING networks are in the individual taxon dirs
#STRING_TAXON_UNIPROT = "%s/%%s/%%s-uniprot-links-v10.5-%%d.txt" % (STRING_TAXON_DIR)

NAME_TO_SHORTNAME = {
    "Neisseria gonorrhoeae FA 1090"                             : "Ng",
    "Peptoclostridium difficile / Clostridioides difficile 630" : "Cd",
    "Helicobacter pylori 85962"                                 : "Hp",
    "Klebsiella pneumoniae"                                     : "Kp",
    "Enterococcus faecium DO"                                   : "Ef",
    "Escherichia coli K-12"                                     : "Ec",
    "Haemophilus influenzae RD KW20"                            : "Hi",
    "Bordetella pertussis Tohama I"                             : "Bp",
    "Burkholderia cepacia"                                      : "Bc",
    "Clostridium botulinum A str. Hall"                         : "Cb",
    "Acinetobacter baumannii"                                   : "Ab",
    "Staphylococcus aureus"                                     : "Sa",
    "Vibrio cholerae O1 biovar El Tor str. N16961"              : "Bc",
    "Yersinia pestis"                                           : "Yp",
    "Streptococcus pyogenes"                                    : "Sp",
    "Pseudomonas aeruginosa"                                    : "Pa",
    "Salmonella typhimurium / Salmonella enterica"              : "Se",
    "Shigella dysenteriae serotype 1 (strain Sd197)"            : "Sd",
    "Mycobacterium tuberculosis"                                : "Mt",
}
NAME_TO_TAX = {}
TAX_TO_NAME = {}

GOA_DIR = "/data/inputs/goa"
GOA_TAXON_DIR = "%s/taxon" % (GOA_DIR)

# input files
GO_FILE = "%s/2017-09-26-go.obo" % (GOA_DIR)
GOA_FILE = "%s/2017-09-26-goa_uniprot_all.gaf.gz" % (GOA_DIR)
GO_FILE_NOPARTOF = "%s/2017-09-26-go-no-partof.obo" % (GOA_DIR)

# parsed input files
# for example: inputs/goa/taxon/22839/22839-goa.gaf
GOA_TAXON_FILE = "%s/%%s/%%s-goa.gaf" % (GOA_TAXON_DIR)
# file containing annotations propogated up the GO DAG hierarchy
# also formatted to be used as input for GAIN
FUN_FILE = "%s/%%s/%%s-goa-all-fun.txt" % (GOA_TAXON_DIR)
FUN_FILE_NOPARTOF = "%s/%%s/%%s-goa-all-fun-nopartof.txt" % (GOA_TAXON_DIR)
# file containing all annotations for the 19 species
GOA_ALL_FUN_FILE = "%s/all-taxon-goa.txt" % (GOA_TAXON_DIR)
# file containing all annotations for the 19 species without IEA
GOA_ALL_FUN_FILE_NOIEA = "%s/all-taxon-goa-noiea.txt" % (GOA_TAXON_DIR)
# file containing all annotations for the 19 species without IEA 
# and without "part_of" relationships in the OBO file
GOA_ALL_FUN_FILE_NOPARTOF = "%s/all-taxon-goa-nopartof.txt" % (GOA_TAXON_DIR)
GOA_ALL_FUN_FILE_NOIEA_NOPARTOF = "%s/all-taxon-goa-noiea-nopartof.txt" % (GOA_TAXON_DIR)

# STRING directories and file templates
STRING_DIR = "/data/inputs/string"
STRING_TAXON_DIR = "%s/taxon" % (STRING_DIR)
STRING_FILE = "%s/protein.links.full.v10.5.txt.gz" % (STRING_DIR)
STRING_TO_UNIPROT = "%s/full_uniprot_2_string.04_2015.tsv" % (STRING_DIR)
# cutoff to be used for the STRING interactions
# Ranges from 150-1000
# 400 is considered a "Medium" cutoff
STRING_CUTOFF = 400

# Template for a species/taxon STRING file
# Last number is the cutoff used on interactions in this file
# for example: inputs/string/taxon/9606/9606.links.full.v10.5-400.txt
STRING_TAXON_FILE = "%s/%%s/%%s.links.full.v10.5-%%d.txt" % (STRING_TAXON_DIR)
# STRING FILE mapped to uniprot IDs
STRING_TAXON_UNIPROT = "%s/%%s/%%s-uniprot-links-v10.5-%%d.txt" % (STRING_TAXON_DIR)

# first column is uniprot ID, last is STRING ID
UNIPROT_TO_STRING = "inputs/protein-similarity/uniprot-species/uniprot-proteins-19-strains-plus-string.tab"
# first column is uniprot ID, second is organism ID
UNIPROT_TO_SPECIES = "inputs/protein-similarity/uniprot-species/2017-10-17-uniprot-prots-19-species.tab"

# The epsilon value (convergence criteria for SinkSource and GeneMANIA) is hard-coded, 
# so I had to re-build biorithm for each of the values we wanted to test
ALLOWED_GAIN_EPSILON = [0.0001, 0.001, 0.01]
DEFAULT_GAIN_EPSILON = 0.0001
BIORITHM_GAIN_EPSILONS = {
        0.0001: "/home/jeffl/src/c++/biorithm/trunk",
        0.001: "/home/jeffl/src/c++/biorithm/eps-0_001-nopartof",  # I modified the "GO.C" script in the libfun dir to not use part_of relationships for propogating annotations
        0.01: "/home/jeffl/src/c++/biorithm/eps-0_01",
    }
BIORITHM_UBUNTU14_GAIN_EPSILONS = {
        0.0001: "/home/jeffl/src/c++/biorithm-ubuntu14/trunk",
        0.001: "/home/jeffl/src/c++/biorithm-ubuntu14/eps-0_001",
        0.01: "/home/jeffl/src/c++/biorithm-ubuntu14/eps-0_01",
    }

# code directory
# TODO make the epsilon value an option
#BIORITHM_ubuntu16 = "/home/jeffl/src/c++/biorithm/trunk"
#BIORITHM_ubuntu16 = "/home/jeffl/src/c++/biorithm/eps-0_001"
#BIORITHM_ubuntu16 = "/home/jeffl/src/c++/biorithm/eps-0_01"
# use the ubuntu14 built version of GAIN on ubuntu 14 because the c++ packages are different
#BIORITHM_ubuntu14 = "/home/jeffl/src/c++/biorithm-ubuntu14/trunk"

#BIORITHM = BIORITHM_ubuntu16
BIORITHM = BIORITHM_GAIN_EPSILONS[DEFAULT_GAIN_EPSILON]
#ubuntu14_hosts = ['spode', 'cuthbert']
ubuntu14_hosts = ['spode', 'agatha', 'prosser', 'molloy', 'pirbright', 'cowcreamer']

# -------------------------------------- Algorithm options ---------------------------------------
#neg_weight = sum([G.degree(p, weight='weight')/G.degree(p) for p in positives]) / float(len(positives))
#print("Setting the weight of the negative node to the avg of the positive nodes: %s" % (str(neg_weight)))
# fix the lambda values for now to be close to the average weight of the entire network
# TODO setup an automatic way for choosing lambda (i.e., the average weight of the positive nodes)
VERSION_SS_LAMBDA = {
    "2017_10-seq-sim": 10,
    "2017_10-seq-sim-x5-string": 50,
    "2017_10-string": 650,
    "2018_02-seq-sim": 70,
}

VERSION = ''
INPUTSPREFIX = ''
RESULTSPREFIX = ''
# processed network file for each version
NETWORK_template = "inputs/%s/%s-net.txt"


def set_version(version, epsilon=DEFAULT_GAIN_EPSILON):
    global VERSION, INPUTSPREFIX, RESULTSPREFIX, NETWORK
    global BIORITHM
    global NAME_TO_TAX, TAX_TO_NAME

    VERSION = version
    print("Using version '%s'" % (VERSION))

    INPUTSPREFIX = "inputs/%s" % VERSION
    RESULTSPREFIX = "outputs/%s" % VERSION
    NETWORK = NETWORK_template % (VERSION, VERSION)

    selected_strains = utils.readItemSet(VERSION_SELECTED_STRAINS[VERSION], 1)
    TAX_TO_NAME = utils.readDict(VERSION_SELECTED_STRAINS[VERSION], 1,2)
    NAME_TO_TAX = utils.readDict(VERSION_SELECTED_STRAINS[VERSION], 2,1)

    # set the biorithm/gain build according to the epsilon value it was built with
    BIORITHM = BIORITHM_GAIN_EPSILONS[epsilon]
    for host in ubuntu14_hosts:
        if host in socket.gethostname():
            BIORITHM = BIORITHM_UBUNTU14_GAIN_EPSILONS[epsilon]

    return INPUTSPREFIX, RESULTSPREFIX, NETWORK, selected_strains
