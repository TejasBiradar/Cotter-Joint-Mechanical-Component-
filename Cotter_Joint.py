import pandas as pd
import math

df = pd.read_excel(r"E:\Tejas\Programs\Intern\project\material_sheet.xlsx")


fos=4
load = int(input("Enter the Load:"))
mat_cott= input("Enter the material of Cotter Joint:")

print("\n")
if(mat_cott == 'c07'):
    yeild_strength=df.iloc[1]['Yield_Strength']
elif(mat_cott == 'c10'):
    yeild_strength=df.iloc[2]['Yield_Strength']
elif(mat_cott == 'c14'):
    yeild_strength=df.iloc[3]['Yield_Strength']
elif(mat_cott == 'c15'):
    yeild_strength=df.iloc[4]['Yield_Strength']
elif(mat_cott == 'c20'):
    yeild_strength=df.iloc[5]['Yield_Strength']
elif(mat_cott == 'c25'):
    yeild_strength=df.iloc[6]['Yield_Strength']
elif(mat_cott == 'c30'):
    yeild_strength=df.iloc[7]['Yield_Strength']
elif(mat_cott == 'c35'):
    yeild_strength=df.iloc[8]['Yield_Strength']
elif(mat_cott == 'c40'):
    yeild_strength=df.iloc[9]['Yield_Strength']
elif(mat_cott == 'c45'):
    yeild_strength=df.iloc[10]['Yield_Strength']
elif(mat_cott == 'c50'):
    yeild_strength=df.iloc[11]['Yield_Strength']
elif(mat_cott == 'c60'):
    yeild_strength=df.iloc[12]['Yield_Strength']
elif(mat_cott == 'c65'):
    yeild_strength=df.iloc[13]['Yield_Strength']
elif(mat_cott == 'fg150'):
    yeild_strength=df.iloc[14]['Yield_Strength']
elif(mat_cott == 'fg200'):
    yeild_strength=df.iloc[15]['Yield_Strength']
elif(mat_cott == 'fg220'):
    yeild_strength=df.iloc[16]['Yield_Strength']
elif(mat_cott == 'fg260'):
    yeild_strength=df.iloc[17]['Yield_Strength']
elif(mat_cott == 'fg300'):
    yeild_strength=df.iloc[18]['Yield_Strength']
elif(mat_cott == 'fg350'):
    yeild_strength=df.iloc[19]['Yield_Strength']
elif(mat_cott == 'fg400'):
    yeild_strength=df.iloc[20]['Yield_Strength']
else:
    print("Material Not Available")
    yeild_strength = int(input("Enter Yield Strength of the material:"))

print("The design is based on the load of",load,"KN and", mat_cott,"material\n")

print("Tensile Strength of the material 'Sd' is:",end=" ")
sd = (yeild_strength/fos)
print(sd,"Mpa")

print("Shear Strength of the material 'Ssd' is:",end=" ")
ssd = (0.5*sd)
print(ssd,"Mpa")

print("Crushing Strength of the material 'Scd' is:",end=" ")
scd = (1.5*sd)
print(scd,"Mpa\n")

d_val= (((4*load)*1000)/(3.142*sd))
D = math.sqrt(d_val)
print("Diameter of Rod 'd' is:",D,"mm")
d = int(round(D,0))
if d%2==0:  
    print("Since d is decimal value, rounding it off to next even number ie:",d+2,'mm\n')
else:
    d=d+1
    print("Since d is decimal value, rounding it off to next even number ie:",d,'mm\n')


        
d1t=((load*1000)/scd)


d1=((4/(3.142*sd))*((load*1000)+(d1t*sd)))
d1_ = math.sqrt(d1)
print("Diameter of Cotter Hole 'd1' is:",d1_,"mm")

d1=round(d1_)
if d1%2==0:

    print("Since d1 is decimal value, rounding it off to next even number ie:",d1+2,'mm\n')

else:
    d1=d1+1
    print("Since d1 is decimal value, rounding it off to next even number ie:",d1,'mm\n')

t = (d1t/d1)
print("Thickness of Cotter 't' :",t,'mm')

t=round(t)
if t%2==0:
    print("Since t is decimal value, rounding it off to next even number ie:",t+2,'mm\n')

else:
    t=t+1
    print("Since t is decimal value, rounding it off to next even number ie:",t,'mm\n')


a = ((load*1000)/(2*d1*ssd))
print("Width of cotter hole 'a' is:",a,"mm")

a=round(a)
if a%2==0:
    print("Since a is decimal value, rounding it off to next even number ie:",a+2,'mm\n')

else:
    a=a+1
    print("Since a is decimal value, rounding it off to next even number ie:",a,'mm\n')

d2 = (4/(3.142*scd))*((load*1000)+(3.142/4)*scd*d1*d1)
d2_ = math.sqrt(d2)
print("Diameter of Collar 'd2' is:",d2_,"mm")

d2_=round(d2_)
if d2_%2==0:
    print("Since d2 is decimal value, rounding it off to next even number ie:",d2_+2,'mm\n')
else:
    d2_=d2_+1
    print("Since d2 is decimal value, rounding it off to next even number ie:",d2_,'mm\n')

t1 = ((load*1000)/(3.142*d1*ssd))
print("Thickness of Collar 't1'is:",t1,"mm")

t1=round(t1)
if t1%2==0:
    print("Since t1 is decimal value,rounding it off to next even number ie:",t1+2,'mm\n')

else:
    t1=t1+1
    print("Since t1 is decimal value,rounding it off to next even number ie:",t1,'mm\n')

b = ((load*1000)/(2*t*ssd))
print("Width of Cotter 'b' is:",b,"mm")

b=round(b)
if b%2==0:
    print("Since b is decimal value,rounding it off to next even number ie:",b+2,'mm\n')
else:
    b=b+1
    print("Since b is decimal value,rounding it off to next even number ie:",b,'mm\n')


D = (((load*1000)/(t*scd))+d1)
print("Diameter of socket under cotter 'D' is:",D,"mm")

if D%2==0:
    print("Since D is decimal value,rounding it off to next even number ie:",D+2,'mm\n')

else:
    D=D+1
    D=round(D)
    if(D%2!=0):
        D=D+1
        print("Since D is decimal value,rounding it off to next even number ie:",D,'mm\n')
    else:
        print("Since D is decimal value,rounding it off to next even number ie:",D,'mm\n')


a1 = ((load*1000)/(2*(D-d1)*ssd))
print("Width of socket 'a1' is:",a1,"mm")

if a1%2==0:
    a1=round(a1)
    print("Since a1 is decimal value,rounding it off to next even number ie:",a1,'mm\n')

else:
    a1=a1+1
    a1=round(a1)
    if(a1%2!=0):
        a1=a1+1
        print("Since a1 is decimal value,rounding it off to next even number ie:",a1,'mm\n')
    else:
        print("Since a1 is decimal value,rounding it off to next even number ie:",a1,'mm\n')


t2 = ((load*1000)/(3.142*d1*ssd))
print("Thickness of socket across rod is:",t2,"mm")

if t2%2==0:
  
    print("Since t2 is decimal value,rounding it off to next even number ie:",t2,'mm\n')

else:
    t2=t2+1
    t2=round(t2)
    if(t2%2!=0):
        t2=t2+1
        print("Since t2 is decimal value,rounding it off to next even number ie:",t2,'mm\n')

    else:
        print("Since t2 is decimal value,rounding it off to next even number ie:",t2,'mm\n')


Sb = (((5/8)*(load*1000*D))/(b*b*t))
print("The bending stress 'σb' is:",Sb,"Mpa\n")

if (Sb < sd):
    print("Since, σb < Sd")
    print("Therfore pin is safe in bending!!!")
else:
    print("Since,σb > Sd")
    print("Therfore pin fails in bending")

