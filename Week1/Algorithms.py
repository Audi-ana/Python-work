def remove(name):
    unique_list = []
    for x in name:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

         
#print(remove(["Jerry", "John", "Abby", "Jerry", "Steven"]))



def largest(num):
    max = num[-1]
    for x in num:
        if x > max:
            max = x
        return max

#print(largest([45, 65, 44, 100, 250]))

def smallest(num):
    least = num[-1]
    for i in num:
        if i < least:
            least = i
    return least

#print(smallest([50, 6, -1, 100]))


numbers = [0,1,2,3,5,6,7,8,9]
missing_num = ""

def missing(num):
    for x in range(10):
        if num[x] != num[x] +1:
            missing_num = num[x]
            return missing_num 

print(missing(numbers))


user = [1,2,3,4,5]

def repeat(numbers):
    dup = [1,2,3,4,5]
    for i in range(0, len(user)):
        print(user + dup)
        break
        
#print(repeat(user))

#def pyr(star):
    #for index in range(0, 17, 2)


    
    


