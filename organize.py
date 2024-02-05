



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
