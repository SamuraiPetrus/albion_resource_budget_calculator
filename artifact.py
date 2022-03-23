import json

def createArtifact( artifact_name = 'artefato', artifact_quantity = 0, artifact_level = 0 ):
    '''
    createArtifact

    This function will create an artifact which is equivalent to an Albion resource (such as Wood, Mine, etc).
    '''
    
    print('\n\nCriando artefato:  '+artifact_name+'\n')
    if artifact_quantity == 0:
        artifact_quantity = int(input('\nQuantas unidades de '+artifact_name+' você quer produzir?:  '))

    if artifact_level == 0:
        artifact_level = int(input('\nQual o grau de '+artifact_name+' ?:  '))

    artifact = {
        'name': artifact_name,
        'quantity': artifact_quantity,
        'level': artifact_level,
        'cost': float(input('\nQual o custo em moedas para produzir '+artifact_name+'?:  ')),
        'materials': []
    }

    materials = str(input('\nQuais os materiais necessários para produzí-lo? (Separe por vírgulas, ou deixe vazio para pular essa etapa):  '))
    materials = materials.replace(', ', ',')
    materials = materials.split(',')

    if materials[0] != '':
        artifact = registerMaterialsToArtifact(materials, artifact)
    
    return artifact

def registerMaterialsToArtifact( materials, artifact ):
    '''
    registerMaterialsToArtifact

    This function will register materials to an artifact.
    '''
    
    materials_to_build_artifact = []

    for material_name in materials:
        material_level = int(input('\nQual o grau de '+material_name+' necessário para construir 1 '+artifact.get('name')+'?:  '))
        material_name += ' (Grau '+str(material_level)+')'
        material_quantity = int(input('\nQuantas unidades de '+material_name+' necessário para construir 1 '+artifact.get('name')+'?:  '))

        materials_to_build_artifact.append({
            'name': material_name,
            'quantity': material_quantity * artifact.get('quantity'),
            'level': material_level,
        })
    
    for material in materials_to_build_artifact:
        artifact.get('materials').append(createArtifact(material.get('name'), material.get('quantity'), material.get('level')))

    return artifact

def saveArtifact( artifact ):
    '''
    saveArtifact

    This function will save an artifact to a json file.
    '''
    artifact_json_file = open('artifact.json', 'w+', encoding='utf-8')
    json.dump(artifact, artifact_json_file, indent=4)
    artifact_json_file.close()

    artifact_json_file = open('artifacts/'+artifact.get('name')+'.json', 'w+', encoding='utf-8')
    json.dump(artifact, artifact_json_file, indent=4)
    artifact_json_file.close()