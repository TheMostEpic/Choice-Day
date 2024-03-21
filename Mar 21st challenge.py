def reverse_string(input_string):

    char_list = list(input_string)

    char_list.reverse()

    reversed_string = ''.join(char_list)
    
    return reversed_string

input_string = input("Gimme words: ")

reversed_string = reverse_string(input_string)

print("Output:", reversed_string)




def unique_values(original_list):
    unique_list = []
    
    for item in original_list:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

original_list = []

repeat_number = input("How many numbers do you want?:")
repeat_number = int(repeat_number)
for i in range(repeat_number):
    y = input("Give a number")
    original_list.append(y)

print("This is your list:", original_list)

unique_list = unique_values(original_list)
print("Unique list:", unique_list)




def has_consecutive_repeats(lst):
    for i in range(len(lst) - 2):
        if lst[i] == lst[i + 1] == lst[i + 2]:
            return True
    return False


lst1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print("Do the following lists have an element that repeats 3 consecutive times")
print(lst1)
print(has_consecutive_repeats(lst1))  

lst2 = [1, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1]
print(lst2)
print(has_consecutive_repeats(lst2))  



def count_lines_with_text(file):
    count = 0
    with open(file, 'r') as file:
        for line in file:
            if line.strip():
                count += 1
    return count


file = r"c:\Users\iCan Student\Desktop\Ican3\Coding Stuff\Choice-Day\Testing.txt"
lines = count_lines_with_text(file)
print("Number of lines with text:", lines)
