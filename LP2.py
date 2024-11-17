def display_main_menu():
    print("display_main_menu")


def get_user_input():
    print("Input the recorded Temperatures :")
    user_input=input()
    z=user_input.split(",")
    z=[float(list) for list in z]
    return z 

def calc_average_temperature(List):
    
    total=sum(List)
    length=len(List)
    average=total/length
    print("The average temperature: "+ str(round(average,2)))

def calc_min_max_temperature(List):
    max_value=max(List)
    min_value=min(List)

    print("Minimum and Maximum Temperature: "+str([min_value, max_value]))

def median_temperature(temp_list):
    # Use a different name for the sorted list
    sorted_list = sorted(temp_list)
    length = len(sorted_list)

    if length % 2 == 1:
        # If odd, pick the middle element
        median_value = sorted_list[length // 2]
    else:
        # If even, take the average of the two middle elements
        median_value = (sorted_list[length // 2 - 1] + sorted_list[length // 2]) / 2

    print(f"The Median temperature is: {median_value:.2f}")
    


def main():
    display_main_menu()
    List=get_user_input()
    calc_average_temperature(List)
    calc_min_max_temperature(List)
    median_temperature(List)
    
    

if __name__=="__main__":
    main()