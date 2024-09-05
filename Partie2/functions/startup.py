# importations des modules
from termcolor import colored

# texte de bienvenue
def startup():
    print(colored('\nBonjour et bienvenue sur le Minitel ETNA.', 'green'))
    print(colored('Que souhaitez-vous faire ? \n', 'green'))
    print(colored('Pour choisir une option, tapez un NUMERO puis tapez la touche ENTREE \n', 'green'))
