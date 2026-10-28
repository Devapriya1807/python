n=int(input("enter the no of colours:"))
colour_list=[]
for i in range(n):
    colour=input("enter the colour:")
    colour_list.append(colour)
    print(colour_list)
    print("the first color is:",colour_list[0])
    print("the last color is:", colour_list[-1])