from tkinter import Tk, Text, END, Button
from tkcalendar import Calendar
import datetime

root = Tk()
root.geometry("1000x630")
root.title("My Diary")

aaj = datetime.datetime.now()
y, m, d = aaj.year, aaj.month, aaj.day
cal = Calendar(root, selectmode="day", year=y, month=m, day=d)
cal.place(x=10, y=10, width=980, height=280)
enter = Text(root)
enter.place(x=10, y=330, width=980, height=290)

def randomise(message: str):
    sentence = message
    ascii_values = [ord(char) for char in sentence]
    ans = ""
    for i in ascii_values:
        ans += str(i) + " "
    return ans
    
def derandomise():
    file = open("D:\\Programs-Python\\Advanced\\diary app\\dbdiary.txt", "r")
    contents = file.read()
    ascii_values = (contents.strip("[]")).split(" ")
    ans = ""
    if ascii_values != [""]:
        for value in ascii_values:
            if value != "":
                ans += chr(int(value))
        return ans
    else:
        return ""

def reader():
    contents = derandomise()
    d = cal.get_date()
    enter.delete("1.0", END)
    if d in contents:
        ans = contents[
            contents.index(d)
            + len(str(d))
            + 8 : contents.index("#end", contents.index(d) + 1)
        ]
        enter.insert("1.0", ans.strip())
    else:
        enter.insert("1.0", "Not Found!")

def writer():
    d = str(cal.get_date())
    y = str(enter.get("1.0", "end-1c"))
    l_old = derandomise()
    finalised_product = ""
    if d in l_old:
        finalised_product = l_old[:l_old.index(d) + 15] + y + l_old[l_old.index("#end") - 1:]
    else:
        date = "#date=[" + cal.get_date() + "]\n"
        entered = str(enter.get("1.0", "end-1c"))
        ans = date + "#text=" + entered + "\n#end\n"
        finalised_product = l_old + ans
    with open("D:\\Programs-Python\\Advanced\\diary app\\dbdiary.txt", "w") as f:
        f.writelines(randomise(finalised_product))

read = Button(root, text="Read Entry", command=reader)
read.place(x=10, y=300, width=100, height=20)
write = Button(root, text="Write Entry", command=writer)
write.place(x=120, y=300, width=100, height=20)

root.mainloop()
