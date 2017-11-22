
#get urls from the file variables.py
import variables

#import python modules to handle the getting of data
import requests
import xml.etree.ElementTree as ET


def return_api_info(url, is_json=True):
    r = requests.get(url=url)
    # check that the status code return is 200
    if r.status_code == 200:
        if is_json:
            #pass the json back
            return r.json()
        else:
            # must be an xml file - send it back as parsed XML file
            return ET.fromstring(r.text)
    else:
        print(r.status_code, r.text)
        return None


