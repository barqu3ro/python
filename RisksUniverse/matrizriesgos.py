import math

# Riesgo 1 : Jorge 
voted_risk = {
    "Nombre": "Jorge",
    "Riesgo": {
        "ID": 1,
        "Riesgo": 1,
        "Entidad": "BAI11 Gestionar los proyectos",
        "Proceso": "BAI11.09 Cerrar un proyecto o iteración",
        "FactorRiesgo": "",
        "Impacto": 5,
        "Probabilidad": 1
    }
}

# Riesgo 2 : Joma 
voted_risk_2 = {
    "Nombre": "Joma",
    "Riesgo":
        {
            "ID": 1,
            "Riesgo": 1,
            "Entidad": "BAI11 Gestionar los proyectos",
            "Proceso": "BAI11.09 Cerrar un proyecto o iteración",
            "FactorRiesgo": "",
            "Impacto": 2,
            "Probabilidad": 5
        }
}

# Riesgo 3 : Jose
voted_risk_3 = {
    "Nombre": "Jose",
    "Riesgo":
        {
            "ID": 1,
            "Riesgo": 1,
            "Entidad": "BAI11 Gestionar los proyectos",
            "Proceso": "BAI11.09 Cerrar un proyecto o iteración",
            "FactorRiesgo": "",
            "Impacto": 3,
            "Probabilidad": 5
        }
}

# Recibe una lista de riesgos y retorna el valor
def calculate_risk_value (risks):    
    voters = 0
    total_values = 0
    for risk in risks:
        risk_value = risk["Riesgo"]["Impacto"] * risk["Riesgo"]["Probabilidad"]
        print (risk_value)
        total_values += risk_value
        voters += 1

    # Promedio de valores
    print ( total_values / voters)

    # return redondeado al entero próximo
    return math.ceil( total_values / voters)

# Con base en el valor obtenido se mapea el tipo de riesgo
def define_risk_type(value):
    if value == 1:
        return "Muy bajo"
    elif value > 1 and value < 5: 
        return "Bajo"
    elif value >= 5 and value < 9:
        return "Moderado"
    elif value >= 9 and value < 13:
        return "Alto"
    elif value >= 13:
        return "Extremo"

risks = []
risks.append (voted_risk)
risks.append (voted_risk_2)
risks.append (voted_risk_3)
print ("Tipo de riesgo: " +  str(define_risk_type(calculate_risk_value(risks))))
