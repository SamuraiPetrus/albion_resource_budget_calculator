try:
    from register_material import registerMaterialsToArtifact
    from budget import calculateBudget

    print('Albion Crafting Calculator\nDeveloped by: SamuraiPetrus\nv1.0\n\n')

    artifact = {
        'quantity': int(input('Quantos artefatos você quer fabricar?:  ')),
        'level': int(input('Qual o grau do seu artefato?:  ')),
        'cost': float(input('Qual o custo em moedas para produzí-lo?:  ')),
        'materials': []
    }

    materials = str(input('Quais os materiais necessários para produzí-lo? (Separe por vírgulas):  '))
    materials = materials.replace(', ', ',')
    materials = materials.split(',')

    artifact = registerMaterialsToArtifact(materials, artifact)
    budget = calculateBudget(artifact)

    print('\n\nRECEITA DO ARTEFATO:\n')

    print('Custo de produção:  ', budget.get('cost'), ' moedas')
    for material in budget.get('materials'):
        print(material, ':  ', budget.get('materials').get(material), ' unidades')

except ImportError:
    print('Erro ao tentar importar módulos necessários.')

    