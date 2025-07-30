print("DIVAGAR INTERNATION[p]LTD")
print("no,15,nagapur dist bangalore")
print("---------------------------")
print("employee payroll system")
print("-----------------------")
id=int(input("enter the employee:"))
name=input("enter the employee name:")
salary=int(input("enter the salary:"))
print("income")
bonus=salary*20/100
print("bonus(20 percentage):",bonus)
ot=salary*10/100
print("overtime (10 percentage):",ot)
ta=salary*5/100
print("travelallowance(5 percentage):",ta)
Gross=bonus+ot+ta+salary
print("Gross pay in rupees:",Gross)
