import datetime
#from datetime import timedelta
print("Basic time delta: "+str(datetime.timedelta(days=356,minutes=1,hours=5,seconds=0)))
x=datetime.datetime.now()
print("Today Date and Time: "+str(x))

z=x+datetime.timedelta(days=2*365)
a=x+datetime.timedelta(days=2,weeks=2)
b=x+datetime.timedelta(weeks=-3)
c=b.strftime("%B %d,%Y")
#christmas=datetime.datetime(2024, 12, 25)
#days=(christmas-x).days
print("2 year from now: "+str(z))
print("In 2 Weeks adn 3 days it will be: "+str(a))
print("Date 3 Weeks ago is : "+str(c))



christmas=datetime.datetime(x.year+1, 12, 25)
days=(christmas-x).days
if(days<0):
    christmas=datetime.datetime(x.year+2, 12, 25)
print("Christmas is in "+str(days)+" days")


