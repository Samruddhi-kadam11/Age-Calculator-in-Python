def Agecalculate(y,m,d):
    import datetime
    today=datetime.datetime.now().date()
    dob=datetime.date(y,m,d)
    age=int((today-dob).days/365)
    print(age)
Agecalculate(2000,10,11)
