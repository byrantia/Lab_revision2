def calculate_bmi(height,weight):
    print("height = " + str(height))
    print("weight = "+ str(weight))
    bmi = weight / (height ** 2)
    #return round(bmi,1)
    if bmi<18.5:
        print( "under weight")
        return -1
    elif bmi>=18.5 and bmi<= 25.0:
        print( "normal weight")
        return 0
    else:
        print( "pver weight")
        return 1

def main():
    bmi= calculate_bmi(weight=590,height=1.76)
    print(bmi)

if __name__ == "__main__":
    main()