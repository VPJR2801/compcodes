def net_salary(a):
    allowance = 0.1 * a
    deduction = 0.03 * a
    netsalary = a + allowance - deduction
    print("Your net salary is:", netsalary)
a = int(input("Enter your salary:"))
net_salary(a)