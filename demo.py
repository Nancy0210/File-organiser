import os
import shutil
from tkinter import *
from threading import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog
import subprocess
import signup



#Modifications can be performed here
# You can add more extensions to this dictionary

Extensions={
   'Documents' : ('.pdf','.doc','.xls','txt','.csv','.zip',\
    '.xml','.zip', '.docx', '.DOCX', '.odt','.log','.rtf'),
   'Pictures' : ('.jpg','.jpeg','.png','.JPG'),
   'Videos' : ('.mp4','.mkv','.3gp','.flv','.mpeg'),
   'Music' : ('.mp3','.wav','.m4a','.webm'),
   'Programs' : ('.py','.cpp','.c','.sh','.js'),
   'Apps' : ('.exe','.apk'),
}


class File_Organizer:
    def __init__(self,root):
        #setting the tkinter main window
        self.window=root
        self.window.geometry("720x600")
        self.window.title("File Organizer ")
        self.window.resizable(False , False)
        self.window.configure(bg='white')
        self.window.wm_attributes("-transparentcolor" , "grey90")
        
        

        self.Selected_Dir=''
        self.Browsed=True

        #Frame 1: For the logo
        self.frame_1=Frame(self.window , bg="white",\
                           width=720, height=120 )
        self.frame_1.place(anchor='center',x=0 ,y=0)
        self.frame_1.pack()
        #opening the logo image
        image=Image.open('Images/final_logo.png')
        #resizing the image
        resized_img=image.resize((720,120))
        #create an obj of tkinter imageTk
        self.img_1= ImageTk.PhotoImage(resized_img)
        #create a lebel widget to display the text or img
        label = Label(self.frame_1, image=self.img_1 , borderwidth=0, relief="raised")
        label.pack()

      

        #Frame 2:for the menus
        self.frame_3=Frame(self.window , width=720, height=50 ,bg="#A033FF" , highlightbackground= "#{:02x}{:02x}{:02x}".format(160,51,255), highlightthickness=2)
        self.frame_3.place(x=0, y=120)
        self.frame_3.pack()

        #canvas in frame 3
        self.canvas= Canvas(self.frame_3 , width=715, height=40 , background="#A033FF" , bd=2 )
        self.canvas.pack()

        #start and end color
        start_color=(160, 51, 255)
        end_color=(213, 128, 255)

        #creating loop for making the gradient
        gradient=[]
        for i in range(256):
            r = int(start_color[0] + (i / 255.0) * (end_color[0] - start_color[0]))
            g = int(start_color[1] + (i / 255.0) * (end_color[1] - start_color[1]))
            b = int(start_color[2] + (i / 255.0) * (end_color[2] - start_color[2]))
            color = "#{:02x}{:02x}{:02x}".format(r, g, b)
            gradient.append(color)

        x0, y0, x1, y1 = 0, 0, 715 , 50
        #self.canvas.create_rectangle(x0,y0,x1,y1 , outline="#{:02x}{:02x}{:02x}".format(160,51,255) , width=2)
        for i in range(256):
            self.canvas.create_rectangle(x0, i*1.5625, x1, (i+1)*1.5625, fill=gradient[i], outline="")


        #opening the backgoung image for main frame out of the function for organise window
        #opening the logo image
        img=Image.open('Images/login_page(1).jpg')
        #resizing the image
        re_img=img.resize((720,480))
        #create an obj of tkinter imageTk
        self.img_2= ImageTk.PhotoImage(re_img)
    

        #About button
        About_btn=Button(self.window , text="About" ,\
                         font= ('Roboto' , 12, 'bold' ) ,bg="#8800cc",\
                         fg="black" , width=6 ,height=2 , command =self.About_Window , relief="raised")
        About_btn.place(x=555 , y=120)

        #logout button
        Logout_Button=Button (self.window , text ="Logout" , \
                              font=("Roboto", 12, 'bold'), bg="#8800cc" ,\
                              fg="black" , width = 6 , height =2, command=self.Logout , relief="raised")
        Logout_Button.place(x=630 , y=120)

        #Organize button
        Org_button=Button(self.window , text="Organize",\
                          font =("Roboto" , 12 , "bold") , bg="#8800cc" ,\
                          fg='black' , width=7 , height =2 , command=self.Org_Page , relief="raised")
        Org_button.place(x=20 , y=120)

        # Frame 2: For the main Page Widgets
        self.frame_2 = Frame(self.window, 
                             width=720,height=580 , bg="white")
        self.frame_2.place(x=0, y=200)
        self.frame_2.pack()

        

        # Calling the function to display main page as default
        # widgets
        self.Org_Page()
        

    

    #logout function
    def Logout(self):
        answer =messagebox.askyesno("Logout" , "Are you sure you want to logout")
        if answer:
            self.window.destroy()
            subprocess.call(['python' , 'signup.py'] , creationflags=subprocess.CREATE_NO_WINDOW)
        else:
            messagebox.showinfo("Cancelled" , "You pressed cancel")

    # This function displays all the widgets in the 'self.frame_2'
    # related to File Organizing Operation
    def Org_Page(self):
        
        # Heading Label
        Heading_Label = Label(self.frame_2, text="Please Select the Folder", \
        font=("Roboto", 20, 'bold')  , bg="white")
        Heading_Label.place(x=160, y=20)

        # Button for selecting the directory(where
        # the desired files are presented)
        Folder_Button = Button(self.frame_2, text="Select Folder", \
        font=("Roboto", 10, 'bold'), bg="#A500FF", width=15, \
        command=self.Select_Directory)
        Folder_Button.place(x=110, y=80)

        # The directory path selected from the Tkinter file dialog 
        # that opens by the 'Folder_Button' is displayed here.
        self.Folder_Entry = Entry(self.frame_2, \
        font=("Helvetica", 12), width=32 , bg="grey70")
        self.Folder_Entry.place(x=256, y=82)

        Status = Label(self.frame_2, text="Status: ", \
        font=("Roboto", 12, 'bold'), bg='white')
        Status.place(x=180, y=130)

        # Status Label:
        # Options: 'Not Started Yet(By Default), or 'Processing...',
        # or 'Complete!''
        self.Status_Label = Label(self.frame_2, text="Not Started Yet", \
        font=("Roboto", 12), bg="white", fg="red")
        self.Status_Label.place(x=256, y=130)

        # Start Button: Users have to press this button
        # to start the operation
        Start_Button = Button(self.frame_2, text="Start", \
        font=("Roboto", 13, 'bold'), bg="#A000FF", fg="black", \
        width=8, command=self.Organizer)
        Start_Button.place(x=280, y=180)

    # This function opens the Tkinter file dialog to
    # let users select the directory where the files are presented
    def Select_Directory(self):
        self.Selected_Dir = filedialog.askdirectory(title = \
        "Select a location")
        # Insert the folder path to the Entry Box
        self.Folder_Entry.insert(0, self.Selected_Dir)

        # Converting the type of 'self.Selected_Dir' variable
        # to String for avoiding any error while checking
        # the path exists or not
        self.Selected_Dir = str(self.Selected_Dir)

        # Checks if the folder path is exists or not
        if os.path.exists(self.Selected_Dir):
            self.Browsed = True

    # Creating a different thread to run the 'self.Organizer' function
    def Threading(self):
        # Killing a thread through "daemon=True" isn't a good idea
        self.x = Thread(target=self.Organizer, daemon=True)
        self.x.start()
    
    # The Organizer function 
    def Organizer(self):
        # If no directory is chosen
        if not self.Browsed:
            messagebox.showwarning('No folders are choosen', \
            'Please Select a Folder First')
            return
        try:
            # Showing the current status of the operation
            self.Status_Label.config(text='Processing...')

            self.Current_Path = self.Selected_Dir
 
            if os.path.exists(self.Current_Path):
            # self.Folder_List1: stores all the folders that 
            # are already presented in the selected directory
                self.Folder_List1 = []
                # self.Folder_List2 stores newly created folders
                self.Folder_List2 = []
                self.Flag = False
 
                for folder, extensions in Extensions.items():
                    self.folder_name = folder
                    self.folder_path = os.path.join(self.Current_Path, self.folder_name)
 
                    # Change the directory to the current 
                    # folder path that we've selected
                    os.chdir(self.Current_Path)
 
                    # If the folder is already present in that directory
                    if os.path.exists(self.folder_name):
                        self.Folder_List1.append(self.folder_name)
                   # If the folder is not present in that directory,
                   # then create a new folder
                    else:
                        self.Folder_List2.append(self.folder_name)
                        os.mkdir(self.folder_path)
                    
                    # Calling the 'File_Finder()' function to
                    # find a specific type of file(extension)
                    # and change their old path to new path(for separation)
                    for item in self.File_Finder(self.Current_Path, extensions):
                        self.Old_File_Path = os.path.join(self.Current_Path,item)
                        self.New_File_Path = os.path.join(self.folder_path,item)
 
                        # Moving each file to their new location(folder)
                        shutil.move(self.Old_File_Path, self.New_File_Path)
                        # Making the 'self.Frag' variable True
                        self.Flag = True
            else:
                messagebox.showerror('Error!','Please Enter a Valid Path!')
 
            # Checking files are separated or not
            # If Flag is True: It means the program had found
            # some matching files and those have been organized
            if self.Flag:
                self.Status_Label.config(text='Complete!')
                messagebox.showinfo('Done!', 'Complete!')
                self.Clear()
            # If Flag is False: It means the program didn't find
            # any matching files there; only folders are created
            if not self.Flag:
                self.Status_Label.config(text='Complete!')
                messagebox.showinfo('Done!', \
                'Folders have been created\nNo Files were there to move')
                self.Clear()
        # If any error occurs
        except Exception as es:
            messagebox.showerror("Error!",f"Error due to {str(es)}")

    # This function finds a specific file-type in
    # the selected directory, appends the matched file path
    # to a list, and returns that list
    def File_Finder(self,folder_path, file_extensions):
        self.files = []
        for file in os.listdir(folder_path):
            for extension in file_extensions:
                if file.endswith(extension):
                    self.files.append(file)
        return self.files

    def Clear(self):
        self.Status_Label.config(text='Not Started Yet')
        self.Folder_Entry.delete(0, END)
        self.Selected_Dir = ''

     # When the 'About' button is pressed, this function gets a call   
    def About_Window(self):
        messagebox.showinfo("Clutter",\
        "Application for organizing for messy folders . Developed jointly by Nancy , Ekta Pugalia and Monika Charan")
    
    # This function closes the main window
    def Exit_Window(self):
        self.window.destroy()

# The main function
if __name__ == "__main__":
    root = Tk()
    # Creating a 'File_Renamer' class object
    obj = File_Organizer(root)
    root.mainloop()


            
