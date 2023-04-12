start_org = int(input("Starting number of organisms:"))
avrg_daily = int(input(" Average daily percentage increase:"))
number_days = int(
    input("Enter the number of days to display the final data: "))


def calculation(start_org, avrg_daily, number_days,):
   
    print("Day approximate \t\tPopulation")
    print("-------------------------------------")
    if start_org and avrg_daily and number_days > 0:
        population = start_org
        for number_days in range(1, number_days+1):
            print(number_days, "\t\t", population)
            population += population*(avrg_daily/100)
           
            

    else:
        print(" Enter the values again")


calculation(start_org, avrg_daily, number_days,)
