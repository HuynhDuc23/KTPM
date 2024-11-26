date_of_birth = input("please enter your birth date? ") # input data -> string
result = 2025 - int(date_of_birth) 
print(str(result) + " result") # convert to str

content =  "Begin for course"
result =  content.upper()
result2 =  content.replace("o","2") # replace all 
print(result2)
result3 =  ("python" in content) # true or fasle
print(result3)

# logic 10 / 3 -> 3.3333
# 10//3 -> 3
# 10%3->1
# 10 ** 3 -> 1000
# and , or
# not : đảo ngược true -> false , false -> true
temperature = 30 
if( temperature> 27):
  print("hot")
elif( temperature< 10):
  print("cold")
else:
  print("normal")
# chúng ta có thể nhận 1 số với 1 chuỗi

i  = 0 
while(i < 0):
  print(i)
  i += 1

names = ["Join","Age","Zed","VN"]
names[0] = "Joi" ,
print(names[0:3]) # "Join->Zed"
print(names[-1]) # "VN" 
# list -> len()
# range(5) : 0,1,2,3,4
# range(5,9):5,6,7,8,9
# range(5,9,2):5,7,9
# tuple in python : là một bộ chúng ta chỉ có quyền đếm ... không được xoá hay insert gì cả
