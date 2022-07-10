from datetime import date
today = date.today()

list_of_number = [2, 5, 6, 3, 4, 9, 2]
new_list = []
for number in list_of_number:
    inc_number = number + 1
    if inc_number < 6:
        new_list.append(number)
print(new_list)

sample_dict = dict()


