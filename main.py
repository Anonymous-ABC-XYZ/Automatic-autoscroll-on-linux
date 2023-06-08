import os
import re

final_numbers = []
all_ids = os.popen('xinput| grep -i Mouse').read()

id_number = all_ids.split()

correct_id_number = []

for n in id_number:
    if "id" in n:
        correct_id_number.append(n)
for n in correct_id_number:
    final_numbers += re.findall(r'\d+', n)

for n in final_numbers:
    os.popen(f'xinput set-prop {int(n)} "libinput Scroll Method Enabled" 0, 0, 1')
    os.popen(f'xinput set-prop {int(n)} "libinput Button Scrolling Button" 2')
