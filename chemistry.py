

chemicals = ['oxygen','carbon','hydrogen','chlorine']

input_first_chemical= input("Please insert first chemical : ")


if not chemicals.count(input_first_chemical) ==1 :
    print("first chemical is not found")

input_sec_chemical= input("Please insert first chemical : ")

if not chemicals.count(input_sec_chemical) ==1 :
    print("the sec chemical is not found")



def ox_hy():
    return "H2O"



if(input_first_chemical=='oxygen' and input_sec_chemical =='hydrogen'):
    print("The chamical compound is "+ox_hy())
