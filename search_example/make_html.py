import pdbe_images
import variables


def build_html(result_list):
    """
    makes a simple web page table with pre-set headers
    :param result_list: this is a list of dictionaries containing results of the search
    :return: html page
    """

    if result_list:
        # table header for html page
        header = """<html><body><table>
                 <tr>
                 <th style='border: #000 1px dashed; vertical-align: top'>entry id</th>
                 <th style='border: #000 1px dashed; text-align: center'>stats</th>
                 <th style='border: #000 1px dashed; text-align: center'>entry image</th>
                 <th style='border: #000 1px dashed; text-align: center'>extra</th>
                 </tr>"""

        footer = "</table></body></html>"
        body = []

        # make a table body in html to display the results
        for result in result_list:
            pdbid = result['pdbid']
            entry_image = pdbe_images.pdb_entry_image(pdbid)

            # start the row and link to PDB
            body.append("<tr>"
                        "<th style='border: #000 1px dashed; vertical-align: top'>"
                        "<a href=//pdbe.org/%s target='_blank'>%s"
                        "</th>" % (pdbid, pdbid))

            # add any extra statistics from the seach to the html
            body.append("<th style='border: #000 1px dashed; vertical-align: top'>")
            for stat, value in result['stats'].iteritems():
                body.append('%s: %s<br>' % (stat, value))
            body.append('</th>')

            # add image of entry from PDBe website
            body.append(variables.image_html % (entry_image, entry_image, variables.image_size))

            # add extra images from PDBe API
            for extra in result['extra']:
                body.append(extra)

            # close the row
            body.append("</td></tr>")

        # change body list into a string which which can be displayed in a web browser
        body_string = '\n'.join(body)

        # put the header, body and footer together into a html page.
        html = header + body_string + footer
        return html
    else:
        return 'no results'
