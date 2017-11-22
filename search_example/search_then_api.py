import requests
from pprint import pprint

pdbe_url = 'http://www.ebi.ac.uk/pdbe'
pdbe_api_url = pdbe_url + '/api'
mutation_url = pdbe_api_url + '/pdb/entry/mutated_AA_or_NA/'
pdbe_search_url = pdbe_url + '/search/pdb/select?q='
search_variables = '&wt=json&rows=10'

def url_response(url):
    r = requests.get(url=url)
    if r.status_code == 200:
        json_result = r.json()
        return json_result
    else:
        print(r.status_code, r.reason)
        return None

def format_search_terms(search_term):
    print('formatting search terms: %s' % search_term)
    if '&' in search_term:
        search_term = search_term.replace('&', ' AND ')
    print('formatted search terms: %s' % search_term)
    return search_term

def get_pdbe_api_json(url, pdbid):
    full_url = url + pdbid
    my_result = url_response(full_url)
    if pdbid in my_result:
        my_entries_results = my_result[pdbid]
        return my_entries_results
    return None

def run_search(pdbe_search_term):
    pdbe_search_term = format_search_terms(pdbe_search_term)
    full_query = pdbe_search_url + pdbe_search_term + search_variables
    print(full_query)
    response = url_response(full_query)
    if 'response' in response:
        if 'docs' in response['response']:
            return response['response']['docs']
    return None

def build_search_url(uniprot_list):
    uniprot_list_modified = []
    uniprot_prefix = 'uniprot_accession'
    for uniprot in uniprot_list:
        uniprot = '%s:%s' %(uniprot_prefix, uniprot)
        uniprot_list_modified.append(uniprot)

    uniprot_string = ' OR '.join(uniprot_list_modified)
    return uniprot_string

def main():

    my_result_dict = {}
    seen_pdbids = []
    uniprot_list = ['Q13224', 'P61073', 'P23975']

    search_string = build_search_url(uniprot_list=uniprot_list)
    results = run_search(search_string)
    for result in results:
        #pprint(result)
        pdbid = result['pdb_id']
        entity_id = result['entity_id']
        uniprots_for_entity = result['uniprot_accession']
        uniprot = list(set(uniprot_list).intersection(uniprots_for_entity))[0]
        #print(pdbid)
        #print(uniprot)

        if pdbid not in seen_pdbids:
            seen_pdbids.append(pdbid)
            my_result_dict.setdefault(uniprot, {}).setdefault(pdbid, [])

            mutations = get_pdbe_api_json(url=mutation_url, pdbid=pdbid)
            if mutations:
                for mutation in mutations:
                    if entity_id == mutation['entity_id']:
                        my_result_dict[uniprot][pdbid].append(mutation)

        return my_result_dict


if '__main__' == __name__:
    my_result = main()
    pprint(my_result)