from datetime import datetime
from dateutil.relativedelta import relativedelta

def meses_completos(desde):
    hoy = datetime.now()
    delta = relativedelta(hoy, desde)
    meses = delta.years * 12 + delta.months
    return meses
    
inicio = datetime(2017, 12, 3)
meses = meses_completos(inicio)
print(meses) # imprimirá el número de meses completos transcurridos desde el 1 de enero de 2022 hasta hoy