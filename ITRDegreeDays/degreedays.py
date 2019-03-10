import math
class DegreeDays(object):
    def __init__(self,TU,TL,tMax,tMin):  
        self.TU=TU
        self.TL=TL
        self.tMax=tMax
        self.tMin=tMin

    def __str__(self):
        return "Degree days: "+str(self.define_case())

    def  define_case(self): #Need to fix
        if self.tMax>=self.tMin:
            if self.tMin>self.TU:
                return self.case_5()
            if self.TL>self.tMax and self.tMin<self.TL:
                return self.case_1()
            if self.TL>self.tMin and self.TU>self.tMax:
                return self.case_2()
            if self.TU>self.tMax and self.TL<self.tMin:
                return self.case_3()
            if self.TU<self.tMax and self.tMin>self.TL:
                return self.case_4()
            if self.TL>self.tMin and self.tMax>self.TU:
                return self.case_6()
        else:
            return "Check temp values\nVerifica los valores de la temperatura"         
    def case_1(self):   #works fine
        return 0

    def case_2(self):   #Need to fix
        angle=self.angle_1(self.TL)
        return (1/math.pi)*((self.case_3()-self.TL)*(math.pi/2-angle)+self.theta()*math.cos(angle))

    def case_3(self): #Works fine
        return  (self.tMax+self.tMin)/2

    def case_4(self): #Works fine
        angle=self.angle_1(self.TU)
        return (1/math.pi)*( (self.case_3()-self.TL)*(self.angle_1(self.TU)+math.pi/2)+ (self.TU- self.TL)*(math.pi/2+angle)- (self.theta()*math.cos(angle)))
  
    def case_5(self):   #Works fine
        return self.TU-self.TL

    def case_6(self):   #Works fine 
        angle1=self.angle_1(self.TL)
        angle2=self.angle_1(self.TU)
        return (1/math.pi)*((self.case_3()-self.TL)*(angle1-angle2)+self.theta()*(math.cos(angle1)-math.cos(angle2))+(self.TU-self.TL)*(math.pi/2 - angle2))

    def theta(self):    #works fine
        return ((self.tMax-self.tMin)/2)

    def angle_1(self,Tn): #Works fine
        a=math.asin((Tn-self.case_3())/self.theta())  
        return a
