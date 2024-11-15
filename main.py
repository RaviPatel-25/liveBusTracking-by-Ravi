import webbrowser
from tkinter import*
import tkinter
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import datetime

class App:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("1100x2130+0+0")
        self.root.resizable(False,False)
        self.root.overrideredirect(True)
        self.root.wm_attributes('-alpha',0.95)
        #self.root.configure(bg='white')
        self.i=6
        self.bg=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Search.jpg")
        self.bar=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Bar3.jpg")
        self.home=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Home.jpg")
        self.ticket=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Ticket.jpg")
        self.community=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Community.jpg")
        self.teamimg=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Teamimg.jpg")
        self.teamphoto=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/TeamPhoto.jpg")
        self.tab=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Tab.jpg")
        self.back=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Back.jpg")
        self.searchbtn=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Searchbtn.jpg")
        self.tic=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Tic.jpg")
        self.bus=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/Bus.png")
        
        #self.bg_image=Frame(self.root,bg='white').place(x=0,y=0,height=2130,width=1100)
        
        
       
        self.frame=Frame(self.root,bg='white').place(x=0,y=0,height=2130,width=1100)
        self.btn=Button(self.frame,image=self.bg,command=self.page2,bg='white',bd=0,font=("times new roman",8)).place(x=0,y=30,height=200,width=1100)
        self.btn=Button(self.frame,command=self.about,bg='white',image=self.bar,bd=0,font=("times new roman",15,'bold')).place(x=90,y=80,height=110,width=120)
        self.btn=Button(self.frame,command=self.main,image=self.home,bg='white',bd=0,font=("times new roman",15,'bold')).place(x=90,y=1870,height=150,width=150)
        self.btn=Button(self.frame,command=self.Ticket_fare,image=self.ticket,bg='white',bd=0,font=("times new roman",15,'bold')).place(x=480,y=1870,height=150,width=150)
        self.btn=Button(self.frame,command=self.Community_page,image=self.community,bg='white',bd=0,font=("times new roman",15,'bold')).place(x=850,y=1870,height=150,width=150)
        
        self.bg_image=Label(self.frame,text="Home",bg='white',font=("times new roman",8)).place(x=90,y=2020)
        self.bg_image=Label(self.frame,text="Ticket fare",bg='white',font=("times new roman",8)).place(x=430,y=2020)
        self.bg_image=Label(self.frame,text="Community",bg='white',font=("times new roman",8)).place(x=790,y=2020)
        self.bg_image=Label(self.frame,image=self.teamimg,bg='white',font=("times new roman",8)).place(x=35,y=300)
        self.bg_image=Label(self.bg_image,image=self.teamphoto,bg='white',font=("times new roman",8)).place(x=35,y=300)
        self.bg_image=Label(self.frame,text="Tech Thinkers",bg='white',font=("times new roman",15,"bold","underline")).place(x=0,y=1400,relwidth=1)
        
        self.start=StringVar()
        self.end=StringVar()
        self.com=StringVar()
        
    def main(self):
        self.start.set("")
        self.end.set("")
        self.frame=Frame(self.root,bg='white').place(x=0,y=0,height=2130,width=1100)
        self.btn=Button(self.frame,image=self.bg,command=self.page2,bg='white',bd=0,font=("times new roman",8)).place(x=0,y=30,height=200,width=1100)
        self.btn=Button(self.frame,command=self.about,bg='white',image=self.bar,bd=0,font=("times new roman",15,'bold')).place(x=90,y=80,height=110,width=120)
        self.btn=Button(self.frame,command=self.main,image=self.home,bg='white',bd=0,font=("times new roman",15,'bold')).place(x=90,y=1870,height=150,width=150)
        self.btn=Button(self.frame,command=self.Ticket_fare,image=self.ticket,bg='white',bd=0,font=("times new roman",15,'bold')).place(x=480,y=1870,height=150,width=150)
        self.btn=Button(self.frame,command=self.Community_page,image=self.community,bg='white',bd=0,font=("times new roman",15,'bold')).place(x=850,y=1870,height=150,width=150)
        
        self.bg_image=Label(self.frame,text="Home",bg='white',font=("times new roman",8)).place(x=90,y=2020)
        self.bg_image=Label(self.frame,text="Ticket fare",bg='white',font=("times new roman",8)).place(x=430,y=2020)
        self.bg_image=Label(self.frame,text="Community",bg='white',font=("times new roman",8)).place(x=790,y=2020)
        self.bg_image=Label(self.frame,image=self.teamimg,bg='white',font=("times new roman",8)).place(x=35,y=300)
        self.bg_image=Label(self.bg_image,image=self.teamphoto,bg='white',font=("times new roman",8)).place(x=35,y=300)
        self.bg_image=Label(self.frame,text="Tech Thinkers",bg='white',font=("times new roman",15,"bold","underline")).place(x=0,y=1400,relwidth=1)
        
    
        
    def Ticket_fare(self):
        self.frame=Frame(self.root,bg="lime")
        self.frame.place(x=0,y=0,height=2130,width=1100)
        self.btn=Button(self.frame,command=self.main,image=self.back,bd=7,font=("times new roman",15,'bold')).place(x=0,y=0,height=150,width=150)
        self.bg_image=Label(self.frame,text='Ticket rate',bg='lime',fg='black',font=("times new roman",15,'bold')).place(x=400,y=20)
        s=ttk.Style()
        s.theme_use('alt')
        # Add the rowheight
        s.configure('Treeview', font=('freesansbold',5),rowheight=50)
        s.configure('Treeview.Heading',font=('freesansbold',10,"bold"), background="white")
        #s.map('Treeview', background=[('selected', 'black')])
        
        treeview=ttk.Treeview(self.root,selectmode='browse',show="headings",height=45)
        
        #verscrlbar = ttk.Scrollbar(self.frame,orient ="vertical",command = treeview.yview)
        
        separator1 = ttk.Separator(self.root, orient='vertical')
        separator2 = ttk.Separator(self.root, orient='vertical')
        separator3 = ttk.Separator(self.root, orient='vertical')
        separator4 = ttk.Separator(self.root, orient='vertical')
        separator1.place(relx=0.199, rely=0.07, relwidth=0.002, relheight=1)
        separator2.place(relx=0.398, rely=0.07, relwidth=0.002, relheight=1)
        separator3.place(relx=0.597, rely=0.07, relwidth=0.002, relheight=1)
        separator4.place(relx=0.796, rely=0.07, relwidth=0.002, relheight=1)
 
 
        #verscrlbar.pack(side ='right', fill ='y')
        #verscrlbar.place()
        #treeview.configure(xscrollcommand = verscrlbar.set)
        
        treeview['columns']=('Stage', 'KM', 'Ticket rate','Half','Night')
        treeview.column('#0', width=0, stretch=NO)
        treeview.column('Stage', anchor=CENTER, width=220)
        treeview.column('KM', anchor=CENTER, width=220)
        treeview.column('Ticket rate', anchor=CENTER, width=220)
        treeview.column('Half', anchor=CENTER, width=220)
        treeview.column('Night', anchor=CENTER, width=220)
        

 
        treeview.heading('Stage',text='Stage',anchor=CENTER)
        treeview.heading('KM',text='KM')
        treeview.heading('Ticket rate',text='Ticket')
        treeview.heading('Half',text='Half')
        treeview.heading('Night',text='Night')
        
        treeview.insert(parent='',index=0,values=('47','90','90','45','9'))
        treeview.insert(parent='',index=0,values=('46','88','90','45','90'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('45','86','85','45','90'))
        treeview.insert(parent='',index=0,values=('44','84','85','45','85'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('43','82','80','40','85'))
        treeview.insert(parent='',index=0,values=('42','80','80','40','85'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('41','78','80','40','80'))
        treeview.insert(parent='',index=0,values=('40','76','75','40','80'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('39','74','75','40','80'))
        treeview.insert(parent='',index=0,values=('38','72','75','35','75'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('37','70','70','35','75'))
        treeview.insert(parent='',index=0,values=('36','68','70','35','75'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('35','66','70','35','70'))
        treeview.insert(parent='',index=0,values=('34','64','65','35','70'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('33','62','65','30','70'))
        treeview.insert(parent='',index=0,values=('32','60','65','30','65'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('31','58','60','30','65'))
        treeview.insert(parent='',index=0,values=('30','56','60','30','65'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('29','54','60','30','60'))
        treeview.insert(parent='',index=0,values=('28','52','55','25','60'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('27','50','55','25','60'))
        treeview.insert(parent='',index=0,values=('26','48','50','25','55'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('25','46','50','25','55'))
        treeview.insert(parent='',index=0,values=('24','44','50','25','55'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('23','42','45','20','50'))
        treeview.insert(parent='',index=0,values=('22','40','45','20','50'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('21','38','40','20','45'))
        treeview.insert(parent='',index=0,values=('20','36','40','20','45'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('19','34','40','20','45'))
        treeview.insert(parent='',index=0,values=('18','32','35','15','40'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('17','30','35','15','40'))
        treeview.insert(parent='',index=0,values=('16','28','35','15','40'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('15','26','30','15','35'))
        treeview.insert(parent='',index=0,values=('14','24','30','15','35'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('13','22','30','15','35'))
        treeview.insert(parent='',index=0,values=('12','20','25','15','30'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('11','18','25','15','30'))
        treeview.insert(parent='',index=0,values=('10','16','25','15','30'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('9','14','20','10','25'))
        treeview.insert(parent='',index=0,values=('8','12','20','10','25'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('7','10','15','10','20'))
        treeview.insert(parent='',index=0,values=('5','8','15','10','20'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('4','6','10','5','15'))
        treeview.insert(parent='',index=0,values=('3','4','10','5','15'), tags = ['t1'])
        treeview.insert(parent='',index=0,values=('2','2','5','5','10'))
        treeview.insert(parent='',index=0,values=('1','0','0','0','0'), tags = ['t1'])
        treeview.tag_configure('t1', background = 'gray77')
   
        
        
     
     
        treeview.place(x=0,y=150)
      
        
        
    def Community_page(self):
        self.frame=Frame(self.root,bg="lime")
        self.frame.place(x=0,y=0,height=2130,width=1100)
        self.bg_image=Label(self.frame,text='Enter your response',fg="black",bg='lime',font=("times new roman",8)).place(x=300,y=0)
        self.commut=Entry(self.frame,textvariable=self.com,bd=0,fg="black",bg="white").place(x=150,y=50,height=100,width=770)
        self.fname=self.com.get()
        self.btn=Button(self.frame,text='>>',bg='white',command=self.commu_show,bd=10,font=("times new roman",15,'bold'))
        self.btn.place(x=920,y=0,height=150,width=150)
        self.btn=Button(self.frame,command=self.main,image=self.back,bd=0,font=("times new roman",15,'bold')).place(x=0,y=0,height=150,width=150)
        
        s=ttk.Style()
        s.theme_use('alt')
        # Add the rowheight
        s.configure('Treeview', font=('freesansbold',5),rowheight=50)
        s.configure('Treeview.Heading',font=('freesansbold',10,"bold"), background="white")
        #s.map('Treeview', background=[('selected', 'black')])
        
        self.treeview=ttk.Treeview(self.root,selectmode='browse',show="headings",height=45)
        
        self.treeview["columns"]=("1","2")
        self.treeview.column("1",width=100,anchor='c')
        self.treeview.column("2",width=1000,anchor='c')
        self.treeview.heading("1",text="No.")
        self.treeview.heading("2",text="Your Response")
        
        self.treeview.insert("",'end',values=('1','My name is Ravi'),tags=['t1'])
        self.treeview.insert("",'end',values=('2','My name is Brijesh'))
        self.treeview.insert("",'end',values=('3','My name is Aditya'),tags=['t1'])
        self.treeview.insert("",'end',values=('4','My name is Arya'))
        self.treeview.insert("",'end',values=('5','My name is Harshal'),tags=['t1'])
        self.treeview.insert("",'end',values=('6','My name is Pranjal'))
        self.treeview.tag_configure('t1', background = 'gray77')
        self.treeview.place(x=0,y=150,height=2130,width=1100)
        
        
        
        
        
    def commu_show(self):
        #self.bg_image=Label(self.frame,text=self.com.get(),fg="black",font=("times new roman",8)).place(x=0,y=0)
        #self.btn=Button(self.frame,command=self.commu_show,bd=10,font=("times new roman",15,'bold'))
        #self.btn.place(x=0,y=0,height=150,width=150)
        
        #global i
        
        self.i=self.i+1
        if (self.i%2==0):
        	self.treeview.insert("",'end',values=(self.i,self.com.get() ))
        	self.com.set('')  
        else:
        	self.treeview.insert("",'end',values=(self.i,self.com.get() ),tags=['t1'])
        	self.com.set('')  
        	self.treeview.tag_configure('t1', background = 'gray77')
        	# reset the text entry box
        #t3.delete('1.0',END)  # reset the text entry box
        #my_str.set("Data added ")
        #self.commut.focus()   
     #l5.after(3000, lambda: my_str.set('') ) 
        
        self.treeview.place(x=0,y=150,height=2130,width=1100)
        
        
        
        
    def about(self):
        self.frame=Frame(self.root,bg="white")
        self.frame.place(x=0,y=0,height=2130,width=500)
        self.bg_image=Label(self.frame,image=self.tab,font=("times new roman",8)).place(x=0,y=0)
        self.btn=Button(self.frame,command=self.des,image=self.back,bd=0,font=("times new roman",15,'bold'))
        self.btn.place(x=0,y=0,height=150,width=150)
        self.bg_image1=Label(self.bg_image,text="About...",bg="lime",font=("times new roman",10))
        self.bg_image1.place(x=200,y=50)
        self.bg_image=Label(self.frame,text="    ● Setting",fg="black",bg="white",font=("times new roman",10))
        self.bg_image.place(x=10,y=200)
        self.bg_image=Label(self.frame,text="    ● Report",fg="black",bg="white",font=("times new roman",10))
        self.bg_image.place(x=10,y=300)
        
    def des(self):
        self.frame.destroy()
        self.bg_image1.destroy()
        
    
        
        
        
        
        pass
        
    def page2(self):
        self.frame=Frame(self.root,bg="white")
        self.frame.place(x=0,y=0,height=2130,width=1100)
        self.btn=Label(self.frame,bg="lime",bd=0,font=("times new roman",10)).place(x=0,y=250,height=250,width=1100)
       
        self.btn=Button(self.frame,image=self.back,bg="white",bd=0,font=("times new roman",8),command=self.main)
        self.btn.place(x=0,y=0)
        self.btn=Label(self.frame,text="● Destination",bg="white",bd=0,font=("times new roman",10)).place(x=170,y=40)
        
        self.fentry=Entry(self.frame,disabledbackground="white",textvariable=self.start,bd=0,fg="gray",bg="white")
        self.fentry.place(x=15,y=160,height=103,width=1045)
        self.fentry.insert(0, "    • Starting point")
        self.fentry.configure(state=DISABLED)
        
        self.btn=Button(self.frame,bg="white",text="Locate",bd=0,font=("times new roman",8),command=self.locate)
        self.btn.place(x=920,y=0,height=150,width=150)
        
        
        
        self.btn=Button(self.frame,bg="black",fg="lime",text="See bus detail",bd=0,font=("times new roman",8),command=self.bus_detail)
        self.btn.place(x=350,y=400,height=80,width=350)
        
        self.lentry=Entry(self.frame,disabledbackground="white",textvariable=self.end,bd=0,fg="gray",bg="white")
        self.lentry.place(x=15,y=262,height=103,width=1045)
        self.lentry.insert(0, "    • Ending point")
        self.lentry.configure(state=DISABLED)
        
        #self.btn=Button(self.7frame,command=self.des,image=self.searchbtn,bd=0,font=("times new roman",15,'bold'))
        #self.btn.place(x=370,y=550,height=150,width=300)
        
        self.on_click_id1 = self.fentry.bind('<Button-1>', self.on_click1)
        self.on_click_id2 = self.lentry.bind('<Button-1>', self.on_click2)
        
        self.btn=Label(self.frame,text="• Places...",bg="white",bd=0,font=("times new roman",7)).place(x=20,y=530)
       
        #treeview
        
        s=ttk.Style()
        s.theme_use('alt')
        # Add the rowheight
        s.configure('Treeview', font=('freesansbold',5),rowheight=50)
        s.configure('Treeview.Heading',font=('freesansbold',6,"bold"), background="white")
        #s.map('Treeview', background=[('selected', 'black')])
        
        self.treeview=ttk.Treeview(self.root,selectmode='browse',show="headings",height=45)
        
        self.treeview["columns"]=("1","2")
        self.treeview.column("1",width=100,anchor='c')
        self.treeview.column("2",width=1000,anchor='c')
        self.treeview.heading("1",text="No.")
        self.treeview.heading("2",text="Place Addresses")
        
        self.treeview.insert("",'end',values=('1','Swarget'),tags=['t1'])
        self.treeview.insert("",'end',values=('2','Shinghad road khandoba mandir'))
        self.treeview.insert("",'end',values=('3','Dandekar pul'),tags=['t1'])
        self.treeview.insert("",'end',values=('4','Panmala'))
        self.treeview.insert("",'end',values=('5','Jal shidhikaran kendra'),tags=['t1'])
        self.treeview.insert("",'end',values=('6','Ganeshmala'))
        self.treeview.insert("",'end',values=('7','PL deshpande udyan'),tags=['t1'])
        self.treeview.insert("",'end',values=('8','Vitthalwadi jakat naka'))
        self.treeview.insert("",'end',values=('9','Jaidev nagar'),tags=['t1'])
        self.treeview.insert("",'end',values=('10','Rajaram pul'))
        self.treeview.insert("",'end',values=('11','Vitthalwadi sinhagad road'),tags=['t1'])
        self.treeview.tag_configure('t1', background = 'gray77')
        self.treeview.place(x=0,y=600,height=2130,width=1100)
        
        self.str2=self.treeview.bind("<Button-1>", self.OnClick2)
        self.str1=self.treeview.bind("<Button-1>", self.OnClick1)
        
        
    def OnClick1(self,item=""):
        item = self.treeview.selection()[0]
        #webbrowser.open(self.url)
        self.start.set(self.treeview.item(item)["values"][1])
        #self.treeview.unbind("<Button-1>", self.str2)
        
    def OnClick2(self,item=""):
        item = self.treeview.selection()[0]
        #webbrowser.open(self.url)
        self.end.set(self.treeview.item(item)["values"][1])
       
        #print("you clicked on", self.tree.item(item,"text"))
        
        
    def locate(self):
    	a=self.start.get()
    	b=self.end.get()
    	url="https://www.google.com/search?q="+str(a)+"+to+"+str(b)+"map&oq="+str(a)+"+to+"+str(b)+"+map"
    	
    	#https://www.google.com/search?q=swarget+to+dhayari+map&oq=swarget+to+dhayari+map&aqs=chrome..69i57j33i10i160l4.18340j0j9&client=ms-android-samsung-gj-rev1&sourceid=chrome-mobile&ie=UTF-8
    	
    	webbrowser.open(url)
    	pass
    
    def on_click1(self,event):
    	self.fentry.configure(state=NORMAL)
    	self.fentry.delete(0, END)
    	# make the callback only work once
    	self.fentry.unbind('<Button-1>', self.on_click_id1)
    	self.treeview.bind('<Button-1>',self.str1)
    
    	#self.treeview.unbind("<Button-1>", self.str2)
    	
    def on_click2(self,event):
    	#self.treeview.bind('<Button>',self.str2)
    
    	self.lentry.configure(state=NORMAL)
    	self.lentry.delete(0, END)
    	# make the callback only work once
    	self.lentry.unbind('<Button-1>', self.on_click_id2)
    	self.treeview.bind('<Button-1>',self.str2)
    
    	#self.treeview.unbind("<Button-1>", self.str1)
    	
    	
    	
    def bus_detail(self):
        self.frame=Frame(self.root,bg="white")
        self.frame.place(x=0,y=0,height=2130,width=1100)
        self.btn=Button(self.frame,image=self.back,bg="white",bd=0,font=("times new roman",8),command=self.page2)
        self.btn.place(x=0,y=0)
        
        #treeview
        
        s=ttk.Style()
        s.theme_use('alt')
        # Add the rowheight
        s.configure('Treeview', font=('freesansbold',5),rowheight=150)
        s.configure('Treeview.Heading',font=('freesansbold',6,"bold"), background="white")
        #s.map('Treeview', background=[('selected', 'black')])
        #item = self.treeview.selection()[0]
        #a=self.treeview.item(item)["values"][1]
        
        cur_t=datetime.datetime.now()
        h=cur_t.hour
        if h>12:
        	h=h-12
        m=cur_t.minute
        a=self.start.get()
        b=self.end.get()
        
        if a=='Swarget':
        	self.dis1=0
        if a=='Shinghad road khandoba mandir':
        	self.dis1=0.7
        if a=='Dandekar pul':
        	self.dis1=1.5
        if a=='Panmala':
        	self.dis1=1.7
        if a=='Jal shidhikaran kendra':
        	self.dis1=2.2
        if a=='Ganeshmala':
        	self.dis1=2.7
        if a=='PL deshpande udyan':
        	self.dis1=2.9
        if a=='Vitthalwadi jakat naka':
        	self.dis1=3.5
        if a=='Jaidev nagar':
        	self.dis1=3.8
        if a=='Rajaram pul':
        	self.dis1=4
        if a=='Vitthalwadi sinhagad road':
        	self.dis1=4.4
       
        if b=='Swarget':
        	self.dis2=0
        if b=='Shinghad road khandoba mandir':
        	self.dis2=0.7
        if b=='Dandekar pul':
        	self.dis2=1.5
        if b=='Panmala':
        	self.dis2=1.7
        if b=='Jal shidhikaran kendra':
        	self.dis2=2.2
        if b=='Ganeshmala':
        	self.dis2=2.7
        if b=='PL deshpande udyan':
        	self.dis2=2.9
        if b=='Vitthalwadi jakat naka':
        	self.dis2=3.5
        if b=='Jaidev nagar':
        	self.dis2=3.8
        if b=='Rajaram pul':
        	self.dis2=4
        if b=='Vitthalwadi sinhagad road':
        	self.dis2=12.5
      
        
        speed=30
      
        	#self.dis1=405
        self.time=round(((self.dis2-self.dis1)/speed)*60,3)
        dis_m_t,dis_s_t=divmod(self.time,1)
        dis_m=int(dis_m_t)
        dis_s_t1=str(dis_s_t)
        dis_s=int(dis_s_t1[2:])
        
        dis_h=0
        main_h=h+dis_h
        main_m=m+int(dis_m)
        
        if dis_s>=60:
        	dis_s=dis_s-60
        	main_m=main_m+1
        	
        if main_m>=60:
        	main_m=main_m-60
        	main_h=main_h+1
        
        if main_h>12:
        	main_h=main_h-12
        	
        

        #q=self.t//
        self.treeview=ttk.Treeview(self.root,selectmode='browse',show="headings",height=45)
        
        self.treeview["columns"]=("1","2","3","4")
        self.treeview['show']='tree headings'
        self.treeview.column("#0",width=100,anchor='c')
        self.treeview.column("1",width=200,anchor='c')
        self.treeview.column("2",width=400,anchor='c')
        self.treeview.column("3",width=200,anchor='c')
        self.treeview.column("4",width=200,anchor='c')
        self.treeview.heading("#0",text="  ")
        self.treeview.heading("1",text="No.")
        self.treeview.heading("2",text="Place Addresses")
        self.treeview.heading("3",text="Time")
        self.treeview.heading("4",text="Rate")
        
        self.treeview.insert("",'end',iid='1',open=True,image=(self.bus),values=('01',a+'\n                to \n'+b,str(main_h)+':'+str(main_m),'10'),tags=['t1'])
        self.treeview.insert("",'end',iid='2',open=True,image=(self.bus),values=('2'))
        
        self.treeview.tag_configure('t1', background = 'gray77')
        
        self.treeview.place(x=0,y=150,height=2130,width=1100)
        
        
    
    	
    

        
        
  
root=Tk()
obj=App(root)
root.mainloop()


'''
a=18.463997
b=73.837617
url="https://www.google.com/search?q="+str(a)+"%2C"+str(b)+"&oq="+str(a)+"%2C"+str(b)+"&aqs=chrome..69i57.1013j0j4&client=ms-android-samsung-gj-rev1&sourceid=chrome-mobile&ie=UTF-8"

webbrowser.open(url)
'''