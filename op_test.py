import os;

restart = input("Do you wish to restart your computer ? (yes / no): ")

if restart == 'no':
    exit()
else:
    os.system("shutdown /r /t 1")