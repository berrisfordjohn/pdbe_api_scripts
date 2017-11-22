import requests

search_url = 'http://www.ebi.ac.uk/pdbe/search/pdb/select?q='
search_variables = '&wt=json&rows=10'

def url_response(url):
    r = requests.get(url=url)
    if r.status_code == 200:
        json_result = r.json()
        return json_result
    else:
        print(r.status_code, r.reason)
        return None

def run_search(pdbe_search_term):
    full_query = search_url + pdbe_search_term + search_variables

    response = url_response(full_query)
    if 'response' in response:
        if 'docs' in response['response']:
            return response['response']['docs']
    return None

search_terms = 'molecule_name:"Dihydrofolate%20reductase" AND organism_scientific_name:"Homo%20sapiens"'
results = run_search(search_terms)

pdb_list = []
for result in results:
    pdb = result['pdb_id']
    if pdb not in pdb_list:
        pdb_list.append(pdb)

print(pdb_list)


