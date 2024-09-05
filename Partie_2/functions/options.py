# importations des modules
import subprocess
from termcolor import colored
from functions.menu import *

# détermination du choix du menu
def options():

    # ------------------------------------------- [INFORMATIONS GENERALES] -------------------------------------------
    # input pour choisir un menu
    optionMenu = int(input(colored('Choisissez une option. \n \n', 'white', attrs=['bold'])))

    while optionMenu != 9:
        if optionMenu == 1:
            print("Vous avez choisi : ")
            print(colored('INFORMATIONS GENERALES', 'blue', attrs=['bold']))

            print("Que souhaitez-vous voir ? \n")
            print(colored('[1] Version OS', 'blue', attrs=['bold']))
            print(colored('[2] Uptime', 'blue', attrs=['bold']))
            print(colored('[3] Version du Kernel', 'blue', attrs=['bold']))
            print(colored('[4] Informations Materiel', 'blue', attrs=['bold']))
            print(colored('[5] Processeur', 'blue', attrs=['bold']))
            print(colored('[6] Mémoire', 'blue', attrs=['bold']))
            print(colored('[7] Disque Durs', 'blue', attrs=['bold']))
            print(colored('[8] Limite Fichiers Ouverts', 'blue', attrs=['bold']))
            print(colored('[9] Retour \n', 'red'))

        # input pour choisir un sous-menu
            option_info_generale = int(input(colored('Choisissez une option. \n \n', 'white', attrs=['bold'])))
    
            while option_info_generale != 9:

                
                if option_info_generale == 1:
                    print(colored('\nVERSION DE L`OS : \n', 'blue', attrs=['bold'] )) 
                    subprocess.run('cat /etc/os-release', shell=True)
                    

                elif option_info_generale == 2:
                    print(colored('\nUPTIME : \n', 'blue', attrs=['bold']))
                    subprocess.run('uptime', shell=True)
                    
                
                elif option_info_generale == 3:
                    print(colored('\nVERSION DU KERNEL : \n', 'blue', attrs=['bold'])) 
                    subprocess.run('uname -r', shell=True)
                    
                
                elif option_info_generale == 4:
                    print(colored('\nINFORMATIONS MATERIEL: \n', 'blue', attrs=['bold']))
                    
                
                elif option_info_generale == 5:
                    print(colored('\nPROCESSEUR : \n', 'blue', attrs=['bold']))
                    subprocess.run('cat /proc/cpuinfo', shell=True)
                    
                
                elif option_info_generale == 6:
                    print(colored('\nMEMOIRE : \n', 'blue', attrs=['bold']))
                    subprocess.run('cat /proc/meminfo', shell=True)
                    
                elif option_info_generale == 7:
                    print(colored('\nDISQUE DURS : \n', 'blue', attrs=['bold']))
                    subprocess.run('df -h', shell=True)
                    
                
                elif option_info_generale == 8:
                    print(colored('\nLIMITE FICHIERS OUVERTS : \n', 'blue', attrs=['bold']))
                    subprocess.run('cat /proc/sys/fs/file-max', shell=True)
                    
                
                else:
                    print(colored('OPTION INVALIDE', 'red'))

                print()
                option_info_generale = int(input(colored('Choisissez une option. \n \n', 'white', attrs=['bold'])))

        elif optionMenu == 2:
            # ------------------------------------------- [RESEAUX] -------------------------------------------
            #Choix des menus
            print("Vous avez choisi : ")
            print(colored('RESEAUX', 'yellow', attrs=['bold']))

            print("Que souhaitez-vous voir ? \n")
            print(colored('[1] Adresse IP', 'yellow', attrs=['bold']))
            print(colored('[2] Interfaces Existantes', 'yellow', attrs=['bold']))
            print(colored('[3] Nombre de paquets transmis / reçus', 'yellow', attrs=['bold']))
            print(colored('[4] Routes', 'yellow', attrs=['bold']))
            print(colored('[5] Foward du Paquet', 'yellow', attrs=['bold']))
            print(colored('[9] Retour', 'yellow', attrs=['bold']))


            
            # input pour choisir un sous-menu
            option_reseaux = int(input(colored('Choisissez une option. \n \n', 'white', attrs=['bold'])))

            while option_reseaux != 9:
                if option_reseaux == 1:
                    print(colored('\nVotre adresse UP est : \n', 'yellow', attrs=['bold'] )) 
                    (subprocess.run('hostname -I', shell=True))


                elif option_reseaux == 2:
                    print(colored('\nInterfaces existantes : \n', 'yellow', attrs=['bold']))
                    subprocess.run('ip link show', shell=True)


                elif option_reseaux == 3:
                    print(colored('\nNonbres de paquets transmis / reçus : \n', 'yellow', attrs=['bold'])) 
                    subprocess.run('cat /proc/net/dev', shell=True)


                elif option_reseaux == 4:
                    print(colored('\nRoutes : \n', 'yellow', attrs=['bold']))
                    subprocess.run('ip route', shell=True)
                    
                elif option_reseaux == 5:
                    print(colored('\Foward du paquet : \n', 'yellow', attrs=['bold']))
                    subprocess.run('sysctl net.ipv4.ip_forward', shell=True)
                    print(colored('\n1 = Foward Activé \n2 = Foward Désactivé', 'white', attrs=['bold']))

                else:
                    print(colored('OPTION INVALIDE', 'red', attrs=['bold']))

                print()
                option_reseaux = int(input(colored('Choisissez une option. \n \n', 'white', attrs=['bold'])))

        
            
        elif optionMenu == 3:
            # ------------------------------------------- [PROCESSUS] -------------------------------------------
            print("Vous avez choisi : ")
            print(colored('PROCESSUS', 'magenta', attrs=['bold']))
            print("Que souhaitez-vous voir ? \n")
            
            print(colored('[1] Processus en cours', 'magenta', attrs=['bold']))
            
            option_processus= int(input(colored('Choisissez une option. \n \n', 'white', attrs=['bold'])))
            
            while option_processus != 9:
                if option_processus== 1:
                    print(colored('Processus en cours :', 'magenta', attrs=['bold']))
                    subprocess.run('ps aux', shell=True)
                
                print()
                option_processus = int(input(colored('Choisissez une option. \n \n', 'white', attrs=['bold'])))
                    
        elif optionMenu == 4:
            # ------------------------------------------- [LISTE DES FICHIERS] -------------------------------------------
            print("Vous avez choisi : ")
            print(colored('LISTE DES FICHIERS', 'cyan', attrs=['bold']))
            subprocess.run('ls')

        else:
            print(colored('\nOPTION INVALIDE.', 'red', attrs=['bold']))

        print()
        menu()
        optionMenu = int(input("Choisissez une option. \n"))

    # sortie de programme
    print(colored("Au revoir.", 'red'))
