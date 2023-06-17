shu_values = {
    'Poblano': 1500,
    'Mirasol': 6000,
    'Serrano': 15500,
    'Cayenne': 40000,
    'Thai'   : 75000,
    'Habanero': 125000
}

n = int(input())
peppers = []
for i in range(n):
    peppers.append(input())


total_spiciness = sum(shu_values[pepper] for pepper in peppers)


print(total_spiciness)
