import variables
import get_api_result

simple_list = ['1cbs', '2gc2']
simple_dictionary = {'pdbid': '1cbs',
                     'mol_name': 'a molecule'}

dictionary_like_pdbe_api = {'1cbs': [
    {
        "related_structures": [],
        "split_entry": [],
        "title": "CRYSTAL STRUCTURE OF CELLULAR RETINOIC-ACID-BINDING PROTEINS I AND II IN COMPLEX WITH ALL-TRANS-RETINOIC ACID AND A SYNTHETIC RETINOID",
        "release_date": "19950126",
        "experimental_method": [
            "X-ray diffraction"
        ],
    }
]
}


def iterate_through_list():
    for item in simple_list:
        print(item)

def get_value_from_list():
    print('item from list')
    first_from_list = simple_list[0]
    #change the number to a higher number to get the next value. Lists are zero indexed so the first value is zero.
    print(first_from_list)

    #pass back the pdbid so you can use it in other functions
    return first_from_list

def get_value_from_dictionary():
    pdbid = simple_dictionary['pdbid']
    #try changing this to get the "mol_name"
    print(pdbid)

    #to pass the pdbid back so you can use it again
    return pdbid

def get_value_from_dictionary_list_pdbe_api(pdbid='1cbs'):
    """

    :param pdbid: this is the pdbid you want to query with. it will default to 1cbs if you don't pass another value
    :return:
    """
    # the pdbe api usually starts with a pdbid then a list then a dictionary
    pdb_details = dictionary_like_pdbe_api[pdbid][0]
    print(pdb_details)
    #to get an item from pdb_details use the "key" to get the information i.e.
    title = dictionary_like_pdbe_api[pdbid][0]['title']
    print(title)
    exp_method_list = dictionary_like_pdbe_api[pdbid][0]['experimental_method']
    print(exp_method_list)

def get_value_from_pdbe_api(pdbid='1cbs'):
    """

    :param pdbid: this is the pdbid you want to query with. it will default to 1cbs if you don't pass another value
    :return:
    """
    #get url from the variables and add the pdbid on the end, + adds two strings together.
    url = variables.summary_url + pdbid
    print(url)
    entry_info = get_api_result.return_api_info(url=url)
    print(entry_info)
    title = entry_info[pdbid][0]['title']
    print(title)

def get_molecule_infomation_from_pdbe_api(pdbid='1cbs'):
    url = variables.molecules_url + pdbid
    molecule_info = get_api_result.return_api_info(url=url)
    print(molecule_info)

    #iterate through the molecules and find entity 1
    for molecule in molecule_info[pdbid]:
        #print(molecule)
        if molecule['entity_id'] == 1:
            molecule_name_list = molecule['molecule_name']
            print(molecule_name_list)

    #what chains does molecule 1 have?
    #what is the ligand in this entry?

    #can you find anything else about this ligand
    #i.e. try using the ligand_summary_url with the het code for this ligand ('chem_comp_ids')


def main():
    # start here!
    print('starting here') # text must be quoted so it prints. variables don't need to be
    a_name = 'bob'
    print(a_name)

    iterate_through_list()
    pdbid = get_value_from_list()   # this pdbid is used in later functions
    get_value_from_dictionary()

    #now lets get a bit more complicated
    #pdbes api returns a JSON which looks a bit like the dictionary_like_pdbe_api
    get_value_from_dictionary_list_pdbe_api(pdbid=pdbid)

    #pdbes api is available through pdbe.org/api
    #some urls are set as variables in the variables.py file
    get_value_from_pdbe_api(pdbid=pdbid)
    get_molecule_infomation_from_pdbe_api(pdbid=pdbid)

if '__main__' in __name__:
    main()
