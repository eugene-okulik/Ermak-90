import os
import re, datetime


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
new_file_path = os.path.join(homework_path, 'eugene_okulik\\hw_13', 'data.txt')

with open(new_file_path, 'r') as data_file:
        for line in data_file.readlines():
            day = re.search('\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}', line)
            data = datetime.datetime.strptime(day.group(), '%Y-%m-%d %H:%M:%S.%f')
            line_num = int(line[0])
            if line_num == 1:
                print(data + datetime.timedelta(days = 7))
            if line_num == 2:
                print(data.weekday())
            if line_num == 3:
                now = datetime.datetime.now()
                print(now - data)
