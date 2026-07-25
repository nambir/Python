import sys






def Add(x, y):
    print(f"Answer is={x + y}")
    print(name)
    print(Active)

name = "John"
age = 20
city = "New York"
height = 1.75
Active=False
print(f"Name is {name}, age is {age}, city is {city}")


Salary=[1000,2000,3000,4000,5000]
Company={"Google","Apple","Microsoft","Amazon","Tesla"}
company2=["Google2","Apple2","Microsoft2","Amazon2","Tesla2"]
print(Company)
print(company2)
print(Salary)

my_tuple = (name, age)
list2=[1,2]
print(list2)
dict1={}
dict1["name"]=name
a_list = [1, 2, 3]
a_tuple = (1, 2, 3)
print("list bytes :", sys.getsizeof(a_list))
print("tuple bytes:", sys.getsizeof(a_tuple))  # usually smaller
#print(my_tuple)
# if __name__ == "__main__":
#     print("inside main function")
#     Add(1, 2)

sq=[n+10 for n in range(1,2)]
print(sq)

set1={n%2 for n in range(1,10)}
print(set1)

items = [
    {"name": "pen",  "amount": 30},
    {"name": "book", "amount": 10},
    {"name": "bag",  "amount": 50},
]
Sorteditems=sorted(items, key=lambda r: r["amount"])
print(Sorteditems)