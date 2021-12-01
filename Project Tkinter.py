from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as messagebox
import mysql.connector as con
import time as t
import os
import datetime




def main():
    global mainwin , myfont, button, wel ,log , icon,del_

    #coustom font
    myfont = ('Courier New' , 20, 'bold')

    #window icon
    icon = 'window.ico'

    #main win
    mainwin = Tk()
    mainwin.config(background ='white')
    mainwin.geometry('400x700')
    mainwin.minsize(400,700)
    mainwin.title('School database - Tkinter by shouryaraj')
    mainwin.iconbitmap(icon)
    #frame style
    framestyle = Style()
    framestyle.configure('TFrame' , background = 'white')

    #label style
    labelstyle = Style()
    labelstyle.configure("TLabel" , background = 'white' , font = myfont)


    #button style,image
    button = PhotoImage(file = f'{os.getcwd()}\\button.png')
    button = button.subsample(2,2)
    #welcome image
    wel = PhotoImage(file =f'{os.getcwd()}\\welcome.png')
    wel = wel.subsample(4,4)
    #logout image
    log = PhotoImage(file = f'{os.getcwd()}\\logout.png')
    log = log.subsample(2,2)

    #delete image
    del_ = PhotoImage(file = f'{os.getcwd()}\\delete.png')
    del_ = del_.subsample(10,10)


    #logframe
    logframe()


    mainwin.grid_columnconfigure(0, weight = 1)
    mainwin.grid_rowconfigure(0, weight =1)

    mainwin.focus_force()
    mainwin.mainloop()


# first frame
def logframe():



    Lframe = Frame(mainwin)
    Lframe.grid(column = 0 , row = 0 , sticky =N+S+W+E , padx = 10, pady = 10)


    #host  label
    host_label = Label(Lframe, text = "Host" )
    host_label.grid(column = 0 , row = 0, sticky = N+S+W+E)
    Lframe.grid_columnconfigure(0 , weight =1)
    Lframe.grid_rowconfigure(0,weight=1)




    #host entry
    host_entry = Entry(Lframe ,font =( None,20),justify = CENTER )
    host_entry.grid(column = 0 , row =1, sticky = N+E+W)
    host_entry.insert(0,'localhost')
    Lframe.grid_rowconfigure(1, weight=1)


    #user label
    user_label = Label(Lframe, text = "User")
    user_label.grid(column = 0 , row = 2, sticky = N+S+W+E)
    Lframe.grid_rowconfigure(2, weight=1)

    # user entry
    user_entry = Entry(Lframe, font=(None, 20),justify = CENTER)
    user_entry.grid(column=0, row=3, sticky=N + E + W)
    user_entry.insert(0, "root")
    Lframe.grid_rowconfigure(3, weight=1)

    # password label
    password_label = Label(Lframe, text="Password")
    password_label.grid(column=0, row=4, sticky=N + S + W + E)
    Lframe.grid_rowconfigure(4, weight=1)

    # password entry
    password_entry = Entry(Lframe, font=(None, 20),justify = CENTER, show = "*")
    password_entry.grid(column=0, row=5, sticky=N + E + W)
    #password_entry.insert(0,'shourya1236')
    Lframe.grid_rowconfigure(5, weight=1)





    def distroy(event = None):
        #print(type(host_entry.get()), user_entry.get(), password_entry.get())
        mycon(host_entry.get() , user_entry.get(), password_entry.get())
        Lframe.destroy()
        #Lframe.grid_forget()





    #login button
    login_button = tk.Button(Lframe ,height = 10, text = "Login",
                             font = myfont ,activebackground = 'white',
                             borderwidth = 0, bg = 'white',
                             image = button, command = distroy ,compound = CENTER, fg = 'blue',
                             activeforeground = 'green',cursor = 'hand2')
    login_button.grid(column = 0 , row = 6 ,sticky = N+S+W+E , pady = 10, padx = 10)
    Lframe.grid_rowconfigure(6, weight =1)

    #my label
    mylabel = tk.Label(Lframe, text = '-Shouryaraj Singh Goud' , fg = 'red' , anchor = E, bg = 'white',
                       font = ('Courier New',15,'bold italic'),cursor = 'exchange')
    mylabel.grid(column = 0 , row = 7 ,sticky = N+S+W+E)
    Lframe.grid_rowconfigure(7 , weight = 1)


    password_entry.bind('<Return>', distroy)
    user_entry.bind('<Return>', distroy)
    host_entry.bind('<Return>', distroy)



#welcome frame
def welframe():

    global n
    Wframe = Frame(mainwin)
    Wframe.grid(column = 0 , row = 0, sticky =N+S+W+E)

    imagel = Label( Wframe ,image = wel,anchor =S ,
                    cursor = 'watch',borderwidth = 0)
    imagel.grid(column = 0 , row = 0, sticky = N+S+W+E)

    #my label
    mylabel = tk.Label(Wframe, text = '-Shouryaraj Singh Goud' , fg = 'red' , anchor =S+E, bg = 'white',height = 1,
                       font = ('Courier New',10,'bold italic'),cursor = 'exchange')
    mylabel.grid(column = 0 , row = 7 ,sticky = S+W+E)
    Wframe.grid_rowconfigure(1 , weight = 1)



    Wframe.grid_columnconfigure(0, weight =1)
    Wframe.grid_rowconfigure(0, weight=1)




    Wframe.update()
    mainwin.update()

    mainwin.after(3000, Wframe.destroy)

date_name = tuple(range(1, 32))
year_name = tuple(range(2020, 1950, -1))
dobentry = None
dojentry = None

current_year = 0
current_month = 0
current_date = 0

Admno = None

def personalframe():
    menuframe = Frame(mainwin)
    menuframe.grid(column = 0 ,row = 0 ,sticky = N+S+W+E)

    #Button actions
    def Logout():
        menuframe.grid_forget()
        menuframe.destroy()
        logframe()


    def distroy_subopt(event ,widget ,frame):
        if event.widget.get() not in ['XI', 'XII']:
            widget.configure(values = ('Non-Opted',) , state = 'disabled')
            widget.current(0)
        else:
            widget.configure(values = ('Maths CS','Maths Hindi','Bio CS','Bio Hindi'), state = 'readonly')
            widget.current(0)

    def date_frame(frame , column , row ,tochange):
        global dobentry,dojentry

        def date_name_change(event):
            global date_name
            if event.widget.get() in ('April','June', 'September', 'November'):

                date_name = tuple(range(1,31))
                date.configure(values = date_name)
                date.current(0)

            elif event.widget.get() =='February':


                date_name = tuple(range(1, 30))

                date.configure(values=date_name)
                date.current(0)
            else:

                date_name = tuple(range(1, 32))
                date.configure(values=date_name)

        def year_name_change(event):
            global year_name
            if date.get() == '29' and month.get() == 'February':

                year_name= tuple(range(2020,1950,-4))
                year.configure(values = year_name )
            else:

                year_name = tuple(range(2020, 1950, -1))
                year.configure(values = tuple(range(2020, 1950, -1)))

        def date_return(event):
            global  dobentry, dojentry
            if tochange == dobentry:
                dobentry = f'{year.get()}-{month.get()}-{date.get()}'
                print(dobentry,'dob')
                reitter()
                date_frame(frame , column , row ,dobentry)

            elif tochange == dojentry:
                dojentry = f'{year.get()}-{month.get()}-{date.get()}'
                print(dojentry,'doj')
                reitter()
                date_frame(frame, column, row, dojentry)

            else : print('nothing')

        def reitter():
            global current_month,current_date,current_year
            current_year = year_name.index(int(year.get()))
            current_date = date_name.index(int(date.get()))
            current_month =  month_name.index(month.get())



        d_frame = tk.Frame(frame , bg = 'white')
        d_frame.grid(column = column , row = row , sticky = N+S+W+E, padx=15, pady=10)

        month_name = ('January', 'February', 'March', 'April', 'May',
                      'June', 'July', 'August', 'September',
                      'October', 'November', 'December')


        month = Combobox(d_frame, state = 'readonly'  , justify= CENTER, values = month_name,
                         cursor = 'hand2', font = (None , 12))
        month.current(current_month)
        month.bind('<<ComboboxSelected>>' ,  lambda e: [date_name_change(e), date_return(e)])
        month.grid(column =  0 ,row =0 , sticky = N+S+W+E)

        date = Combobox(d_frame , state = 'readonly'  , justify= CENTER, values =date_name,
                        cursor = 'hand2', font = (None , 12))
        date.current(current_date)
        date.grid(column=1, row=0, sticky = N + S + W + E)

        year = Combobox(d_frame , state = 'readonly'  , justify= CENTER, values = year_name,
                        cursor = 'hand2', font = (None , 12))
        year.current(current_year)
        year.grid(column=2, row=0, sticky = N + S + W + E)
        date.bind("<<ComboboxSelected>>" , lambda e :[year_name_change(e) ,date_return(e)] )
        year.bind("<<ComboboxSelected>>", lambda e: date_return(e))



        for i in range(3):
            d_frame.grid_columnconfigure(i, weight =1)
        d_frame.grid_rowconfigure(0,weight =1)

    def convert_date(string):
        date = ''
        month = {'January':'01','February':'02','March':'03',
                 'April':'04' ,'May':'05' ,'June': '06','July':'07',
         'August':'08' ,'September':'09','October':'10','November':'11','December':'12' }

        if string == None:string = '2020-January-1'

        string = str(string)
        print(string)
        date = date + string[:4]+'-'
        print(date,string)
        string = string[5:]
        date = date + month[string[:string.index('-')]]+'-'
        string = string[string.index('-')+1:]
        if len(string) == 1:
            date = date +'0'+string
        else:
            date = date+string
        print(date)
        return date


    def roman_convert(class_):
        dict = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10,'XI':11,'XII':12}

        class_ = dict[class_]

        return class_

    def sub(window, name, gen, class_, subopt, doj , dob  ):
        try:
            if name == '' or name is None:
                print(name)
                raise(ValueError)
            query1= r"insert into school(name,gen,class,subopt, date_of_join,date_of_birth) values('%s','%s' ,'%s', '%s', '%s','%s');"%(name,gen,class_,subopt,doj,dob)
            cur.execute(query1)
            class_ = roman_convert(class_)
            cur.execute(f'select admno from school where name = "{name}" and date_of_birth = "{dob}";')
            admo = cur.fetchone()[0]

            query2 = f"insert into class{class_}(name, admno) values('{name}',{admo});"
            cur.execute(query2)
            window.destroy()

            print(f'executed{query2}')
        except:
            messagebox.showerror('Invalid Entry','Name should not be empty or exceed than 30 characters or wrong date')
            window.focus_force()

    def Admit_Student():



        Student_form = Toplevel()
        Student_form.focus_force()
        Student_form.iconbitmap(icon)
        Student_form.title('New Student Form')
        Student_form.configure(background = 'white')
        Student_form.geometry('900x650')
        Student_form.minsize(900,650)

        global dobentry,dojentry
        formframe = tk.Frame(Student_form)
        formframe.grid(column = 0 , row = 0 ,sticky = N+S+E+W)

        formframe.configure(bg ='white')
        Student_form.grid_columnconfigure(0,weight =1)
        Student_form.grid_rowconfigure(0, weight=1)

        ###Column 1  labels
        namelabel = Label(formframe ,text = 'Name:', font = myfont , background = 'white' ,
                          anchor = 'w')
        namelabel.grid(column = 0 ,row = 0 , sticky = N+S+W+E)

        genlabel = Label(formframe, text='Gender:', font=myfont, background='white',
                          anchor='w')
        genlabel.grid(column=0, row=1 , sticky = N+S+W+E)

        classlabel = Label(formframe, text='Class:', font=myfont, background='white',
                         anchor='w')
        classlabel.grid(column=0, row=2, sticky=N + S + W + E)

        suboptlabel = Label(formframe, text='Optional Subject:', font=myfont, background='white',
                         anchor='w')
        suboptlabel.grid(column=0, row=3, sticky=N + S + W + E)

        dojlabel = Label(formframe, text='Date of Joining:', font=myfont, background='white',
                         anchor='w')
        dojlabel.grid(column=0, row=4, sticky=N + S + W + E)

        doblabel = Label(formframe, text='Date of Birth:', font=myfont, background='white',
                         anchor='w')
        doblabel.grid(column=0, row=5, sticky=N + S + W + E)

        formframe.grid_columnconfigure(0 , weight =1)
        formframe.grid_columnconfigure(1, weight=1)



        for i in range(7):
            formframe.grid_rowconfigure(i, weight=1)


        #Column 1
        nameentry = Entry(formframe , justify = CENTER, font = (None , 20) , background = 'white')
        nameentry.grid(column = 1 , row =0 ,sticky = N+S+W+E , padx =15, pady =10)

        genentry = Combobox(formframe, justify = CENTER ,values= ('M' ,'F'),
                            state = 'readonly' , font=(None , 20) , cursor = 'hand2')
        genentry.current(0)
        genentry.grid(column=1, row=1, sticky=N + S + W + E, padx=15, pady=10)

        classentry = Combobox(formframe, font = (None, 20) ,state = 'readonly',justify = CENTER,
                              values=('I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII')
                              , cursor = 'hand2')
        classentry.current(11)

        classentry.grid(column = 1 , row =2 ,sticky = N+S+W+E , padx =15, pady =10)



        suboptentry = Combobox(formframe, font = (None, 20) ,state = 'readonly',
                              values=('Maths CS','Maths Hindi','Bio CS','Bio Hindi'),
                               justify = CENTER,cursor = "hand2")

        classentry.bind("<<ComboboxSelected>>" , lambda event :distroy_subopt(event,suboptentry,formframe) )
        suboptentry.current(0)
        Student_form.update()
        Student_form.update_idletasks()
        suboptentry.grid(column=1, row=3, sticky=N + S + W + E, padx=15, pady=10)


        date_frame(formframe, 1, 4,dobentry)


        date_frame(formframe, 1, 5,dojentry)


        #submit button

        subbutton = tk.Button(formframe , text = "Submit",
                             font = myfont ,activebackground = 'white',
                             borderwidth = 0, bg = 'white',
                             image = button ,compound = CENTER, fg = 'blue',
                              command = lambda : sub(Student_form ,str(nameentry.get()),str(genentry.get()),str(classentry.get()),str(suboptentry.get()), str(convert_date(dojentry)),convert_date(dobentry)),
                              activeforeground = 'green')
        subbutton.grid(column = 1 , row = 6 ,sticky = N+S+W+E , pady = 10, padx = 10)

        Student_form.bind('<Return>' , lambda e:  sub(Student_form ,str(nameentry.get()),str(genentry.get()),str(classentry.get()),str(suboptentry.get()), str(convert_date(dojentry)),convert_date(dobentry) ))
        Student_form.mainloop()

    def tablewindow(   title,fun , colour = 'white' ,orientation = 'vertical'):
        ''' title, colour = 'white' , fun , orient = 'vertical' '''


        tablewin = Toplevel()


        if fun == 'student_details':
            cur.execute(f"select * from school where admno = {Admno};")
            table_recs = cur.fetchall()
            table_cols = cur.column_names
            table_recs = list(table_recs)
            print(table_recs)
            print(table_cols)
            table_recs.insert(0, table_cols)
            print(table_recs)
            table_elements = tuple(table_recs)
            text = table_elements[1][0]
        elif fun == 'student_marks':
            cur.execute(f"select class from school where admno = {Admno};")
            class_ = cur.fetchone()[0]
            class_ = roman_convert(class_)
            cur.execute(f"select subopt from school where admno = {Admno};")
            optsub = cur.fetchone()[0]
            if class_ in range(0,9):
                cur.execute(f"select name,physics , chemistry ,maths,bio , sst,hindi , sanskrit from class{class_}  where admno ={Admno} ;")
            elif class_ in range(9,11):
                cur.execute(f"select name,physics , chemistry ,maths,bio , sst,hindi from class{class_}  where admno ={Admno} ;")
            elif class_ in range(11,13):

                if optsub == 'Maths CS': subs = 'maths , cs'
                elif optsub == 'Maths Hindi':subs = 'maths , hindi'
                elif optsub == 'Bio CS':subs = 'bio, cs'
                elif optsub == 'Bio Hindi':subs = 'maths ,hindi'

                cur.execute(f"select name, physics , chemistry ,{subs} from class{class_} where admno ={Admno} ;")

            table_recs = cur.fetchall()
            table_recs = list(table_recs)
            print(table_recs)
            table_cols = cur.column_names

            table_recs.insert(0, table_cols)
            table_elements = tuple(table_recs)
            print(table_elements)
            text= table_elements[1][0]

        elif fun  == 'class_rec' :
            cur.execute(f'select * from class{Admno} order by sno;')
            table_recs = cur.fetchall()
            table_recs = list(table_recs)
            print(table_recs)
            table_cols = cur.column_names

            table_recs.insert(0, table_cols)
            table_elements = tuple(table_recs)
            print(table_elements)
            text = f'Class{Admno}'
        elif fun == 'school_rec':
            cur.execute(f"select * from school order by admno;")
            table_recs = cur.fetchall()
            table_recs = list(table_recs)
            print(table_recs)
            table_cols = cur.column_names

            table_recs.insert(0, table_cols)
            table_elements = tuple(table_recs)
            print(table_elements)
            text = 'School Records'





        tablewin.iconbitmap(icon)
        tablewin.title(title)
        tablewin.geometry('800x500')
        tablewin.configure(background = colour)
        tablewin.minsize(tablewin['width'],tablewin['height'])

        tableframe = tk.Frame(tablewin, bg = colour)
        tableframe.grid(column = 0 , row = 0 , sticky = N+S+W+E)
        tablewin.grid_columnconfigure(0, weight =1)
        tablewin.grid_rowconfigure(0, weight =1)

        toplabel = tk.Label(tableframe,text = text , bg = colour, font= myfont)
        toplabel.grid(column = 0 , row = 0, sticky = N+W+E+S)


        #scrollbar
        tablesby = Scrollbar(tablewin)
        tablesby.grid(column = 0 , row = 0,sticky = N+S+E)

        tablesbx = Scrollbar(tablewin , orient = HORIZONTAL)
        tablesbx.grid(column=0, row=0, sticky=W+ E+S)

        tablecanvas = Canvas(tableframe, background = colour,
                             yscrollcommand = tablesby.set, xscrollcommand = tablesbx.set)
        tablecanvas.grid(column = 0 , row =1,sticky = N+W+E)
        tableframe.grid_columnconfigure(0 , weight = 1)
        #tableframe.grid_rowconfigure(0, weight=1)
        tableframe.grid_rowconfigure(1, weight=1)

        tablesby.config(command = tablecanvas.yview)
        tablesbx.config(command=tablecanvas.xview)

        tablecanvas.bind('<Configure>' , lambda e : tablecanvas.configure(scrollregion = tablecanvas.bbox('all')))

        frame = Frame(tablecanvas)
        frame.grid(column =0 , row = 0 ,sticky = N+S+W+E)

        tablecanvas.grid_columnconfigure(0, weight =1)
        tablecanvas.grid_rowconfigure(0, weight =1)

        tablecanvas.create_window((0,0) ,window = frame)


        if orientation == 'vertical':

            for i in range(len(table_elements[1])):
                for j in range(len(table_elements)):
                    block  = tk.Entry(frame , font = (15), bg = 'white',
                                      borderwidth = 5)
                    if type(table_elements[j][i]) == str or type(table_elements[j][i]) == int:
                        block.insert(END,table_elements[j][i])
                    elif table_elements[j][i]  is None or table_elements[j][i] == '':
                        block.insert(END,'Null')
                    else :
                        date = table_elements[j][i]
                        date = date.strftime('%d'), date.strftime('%B'), date.strftime('%Y')
                        block.insert(END, date)
                    block.configure(state = 'readonly')
                    block.grid(column = j, row = i , sticky = N+S+W+E, padx = 2)
                    frame.grid_columnconfigure(j,weight =1)
                    frame.grid_rowconfigure(i, weight = 1)

        elif orientation == 'horizontal':

            for i in range(len(table_elements)):
                for j in range(len(table_elements[0])):
                    block  = tk.Entry(frame , font = (15), bg = 'white',
                                      borderwidth = 5)
                    if type(table_elements[i][j]) == str or type(table_elements[i][j]) == int:
                        block.insert(END,table_elements[i][j])
                    elif table_elements[i][j] is None or table_elements[i][j] =='':

                        block.insert(END, 'Null')
                    else :
                        date = table_elements[i][j]
                        date = date.strftime('%d'), date.strftime('%B'), date.strftime('%Y')
                        block.insert(END, date)
                    block.configure(state = 'readonly')
                    block.grid(column = j, row = i , sticky = N+S+W+E, padx = 2)
                    frame.grid_columnconfigure(j,weight =1)
                    frame.grid_rowconfigure(i, weight = 1)

    def deldistroy(delframe):
        delframe.destroy()
        personalframe()

    def deleteframe():

        delframe = Frame(mainwin)
        delframe.grid(column = 0 , row = 0 , sticky = N+S+W+E)

        label1 = tk.Label(delframe, image = del_, bg = 'white')
        label1.grid(column = 0 , row = 0 , sticky = N+S+W+E,padx = 10 , pady = 10)

        label2 = Label(delframe , text = "Record Deletd" , font = myfont, anchor = N)
        label2.grid(column = 0 , row = 1 , sticky = N+S+W+E)

        delframe.grid_columnconfigure(0, weight = 1)
        delframe.grid_rowconfigure(0, weight=1)
        delframe.grid_rowconfigure(1, weight=1)

        mainwin.after(3000,lambda :deldistroy(delframe))

    def mod_sub(window, name, gen, class_, subopt, doj, dob, current_state = 'TC'):
        try:
            if name == '':
                raise (ValueError)

            query = f"update school set name = '{name}',gen = '{gen}',class = '{class_}' , subopt = '{subopt}' ,date_of_join = '{doj}',date_of_birth = '{dob}', current_state = '{current_state}' where admno = {Admno};"
            cur.execute(query)
            print("updateed student ", query)
            window.destroy()

            print(f'executed{query}')
        except:
            messagebox.showerror('Invalid Entry', 'Name should not be empty or exceed than 30 characters or wrong date')
            window.focus_force()


    def mod_Admit_Student():



        mod_Student_form = Toplevel()
        mod_Student_form.focus_force()
        mod_Student_form.iconbitmap(icon)
        mod_Student_form.title('Modify Student details')
        mod_Student_form.configure(background = '#03fcf8')
        mod_Student_form.geometry('900x750')
        mod_Student_form.minsize(900,750)

        global dobentry,dojentry
        formframe = tk.Frame(mod_Student_form)
        formframe.grid(column = 0 , row = 0 ,sticky = N+S+E+W)

        formframe.configure(bg ='#03fcf8')
        mod_Student_form.grid_columnconfigure(0,weight =1)
        mod_Student_form.grid_rowconfigure(0, weight=1)

        ###Column 1  labels
        namelabel = Label(formframe,text = 'Name:', font = myfont , background = '#03fcf8' ,
                          anchor = 'w')
        namelabel.grid(column = 0 ,row = 0 , sticky = N+S+W+E)

        genlabel = Label(formframe, text='Gender:', font=myfont, background='#03fcf8',
                          anchor='w')
        genlabel.grid(column=0, row=1 , sticky = N+S+W+E)

        classlabel = Label(formframe, text='Class:', font=myfont, background='#03fcf8',
                         anchor='w')
        classlabel.grid(column=0, row=2, sticky=N + S + W + E)

        suboptlabel = Label(formframe, text='Optional Subject:', font=myfont, background='#03fcf8',
                         anchor='w')
        suboptlabel.grid(column=0, row=3, sticky=N + S + W + E)

        dojlabel = Label(formframe, text='Date of Joining:', font=myfont, background='#03fcf8',
                         anchor='w')
        dojlabel.grid(column=0, row=4, sticky=N + S + W + E)

        doblabel = Label(formframe, text='Date of Birth:', font=myfont, background='#03fcf8',
                         anchor='w')
        doblabel.grid(column=0, row=5, sticky=N + S + W + E)

        current_statuslabel = Label(formframe, text='Current Status:', font=myfont, background='#03fcf8',
                         anchor='w')
        current_statuslabel.grid(column=0, row=6, sticky=N + S + W + E)

        formframe.grid_columnconfigure(0 , weight =1)
        formframe.grid_columnconfigure(1, weight=1)



        for i in range(8):
            formframe.grid_rowconfigure(i, weight=1)


        #Column 1
        nameentry = Entry(formframe , justify = CENTER, font = (None , 20) , background = 'white')
        nameentry.grid(column = 1 , row =0 ,sticky = N+S+W+E , padx =15, pady =10)

        genentry = Combobox(formframe, justify = CENTER ,values= ('M' ,'F'),
                            state = 'readonly' , font=(None , 20) , cursor = 'hand2')
        genentry.current(0)
        genentry.grid(column=1, row=1, sticky=N + S + W + E, padx=15, pady=10)

        classentry = Combobox(formframe, font = (None, 20) ,state = 'readonly',justify = CENTER,
                              values=('I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII')
                              , cursor = 'hand2')
        classentry.current(11)

        classentry.grid(column = 1 , row =2 ,sticky = N+S+W+E , padx =15, pady =10)



        suboptentry = Combobox(formframe, font = (None, 20) ,state = 'readonly',
                              values=('Maths CS','Maths Hindi','Bio CS','Bio Hindi'),
                               justify = CENTER,cursor = "hand2")

        classentry.bind("<<ComboboxSelected>>" , lambda event :distroy_subopt(event,suboptentry,formframe) )
        suboptentry.current(0)
        mod_Student_form.update()
        mod_Student_form.update_idletasks()
        suboptentry.grid(column=1, row=3, sticky=N + S + W + E, padx=15, pady=10)


        date_frame(formframe, 1, 4,dobentry)


        date_frame(formframe, 1, 5,dojentry)

        current_statusentry = Combobox(formframe, font=(None, 20), state='readonly', justify=CENTER,
                              values=('Active', 'TC')
                              , cursor='hand2')
        current_statusentry.current(1)

        current_statusentry.grid(column=1, row=6, sticky=N + S + W + E, padx=15, pady=10)


        #submit button

        subbutton = tk.Button(formframe , text = "Submit",
                             font = myfont ,activebackground = '#03fcf8',
                             borderwidth = 0, bg = '#03fcf8',
                             image = button ,compound = CENTER, fg = 'blue',
                              command = lambda : mod_sub(mod_Student_form ,str(nameentry.get()),str(genentry.get()),str(classentry.get()),str(suboptentry.get()), str(convert_date(dojentry)),convert_date(dobentry),str(current_statusentry.get())),
                              activeforeground = 'green')
        subbutton.grid(column = 1 , row = 7 ,sticky = N+S+W+E , pady = 10, padx = 10)

        mod_Student_form.bind('<Return>' , lambda e : mod_sub(mod_Student_form ,str(nameentry.get()),str(genentry.get()),str(classentry.get()),str(suboptentry.get()), str(convert_date(dojentry)),convert_date(dobentry),str(current_statusentry.get()))  )
        mod_Student_form.mainloop()



    logoutbutton = tk.Button(menuframe , image = log , relief = RAISED , compound = CENTER ,
                             command = Logout,cursor = "hand2",activebackground = 'white',width = 300,
                       activeforeground = 'blue' , bg  = 'white' , borderwidth = 0)
    logoutbutton.grid(column = 0 , row = 0,sticky = N+S,padx = 150, pady = 10)

    admit_student = tk.Button(menuframe,text ='Admit Student', image = button , relief = RAISED , font = myfont ,width = 300,
                              borderwidth = 0 ,compound = CENTER ,command = Admit_Student,activebackground = 'white',
                              fg = 'green', activeforeground = 'blue', cursor = 'hand2',bg ="white")

    admit_student.grid(column = 0 , row = 1,sticky = N+S ,padx =20)

    student_details =tk.Button(menuframe,text ='Student Details', image = button , relief = RAISED , font = myfont ,
                              borderwidth = 0 ,compound = CENTER ,activebackground = 'white',width = 300,
                              fg = 'green', activeforeground = 'blue', cursor = 'hand2',bg ="white",
                               command = lambda: [Admno_fun('Student details', 'student_details','yellow','vertical')])
    student_details.grid(column = 0 , row = 2,sticky = N+S,padx =20)

    student_marks =tk.Button(menuframe,text ='Student Marks', image = button , relief = RAISED , font = myfont ,
                              borderwidth = 0 ,compound = CENTER ,activebackground = 'white',width = 300,
                              fg = 'green', activeforeground = 'blue', cursor = 'hand2',bg ="white",
                             command = lambda: Admno_fun('Student Manrks','student_marks','#3077cf','vertical',True))
    student_marks.grid(column = 0 , row = 3,sticky = N+S,padx =20)

    update_marks =tk.Button(menuframe,text =r'Enter\Update Marks', image = button , relief = RAISED , font = myfont ,
                              borderwidth = 0 ,compound = CENTER ,activebackground = 'white',width = 300,
                              fg = 'green', activeforeground = 'blue', cursor = 'hand2',bg ="white",
                            command = lambda : Admno_fun('Enter\\Update Marks','update_marks','#ad3b3b'))
    update_marks.grid(column = 0 , row = 4,sticky = N+S,padx =20)

    school_rec =tk.Button(menuframe,text ='School Records', image = button , relief = RAISED , font = myfont ,width = 300,
                              borderwidth = 0 ,compound = CENTER ,activebackground = 'white',
                              fg = 'green', activeforeground = 'blue', cursor = 'hand2',bg ="white",
                          command = lambda : Admno_fun('School Records', 'school_rec', '#710bbf','horizontal',False))
    school_rec.grid(column = 0 , row = 5,sticky = N+S,padx =20)

    class_rec =tk.Button(menuframe,text ='Class Records', image = button , relief = RAISED , font = myfont ,
                              borderwidth = 0 ,compound = CENTER ,activebackground = 'white',width = 300,
                              fg = 'green', activeforeground = 'blue', cursor = 'hand2',bg ="white",
                         command = lambda: Admno_fun('Class Records', 'class_rec','#86cf00','horizontal' ))
    class_rec.grid(column = 0 , row = 6,sticky = N+S,padx =20)

    update_student = tk.Button(menuframe,text ='MOD Student Info', image = button , relief = RAISED , font = myfont ,
                              borderwidth = 0 ,compound = CENTER ,activebackground = 'white',width = 300,
                              fg = 'green', activeforeground = 'blue', cursor = 'hand2',bg ="white",
                               command = lambda :   Admno_fun('Update Student Details', 'update_student' )    )
    update_student.grid(column = 0 , row = 7,sticky = N+S,padx =20)



    delete_rec = tk.Button(menuframe,text ='Delete Record', image = button , relief = RAISED , font = myfont ,
                              borderwidth = 0 ,compound = CENTER ,activebackground = 'white',width = 300,
                              fg = 'green', activeforeground = 'blue', cursor = 'hand2',bg ="white",
                           command = lambda:Admno_fun('Record Deleted', 'delete_rec','green'))
    delete_rec.grid(column = 0 , row = 8,sticky = N+S,padx =20)

    #my label
    mylabel = tk.Label(menuframe, text = '-Shouryaraj Singh Goud' , fg = 'red' , anchor = S+E, bg = 'white',
                       font = ('Courier New',10,'bold italic'),cursor = 'exchange')
    mylabel.grid(column = 0 , row = 9 ,sticky = N+S+W+E)
    menuframe.grid_rowconfigure(9 , weight = 1)


    menuframe.grid_columnconfigure(0,weight=1)
    for i in range(9):
        menuframe.grid_rowconfigure(0, weight=1)




    def updating(class_ , physics , chem , maths,bio, cs, hindi , sst, skt ,subopt,window ,frame):

        if class_  < 9 :
            cur.execute(f"update class{class_} set physics =  {physics if physics!= '' else 'null'},chemistry= {chem if chem != '' else 'null'},bio = {bio if bio!= '' else 'null'}, maths ={maths if maths!='' else 'null'}   , sst = {sst if sst!='' else 'null'}, hindi = {hindi if hindi !='' else 'null'}, sanskrit = {skt if skt!='' else 'null'} where admno = {Admno};")
            #print(f"insert into class{class_}(physics,chemistry, bio,maths , sst , hindi , sanskrit ) values(  {physics} , {chem}, {bio} ,{maths} ,{sst} ,{hindi},{skt});")
            print(class_,'executed')
        elif class_ < 11:
            cur.execute(f"update class{class_} set physics =  {physics if physics!= '' else 'null'},chemistry= {chem if chem != '' else 'null'},bio = {bio if bio!= '' else 'null'}, maths ={maths if maths!='' else 'null'}   , sst = {sst if sst!='' else 'null'}, hindi = {hindi if hindi !='' else 'null'}  where admno = {Admno};")
            print(class_,'executed')

        elif subopt == 'Maths CS':
            cur.execute(f"update class{class_} set physics =  {physics if physics!= '' else 'null'},chemistry= {chem if chem != '' else 'null'},maths ={maths if maths!='' else 'null'},cs ={cs if cs!='' else 'null'}  where admno = {Admno};")
            print(class_,'executed')

        elif subopt == 'Maths Hindi':
            cur.execute(f"update class{class_} set physics =  {physics if physics!= '' else 'null'},chemistry= {chem if chem != '' else 'null'},maths ={maths if maths!='' else 'null'},hindi = {hindi if hindi!='' else 'null'}  where admno = {Admno};")
            print(class_,'executed')

        elif subopt == 'Bio Hindi':
            cur.execute(f"update class{class_} set physics =  {physics if physics!= '' else 'null'},chemistry= {chem if chem != '' else 'null'},bio ={bio if bio != '' else 'null'},hindi  ={hindi if hindi!='' else 'null'} where admno = {Admno};")
            print(class_,'executed')

        elif subopt == 'Bio CS':
            cur.execute( f"update class{class_} set physics =  {physics if physics!= '' else 'null'},chemistry= {chem if chem != '' else 'null'},bio ={bio if bio!= '' else 'null'},cs ={cs if cs!='' else 'null'} where admno = {Admno};")
            print(class_,'executed')
        else : print('not entered in any class')


        if physics=='' and chem== '' and  maths==''and bio=='' and cs==''and hindi ==''and sst==''and skt=='':
            messagebox.showinfo('Updated' , 'All feilds set to NULL')

        frame.grid_forget()

        success = Frame(window)
        success.grid(column = 0 , row = 0, sticky = N+S+W+E)

        update_success = tk.Label(success , text = '!!update success!!', font = myfont,
                              cursor = 'watch' ,fg = 'green' , bg = 'white',anchor = CENTER)
        update_success.grid(sticky = N+S+E+W)
        success.grid_columnconfigure(0 , weight = 1)
        success.grid_rowconfigure(1, weight = 1)


        window.after(3000,lambda : window.destroy())
    #update marks
    def update_marksfun(title,fun , colour = 'white'):
        cur.execute(f"select class,subopt from school where admno = {Admno};")
        classno,optsub = cur.fetchone()
        classno = roman_convert(classno)
        print(classno , optsub)

        marksentry = Toplevel()
        marksentry.title(title)
        marksentry.iconbitmap(icon)
        marksentry.minsize(500,600)
        marksentry.configure(background = 'white')
        marksentry.focus_force()

        marksframe = tk.Frame(marksentry, bg = colour)
        marksframe.grid(column = 0 , row = 0, sticky = N+S+W+E)
        marksentry.grid_rowconfigure(0,weight = 1)
        marksentry.grid_columnconfigure(0, weight=1)

        physicslabel = Label(marksframe, text = 'Physics:', font = myfont , background = colour ,
                          anchor = 'w')
        physicslabel.grid(column = 0  ,row = 0, sticky = N+S+W+E, padx = 5, pady = 5)

        chemistrylabel = Label(marksframe ,text = 'Chemistry:', font = myfont , background = colour ,
                          anchor = 'w')
        chemistrylabel.grid(column = 0 ,row = 1,  sticky = N+S+W+E, padx = 5, pady = 5)

        #labels
        mathslabel = Label(marksframe ,text = 'Maths:', font = myfont , background = colour ,
                          anchor = 'w')
        mathslabel.grid(column = 0 ,row = 2,sticky = N+S+W+E, padx = 5, pady = 5)

        biolabel = Label(marksframe, text='Bio:', font=myfont, background=colour,
                           anchor='w')
        biolabel.grid(column=0,row = 3, sticky=N + S + W + E, padx=5, pady=5)

        cslabel = Label(marksframe, text='Comp. Science:', font=myfont, background=colour ,
                         anchor='w')
        cslabel.grid(column=0,row = 4, sticky=N + S + W + E, padx=5, pady=5)

        hindilabel = Label(marksframe, text='Hindi:', font=myfont, background=colour ,
                        anchor='w')
        hindilabel.grid(column=0,row = 5, sticky=N + S + W + E, padx=5, pady=5)


        sstlabel = Label(marksframe, text='Social Science:', font=myfont, background=colour,
                        anchor='w')
        sstlabel.grid(column=0,row = 6, sticky=N + S + W + E, padx=5, pady=5)


        sanskritlabel = Label(marksframe, text='Sanskrit', font=myfont, background=colour,
                        anchor='w')
        sanskritlabel.grid(column=0,row = 7, sticky=N + S + W + E, padx=5, pady=5)

        #entries

        physicsentry  = Entry(marksframe , font = (None, 20)  , justify = CENTER )
        physicsentry.grid(column = 1 ,row = 0, sticky = N+S+W+E , padx = 15 , pady = 5)

        chemistryentry = Entry(marksframe, font=(None, 20), justify=CENTER)
        chemistryentry.grid(column=1,row = 1, sticky=N + S + W + E, padx=15, pady=5)


        mathsentry = Entry(marksframe, font=(None, 20), justify=CENTER)
        mathsentry.grid(column=1,row = 2, sticky=N + S + W + E, padx=15, pady=5)

        bioentry = Entry(marksframe, font=(None, 20), justify=CENTER)
        bioentry.grid(column=1,row = 3, sticky=N + S + W + E, padx=15, pady=5)

        csentry = Entry(marksframe, font=(None, 20), justify=CENTER)
        csentry.grid(column=1,row = 4, sticky=N + S + W + E, padx=15, pady=5)

        hindientry = Entry(marksframe, font=(None, 20), justify=CENTER)
        hindientry.grid(column=1,row = 5, sticky=N + S + W + E, padx=15, pady=5)

        sstentry = Entry(marksframe, font=(None, 20), justify=CENTER)
        sstentry.grid(column=1, row = 6,sticky=N + S + W + E, padx=15, pady=5)

        sanskritentry = Entry(marksframe, font=(None, 20), justify=CENTER)
        sanskritentry.grid(column=1,row = 7, sticky=N + S + W + E, padx=15, pady=5)


        if optsub == 'Bio CS' or optsub == 'Bio Hindi':
            mathsentry.config(state = 'disabled')

        if optsub == 'Maths CS' or optsub == 'Maths Hindi' :
            bioentry.config(state = 'disabled')

        if optsub == 'Bio Hindi' or optsub == 'Maths Hindi' or classno < 10:
            csentry.config(state = 'disabled')
        if optsub == 'Bio CS' or optsub == 'Maths CS':
            hindientry.config(state = 'disabled')
        if classno > 8:
            sanskritentry.config(state = 'disabled')

        if classno > 10:
            sstentry.config(state = 'disabled')

        insertall = tk.Button(marksframe,text ='Insert', image = button , relief = RAISED , font = myfont ,
                              borderwidth = 0 ,compound = CENTER ,activebackground = colour,
                              fg = 'green', activeforeground = 'blue', cursor = 'hand2',bg = 'white',
                              command = lambda :updating(classno,physicsentry.get(),chemistryentry.get(),mathsentry.get(),bioentry.get(),csentry.get(),hindientry.get(),sstentry.get(),sanskritentry.get(),optsub,marksentry,marksframe))
        insertall.grid(column = 1 , row = 8, sticky = N+S ,padx = 30 ,pady = 20)

        marksframe.grid_columnconfigure(0 , weight = 1)
        marksframe.grid_columnconfigure(1, weight=1)

        for i in range(9):
            marksframe.grid_rowconfigure(i, weight =1)

        marksentry.bind('<Return>' , lambda e:updating(classno,physicsentry.get(),chemistryentry.get(),mathsentry.get(),bioentry.get(),csentry.get(),hindientry.get(),sstentry.get(),sanskritentry.get(),optsub,marksentry,marksframe))

        marksentry.mainloop()







    #admission frame
    def admbuttoncmd(admentry,frame,title,fun , colour = 'white' ,orientation = 'vertical', required = False):
        try:
            print('not converted')
            Admnol = int(admentry.get())
            print('converted')
            if Admnol not in range(1,13):
                cur.execute(f'select admno from school where admno = {Admnol}')
                print('command executed',Admnol)
                adm = cur.fetchone()
                if Admnol not  in adm:
                    print(adm, 'this is adm')
                    raise(ValueError)

            global Admno
            #print(adm , 'is executing properly')
            Admno = Admnol
            print(Admno)
            print('no error 1')
            frame.grid_forget()
            print('no error 1')
            frame.destroy()
            print('no error 1')
            if fun == 'class_rec' and Admno not in range(1,13):
                raise(ValueError)
            elif fun == 'delete_rec':

                cur.execute(f"delete from school where admno = {Admno};")
                print(f"{Admno} , record deleted")
                menuframe.destroy()
                #menuframe.grid_forget()
                deleteframe()
                #personalframe()
            elif fun == 'update_student':
                personalframe()
                mod_Admit_Student()

            elif fun == 'update_marks':
                personalframe()
                update_marksfun(title,fun , colour)


            else:
                personalframe()
                tablewindow(title, fun, colour, orientation)


            return Admnol
        except:
            if  not required :
                frame.grid_forget()
                print('no error 1')
                frame.destroy()
                print('no error 1')
                personalframe()
                tablewindow(title, fun, colour, orientation)
            if fun == 'class_rec':
                messagebox.showerror('Class' ,'Wrong Class Number')
            elif fun == 'school_rec':pass
            else:
                messagebox.showerror('Invalid','Wrong Addmission Number')



    def Admno_fun(title,fun , colour = 'white' ,orientation = 'vertical', required = True):
        global Admno
        menuframe.grid_forget()
        menuframe.destroy()

        admoframe = Frame(mainwin)
        admoframe.grid(column = 0 , row = 0 , sticky = N+S+W+E)

        admlabel = Label(admoframe, text='Addmission number:' if fun != 'class_rec' else 'Class:',
                        font=myfont, background='white', anchor = CENTER)
        admlabel.grid(column = 0 , row = 0, sticky = N+S+W+E , padx =10 , pady =10)

        admentry = 'none'
        if required:
            admentry = Entry(admoframe, justify = CENTER , font = (None, 20))
            admentry.grid(column =0 , row = 1, padx =10 , pady =10)

        admbutton = tk.Button(admoframe, text = 'Enter', image = button ,compound = CENTER,
                           command = lambda: admbuttoncmd(admentry,admoframe,title,fun , colour  ,orientation, required ), bg = 'white', borderwidth = 0,
                              activebackground  = 'white', font = myfont)
        admbutton.grid(column = 0 , row = 2 ,padx = 10 , pady = 10)

        # my label
        mylabel = tk.Label(admoframe, text='-Shouryaraj Singh Goud', fg='red', anchor=S + E, bg='white', height=1,
                           font=('Courier New', 10, 'bold italic'), cursor='exchange')
        mylabel.grid(column=0, row=3, sticky=S + W + E)
        #admoframe.grid_rowconfigure(3, weight=1)

        if not required :
            admlabel.config(text = '!!Click to Continue!!')

        admoframe.grid_columnconfigure(0, weight = 1)
        for i in range(3):
            admoframe.grid_rowconfigure(i , weight = 1)

        mainwin.bind('<Return>',lambda e: admbuttoncmd(admentry,admoframe,title,fun , colour  ,orientation, required ) )





#mysql Funcs
def mycon(host , user , password):

    try:
        global schooldb , cur
        schooldb = con.connect(host= str(host) , user = str(user), password = str(password))
        welframe()
        cur = schooldb.cursor()
        schooldb.autocommit = True



    except:
        messagebox.showerror("Invalid Entry", "Wrong info")
        logframe()


    mysqlpreprocess()
    mainwin.after( 3000, personalframe)

def mysqlpreprocess():
    def ex(command):
        try :
            cur.execute(command)
            print("executed",command)
        except:print(command ,"not executed")


    ex("create database schooldb;")
    cur.execute("use schooldb;")

    ex(command = "create table school(Name varchar(30) ,Gen enum('M', 'F') not null,AdmNo int auto_increment unique key,Class enum('I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII') not null,SubOpt enum('Non-Opted','Maths CS' ,'Maths Hindi' , 'Bio CS','Bio Hindi') default  'Non-Opted',Date_of_Join date not null,Date_of_Birth date not null,Current_state enum('Active','TC') not null default 'Active',primary key (Name, AdmNo) );")

    for i in range(1, 11):
        ex(f"create table Class{i}(Sno int auto_increment unique key,Name varchar(30) ,AdmNo int unique key,Physics int(3),Chemistry int(3),Bio int(3),Maths int(3),SST int(3),Hindi int(3),"+  ("Sanskrit int(3)," if i not in [9,10] else "")+ f"constraint fkclass{i}_{1+i}  foreign key (Name) references school(Name) on delete cascade on update cascade,constraint fkclass{i}_{2+i}  foreign key (AdmNo) references school(AdmNo) on delete cascade on update cascade);")

    for i in range(11,13):
        ex(f"create table Class{i}(Sno int auto_increment unique key,Name varchar(30) ,AdmNo int unique key,Physics int(3),Chemistry int(3),Bio int(3),Maths int(3),CS int(3),Hindi int(3),constraint fkclass{i}_{1+i}  foreign key (Name) references school(Name) on delete cascade on update cascade,constraint fkclass{i}_{2+i}  foreign key (AdmNo) references school(AdmNo) on delete cascade on update cascade) ;")




'''localhost root shourya1236'''




if __name__ == "__main__":

    main()
    schooldb.close()