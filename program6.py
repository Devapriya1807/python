li1=[1,2,3,4,5]
li2=[2,4,6,8]
print("elements in list one is",li1)
print("elements in list two is:",li2)
if len(li1)==len(li2):
    print("list have same length")
else:
    print("list have diffrent length")
s1=0
s2=0
for i in range(len(li1)):
    s1=s1+li1[i]
print("the sum of list is:",s1)
for i in range(len(li2)):
    s2=s2+li2[i]
print("the sum of list is:",s2)
if s1==s2:
    print("the sum of list are same")
else:
    print("the sum of list are different")
print("the common element in list is:")
for i in li1:
    for j in li2:
        if i==j:
            print(i)


