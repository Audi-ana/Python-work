total = float(input (f"Total amount?"))
percent = float(input(f"What percent do you want to give?"))

def Divide(total, percent):
    percent = percent/100
    return (total*percent)
    

Total = Divide(total, percent)

print(Total)