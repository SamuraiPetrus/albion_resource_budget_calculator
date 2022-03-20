def calculateBudget(artifact):
    '''
    calculateBudget

    After creating the artifact object, this function will read it
    and calculate the total production budget.
    '''

    return {
        "cost": calculateTotalCosts(artifact),
        "materials": calculateMaterialsQuantity(artifact)
    }

def calculateTotalCosts(artifact):
    '''
    calculateTotalCosts

    This function will calculate the total production costs of the artifact.
    '''

    total_costs = artifact.get("cost") * artifact.get("quantity")

    if (artifact.get("materials")):
        for material in artifact.get("materials"):
            total_costs += calculateTotalCosts(material)

    return total_costs

def calculateMaterialsQuantity(artifact):
    '''
    calculateMaterialsQuantity

    This function will calculate the total production quantity of the artifact.
    '''
    
    materials_quantity = {
        artifact.get('name'): artifact.get('quantity')
    }

    for material in artifact.get("materials"):
        materials_quantity[material.get("name")] = material.get("quantity")
        if (material.get("materials")):
            materials_quantity.update(calculateMaterialsQuantity(material))
    
    return materials_quantity


print('\n\n')
print(calculateBudget({'name': 'Barra de Ferro', 'quantity': 100, 'level': 4, 'cost': 10.0, 'materials': [{'name': 'Minério (Grau 4)', 'quantity': 2, 'level': 4, 'cost': 0.0, 'materials': []}, {'name': 'Barra (Grau 3)', 'quantity': 1, 'level': 3, 'cost': 5.0, 'materials': [{'name': 'Minério (Grau 3)', 'quantity': 2, 'level': 3, 'cost': 0.0, 'materials': []}, {'name': 'Barra (Grau 2)', 'quantity': 1, 'level': 2, 'cost': 0.0, 'materials': [{'name': 'Minério (Grau 2)', 'quantity': 1, 'level': 2, 'cost': 0.0, 'materials': []}]}]}]}))
print('\n\n')