#inputs = input("Enter your numbers : ").split()

# def is_numeric(x):
#     try:
#         float(x)
#         return True
#     except:
#         return False
    
# numeric_string = list(filter(is_numeric, inputs))


# if numeric_string:
#     numbers = map(float, numeric_string)
#     print("numeric_string : ", numeric_string)
# else:
#     print("No numeric values")


letters = ["a","b","c"]
print(letters[2:].index("c"))

s = [1,"d",3]
a , b , *c= s
print(a,b,c)