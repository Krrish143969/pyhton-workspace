class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def arrange_value(self):                #instance method
        date = str(self.day) + '-' + str(self.month) + '-' + str( self.year)
        return date
    
    @classmethod
    def getdatafromstring(clr,string):
        import re
        data = re.findall('\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}',string)[0]
        list_date = data.replace('/','-').split('-')
        date = list_date[0]
        month = list_date[1]
        year = list_date[2]
        return clr(date,month,year)
    
    
   
d1 =    Date(2022,6,17)

d2 = Date.getdatafromstring('today date is 17-06-2022')
print(d2.__dict__)


