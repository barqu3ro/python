# Create a list of 4 float numbers, compute the average and print it
def average():
    my_list = [2.3, 4.5, 6.4, 8.0]
    t = sum(my_list)
    l = len(my_list)
    average = t/l    
    print("The average is {0}".format(average))


average()
