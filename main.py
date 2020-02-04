import shutil
import pathlib

orginal_exe_path = pathlib.Path("./Celeste_Test/orgi/CelesteEXE")
everest_exe_path = pathlib.Path("./Celeste_Test/oeve/CelesteEXE")
destination_path = pathlib.Path("./Celeste_Test/CelesteEXE")
choice = '0'

while(choice != '3'):
    print("1. Set Celeste to original")
    print("2. Set Celeste to Everest mod")
    print("3. Quit")
    choice = input("Choice: ")


    if(choice == '1'):
        shutil.copy2(orginal_exe_path, destination_path)
        print("Game switched to Orginal version")
    elif(choice == '2'):
        shutil.copy2(everest_exe_path, destination_path)
        print("Game switched to Everest version")
    elif(choice == '3'):
        print("Bye")
    else:
        print("Undefined option")


