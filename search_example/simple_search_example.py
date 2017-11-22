import requests
import pprint

search_url = 'http://www.ebi.ac.uk/pdbe/search/pdb/select?q='
search_variables = '&wt=json&rows=10'


def format_search_terms(search_term):
    print('formatting search terms: %s' % search_term)
    if '&' in search_term:
        search_term = search_term.replace('&', ' AND ')
    print('formatted search terms: %s' % search_term)
    return search_term


def url_response(url):
    print(url)
    r = requests.get(url=url)
    if r.status_code == 200:
        json_result = r.json()
        return json_result
    else:
        print(r.status_code, r.reason)
        return None


def run_search(pdbe_search_term):
    pdbe_search_term = format_search_terms(pdbe_search_term)
    full_query = search_url + pdbe_search_term + search_variables
    print(full_query)

    response = url_response(full_query)
    if 'response' in response:
        if 'docs' in response['response']:
            return response['response']['docs']
    return None

search_terms = 'molecule_name:"Dihydrofolate%20reductase"&organism_scientific_name:"Homo%20sapiens"'
results = run_search(search_terms)
pprint.pprint(results)

pdb_list = []
for result in results:
    #print(result['all_authors'])
    pdb = result['pdb_id']
    if pdb not in pdb_list:
        pdb_list.append(pdb)

print(pdb_list)