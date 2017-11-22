from bottle import Bottle, run, request, template
import main_script
app = Bottle()


@app.route('/')
def sequence():
    return '''
        <form action="/sequence_result" method="post">
            Get Pfam domains from entries with a similar sequence <br>
            Enter a protein sequence in one letter code to search the PDB with. <br>
            example<br>
            MMYKEPFGVKVDFETGIIEGAKKSVRRLSDMEGYFVDERAWKELVEKEDPVVYEVYAVEQEEKEGDLNFATTVLYPGKVGKEFFFTKGHFHAKLDRAEVYVALKGKGG
            MLLQTPEGDAKWISMEPGTVVYVPPYWAHRTVNIGDEPFIFLAIYPADAGHDYGTIAEKGFSKIVIEENGEVKVVDNPRW<br>
            Sequence to search: <input name="sequence" type="textbox" />
            <input value="enter" type="submit" />
        </form>
        <br><br>
        <form action="/search_result" method="post">
            Use the PDBe API to search the PDB <br>
            Enter a search term to search the PDB with. <br>
            See http://www.ebi.ac.uk/pdbe/api/doc/search.html <br>
            for full list <br>
            example: all_molecule_names:"Phosphoglucose%20isomerase"<br>
            Search term: <input name="search" type="textbox" />
            <input value="enter" type="submit" />
        </form>
    '''


@app.route('/sequence_result', method='POST')
def do_sequence():
    sequence_from_html = request.forms.get('sequence')
    sequence_result_html = main_script.sequence_search_example(sequence_in=sequence_from_html, domain_type='Pfam')
    if sequence_result_html:
        return sequence_result_html
    else:
        return "<p> no results found</p>"


@app.route('/search_result', method='POST')
def do_search():
    search_from_html = request.forms.get('search')
    search_result_html = main_script.pdbe_search_example(search_query=search_from_html)
    if search_result_html:
        return search_result_html
    else:
        return "<p> no results found</p>"


@app.route('/test')
def simple_test():
    result_list = [{'pdbid':'2gc2','entity_id':1,'mutation':['A34S','G67R']},
                   {'pdbid':'2yi7','entity_id':1,'mutation':['A34S','G67R']},
                   {'pdbid':'2gc3','entity_id':1,'mutation':['A34S','G67R']}
                   ]
    return template('simple_test.tpl', result_list=result_list)

if '__main__' in __name__:
    run(app, host='localhost', port=10000)

