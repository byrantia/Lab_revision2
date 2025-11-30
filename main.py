def main():
    print("ET0735")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    avg = cal_averge(num_list)
    print(avg)
    min_max = find_min_max(num_list)
    print(min_max)

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

    return avg

def find_min_max(num_list):
    print("find min and max")
    maximum = max (num_list)
    minimum = min(num_list)

    return [minimum,maximum]


if __name__ == "__main__":
    main()