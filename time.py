import time;

ticks = time.time()
print("Berjalan sejak 12:00am, January 1, 1970:", ticks)


localtime = time.localtime(time.time())
print("method localtime", localtime)
print("Example : localtime.tm_year.  #remember its almost looks like object in javascript")
print("Waktu Sekarang :", localtime.tm_year, localtime.tm_mday,localtime.tm_mon)



import calendar;

cal = calendar.month(2008, 1)
print("Above this line is a calendar in python.  #wait what ?. just like that?")
print(cal)


print("\n\nFor more method see the documentation or tuorial out there. belajarpython.com/tutorial/tanggal-waktu-python")