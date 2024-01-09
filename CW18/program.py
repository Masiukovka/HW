import HR


salary_employee = HR.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = HR.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = HR.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
payroll_system = HR.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])