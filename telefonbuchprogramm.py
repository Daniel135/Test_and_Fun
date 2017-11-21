import json
import os
import re

class SearchNumbers:
    def __init__(self,fielname, encodingmethod):
        self.file_test = file_zero_test()
        self.f = open(fielname, 'r', encoding=encodingmethod)
        if self.file_test.is_non_zero_file(fielname):          
            self.telefonbuch = json.load(self.f)
            
        self.f.close()
        



    def searchNumber(self, values, searchFor):
        if values:

            for k in values:

                for v in k:

                    if searchFor in k[v]:
                        keys=["Mobil","Telefon"]
                        return [k.get(key) for key in keys]
        return ["Kein Eintrag Vorhanden",""]


    


class WriteNumbers:
    
        
    def writeJSON(self, fielname,encodingmethod, name, telefon, mobil):
        self.file_test = file_zero_test()
        f = open(fielname, 'r+', encoding=encodingmethod)
        input = ""
        if self.file_test.is_non_zero_file(fielname):

            numberstring = json.load(f)       
            input = json.dumps(numberstring)

            newstr = input.replace("[", "")

            input = newstr.replace("]", "")

            input = input + ","
            
        f.close()
        if self.file_test.is_non_zero_file(fielname):
            with open(fielname, "w", encoding=encodingmethod):
                pass   

        telefonbuch = open(fielname, 'w', encoding=encodingmethod)
        newPerson = {"Name" : name, "Telefon" : telefon, "Mobil" : mobil}
        newpersonstring = json.dumps(newPerson)
        newpersonstring = input + newpersonstring
        
        newpersonstring = "[" + newpersonstring + "]"

        my_dict = json.loads(newpersonstring)
        

        json.dump(my_dict, telefonbuch, ensure_ascii=False)
        telefonbuch.close()
        
class file_zero_test:
    def is_non_zero_file(self, fpath):  
        print(os.path.getsize(fpath))
        return os.path.isfile(fpath) and os.path.getsize(fpath) > 3
  
        
        
# writenumbers = WriteNumbers()


# writenumbers.writeJSON('telefonbuch.JSON','utf-8-sig', "Mathias", "Landau", "0821345", "01514864846")
# writenumbers.writeJSON('telefonbuch.JSON','utf-8-sig', "Doris", "Gerda", "0821737345", "01514898864846")
# writenumbers.writeJSON('telefonbuch.JSON','utf-8-sig', "Hans", "Zimmermann", "082137345", "016366514864846")





# searchnumbers =  SearchNumbers('telefonbuch.JSON','utf-8-sig') 
# print(searchnumbers.searchNumber(searchnumbers.telefonbuch, 'Mathias'))
# searchnumbers =  SearchNumbers('telefonbuch.JSON','utf-8-sig') 
# print(searchnumbers.searchNumber(searchnumbers.telefonbuch, 'Hans'))
