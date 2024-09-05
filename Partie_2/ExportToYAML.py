import yaml
import tarfile
import datetime

from scrapInfo import GeneralInfo
from scrapInfo import NetworkInfo
from scrapInfo import ProcessusInfo

def saveScrapInfo():
    
    INFORMATIONS = {    'OS' : GeneralInfo.getOS(),
                        'VERSION DE L`OS': GeneralInfo.getOSversion(),
                        'UPTIME': GeneralInfo.getUptime(),
                        'VERSION DU KERNEL' : GeneralInfo.getKernelVersion(),
    }
    
    RESEAUX = {
                'ADRESSE IP' : NetworkInfo.GetIP(),
                'INTERFACES' : NetworkInfo.GetInterfaces(),
                'PAQUETS TRANSMIS' : NetworkInfo.GetPackets(),
                'ROUTES' : NetworkInfo.GetRoutes(),
                'FOWARD DU PAQUET' : NetworkInfo.GetFwdPackets(),
    }
    
    PROCESSUS = {
                'PROCESSUS EN COURS' : ProcessusInfo.GetProcessusInfo(),
    }
    
    with open('DeviceInformations.yaml', 'w') as f:
        data = yaml.dump(INFORMATIONS, f, sort_keys=False, default_flow_style=False)
    
    with open('NetworkInformations.yaml', 'w') as f:
        data = yaml.dump(RESEAUX, f, sort_keys=False, default_flow_style=False)
    
    with open('ProcessusInformations.yaml', 'w') as f:
        data = yaml.dump(PROCESSUS, f, sort_keys=False, default_flow_style=False)

saveScrapInfo()