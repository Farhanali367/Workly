# li=[1,2,3,4]

# def my(li):
#     global li
#     li.append(7)
#     li=[8,8,8]
#     li.append(9)

# my(li)
# print(li)
# while 0 > 1: print(1)
# for i in []:
#     print('ok')
# name=b"mustved"
# with open("media/cover_image.png",'rb') as f:
#     data=f.read()
# print(data)

# print(name:=input("enter your name :"))
# l1=[23,4,32,4,353,6,5,23,41,3,4,23]

# print(sorted(l1,reverse=True))

# t1=(10,[1,2])
# t1[1].append(3)
# print(t1)
# s1={1,2,3}
# s2={3,4,5}
# print(s1 ^ s2)
# print(s1.symmetric_difference(s2))

# d1={"1":1,"2":2}
# d2={"3":3,"4":4}
# # d1.update(d2)
# print(d1)

name="mustved"

r=4
s=r-2
p=0
p1=1
for i in range(len(name)):
    print(name[p],end=" "*s)
    p+=r+s
    if p >= len(name):
        print()
        p=p1
        p1+=1
        s-=1
        r-=1
        if s<=0:
            r+=len(name)
            
            s=0
        continue