import pprint
import re
import requests
import variables

def main():
    # test the PDBe search

    # search_term = 'all_molecule_names:"Phosphoglucose%20isomerase"'
    # result = format_pdbe_search_result(entered_search_term=search_term)
    # print(result)

    seq = '''
        MVDREQLVQKARLAEQAERYDDMAAAMKNVTELNEPLSNEERNLLSVAYKNVVGARRSSW
    RVISSIEQKTSADGNEKKIEMVRAYREKIEKELEAVCQDVLSLLDNYLIKNCSETQYESK
    VFYLKMKGDYYRYLAEVATGEKRATVVESSEKAYSEAHEISKEHMQPTHPIRLGLALNYS
    VFYYEIQNAPEQACHLAKTAFDDAIAELDTLNEDSYKDSTLIMQLLRDNLTLWTSDQQDD
    DGGEGNN
    '''

def url_response(url, description):
    print(url)
    url = encode_url(url=url)
    r = requests.get(url=url)
    if r.status_code == 200:
        json_result = r.json()
        return json_result

    else:
        print(r.status_code, r.reason)
        return None

def encode_url(url):
    print('encoding url: %s' % url)
    url = re.sub(" ", "%20", url)
    print('encoded url: %s' % url)
    return url

def format_search_terms(search_term):

    print('formating search terms: %s' % search_term)
    if '&' in search_term:
        search_term = search_term.replace('&', ' AND ')
    print('formatted search terms: %s' % search_term)
    return search_term

def pdbe_search(pdbe_search_term):
    """
    use PDBe's search API to search the PDB
    see
    http://www.ebi.ac.uk/pdbe/api/doc/search.html
    for documentation
    search using PDBe's API
    :param pdbe_search_term: the search term used to search the API
    :return:
    """
    search_url = variables.base_url + 'search/pdb/select?q='
    # suffix = '&wt=json&indent=true&rows=10'
    suffix = '&wt=json&indent=true&rows=10'
    pdbe_search_term = format_search_terms(pdbe_search_term)

    full_query = search_url + pdbe_search_term + suffix

    '''print(the query so we can see what is going on '''
    print(full_query)
    print('run the query \n')

    response = url_response(full_query, 'search')

    '''to look into the search results for pdbids's do something like this'''
    if 'response' in response:
        if 'docs' in response['response']:
            return response['response']['docs']
        else:
            print('No results')
            return None
    else:
        print('No results')
        return None


def format_pdbe_search_result(entered_search_term):
    result_list = []
    pdbid_list = []
    search_result = pdbe_search(pdbe_search_term=entered_search_term)
    if search_result:
        for res in search_result:
            #pprint.pprint(res)
            status = res['status']
            if status == 'REL':
                pdbid = res['pdb_id']
                species = res['entry_organism_scientific_name']

                # check we haven't seen the PDB ID yet
                if pdbid not in pdbid_list:
                    result_dict = {'pdbid': pdbid, 'species': species,
                                   'extra': []}
                    result_list.append(result_dict)

                    # keep track of PDB ID's already seen
                    pdbid_list.append(pdbid)
        return result_list
    else:
        return None

def pdbe_mappings(pdbid):
    mappings_query = variables.mappings_url + pdbid
    do_mappings_query = url_response(mappings_query, 'mappings')
    if pdbid in do_mappings_query:
        mapping_result = do_mappings_query[pdbid]
    else:
        mapping_result = None

    return mapping_result


def pdbe_api_return(pdbid, url):
    query = url + pdbid
    do_query = url_response(query, 'pdbe_api')
    if pdbid in do_query:
        result = do_query[pdbid]
    else:
        result = None

    return result


if '__main__' in __name__:
    main()