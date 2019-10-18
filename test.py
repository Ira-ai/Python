import math as m
R=6371
a=6378137.0
b=6356752.3142 
f=(a-b)/a
e=m.sqrt(2*f-f**2)

class Gis():
    def __init__(self, *coord):
        if (isinstance(coord[0], pointDegree) and isinstance(coord[1], pointHours)):
            self.fi=coord[0]
            self.lymda=coord[1]
        else:
            self.x0=coord[0]
            self.y0=coord[1]
            
    def Merc(self):

        fi = self.fi.fromDegreeToRadian()
        lymda=self.lymda.fromDegreeToRadian()
        
        x=a*lymda
        y=a*m.log(m.tan(m.pi/4+fi/2)*((1-e*m.sin(fi))/(1+e*m.sin(fi)))**(e/2))
        
        return x, y
    
    def Obrat(self):

       # print(x0, y0)

        self.lymda=pointHours((self.x0/a)*180/m.pi) #пересчет долготы

        ts=m.exp(-self.y0/a)
        self.fi=m.pi/2-2*m.atan(ts)
        i=0
        phi=1
        while(self.fi<0.00000000000001):
            con=e*m.sin(self.fi)
            phi=m.pi/2-2*m.atan(ts*((1-con)/(1+con))**e)-self.fi
            self.fi=self.fi+phi
            break
        self.fi=pointDegree(self.fi*180/m.pi)
        
    def distance(self, other):
        
        fi1 = self.fi.fromDegreeToRadian()
        lymda1=self.lymda.fromDegreeToRadian()

        fi2 = other.fi.fromDegreeToRadian()
        lymda2=other.lymda.fromDegreeToRadian()

        o=m.sin(fi1)*m.sin(fi2)+m.cos(fi1)*m.cos(fi2)*m.cos(lymda1-lymda2)
        d=m.acos(o)
        L=d*R
        return L

    def __str__(self):
        return "{0}, {1}".format(self.fi, self.lymda)
     
class pointDegree():
    def __init__(self, *coord):
        print(coord)
        if (len(coord)==3):
            self.fi=coord[0]/1+coord[1]/60+coord[2]/3600   
        else:
            self.fi=coord[0]   
            
    def fromDegreeToRadian(self):
        return self.fi*m.pi/180   

    def fromRadianToDegree(self):
        return self.fi/m.pi*180

    def __str__(self):
        gr=int(self.fi)
        mi=int((self.fi-gr)*60)
        se=((self.fi-gr)*60-mi)*60
        return str("Широта: "+str(gr)+"гр "+ str(mi)+"мин "+ str(se)+"сек" )
           
class pointHours():
    def __init__(self, *coord):
        print(coord)
        if (len(coord)==3):
            self.lymda=(coord[0]/1+coord[1]/60+coord[2]/3600)*15
        else:
            self.lymda=coord[0]*15

    def fromDegreeToRadian(self):
        return self.lymda/180*m.pi   

    def fromRadianToDegree(self):
        return self.lymda/m.pi*180
    
    def __str__(self):
        gr1=int(self.lymda)
        mi1=int((self.lymda-gr1)*60)
        se1=((self.lymda-gr1)*60-mi1)*60
        return str("Долгота: "+str(gr1)+"h "+ str(mi1)+"мин "+ str(se1)+"сек" )
    
