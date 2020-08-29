
print ("Hello world")


a = 1
b = 2
c = a + b
print (c)

a = "selva"
b = "test"
c = a + b
print (c)

for i in range(10):
    print("a->",i)

print("\n")

for i in range(1,10):
    print("b->", i)

print("\n")

for i in range(1,10,2):
    print("c->", i)


def my_sum(x,y):
    return x+y

print (my_sum(1,2))
    

a = ["selvar", "parvathy" , "mukil", "akhil"]

for i in a:
    print(i)

b = ["selvar", 1 , "mukil", "akhil"]
for i in b:
    print(i)

print(b)


c = ["selvar", 1 ,[1,2,3], "mukil", "akhil"]
for i in c:
    print(i)

print(c)
c[2] = 4
print (c)

c = ("selvar", 1 ,[1,2,3], "mukil", "akhil")
print (c)
#c[2] = 4
#print (c)

thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
  print(x) 



thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


for x in thisdict:
  print(x) 

print (thisdict["brand"])


