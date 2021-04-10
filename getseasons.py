import datetime
dt = datetime.datetime.today()
if (dt.month >=4 and dt.month <=6):
    print("summer")
elif (dt.month >=7 and dt.month <=9):
    print("rainy")
elif (dt.month >=10 and dt.month <=12 and dt.month == 1):
    print("winter")
elif (dt.month >=2 and dt.month <=3):
    print("springs")
          
    #summer april-june
    #rainy july-september
    #winter october-january
    #springs february-march
