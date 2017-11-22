<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

</head>
<body>
    <title>search results</title>

    <html><body><table>
                 <tr>
                 <th style='border: #000 1px dashed; vertical-align: top'>PDB ID</th>
                 <th style='border: #000 1px dashed; text-align: center'>Species</th>
                 <th style='border: #000 1px dashed; text-align: center'>Entry image</th>
                 <th style='border: #000 1px dashed; text-align: center'>Domains</th>
                 </tr>

                % for result in result_list:
                        <tr>
                            <th style='border: #000 1px dashed; vertical-align: top'>
                                <a href=//pdbe.org/{{result['pdbid']}} target='_blank'>{{result['pdbid']}}</a>
                            </th>
                            <th style='border: #000 1px dashed; vertical-align: top'>
                                <p>{{'\n'.join(result['species'])}}</p>
                            </th>
                            <th style='border: #000 1px dashed; vertical-align: top'>
                                <a href="http://www.ebi.ac.uk/pdbe/static/entry/{{result['pdbid']}}_deposited_chain_front_image-800x800.png">
                                    <img src="http://www.ebi.ac.uk/pdbe/static/entry/{{result['pdbid']}}_deposited_chain_front_image-200x200.png" target='_blank' width=200></a>
                            </th>

                            <th style='border: #000 1px dashed; vertical-align: top'>
                                % for domain in result['extra']:
                                    <a href="http://www.ebi.ac.uk/pdbe/static/entry/{{domain}}_image-800x800.png">
                                        <img src="http://www.ebi.ac.uk/pdbe/static/entry/{{domain}}_image-200x200.png" target='_blank' width=200></a>
                                % end
                            </th>
                        </tr>
                % end

    </table>

</body>
</html>