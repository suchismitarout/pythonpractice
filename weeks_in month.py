import datetime
from datetime import date
from datetime import timedelta, datetime
#
# # d1 = date(2021,3,1)
# # d2 = date(2021,3,31)
# #
# # weekly = d1
# #
# # while weekly <= d2:
# #     print(weekly)
# #     weekly = weekly + datetime.timedelta(days=7)
#
#
#
# d1 = datetime.strptime('2021-03-01', "%Y-%m-%d")
# d2 = datetime.strptime('2021-03-31', "%Y-%m-%d")
#
# weekly = d1
# date_list = []
# while weekly <= d2:
#     date_list.append(str(weekly.date()))
#     weekly = weekly + timedelta(days=7)
# print(date_list)
#
# def week_magic(day):
#     day = datetime.strptime(day, "%Y-%m-%d")
#     day_of_week = day.weekday()
#
#     to_beginning_of_week = timedelta(days=day_of_week)
#     beginning_of_week = day - to_beginning_of_week
#
#     to_end_of_week = timedelta(days=6 - day_of_week)
#     end_of_week = day + to_end_of_week
#
#     return (str(beginning_of_week), str(end_of_week))
#
# print(week_magic('2021-03-05'))
#


start_date = '21-03-01'
r = datetime.strptime(start_date, '%y-%m-%d').strftime('%Y-%m-%d')
r = datetime.strptime(r, '%Y-%m-%d') + timedelta(days=1)
print(r.strftime('%Y-%m-%d'))