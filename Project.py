from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import bs4
import matplotlib.pyplot as plt

def f1():
	add_window.deiconify()
	main_window.withdraw()

def f2():
	view_window.deiconify()
	main_window.withdraw()
	view_window_st_data.delete(1.0, END)
	info = ''
	con = None
	try:
		con = connect("student.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		heading = "Roll no." + "\t" + "Name" + "\t\t" + "Marks" + "\n"
		underline = "--------------------------------------------------\n"
		view_window_st_data.insert(INSERT, heading)
		view_window_st_data.insert(INSERT, underline)
		for d in data:
			info = info + str(d[0]) + "\t" + str(d[1]) + "\t\t" + str(d[2]) + "\n"
		view_window_st_data.insert(INSERT, info)
	except Exception as e:
		showerror('Failure', e)
	finally:
		if con is not None:
			con.close()	

def f3():
	update_window.deiconify()
	main_window.withdraw()

def f4():
	delete_window.deiconify()
	main_window.withdraw()

def f5():
	info = ''
	con = None
	try:
		con = connect("student.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			name = d[1]
			marks = d[2]
			plt.bar(name, marks, linewidth = 4)
		plt.ylabel("Marks")
		plt.title("Batch Information!")
		plt.show()
	except Exception as e:
		showerror('Failure', e)
	finally:
		if con is not None:
			con.close()
		f13()

def f6():
	con = None
	try:
		con = connect("student.db")
		cursor = con.cursor()
		sql = "insert into student values('%d', '%s', '%d')"
		rno = int(add_window_ent_rno.get())
		if rno <= 0:
			raise Exception("Invalid roll number")
		name = add_window_ent_name.get()
		if (len(name) < 2) or (not name.isalpha()):
			raise Exception("Invalid name")
		marks = int(add_window_ent_marks.get())
		if (marks < 0) or (marks > 100):
			raise Exception("Invalid marks")
		cursor.execute(sql % (rno, name, marks))
		con.commit()
		showinfo('Success', 'Record added')
	except ValueError:
		showerror('Failure', "ValueError:\nYou need to enter correct values in each field")
	except Exception as e:
		showerror('Failure', e)
	finally:
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0,END)
		add_window_ent_marks.delete(0,END)
		if con is not None:
			con.close()

def f7():
	main_window.deiconify()
	add_window.withdraw()
	add_window_ent_rno.delete(0, END)
	add_window_ent_name.delete(0,END)
	add_window_ent_marks.delete(0,END)

def f8():
	main_window.deiconify()
	view_window.withdraw()

def f9():
	con = None
	try:
		con = connect("student.db")
		cursor = con.cursor()
		sql = "update student set name = '%s', marks = '%d' where rno = '%d'"
		rno = int(update_window_ent_rno.get())
		if rno <= 0:
			raise Exception("Invalid roll number")
		name = update_window_ent_name.get()
		if (len(name) < 2) or (not name.isalpha()):
			raise Exception("Invalid name")
		marks = int(update_window_ent_marks.get())
		if (marks < 0) or (marks > 100):
			raise Exception("Invalid marks")
		cursor.execute(sql % (name, marks, rno))
		if cursor.rowcount > 0:
			con.commit()
			showinfo('Success', 'Record updated')
		else:
			showerror('Failure', 'Record does not exist')
	except ValueError:
		showerror('Failure', "ValueError:\nYou need to enter correct values in each field")
	except Exception as e:
		showerror('Failure', e)
	finally:
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0,END)
		update_window_ent_marks.delete(0,END)
		if con is not None:
			con.close()

def f10():
	main_window.deiconify()
	update_window.withdraw()
	update_window_ent_rno.delete(0, END)
	update_window_ent_name.delete(0,END)
	update_window_ent_marks.delete(0,END)

def f11():
	con = None
	try:
		con = connect("student.db")
		cursor = con.cursor()
		sql = "delete from student where rno = '%d'"
		rno = int(delete_window_ent_rno.get())
		if rno <= 0:
			raise Exception("Invalid roll number")
		cursor.execute(sql % (rno))
		if cursor.rowcount > 0:
			con.commit()
			showinfo('Success', 'Record deleted')
		else:
			showerror('Failure', 'Record does not exist')
	except ValueError:
		showerror('Failure', "ValueError:\nYou need to enter correct values in each field")
	except Exception as e:
		showerror('Failure', e)
	finally:
		delete_window_ent_rno.delete(0, END)
		if con is not None:
			con.close()

def f12():
	main_window.deiconify()
	delete_window.withdraw()
	delete_window_ent_rno.delete(0, END)

main_window = Tk()
main_window.title("S. M. S.")
main_window.geometry("1140x450+150+0")
main_window.configure(background = 'palegreen')

wa1 = "http://ipinfo.io/"
r1 = requests.get(wa1)
data1 = r1.json()
location = data1['loc']
city_name = data1['city']
a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
a2 = "&q=" + city_name
a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
wa2 = a1 + a2 + a3
r2 = requests.get(wa2)
data2 = r2.json()
main = data2['main']
temperature = main['temp']
loctemp = "Location: " + location + "\t\t\t\t\t\t            Temperature: " + str(temperature)
wa3 = "https://www.brainyquote.com/quote_of_the_day"
r3 = requests.get(wa3)
data3 = bs4.BeautifulSoup(r3.text, 'html.parser')
info = data3.find('img', {'class':'p-qotd'})
msg = info['alt']
quote = "QOTD: " + msg

main_window_btn_add = Button(main_window, text = "Add", font = ('Arial', 15, 'bold'), width = 15, command = f1)
main_window_btn_view = Button(main_window, text = "View", font = ('Arial', 15, 'bold'), width = 15, command = f2)
main_window_btn_update = Button(main_window, text = "Update", font = ('Arial', 15, 'bold'), width = 15, command = f3)
main_window_btn_delete = Button(main_window, text = "Delete", font = ('Arial', 15, 'bold'), width = 15, command = f4)
main_window_btn_charts = Button(main_window, text = "Charts", font = ('Arial', 15, 'bold'), width = 15, command = f5)
main_window_lbl_qotd = Label(main_window, text = quote, font = ('Arial', 15, 'bold'), background = 'palegreen')
main_window_btn_location_temp = Button(main_window, text = loctemp, font = ('Arial', 17, 'bold'), background = 'palegreen')
main_window_btn_qotd = Button(main_window, text = quote, font = ('Arial', 15, 'bold'), background = 'palegreen')

main_window_btn_add.pack(pady = 10)
main_window_btn_view.pack(pady = 10)
main_window_btn_update.pack(pady = 10)
main_window_btn_delete.pack(pady = 10)
main_window_btn_charts.pack(pady = 10)
main_window_btn_location_temp.pack(pady = 10)
main_window_btn_qotd.pack(pady = 10)

add_window = Toplevel(main_window)
add_window.title("Add St.")
add_window.geometry("500x550+400+50")
add_window.configure(background = 'LightSteelBlue')

add_window_lbl_rno = Label(add_window, text = "Enter rno:", font = ('Arial', 20, 'bold'), background = 'LightSteelBlue')
add_window_ent_rno = Entry(add_window, bd = 5, font = ('Arial', 20, 'bold'))
add_window_lbl_name = Label(add_window, text = "Enter name:", font = ('Arial', 20, 'bold'), background = 'LightSteelBlue')
add_window_ent_name = Entry(add_window, bd = 5, font = ('Arial', 20, 'bold'))
add_window_lbl_marks = Label(add_window, text = "Enter marks:", font = ('Arial', 20, 'bold'), background = 'LightSteelBlue')
add_window_ent_marks = Entry(add_window, bd = 5, font = ('Arial', 20, 'bold'))
add_window_btn_save = Button(add_window, text = "Save", font = ('Arial', 20, 'bold'), width = 10, command = f6)
add_window_btn_back = Button(add_window, text = "Back", font = ('Arial', 20, 'bold'), width = 10, command = f7)

add_window_ent_rno.focus()

add_window_lbl_rno.pack(pady = 10)
add_window_ent_rno.pack(pady = 10)
add_window_lbl_name.pack(pady = 10)
add_window_ent_name.pack(pady = 10)
add_window_lbl_marks.pack(pady = 10)
add_window_ent_marks.pack(pady = 10)
add_window_btn_save.pack(pady = 10)
add_window_btn_back.pack(pady = 10)
add_window.withdraw()

view_window = Toplevel(main_window)
view_window.title("View St.")
view_window.geometry("500x500+400+100")
view_window.configure(background = 'LemonChiffon')


view_window_st_data = ScrolledText(view_window, width = 30, height = 10, font = ('Arial', 20, 'bold'), background = 'LemonChiffon')
view_window_btn_back = Button(view_window, text = "Back", font = ('Arial', 20, 'bold'), command = f8)
view_window_st_data.pack(pady = 10)
view_window_btn_back.pack(pady = 10)
view_window.withdraw()

update_window = Toplevel(main_window)
update_window.title("Update St.")
update_window.geometry("500x550+400+50")
update_window.configure(background = 'PeachPuff')

update_window_lbl_rno = Label(update_window, text = "Enter rno", font = ('Arial', 20, 'bold'), background = 'PeachPuff')
update_window_ent_rno = Entry(update_window, bd = 5, font = ('Arial', 20, 'bold'))
update_window_lbl_name = Label(update_window, text = "Enter name", font = ('Arial', 20, 'bold'), background = 'PeachPuff')
update_window_ent_name = Entry(update_window, bd = 5, font = ('Arial', 20, 'bold'))
update_window_lbl_marks = Label(update_window, text = "Enter marks", font = ('Arial', 20, 'bold'), background = 'PeachPuff')
update_window_ent_marks = Entry(update_window, bd = 5, font = ('Arial', 20, 'bold'))
update_window_btn_save = Button(update_window, text = "Save", font = ('Arial', 20, 'bold'), width = 10, command = f9)
update_window_btn_back = Button(update_window, text = "Back", font = ('Arial', 20, 'bold'), width = 10, command = f10)

update_window_ent_rno.focus()

update_window_lbl_rno.pack(pady = 10)
update_window_ent_rno.pack(pady = 10)
update_window_lbl_name.pack(pady = 10)
update_window_ent_name.pack(pady = 10)
update_window_lbl_marks.pack(pady = 10)
update_window_ent_marks.pack(pady = 10)
update_window_btn_save.pack(pady = 10)
update_window_btn_back.pack(pady = 10)
update_window.withdraw()

delete_window = Toplevel(main_window)
delete_window.title("Delete St.")
delete_window.geometry("500x550+400+50")
delete_window.configure(background = 'LightSteelBlue')

delete_window_lbl_rno = Label(delete_window, text = "Enter rno:", font = ('Arial', 20, 'bold'), background = 'LightSteelBlue')
delete_window_ent_rno = Entry(delete_window, bd = 5, font = ('Arial', 20, 'bold'))
delete_window_btn_save = Button(delete_window, text = "Save", font = ('Arial', 20, 'bold'), width = 10, command = f11)
delete_window_btn_back = Button(delete_window, text = "Back", font = ('Arial', 20, 'bold'), width = 10, command = f12)

delete_window_ent_rno.focus()

delete_window_lbl_rno.pack(pady = 10)
delete_window_ent_rno.pack(pady = 10)
delete_window_btn_save.pack(pady = 10)
delete_window_btn_back.pack(pady = 10)
delete_window.withdraw()

main_window.mainloop()