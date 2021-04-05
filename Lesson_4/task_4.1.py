from sys import argv

_, sap_h, cost_h, prize = argv

# salary_c =
sap_h = int(sap_h)
cost_h = int(cost_h)
prize = int(prize)
salary = sap_h * cost_h + prize

print(f'SLA {salary}')
