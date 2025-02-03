def sale(gross_sales):
    netsales = gross_sales + 0.1*gross_sales
    print("The net sale is :", netsales)
gross_sales = int(input("Enter the gross sales"))
sale(gross_sales)