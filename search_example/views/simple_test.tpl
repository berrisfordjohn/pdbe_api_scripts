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
                     <th style='border: #000 1px dashed; vertical-align: top'>Protein Name</th>
                     <th style='border: #000 1px dashed; vertical-align: top'>Ligands</th>
                     <th style='border: #000 1px dashed; vertical-align: top'>Mutation</th>
                     <th style='border: #000 1px dashed; vertical-align: top'>Uniprot Acc</th>
                     <th style='border: #000 1px dashed; vertical-align: top'>Picture</th>

                 </tr>

                % for result in result_list:
                        <tr>
                            <th style='border: #000 1px dashed; vertical-align: top'>
                                <a href=//pdbe.org/{{result['pdbid']}} target='_blank'>{{result['pdbid']}}</a>
                            </th>
                            <th style='border: #000 1px dashed; vertical-align: top'>
                                <p>{{result['entity_id']}}</p>
                            </th>
                            <th> style='border: #000 1px dashed; vertical-align: top'>
                                <p>{{result}}</p>
                            </th>
                            <th style='border: #000 1px dashed; vertical-align: top'>
                                % for mutation in result['mutation']:
                                    <p>{{mutation}}</p>
                                % end
                            </th>

                        </tr>
                % end

            </table>

</body>
</html>