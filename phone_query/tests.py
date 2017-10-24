from django.test import TestCase

# Create your tests here.


a = "这是中guo"

# a = [1,2,3,4]
# b = [2,3,5,6]
# # c = a.extend(b)
# c = 0
# def d(x):
#     global c
#     if (a+b).index(x) == 0:
#         return x
#     c = c+1
#     return x not in (a+b)[0:c]
#
#
# f = list(filter(d,a+b))
# print(f)
#
# # print({}.fromkeys(a+b,None).keys())
#
# print(a[0:1])

e = list(filter(lambda x:len(bytes(x,encoding="utf-8")) != 3,a))
print(e)