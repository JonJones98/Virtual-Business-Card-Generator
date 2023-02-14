import qrcode
from PIL import Image
from Excel_connection_csv import Employee_info, employee_data,x,current_path
import os

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
#Employee Data
img_type=".jpg"


#Setting Vcard
employee_info= '''BEGIN:VCARD
VERSION:3.0
N:{l_name};{f_name};
FN: {f_name} {l_name}
ADR;TYPE=dom,work:{office}
TITLE:{title}
ORG:Br+A Consulting Engineers;{section_name}
EMAIL;TYPE=internet:{email}
TEL;TYPE=voice,work,pref:{direct_num}
TEL;TYPE=voice,mobile,pref: {mobile_num}
END:VCARD'''
qr.add_data(employee_info.format(f_name=Employee_info[1],
                                        l_name=Employee_info[3],
                                        office=Employee_info[4],
                                        title=Employee_info[5],
                                        section_name=Employee_info[6],
                                        email=Employee_info[7],
                                        direct_num=Employee_info[8],
                                        mobile_num=Employee_info[9]
                                        ))

    
#Creating QR Code
qr.make(fit=True)
img = qr.make_image()
file_name=str(Employee_info[3])+"_"+str(Employee_info[1])+"_"+str(Employee_info[6])+img_type
fullname=str(Employee_info[3])+"_"+str(Employee_info[1])+"_"+str(Employee_info[6])
img.save("{num}_Img/{file}".format(num=(str(0)+str(2)) ,file=file_name))
place='{current_path}/{num}_Img/{file}'

#Adding Location of Logo and QR Code
logos=os.listdir(r"03_Logos")
print(logos)
for logo in logos:
    print(logo[:8])
    print(Employee_info[6])
    if Employee_info[6]== logo[:4]:
        print("Here")
        logo_name='{current_path}/{num}_Logos/{logo}'.format(current_path=current_path ,num=str(0)+str(3), logo=logo)
        break
    elif "Default" in logo:
        print("there")
        logo_name='{current_path}/{num}_Logos/{logo}'.format(current_path=current_path ,num=str(0)+str(3), logo=logo)
        break
    

print(logo_name)
employee_data.loc[x,["@IMG_Location"]] = place.format(current_path=current_path ,num=(str(0)+str(2)),file=file_name)
employee_data.loc[x,["@Branch_Logo"]] = logo_name
qr.clear()





