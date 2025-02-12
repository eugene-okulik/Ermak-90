import datetime

current_date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(current_date, '%b %d, %Y - %H:%M:%S')
human_date = python_date.strftime('%B %d, %Y - %H:%M:%S')

print(human_date.split(' ', 1)[0])

human_date2 = python_date.strftime('%d.%m.%Y, %H:%M')
print(human_date2)
