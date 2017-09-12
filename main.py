from math import cos
from math import sin
from math import acos
from math import degrees
import ttk
import Tkinter as tk



def to_radian(n):
    return n*(3.14/180)
def days_calculate(m,d,l):
    dict={"Jan":0,"Feb":31,"March":59,"April":90,"May":120,"June":151,"July":181,"Aug":212,"Sept":243,
          "Oct":273,"Nov":304,"Dec":334}


    days=dict[m]+int(d)
    if(l=="Yes" and m!="Jan" and m!="Feb"):
        days+=1
    return days

def convert_to_hour_decimal(n):
    hrs=float(int(n/60))
    mins=(n%60)/60
    converted=hrs+mins
    return converted
def mins_to_hours(n):
   hrs=float(int(n/60))
   print(hrs)
   mins=((n-hrs*60))/100
   print(mins)
   converted=hrs+mins
   return converted
def hrs_to_mins(n):
    hr=int(n)*60
    mins=(n%(float(int(n))))*100
    converted=hr+mins
    print("hrs",converted)
    return converted




def calculate(l_st_enter,std_time_enter,l_loc_lat_enter,l_loc_lon_enter,l_local_time_enter,slope_enter,incline_enter,var,var2,var3):
    print("in")
    try:
        st_longitude=float(l_st_enter.get())
        stdtime=float(std_time_enter.get())
        local_latitide=float(l_loc_lat_enter.get())
        local_longitude=float(l_loc_lon_enter.get())
        local_time=float(l_local_time_enter.get())
        sl=float(slope_enter.get())
        inc=float(incline_enter.get())
        month=var.get()
        day=var2.get()
        leap=var3.get()



        n=days_calculate(month,day,leap)


        st_longitude=float(int(st_longitude))+(float(st_longitude)-float(int(st_longitude)))/0.6                #degree and minutes to decimal
        local_latitide=float(int(local_latitide)) + (float(local_latitide) - float(int(local_latitide)))/0.6
        local_longitude=float(int(local_longitude)) + (float(local_longitude) - float(int(local_longitude)))/0.6


        B=(360.0/364.0)*(n-81)
        B_to_radian=to_radian(B)     #degree to radian
        E=9.87*sin(2*B_to_radian)-7.53*cos(B_to_radian)-1.5*sin(B_to_radian)
        print(E)

        solar_time= hrs_to_mins(stdtime) -4*(st_longitude -local_longitude)+E
        print(solar_time)
        value=(360.0*(284.0+n)/365.0)*(3.14/180.0)
        delta=23.45*sin(value)

        degree=15
        if(solar_time>720):
            degree=-degree

        hour_angle=convert_to_hour_decimal(hrs_to_mins(12.00)-solar_time)*degree

        deltar=to_radian(delta)
        local_latitider=to_radian(local_latitide)
        slr=to_radian(sl)
        incr=to_radian(inc)
        hour_angler=to_radian(hour_angle)

        incidence_do=(sin(deltar)*sin(local_latitider)*cos(slr)) - (sin(deltar)*cos(local_latitider)*sin(slr)*cos(incr)) \
                  + (cos(deltar)*cos(local_latitider)*cos(slr)*cos(hour_angler))  \
                  + (cos(deltar)*sin(local_latitider)*sin(slr)*cos(incr)*cos(hour_angler)) \
                  + (cos(deltar)*sin(slr)*sin(incr)*sin(hour_angler))
        incidence=degrees(acos(incidence_do))
        print(str(mins_to_hours(solar_time)))
        format_solartime=str(mins_to_hours(solar_time))[0:2]+":"+str(mins_to_hours(solar_time))[3:5]+":"+str(mins_to_hours(solar_time))[5:7]
        v1.set(str(n))
        v2.set(format_solartime)
        v3.set(str(delta)[0:7])
        v4.set(str(hour_angle)[0:7])
        v5.set(str(incidence)[0:5])

        main.update()

    except ValueError:
        v1.set("Error")
        v2.set("Error")
        v3.set("Error")
        v4.set("Error")
        v5.set("Error")






main=tk.Tk()
v1=tk.StringVar()
v2=tk.StringVar()
v3=tk.StringVar()
v4=tk.StringVar()
v5=tk.StringVar()
v6=tk.StringVar()
main.geometry('400x450')
main.title("Beam Radiation Calculator")
title=tk.Label(main,text="Beam Radiation Calculator")
title.config(font=('courier',15))
title.place(x=50,y=5)
l_st=tk.Label(main,text="Standard Longitude(deg.mins):")
l_st.config(font=('courier',10))
l_st.place(x=50,y=50)

l_st_enter=tk.Entry(main,width=8)
l_st_enter.insert(tk.END,0)
l_st_enter.place(x=285,y=50)

std_time=tk.Label(main,text="Standard Time (hour.minutes):")
std_time.config(font=('courier',10))
std_time.place(x=50,y=80)

std_time_enter=tk.Entry(main,width=8)
std_time_enter.insert(tk.END,0)
std_time_enter.place(x=285,y=80)

frame1=tk.Frame(main,width=330,height=105,relief="ridge",bd=2)   #sunken,groove,ridge,solid,flat,raised
frame1.place(x=40,y=110)

l_loc_lat=tk.Label(main,text="Local Latitude(deg.mins):")
l_loc_lat.config(font=('courier',10))
l_loc_lat.place(x=50,y=120)

l_loc_lat_enter=tk.Entry(main,width=8)
l_loc_lat_enter.insert(tk.END,0)
l_loc_lat_enter.place(x=285,y=120)

l_loc_lon=tk.Label(main,text="Local Longitude(deg.mins):")
l_loc_lon.config(font=('courier',10))
l_loc_lon.place(x=50,y=150)

l_loc_lon_enter=tk.Entry(main,width=8)
l_loc_lon_enter.insert(tk.END,0)
l_loc_lon_enter.place(x=285,y=150)

l_local_time=tk.Label(main,text="Local Time (hour.minute):")
l_local_time.config(font=('courier',10))
l_local_time.place(x=50,y=180)

l_local_time_enter=tk.Entry(main,width=8)
l_local_time_enter.insert(tk.END,0)
l_local_time_enter.place(x=285,y=180)

slope=tk.Label(main,text="Slope (degrees):")
slope.config(font=('courier',10))
slope.place(x=50,y=220)

slope_enter=tk.Entry(main,width=8)
slope_enter.insert(tk.END,0)
slope_enter.place(x=285,y=220)

incline=tk.Label(main,text="Inclination (degrees):")
incline.config(font=('courier',10))
incline.place(x=50,y=250)

incline_enter=tk.Entry(main,width=8)
incline_enter.insert(tk.END,0)
incline_enter.place(x=285,y=250)

frame1=tk.Frame(main,width=330,height=40,relief="ridge",bd=2)   #sunken,groove,ridge,solid,flat,raised
frame1.place(x=40,y=280)

var=tk.StringVar(main)
var.set("Jan")                 #default value
option=ttk.Combobox(main,textvariable=var,values=["Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec"])
option.config(font=('courier',10),width=6,height=12)
option.place(x=50,y=288)

values=range(1,32)
var2=tk.StringVar(main)
var2.set(1)                 #default value
option=ttk.Combobox(main,textvariable=var2,values=values)
option.config(font=('courier',10),width=5,height=15)
option.place(x=150,y=288)

leap=tk.Label(main,text="Leap Year")
leap.config(font=('courier',10))
leap.place(x=220,y=287)

var3=tk.StringVar(main)
var3.set("No")
option=ttk.Combobox(main,textvariable=var3,values=["Yes","No"])
option.config(font=('courier',10),width=5,height=1)
option.place(x=303,y=287)

label1=tk.Label(main,text="Days",bd=3,relief='ridge',width=10)
label1.place(x=45,y=330)
label2=tk.Label(main,textvariable=v1,bd=3,relief='ridge',width=10)
label2.place(x=45,y=350)

label3=tk.Label(main,text="Solar Time",bd=3,relief='ridge',width=10)
label3.place(x=125,y=330)
label4=tk.Label(main,textvariable=v2,bd=3,relief='ridge',width=10)
label4.place(x=125,y=350)

label5=tk.Label(main,text="Delta",bd=3,relief='ridge',width=10)
label5.place(x=205,y=330)
label6=tk.Label(main,textvariable=v3,bd=3,relief='ridge',width=10)
label6.place(x=205,y=350)

label7=tk.Label(main,text="Hour Angle",bd=3,relief='ridge',width=10)
label7.place(x=285,y=330)
label8=tk.Label(main,textvariable=v4,bd=3,relief='ridge',width=10)
label8.place(x=285,y=350)

label7=tk.Label(main,text="Angle Of Incidence",bd=3,relief='ridge',width=20)
label7.place(x=80,y=390)
label8=tk.Label(main,textvariable=v5,bd=3,relief='ridge',width=20)
label8.place(x=80,y=410)


button=tk.Button(main,text="Calculate",width=10,height=2,relief='raised',command=lambda :calculate(l_st_enter,std_time_enter,l_loc_lat_enter,l_loc_lon_enter,l_local_time_enter,slope_enter,incline_enter,var,var2,var3))
button.place(x=280,y=390)

tk.mainloop()

