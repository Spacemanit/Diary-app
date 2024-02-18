"""
Author: Manit Bisht
Github: https://github.com/Spacemanit1709
"""

from tkinter import Tk, Text, END, Button
from tkcalendar import Calendar
import datetime

root = Tk()
root.geometry("1000x630")
root.title("My Diary")

aaj = datetime.datetime.now()
y, m, d = aaj.year, aaj.month, aaj.day
cal = Calendar(root, selectmode = 'day', year = y, month = m, day = d)
cal.place(x=10, y=10, width=980, height=280) 
enter = Text(root)
enter.place(x=10, y=330, width=980, height=290)


def reader():	
	file = open(r"dbdiary.txt", "r")
	contents = str(file.read())
	d = cal.get_date()
	enter.delete("1.0", END)
	if d in contents:
		ans = contents[contents.index(d)+len(str(d))+8:contents.index("#end", contents.index(d) + 1)]
		enter.insert("1.0", ans.strip())
	else:
		enter.insert("1.0", "Not Found!")

def writer():
	d = str(cal.get_date())
	y = str(enter.get("1.0", "end-1c") + '\n')
	file = open(r"dbdiary.txt", "r+")
	l = file.readlines()
	c = 0
	boo = True
	for m in range(len(l)):
		if d in l[m]:
			l[m+1] = l[m+1][:6] + y
			boo = False
		c += 1
	if boo:
		date = "#date=[" + cal.get_date() + "]\n"
		entered = str(enter.get("1.0", "end-1c"))
		ans = [date, "#text=", entered, "\n#end\n"]
		file.writelines(ans)
	else:	
		with open('dbdiary.txt', 'w') as f:
			for line in l:
				f.write(line)
	file.close()

read = Button(root, text = "Read Entry", command = reader)
read.place(x=10, y=300, width=100, height=20) 
write = Button(root, text = "Write Entry", command = writer)
write.place(x=120, y=300, width=100, height=20) 

root.mainloop()
