#question no 26 by anusree
salary = int(input("Enter your salary"))
if salary>=5000:
    hra=salary*0.15
    da=salary*1.5
    gross_salary=hra+da+salary
    print("Gross salary",gross_salary)

else:
    hra=salary*0.10
    da=salary*1.1
    gross_salary=hra+da+salary
    print("Gross  salary",gross_salary)