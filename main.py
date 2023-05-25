import os

final_numbers = []
all_ids = os.popen('xinput| grep -i Mouse').read()

id_number = all_ids.split()
print(id_number)

correct_id_number = []

for n in id_number:
    if "id" in n:
        correct_id_number.append(n)


final_numbers.append(int(correct_id_number[0][3]))
final_numbers.append(int(correct_id_number[1][3]))

os.popen(f'xinput set-prop {final_numbers[0]} "libinput Scroll Method Enabled" 0, 0, 1')
os.popen(f'xinput set-prop {final_numbers[0]} "libinput Button Scrolling Button" 2')
os.popen(f'xinput set-prop {final_numbers[1]} "libinput Scroll Method Enabled" 0, 0, 1')
os.popen(f'xinput set-prop {final_numbers[1]} "libinput Button Scrolling Button" 2')
