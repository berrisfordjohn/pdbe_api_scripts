import requests

id_code = '1cbs'
molecules_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/'

full_url = molecules_url + id_code

def url_response(url):
    r = requests.get(url=url)
    if r.status_code == 200:
        json_result = r.json()
        return json_result
    else:
        print(r.status_code, r.reason)
        return None

my_result = url_response(full_url)
my_entries_results = my_result[id_code]
for molecule in my_entries_results:
    entity_id = molecule['entity_id']
    molecule_names = molecule['molecule_name']
    print('%s: %s' % (entity_id, molecule_names))
