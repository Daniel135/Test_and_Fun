from tkinter import *
from tkinter import filedialog
from telefonbuchprogramm import *
import ntpath


class App:
    def __init__(self, master):
        self.file_path = 'telefonbuch.JSON'
        frame = Frame(master)
        frame.pack()
        self.numbersearch = SearchNumbers(self.file_path, 'utf-8-sig')
        master.geometry("350x250+50+50") 
        master.title("Telefonbuch")

        
        self.labelName = Label(frame, text = "Name: ")
        self.labelName.grid(row = 1,column = 1)
        self.labelMobil = Label(frame, text = "")
        self.labelMobil.grid(row = 2,column = 2)
        self.labelTelefon = Label(frame, text = "")
        self.labelTelefon.grid(row = 3,column = 2)
        self.labelMobilLabel = Label(frame, text = "Handy: ")
        self.labelMobilLabel.grid(row = 2,column = 1)
        self.labelTelefonLabel = Label(frame, text = "Telefon: ")
        self.labelTelefonLabel.grid(row = 3,column = 1)

        self.name_text = StringVar()
        self.entry = Entry(frame, textvariable = self.name_text)
        self.entry.grid(row = 1, column = 2)

        self.searchbutton = Button(frame, text = "Suchen", command = self.get_number)
        self.searchbutton.grid(row = 1, column = 3)
        self.filebutton = Button(frame, text = "Datei waehlen", command = self.get_file)
        self.filebutton.grid(row = 5, column = 1)
        self.labelPath = Label(frame, relief=RIDGE, text = "telefonbuch.JSON")
        self.labelPath.grid(row = 5,column = 2)
        
        self.labelNew = Label(frame, text = "Neuen Eintrag erstellen", relief=RIDGE)
        self.labelNew.grid(row = 6,column = 2)
        

        self.labelNamenew = Label(frame, text = "Name: ")
        self.labelNamenew.grid(row = 7,column = 1)
        self.labelMobilnew = Label(frame, text = "Handy: ")
        self.labelMobilnew.grid(row = 8,column = 1)
        self.labelTelefonnew = Label(frame, text = "Telefon: ")
        self.labelTelefonnew.grid(row = 9,column = 1)
        self.name_entry = StringVar()
        self.entry = Entry(frame, textvariable = self.name_entry)
        self.entry.grid(row = 7, column = 2)
        self.mobil_entry = StringVar()
        self.entry = Entry(frame, textvariable = self.mobil_entry)
        self.entry.grid(row = 8, column = 2)
        self.telefon_entry = StringVar()
        self.entry = Entry(frame, textvariable = self.telefon_entry)
        self.entry.grid(row = 9, column = 2)

        self.newbutton = Button(frame, text = "Hinzufügen", command = self.get_newPerson)
        self.newbutton.grid(row = 9, column = 3)
        
    def get_newPerson(self):
        writenumbers = WriteNumbers()
        writenumbers.writeJSON(self.file_path ,'utf-8-sig', self.name_entry.get(),
                                self.telefon_entry.get(), self.mobil_entry.get())
        
        
        
    def get_file(self):
    
        self.file_path = filedialog.askopenfilename()
        head, tail = ntpath.split(self.file_path)       
        
        self.labelPath.config(text=(tail or ntpath.basename(head)))
        self.numbersearch = SearchNumbers(self.file_path, 'utf-8-sig')
        return
    
    
    
    
    def get_number(self):
        
        name_string = self.name_text.get()
        name_string = name_string.replace(" ", "")
        if not name_string:
            return
        print(name_string)
        numbers = self.numbersearch.searchNumber(self.numbersearch.telefonbuch, name_string)
        
        self.labelMobil.config(text=numbers[0])
        
        self.labelTelefon.config(text=numbers[1])
        return
        
                                    

root = Tk()
app = App(root)
root.mainloop()