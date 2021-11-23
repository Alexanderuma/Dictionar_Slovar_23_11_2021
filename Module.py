def loe_failist(file:str)->list:
    '''Loeme failist read ja lisame järjendisse
    :param str f: 
    '''
    fail=open(file,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def uus_sona(file: str, x: str)-> list:
    '''Loeme failist read ja lisame järjendisse
    :param str f: Faili nimetus
    '''
    mas=[] 
    with open(file, "a") as f:
        f.write(x+"\n")
    mas=loe_failist(file)
    return mas
def correction(sona:str, mas:list)->list:
    """Parandamine
    :param srt sona: sõna parandamiseks
    :param list masx: järjend kus asub sõna
    """
    
    for i in range (len(mas)):
        if mas[i]==sona:
            uus_sona=sona.replace(sona, input('Uus sõna:'))
            mas.insert(i,uus_sona)
            mas.remove(sona)
    return mas
def failisse(mas:list,file:str):
    f=open(file,'w',encoding="utf-8-sig")
    for e in mas:
        f.write(e+"\n")
    f.close()
    
from gtts import gTTS #from playsound import playsound
import os
def heli(text:str, language:str):
    """ Tekst salvestamine mp3 failisse ja mängimine
    """

    #language='en','fi','ru'
    obj = gTTS (text=text, lang=language, slow=False).save("heli.mp3")
    #playsound("heli.mp3")
    os.systen("heli.mp3")
    import pyttsx3
    def heli2(text:str):
        heli==pyttsx3.int()
        #heli.setProperty('volume',0.5)#0-1
        #heli.setProperty('rate',150)#>100
        voices = converter.getProperty('voices')