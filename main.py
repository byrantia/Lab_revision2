def main():
    print("ET0735")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    avg = cal_averge(num_list)
    print(avg)
    min_max = find_min_max(num_list)
    print(min_max)
    sort = sort_temp(num_list)
    print(sort)
    median = cal_median(num_list)
    print(median)

def display_main_menu():
    print("Enter some number seperated by commas")

def get_user_input():
    x = input()
    x = x.split(",")
    print(x)
    num_list = []
    for numebr in x:
        num_list.append(float(numebr))
    
    return num_list


def cal_averge(num_list):
    print("average:")

    total = sum(num_list)
    avg = total / len(num_list)

    return round(avg,1)

def find_min_max(num_list):
    print("find min and max")
    maximum = max (num_list)
    minimum = min(num_list)

    return [minimum,maximum]

def sort_temp(num_list):
    print("sorted")
    num_list = sorted(num_list) # small to big
    #num_list = sorted(num_list,reverse=True)#big to small
    return num_list

def cal_median(num_list):
    print("median")
    
    sort = sorted(num_list)
    if len(num_list)%2 == 0: # even
        middle_number_plus1 = len(num_list)//2
        middle = middle_number_plus1 - 1
        median = (sort[middle_number_plus1] + sort[middle])/2

        return round(median,1)
        
        
    
    else: # odd
        middle = len(sort) // 2
        return sort[middle]

if __name__ == "__main__":
    main()