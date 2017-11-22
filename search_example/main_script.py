# example scripts for how to use the PDB API to do a simple sequence search or query the PDBe search API
# author: John Berrisford
# date: June 2016

import argparse

import search
import ebi_search
import variables
import pdbe_images
import bottle

def main():
    # test sequence
    seq = 'MMYKEPFGVKVDFETGIIEGAKKSVRRLSDMEGYFVDERAWKELVEKEDPVVYEVYAVEQEEKEGDLNFATTVLYPGKVGKEFFFTKGHFHAKLDRAEVYVALKGKGGMLLQTPEGDAKWISMEPGTVVYVPPYWAHRTVNIGDEPFIFLAIYPADAGHDYGTIAEKGFSKIVIEENGEVKVVDNPRW'
    test_domain_type = 'Pfam'

    # run the main method with the seq and test_domain_type
    html = sequence_search_example(sequence_in=seq, domain_type=test_domain_type)

    print(html)


def pdbe_search_example(search_query):
    """
    do a search of the PDBe search API and return PDB ID and species name
    :param search_query: this should be a text string which will return a search result.
    for example: all_molecule_names:"Phosphoglucose%20isomerase"
    :return: this returns a web page to be displayed
    """

    result_list = search.format_pdbe_search_result(entered_search_term=search_query)
    '''
        example result_list
        result_dict = {'pdbid': pdbid, 'species': species,
                                       'extra': []}

        extra is a list of image urls
        '''
    if result_list:
        result_list = add_domains(result_list=result_list, domain_type='Pfam')
        print(result_list)
        return bottle.template('test_template', result_list=result_list)
        # make a web page to display to the user
        #result_html = make_html.build_html(result_list=result_list)
        #if result_html:
        #    return result_html
    else:
        return "no results"

def add_domains(result_list, domain_type):
    if result_list:
        print(result_list)
        for instance, result in enumerate(result_list):
            pdbid = result['pdbid']

            # find all domains for the PDB id using the PDBe API
            pdb_mapping = search.pdbe_mappings(pdbid)

            # if the PDB has domains of type domain_type then add them to the result
            if domain_type in pdb_mapping:
                for domain in pdb_mapping[domain_type]:
                    # add each domain to result list
                    domain_image = pdbe_images.get_domain_url(pdbid, domain_type, domain)
                    #image = variables.image_html % (domain_image, domain_image, variables.image_size)
                    result_list[instance]['extra'].append(domain_image)

    return result_list

def sequence_search_example(sequence_in, domain_type):
    """
    do a search - go through results and look for domains defined by domainType - then return a webpage.
    :param sequence_in: this is a sequence of amino acids
    :param domain_type: only get results with this domain type, for example Pfam
    :return: a html document which can be displayed in a browser
    """

    # do a search using fasta serach at EBI
    result_list = ebi_search.ebi_search(sequence=sequence_in, email='jmb@ebi.ac.uk').return_result()

    # do a search using hmmer at EBI using the seq, results are in result_list
    #result_list = search.format_hmmer_result(sequence_in)  # result list is a list of dictionaries
    '''
    example result_list
    result_dict = {'pdbid': pdbid, 'eValue': e_value, 'species': species,
                                   'extra': []}

    extra is a list of image urls
    '''

    # if there is a result from the search
    if result_list:
        result_list = add_domains(result_list=result_list, domain_type=domain_type)

        # make a web page to display to the user
        return bottle.template('test_template', result_list=result_list)
        #result_html = make_html.build_html(result_list=result_list)
        #if result_html:
        #    return result_html
    else:
        return "no results"

# start here.    To see how this looks on a web page run web_response.py
if __name__ == '__main__':

    main()