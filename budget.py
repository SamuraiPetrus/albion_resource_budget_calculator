def calculateBudget(artifact):
    return {
        "cost": calculateTotalCosts(artifact),
        "materials": calculateMaterialsQuantity(artifact)
    }

def calculateTotalCosts(artifact):
    total_costs = artifact.get("cost") * artifact.get("quantity")

    for material in artifact.get("materials"):
        total_costs += material.get("cost") * material.get("quantity")

    return total_costs

def calculateMaterialsQuantity(artifact):
    materials_quantity = {}

    for material in artifact.get("materials"):
        materials_quantity[material.get("name")] = material.get("quantity") * artifact.get("quantity")
    
    return materials_quantity


