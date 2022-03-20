try:
    from artifact import createArtifact
    from budget import calculateBudget

    print('Albion Crafting Calculator\nDeveloped by: SamuraiPetrus\nv1.0\n\n')

    artifact = createArtifact( str(input('Qual o nome do artefato que quer produzir?:  ')) )
    budget = calculateBudget( artifact )

    print(artifact)

    print('\n\nRECEITA DO ARTEFATO:\n')

    print('Custo de produção:  ', budget.get('cost'), ' moedas')
    for material in budget.get('materials'):
        print(material, ':  ', budget.get('materials').get(material), ' unidades')

except ImportError:
    print('Erro ao tentar importar módulos necessários.')

    