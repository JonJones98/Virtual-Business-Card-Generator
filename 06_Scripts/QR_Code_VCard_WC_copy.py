import qrcode
from PIL import Image
from Excel_connection_csv import Employee_info, employee_data,x,current_path,logo
import os
import base64

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
#Employee Data
img_type=".jpg"
with open(Employee_info[13],'rb') as image2string:
    converted_string = base64.b64encode(image2string.read())




#Setting Vcard
employee_info= '''BEGIN:VCARD
VERSION:3.0
N:{l_name};{f_name};
FN: {f_name} {l_name}
EMAIL;TYPE=internet:{email}
TEL;TYPE=voice,mobile,pref: {mobile_num}
URL;TYPE=Linktree:{linktree}
END:VCARD'''
qr.add_data(employee_info.format(f_name=Employee_info[1],
                                        l_name=Employee_info[3],
                                        email=Employee_info[7],
                                        mobile_num=Employee_info[8],
                                        linktree=Employee_info[12]
                                        ))

print(Employee_info[1])
print(Employee_info[3])
print(Employee_info[7])
print(Employee_info[8])
print(Employee_info[12])
print(Employee_info[13])
#Creating QR Code
qr.make(fit=True)
img = qr.make_image()
file_name=str(Employee_info[1])+"_"+str(Employee_info[3])+"_"+str(Employee_info[5])+img_type
fullname=str(Employee_info[1])+"_"+str(Employee_info[2])+"_"+str(Employee_info[3])
img.save("{num}_Img/{file}".format(num=(str(0)+str(2)) ,file=file_name))
place='{current_path}/{num}_Img/{file}'

#Adding Location of Logo and QR Code
print(x)
if x <= 1:
    y=x-1
    employee_data.loc[y,["@IMG_Location"]] = (place.format(current_path=current_path ,num=(str(0)+str(2)),file=file_name)).replace('/',':')[1:]
    employee_data.loc[y,["@Branch_Logo"]] = (logo.name).replace('/',':')[1:]
        
qr.clear()





