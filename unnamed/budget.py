master_degree_description = "MBA Master in Data Science"
master_cost = 8900.00
exchange_rate = 588.12 # Considerar conectarme con algún API del banco
reservation = 900
discount_percentage = 50
# Este es el dato que tengo
payment_cuotes = [900,435,501,501,501,501,501,501,498]

def colonizar (euro_cost, exchange_rate):
    list_colonizada = []
    for i in euro_cost:
        list_colonizada.append(exchange_rate * i)
    return list_colonizada



def original_payment_cuotes (payment_cuotes, discount):
    total_payments = []
    for payment in payment_cuotes:
        payment = (payment * 100  )/ (100 - discount)
        total_payments.append(payment)

    #print(total_payments)
    return total_payments

def Costs_with_discount (total_payments):
    payments_with_discount = []
    for payment in total_payments:
        payment = payment - ((payment *  discount_percentage) / 100)
        payments_with_discount.append(payment)   
    
    return payments_with_discount


def Total_cost ():  

#    costo_colonizado_master = colonizar(master_cost, exchange_rate)
    #print (costo_colonizado_total)
    print ("COSTO DEL MASTER: " + str(master_cost) + " Euros, " + str(master_cost* exchange_rate) + " Colones. ")

    #Detalle de pagos original
    total_payment_cuotes = original_payment_cuotes(payment_cuotes, 40)
    print ("Detalle de pagos original")    
    print (original_payment_cuotes(payment_cuotes, 40))


    #calcular costo con descuento 50%      
    real_cost = Costs_with_discount(total_payment_cuotes)
    print ("Costo Real")
    print (real_cost)


    #costos en colones
    costo_real_colonizado = colonizar(real_cost,exchange_rate)
    print ("Costo Pagos en colones")
    print (costo_real_colonizado)

    total = 0

    for i in costo_real_colonizado:
        total += i

    print ("Costo Total del Master: " + str(round( sum(costo_real_colonizado),2)))


#colonizar (100, 10)
Total_cost()