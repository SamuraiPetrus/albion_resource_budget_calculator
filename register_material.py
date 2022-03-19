QUALITY_IMPROVEMENT_MATERIAL = 2

def registerMaterialsToArtifact(materials, artifact):
    for material in materials:
        material_level = 2
        required_quantity_to_build_artifact = int(input('Quantas unidades de '+material+' (Grau '+str(artifact.get('level'))+') serão necessárias?:  '))
        
        while material_level <= artifact.get('level'):
            material_name = material + ' (Grau '+str(material_level)+')'
            material_cost = float(input('Qual o custo em moedas para produzir '+material_name+'?:  '))
            material_quantity = required_quantity_to_build_artifact
            if (material_level > QUALITY_IMPROVEMENT_MATERIAL):
                material_quantity *= QUALITY_IMPROVEMENT_MATERIAL

            material_artifact = {
                'name': material_name,
                'quantity': material_quantity,
                'level': material_level,
                'cost': material_cost
            }

            artifact.get('materials').append(material_artifact)

            material_level+=1

        material_level = 2

    return artifact