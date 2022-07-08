import datetime
import time
begin = datetime.date(2014,6,1)
end = datetime.date(2014,6,7)
d = begin
delta = datetime.timedelta(days=1)
while d <= end:
    print(d.strftime("%Y-%m-%d"))
    d += delta
    time.sleep(10)