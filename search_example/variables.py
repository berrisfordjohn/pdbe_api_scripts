# PDBe base urls
base_url = 'http://www.ebi.ac.uk/pdbe/'
api_base = base_url + 'api/'
mappings_url = api_base + 'mappings/'
molecules_url = api_base + 'pdb/entry/molecules/'

# urls for images
images_base_url = base_url + 'static/entry/'
image_suffix = "_image-800x800.png"
image_size = '200'
image_html = "<th style='border: #000 1px dashed; vertical-align: top'>" \
             "<a href='%s'><img src='%s' target='_blank' width=%s></a>" \
             "</th>"

hmmer_url = 'http://www.ebi.ac.uk/Tools/hmmer/search/phmmer'
