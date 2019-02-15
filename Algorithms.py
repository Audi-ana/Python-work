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




def missing(num_list):
    original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
    num_list = set(num_list)
    return (list(num_list ^ set(original_list)))

print(missing([0,1,2,4,8,9]))







    

