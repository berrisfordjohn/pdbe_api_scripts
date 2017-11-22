import requests
from pprint import pprint
import json


#search_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/'
id_code = '1cbs'
search_url = 'http://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/' + id_code

def url_response(url):
    print(url)
    r = requests.get(url=url)
    if r.status_code == 200:
        json_result = r.json()
        return json_result
    else:
        print(r.status_code, r.reason)
        return None


results = url_response(search_url)
molecules_list = results[id_code]
#pprint(molecules_list)
for dict in molecules_list:
    entity_id = dict['entity_id']
    molecule_name_list = dict['molecule_name']
    molecule_name = ','.join(molecule_name_list)
    print('entity id is %s ' % entity_id)
    print('molecule name is %s ' % molecule_name)
#pprint.pprint(results)
