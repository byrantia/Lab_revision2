def calculate_bmi(height,weight):
    print("height = " + str(height))
    print("weight = "+ str(weight))
    bmi = weight / (height ** 2)
    #return round(bmi,1)
    if bmi<18.5:
        return "under weight"
    elif bmi>=18.5 and bmi<= 25.0:
        return "Nomal weight"
    else:
        return "over weiht"

def main():
    bmi= calculate_bmi(weight=590,height=1.76)
    print(bmi)

if __name__ == "__main__":
    main()