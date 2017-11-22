import requests
import variables
import time
import xml.etree.ElementTree as ET

ebi_rest_url = 'http://www.ebi.ac.uk/Tools/services/rest/fasta/'

class ebi_search:

    def __init__(self, sequence, email):

        self.result_list = []
        self.sequence = sequence
        self.search_parameters = {'email': email,
                        'program': 'fasta',
                        'database': 'pdb',
                        'stype': 'protein',
                        'sequence': self.sequence}

        self.search_id = self.post_sequence()
        if self.search_id:
            finished = self.get_search_status()
            if finished:
                self.xml_text = self.get_search_result()
                if self.xml_text:
                    self.result_list = self.format_xml()
                else:
                    print('no xml file output')
            else:
                print('search failed')
        else:
            print('no search id issued')

    def return_result(self):
        return self.result_list

    def post_sequence(self):
        r = requests.post(ebi_rest_url + 'run/', data=self.search_parameters)
        #print(r.url)
        #print(r.text)
        #print(r.status_code, r.reason)
        if r.status_code == 200:
            return r.text
        return False

    def get_search_status(self):
        finished = False
        time.sleep(5)
        url = ebi_rest_url + 'status/' + self.search_id
        #print(url)
        while not finished:
            r = requests.get(url=url)
            print(r.text)
            if r.text == 'RUNNING':
                time.sleep(5)
            elif r.text == 'FINISHED':
                return True
            else:
                finished = True
                print(r.text)
        return False

    def get_search_result(self, output_format='xml'):
        url = ebi_rest_url + 'result/' + self.search_id + '/' + output_format
        #print(url)
        r = requests.get(url=url)
        #print(r.status_code, r.reason)
        if r.status_code == 200:
            return r.text
        return False

    def format_xml(self):
        result_list = []
        found_pdbs = []
        root = ET.fromstring(self.xml_text)
        for child in root:
            #print(child.tag, child.attrib)
            if 'SequenceSimilaritySearchResult' in child.tag:
                for hitsummary in child:
                    num_results = hitsummary.attrib['total']
                    #print(num_results)
                    for hit in hitsummary:
                        score = None
                        pdbid = hit.attrib['id'][:4].lower()   # pdb code is the first 4 characters of the attribute id
                        chain = hit.attrib['id'][-1]           # chain id is the last character of the attribute it

                        for h in hit[0][0]:
                            if 'score' in h.tag:
                                score = int(h.text)
                        if pdbid not in found_pdbs:
                            species_list = self.get_species(pdbid=pdbid, chain=chain)
                            entry_dict = {'pdbid': pdbid, 'score': score, 'chain': chain,
                                          'extra': [], 'eValue': score, 'species': species_list}
                            result_list.append(entry_dict)
                            found_pdbs.append(pdbid)

        return result_list

    def get_species(self, pdbid, chain):
        species_list = []
        molecules_url = variables.molecules_url + pdbid
        #print(molecules_url)
        r = requests.get(url=molecules_url)
        if r.status_code == 200:
            json_result = r.json()
            if pdbid in json_result:
                for entity in json_result[pdbid]:
                    #print(entity)
                    if chain in entity['in_chains']:
                        if 'source' in entity:
                            for source in entity['source']:
                                organism = source['organism_scientific_name']
                                #print organism
                                species_list.append(organism)
        else:
            print(r.status_code, r.reason)

        return species_list

if '__main__' in __name__:
    seq = """MMYKEPFGVKVDFETGIIEGAKKSVRRLSDMEGYFVDERAWKELVEKEDPVVYEVYAVEQEEKEGDLNFATTVLYPGKVGKEFFFTKGHFHAKLDRAEVYVALKGKGGMLLQTPEGDAKWISMEPGTVVYVPPYWAHRTVNIGDEPFIFLAIYPADAGHDYGTIAEKGFSKIVIEENGEVKVVDNPRW"""
    result_list = ebi_search(sequence=seq, email='jmb@ebi.ac.uk').return_result()
    print(result_list)