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

def calculateMaterialsQuantity(artifact, materials_quantity = {}):
    '''
    calculateMaterialsQuantity

    This function will calculate the total production quantity of the artifact.
    '''

    for material in artifact.get("materials"):
        materials_quantity[material.get("name")] = material.get("quantity")

        if (material.get("materials")):
            materials_quantity.update(calculateMaterialsQuantity(material))
    
    return materials_quantity