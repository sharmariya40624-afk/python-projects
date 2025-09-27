from tkinter import*
import tkinter as ttk
import random

class chatbot:
    def __init__(self,root):
       self.root = root
       self.lbl_msg=Label(self.root,text="Status:Ready",fg='black')
       self.root.geometry('700x600+250+10')
       self.root.title('My ChatGPT')
       self.root.bind('<Return>',self.ent_func)
       
       #========Title==============
       self.lbl_title = Label(self.root,text = 'ChatGPT Developed by Riya', font=('times new roman',20,'bold'))
       self.lbl_title.place(x=130,y=10)

       #========main Frame with scroll bar and text area============
       main_frame = Frame(self.root,bd=2,relief=RAISED,bg='green')
       main_frame.place(x=0,y=60,width=700,height=400)

       #==========Text area with scrollbar===
       self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
       self.text = Text(main_frame, width=65, height=20, font=('arial', 14), relief=RAISED, yscrollcommand=self.scroll_y.set)
       self.scroll_y.pack(side=RIGHT, fill=Y)
       self.text.pack()


       #=============search label ========
       lbl_search = Label(self.root,text='Search Here',font=('times new roman',20,'bold'))
       lbl_search.place(x=20,y=470)

       #============Entry area=========
       self.ent = StringVar()
       self.entry=ttk.Entry(self.root,textvariable=self.ent,font=('times new roman',15,'bold'))
       self.entry.place(x=200,y=470,width=400,height=35)

       #======btn save
       self.btn_send = ttk.Button(self.root,command=self.send,width=20,text='Send',font=('times new roman',14,'bold'), bg='black', fg='white')
       self.btn_send.place(x=200,y=520,width=200,height=30)
       
       #===btn clr
       self.btn_clr = ttk.Button(self.root,command=self.clear,width=20,text='Clear', font=('times new roman',14,'bold'), bg='black', fg='white')
       self.btn_clr.place(x=410,y=520,width=200,height=30)


#==================Functions starts=============\
    def ent_func(self,event):
       self.btn_send.invoke()
       self.ent.set("")

    def clear(self):
       self.text.delete('1.0',END)
       self.ent.set("")

    def send(self):
       user_input = "\t\t\t"+ "You: "+ self.entry.get()
       self.text.insert(END,"\n"+user_input)

       if(self.entry.get()==""):
          self.msg="Please type something"
          self.lbl_msg.config(text=self.msg,fg='black')
          print(self.lbl_msg)
       else:
          self.msg = ""
          self.lbl_msg.config(text=self.msg,fg='black')  
    
       input_list = ['hey','how are you?','i am fine','wassup']
       output_list = ['hello','great! What about you?', 'nice! keep going.','nice to meet you']
       for mess in input_list:
          if self.entry.get() == mess:
             mess_into_text = random.choice(output_list)
             self.text.insert(END,'\n\n'+'Bot :'+ mess_into_text)

       data_science = "data science is a growing field nowadays. It has many \n""application in daily life. It has the following branch \n1: Machine Learning\n2: Deep Learning \n3: Artificial Intelligence "
       if self.entry.get()=="what is data science?" or self.entry.get()=="tell me about data science":
          self.text.insert(END,'\n\n'+ data_science)

       google = "Google is a big tech company throughout the world.\nChrome is the leading app of Google."
       if self.entry.get()== "Google" or self.entry.get()== "tell me about google":
          self.text.insert(END,'\n\n'+ google)

       richest_person = "Top 3 Richest person in the world are, \n 1 Elon Musk \n 2 Larry Ellison \n 3 Bill Gates \n"
       if self.entry.get() == "richest  person" or self.entry.get() == "top richest person":
          self.text.insert(END,'\n\n'+'Bot :'+ richest_person)
         
       if(self.entry.get()==""):
          self.msg="Please type something"
          self.lbl_msg.config(text=self.msg,fg='black')
          print(self.lbl_msg)
       else:
          self.msg = ""
          self.lbl_msg.config(text=self.msg,fg='black')

#====================================
if __name__ == "__main__":
   root = Tk()
   obj = chatbot(root)
   root.mainloop()