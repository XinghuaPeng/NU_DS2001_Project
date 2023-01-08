"""

Xinghua Peng
DS 2001: Intro to Programming with Data

Filename: gad.py 
    
Description: Analyzing connections between genes
and diseases.

Program Outputs: 
    - Best match to asthma: diabetes type 1 (18 genes.)
    - Yes, the research suggest that there is a biological connection between 
    Asthma and the diabetes type 1. 
    - Example URL: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4616625/
    - Survey all diseases: see program_outputs.txt for more information
    
"""


def read_data(filename):
    """Read csv file into a list of lists"""
    with open(filename, "r") as infile:
        # Skip header through data slicing
        data = infile.readlines()[1:]
        for i in range(len(data)):
            data[i] = data[i].split(",")
    
    return data

def build_dictionary(data):
    """ Construct a disease->[gene list] mapping """
    gad_dict = {}
    for line in data:
        gene = line[0]
        disease = line[1]
        if disease in gad_dict:
            if gene not in gad_dict[disease]:
                gad_dict[disease].append(gene)
        else:
           gad_dict[disease] = [gene]
            
    return gad_dict


def intersection(list1, list2):
    """ Return intersection of two lists """
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

def find_max_overlapping_disease(gad_dict, disease):
    """ For a given disease find the disease
    that has the most overlapping genes """
    disease_genes = gad_dict[disease]
    best_match = None
    max_overlap = 0
    
    for dis, genes in gad_dict.items():
        if dis != disease:
            overlap = intersection(disease_genes, genes)
            if len(overlap) > max_overlap:
            # update max_overlap
                max_overlap = len(overlap)
                best_match = dis

    return best_match, max_overlap


def show_all_disease_matches(gad_dict, min_overlap = 1):
    """ For every disease in the dictionary
    find the disease with the most overlapping
    genes.  Print the disease, best match, and
    number of overlapping genes """
    
    for dis, genes in gad_dict.items():
        match, overlap = find_max_overlapping_disease(gad_dict, dis)
        if overlap >= min_overlap:
            print(dis, match, overlap)


def main():
    # Fetch a list of lines
    data = read_data("gad.csv")

    # Create a dictionary: disease (key) -> [gene1,gene2,....] (value)
    gad_dict = build_dictionary(data)
    #print(gad_dict)
    # Find all genes linked to Asthma 
    print("All genes linked to Asthma:", gad_dict["asthma"])
    print("")
    # Compare genes of each disease in dictionary with asthma
    # Find disease with biggest overlap (in terms of # of genes overlapping)
    best_match, num_overlapping = find_max_overlapping_disease(gad_dict, "asthma")


    # Report results
    print("Best match to asthma: "+best_match+" ("+str(num_overlapping)+" genes.)")
    print("")
    
    # Generate all best matches
    print('Survey all diseases and find the most gene overlaps')
    show_all_disease_matches(gad_dict, min_overlap=15)


if __name__ == "__main__":
    main()
