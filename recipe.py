def saveRecipe( artifact, budget ):
    recipe = '''
    \n\nRECEITA PARA PRODUZIR {} UNIDADES DE {}:\n\nCusto de produção: {} moedas
    '''.format(
        str(artifact.get('quantity')),
        artifact.get('name'),
        budget.get('cost')
    )

    for material in budget.get('materials'):
        recipe += '\n'+material+':  '+str(budget.get('materials').get(material))+' unidades'

    recipe_file = open('recipes/'+artifact.get('name')+'.txt', 'w+', encoding='utf-8')
    recipe_file.write(recipe)
    recipe_file.close()

    return recipe