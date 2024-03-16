               #  LAB 01
# 1
# def fill_incresed(length, start):
#     my_list = range([start,length])
#     print(my_list)
# fill_incresed(4,2)

# 2
# def fill_list(length,start):
#     print(list(range(start,length)))

# fill_list(9,1)

# # 3
# my_list = []
# for i in range(0,5):
#     x = int(input("the element is : "))
#     my_list.append(x)
# print(my_list.sort())
# # print(my_list.sort(reverse=True))

# 4

# def dev_by_three(x):
#     if x%3 == 0 and x%5 == 0 :
#         print("FizzBuzz")
#     elif x%5 == 0:
#         print("Buzz")
#     elif x%3 == 0:
#         print("Fizz")
# dev_by_three(13)

# 5
# def reverse_str(my_str):
#     my_string = ""
#     for i in my_str:
#         my_string = i + my_string
#     return my_string

# my_in = input("Type your string: ")
# print (f"the Reversed string is : " , reverse_str(my_in))


# # 6
# PI = 3.14
# def find_area(r):
#     return  PI * r * r
# def find_cir(r):
#     return 2 * PI * r

# my_in2 = float(input("Enter your radius to calc the area and the circ of circle:  " ))
# print(f"the area of circle is : ",find_area(my_in2))
# print(f"the Circ of circle is : ",find_cir(my_in2))

# 7
my_inp = input("Enter your Name: ")
if my_inp == "" or my_inp == " ":
    print("This is A not valid Name Empty string.")
else:
    print(f"Your Name is: ", my_inp)

my_inp2 = input("Enter your Email: ")
is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|org)", my_inp2)
if is_email:
    print("This is A valid Email.")
else:
    print("This is A not valid Email.")