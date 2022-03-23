import json

try:
    from artifact import createArtifact, saveArtifact
    from budget import calculateBudget
    from recipe import saveRecipe

    print('\n\nAlbion Crafting Calculator\n\nDeveloped by: SamuraiPetrus\n\nv1.0\n')

    try:
        artifact_json_file = open('artifact.json', 'r', encoding='utf-8')
        artifact = json.load(artifact_json_file)
    except:
        getting_artifact_from_json = False
        print('Nenhum arquivo json encontrado, criando um artefato do zero...\n')
        artifact = createArtifact( str(input('Qual o nome do artefato que quer produzir?:  ')) )
        

    budget = calculateBudget( artifact )
    recipe = saveRecipe( artifact, budget )
    saveArtifact( artifact )
    print(recipe)

except ImportError:
    print('Erro ao tentar importar módulos necessários.')

    