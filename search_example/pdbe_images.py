import variables
from search import url_response

def get_domain_url(pdbid, domain_type, domain_id):
    """
    get a URL for the image of the domain_id for a given PDB entry
    :param pdbid: PDB id code
    :param domain_type: type of the domain (Pfam, SCOP, CATH)
    :param domain_id: identifier of the domain
    :return: URL for the image used on the PDBe website for the domain for the PDB entry.
    """
    json_url = variables.images_base_url + pdbid + '_json'
    image_json = url_response(json_url, 'image_json')
    filename = ''
    if pdbid in image_json:
        if 'entity' in image_json[pdbid]:
            for entity in image_json[pdbid]['entity']:
                if 'database' in image_json[pdbid]['entity'][entity]:
                    if domain_type in image_json[pdbid]['entity'][entity]['database']:
                        if domain_id in image_json[pdbid]['entity'][entity]['database'][domain_type]:
                            for image in image_json[pdbid]['entity'][entity]['database'][domain_type][domain_id]['image']:
                                filename = image['filename']
    if filename:
        #image_url = variables.images_base_url + filename + variables.image_suffix
        return filename

        #return image_url
    else:
        return None
