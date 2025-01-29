import csv

f = open("sells.csv", 'r')
reader = csv.reader(f)

data = []
for row in reader:
    data.append(row)

f.close()




# data is ready
mx = 0
best_customer = []

for row in data[1:]:
    name, price, age = row
    if int(price) > mx:
        mx = int(price)
        best_customer = row

#print(mx)
#print(best_customer)

#rows = list(map(lambda row: row[1], data))[1:]
#print(max(rows))

# rows = list(map(lambda row: [row[0], int(row[1]), row[2]], data[1:]))
rows = list(
    map(lambda row: [row[0], int(row[1]), row[2]], data[1:])
)
result = max(data[1:], key=lambda row: row[1])
print(result)

# convert to int

# numbers = ['1200', '3300', '4800', '8900', '7900', '800', '600']
# res = list(map(int, numbers))
# print(res)


with open("sells.csv", 'r') as f:
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row)

print(data)

phones = ['12341234', '143134', '12341234']

people = [
    {'name': 'john', 'age': 12},
    { 'name': 'bob', 'age': 15 },
    {'name': 'kate','age': 19}
]