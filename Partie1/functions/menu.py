# importations des modules
from termcolor import colored

# les différentes options du menu
def menu():    
    print(colored('[1] Voir les informations générales', 'blue', attrs=['bold']))     
    print(colored('[2] Voir les informations réseaux', 'yellow'))
    print(colored('[3] Voir les informations processus', 'magenta', attrs=['bold']))
    print(colored('[4] Liste des fichiers', 'cyan'))
    print(colored('[9] Quitter le programme \n', 'red'))