from requests import post
from random import shuffle , randint
from time import sleep
from colorama import Fore,init
init()

print ()
print (Fore.CYAN+'''
 $$$$$$$    $$$$$$$  $     $  $$$$$$$  $$$$$$$  $        $$$$$$$    
    $       $     $  $$$   $     $     $     $  $           $            
    $       $     $  $  $  $     $     $     $  $           $              
    $       $     $  $   $$$     $     $     $  $           $           
    $       $$$$$$$  $     $  $$$$$$$  $$$$$$$  $$$$$$   $$$$$$$    's scipt
'''+Fore.WHITE)

fichier = open('config.txt', 'r')
settings = fichier.read().split('"')
fichier.close

header = {'authorization': settings[1]}

link = "https://discord.com/api/v9/channels/"+settings[3]+"/messages"

fichier = open(settings[7], 'r')
content = fichier.read().splitlines()
fichier.close

payload = {'content': content[0]}


def sendlemessageenquestion(nombredelement):
        if settings[5] == "687367852977946734":
            print (Fore.RED + "FDP ne fais pas ca !" + Fore.WHITE)
        else:
            listedemot = '\n\n**--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**\n\nCher <@'+settings[5]+'> quand j\'ai lu ces lignes j\'ai pensé a toi je te les comunique donc :\n\n"'
            for nombredelement in range (nombredelement):
                shuffle(content)
                if len(listedemot) == 282:
                    listedemot = listedemot +content[0]
                else:
                    listedemot = listedemot +" "+content[0]
    
            listedemot = listedemot +'"\n\nCordialement\n\n**<3**'
            payload = {'content': str(listedemot)}
            post(link, data=payload, headers=header)
            print (Fore.LIGHTMAGENTA_EX +"Message Send <3"+Fore.WHITE)

run = True

while run == True:
    sendlemessageenquestion(randint(1 ,100))
    sleep(randint(1,10))
