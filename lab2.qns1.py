num_years = int(input("Enter the number of years: "))

for year in range(1, num_years+1):
    total_rainfall = 0
    print("For year {}:".format(year))
    for month in range(1, 13):
        rainfall = float(input("Enter the rainfall amount for the month-{}: ".format(month)))
        total_rainfall += rainfall
    
    avg_monthly_rainfall = total_rainfall / 12
    print("For 12 months")
    print("Total rainfall:  {} inches".format(total_rainfall))
    print("Average monthly rainfall:  {}  inches".format(avg_monthly_rainfall))
