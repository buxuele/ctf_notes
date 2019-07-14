from datetime import datetime, date, timedelta


print(datetime.today())		# 2019-03-04 18:40:36.196136
print(date.today())			# 2019-03-04

print(date.today().month)	# 3
print(date.today().year)	# 2019
print(date.today().day)		# 4

t = timedelta(days=4, hours=10)
print(t.days)	# 4
print(t.seconds)	# 36000
# print(t.hours)	#  object has no attribute 'hours'

new_date = datetime.today() + timedelta(hours=24)
print(new_date)		# 2019-03-05 18:47:37.358280