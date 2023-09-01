import math


# Riesgo 1 : Johnny 
voted_risk = {    
    "NombreVotante": "Johnny ",
    "Riesgo": 
    {
        "Proceso Nivel 1": "BAI11 Gestionar los proyectos",
        "Proceso nivel 2": "BAI11.01 Mantener un enfoque estándar en la gestión de proyectos.",
        "Categoría":"Riesgo Operativo",
        "Riesgo":"Proyecto iniciado con documentación insuficiente",
        "FactorRiesgo": "Proyecto iniciado sin el acta de constitución",
        "Impacto": 5,
        "Probabilidad": 1
    }
}

# Riesgo 2 : Jorge 
voted_risk = {    
    "NombreVotante": "Jorge",
    "Riesgo": 
    {
        "Proceso Nivel 1": "BAI11 Gestionar los proyectos",
        "Proceso nivel 2": "BAI11.01 Mantener un enfoque estándar en la gestión de proyectos.",
        "Categoría":"Riesgo Operativo",
        "Riesgo":"Proyecto iniciado con documentación insuficiente",
        "FactorRiesgo": "Proyecto iniciado sin el acta de constitución",
        "Impacto": 2,
        "Probabilidad": 3
    }
}


# Recibe una lista de riesgos y retorna el valor
def calculate_risk_value (risks):    
    voters = 0
    total_values = 0
    for risk in risks:
        if risk > 0 and risk <=5:
            risk_value = risk["Riesgo"]["Impacto"] * risk["Riesgo"]["Probabilidad"]
            print (risk_value)
            total_values += risk_value
            voters += 1
        else:
            print ("Número en rango no válido. Valor recibido = ",str(risk))
            

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
