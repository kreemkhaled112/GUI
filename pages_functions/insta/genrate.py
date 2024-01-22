from init import *
from insta.init import *
from insta.Edit import *
from insta.Maokt import *
from insta.Follow import *
from insta.Share import *
from insta.Chrome import *
from Data.Chrome import *

class Genrate(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.edit_Account = master
        self.primary_key = 1
        self.is_running = False

        self.edit_Account  = CTkFrame(master,width=740,height=650)
        self.edit_Account.place(x=155,y=45)
        #_____________________Variable_____________________#
        self.check_Edit_Photo = IntVar()
        self.check_Edit_Bio = IntVar()
        self.check_Add_Photo = IntVar()
        self.check_Edit_Professional = IntVar()
        self.check_Follow = IntVar()
        
        self.Email=CTkEntry(self.edit_Account,placeholder_text="Email",width=730)
        self.Email.place(x=2,y=10)
        self.Password=CTkEntry(self.edit_Account,placeholder_text="Password",width=730)
        self.Password.place(x=2,y=50)
        self.Cookie=CTkEntry(self.edit_Account,placeholder_text="Cookie",width=730)
        self.Cookie.place(x=2,y=90)

        fram_tree=CTkFrame(self.edit_Account,height=200,width=750)
        fram_tree.place(y=130)

        self.table_edit_Account = ttk.Treeview(fram_tree, columns=('1','2','3','4','5'),height=200,style="Custom.Treeview",show="headings",selectmode="browse")
        
        self.table_edit_Account.heading("1", text="ID",anchor="center")
        self.table_edit_Account.heading("2", text="UserName",anchor="center")
        self.table_edit_Account.heading("3", text="Email",anchor="center")
        self.table_edit_Account.heading("4", text="Password",anchor="center")
        self.table_edit_Account.heading("5", text="Cookie",anchor="center")
        
        self.table_edit_Account.column("1",  width=30, anchor="center")
        self.table_edit_Account.column("2", width=140,   anchor="center")
        self.table_edit_Account.column("3", width=110,  anchor="center")
        self.table_edit_Account.column("4",  width=150,  anchor="center")
        self.table_edit_Account.column("5",  width=320,  anchor="center")
        self.table_edit_Account.place(x=0,y=0)

        self.table_edit_Account.tag_bind("row","<Button-3>",lambda event : self.Menu_tabel(event,self.table_edit_Account))

        Edit_Photo = CTkCheckBox(self.edit_Account, text="Edit Photo",variable=self.check_Edit_Photo)
        Add_Photo = CTkCheckBox(self.edit_Account, text="Add Photo", variable=self.check_Add_Photo)
        Bio = CTkCheckBox(self.edit_Account, text="Bio", variable=self.check_Edit_Bio)
        Edit_Professional = CTkCheckBox(self.edit_Account, text="Switch Professional", variable=self.check_Edit_Professional)
        Follow = CTkCheckBox(self.edit_Account, text="Follow", variable=self.check_Follow)

        Edit_Photo.place(x=2,y=350)
        Add_Photo.place(x=100,y=350)
        Bio.place(x=200,y=350)
        Edit_Professional.place(x=250,y=350)
        Follow.place(x=400,y=350)

        self.check_Edit_Photo.set(1)
        self.check_Add_Photo.set(1)
        self.check_Edit_Bio.set(1)

        self.start = CTkButton(self.edit_Account, text="Start",width=100,height=40,command=lambda: Thread(target=self.Start).start())
        self.start.place(x=320,y=550)
        

    def Get(self):
        cursor.execute(f"SELECT * FROM account  ")
        ac = cursor.fetchall()
        for row in ac :
            if row[6] == 'pending' :
                self.Email.insert(0,row[1])
                self.Password.insert(0,'pastaaa6000')
                self.Cookie.insert(0,row[4])
                self.pas = row[2]
                break


    def switch(self):
        self.c = Chrom_Insta()
        switch = self.c.switch(self.Email.get(),self.Password.get(),self.Cookie.get(),self.pas)
        if switch is not None:
            Username , Cookie = switch
            if Cookie is None:
                cursor.execute(f"UPDATE account SET insta = 'ban' WHERE email = '{self.Email.get()}' ")
                conn.commit()
                self.c.bot.quit()
                print(Colorate.Diagonal(Colors.red_to_blue, f'[ BAN ] : [ {self.Email.get()}:{self.pas} ]', 1))
            else:
                self.table_edit_Account.insert('', 'end',  values=( self.primary_key, Username , self.Email.get(), self.Password.get(),  Cookie ),tags=('row'))
        self.Email.delete(0, "end")
        self.Password.delete(0, "end")
        self.Cookie.delete(0, "end")
        self.primary_key += 1
        
    def Start(self):
        if self.is_running == False :
            self.start.configure(text="Stop")
            self.start.configure(fg_color='#9b111e')
            self.start.configure(hover_color='#9b111e')
            self.is_running = True
        elif self.is_running :
            self.start.configure(text="Start")
            self.start.configure(fg_color='#1f538d')
            self.is_running = False
        while self.is_running:
            self.Get()
            self.switch()
            try:
                items = self.table_edit_Account.get_children()
                for item in items:
                    values = self.table_edit_Account.item(item, 'values')
                    cookie = values[4]
                    if self.check_Edit_Photo.get() == 1 :
                        photo = f"E:\\New folder (5)\\Face\\Facebook Api\\Creat\\instaphoto\\{random.randrange(1,8)}.jpg"
                        phote = self.c.Edit_Photo(photo)
                        if phote == 'Ban' :
                            break
                    if self.check_Add_Photo.get() == 1 :
                        photo = f"E:\\New folder (5)\\Face\\Facebook Api\\Creat\cover\\{random.randrange(1,382)}.jpg"
                        self.c.AddPhoto(photo)
                    if self.check_Edit_Bio.get() == 1 :
                        random_bio = cursor.execute('SELECT bio FROM bio ORDER BY RANDOM() LIMIT 1').fetchone()
                        self.c.Edit_Bio(random_bio[0])
                    if self.check_Edit_Professional.get() == 1 :
                        type = self.c.profrssional()
                        if type == 'good':type = 'pro'
                        else:type = 'normal'    
                    else:
                        type = 'normal' 
                    if self.check_Follow.get() == 1 :
                        id = ["kreem.khaled112"]
                        for row in id:
                            Follow_insta(row,cookie)
                    cursor.execute(f"SELECT email FROM insta WHERE email = '{values[3]}' ")
                    existing_id = cursor.fetchone()
                    if not existing_id :
                        try:
                            cursor.execute('INSERT INTO insta (username , email, password, cookies, type) VALUES (  ?, ?, ?, ?, ?)', (   values[1], values[2], values[3], values[4], type))
                            cursor.execute(f"UPDATE account SET insta = 'good' WHERE email = '{values[2]}' ")
                            conn.commit()
                            print(Colorate.Diagonal(Colors.green_to_blue, f'[ Done Add Account ] : [ {values[2]}:{values[3]} ]', 1))
                            self.table_edit_Account.delete(item)
                        except:print(f"Faild Contect Database ")
                    else:
                        pass
            except:
                pass
        
        
    def Menu_tabel(self,event,treeview):
        self.treeview = treeview
        row_id = treeview.identify_row(event.y)
        treeview.selection_set(row_id)
        row_values = treeview.item(row_id)['values']
        popMenu = Menu(self.treeview,tearoff=0 , font=("verdana",8)) 
        popMenu.add_command(label="Edit/Update",accelerator="Ctrl+E",command= lambda : self.Edit(row_values))
        popMenu.add_command(label="Delete",accelerator="Delete",command= lambda : self.treeview.delete(row_id))
        popMenu.add_command(label="View",accelerator="Ctrl+V",command= lambda : Thread(target=Chrom_Insta().View(row_values[4])).start())
        popMenu.post(event.x_root,event.y_root)
    def Edit(self,row_values):
        self.Email.insert(0, row_values[2]) 
        self.Password.insert(0, row_values[3]) 
        self.Cookie.insert(0, row_values[4])