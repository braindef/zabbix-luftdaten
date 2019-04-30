#coding=utf-8
import argparse
import time
import os.path
import requests
import sys
import re

#auf UTF-8 Zeichensatz einstellen
reload(sys)
sys.setdefaultencoding('utf8')

#Adresse der Webseite(n)
#---------------------------------------------------------------------------
url1 = 'http://192.168.179.200/values'

#Eingabeparameter verarbeiten
# Instantiate the parser
def parseArgs():
  parser = argparse.ArgumentParser(description='Liest Werte aus Stiebel Elron Webinterface aus aufruf z.B: $ python get.py --live "PUFFERISTTEMPERATUR"')
  #parser.add_argument('--csv', action="store_true", default=False, help='gibt alle Daten als CSV aus')
  parser.add_argument('--pm25', action="store_true", help='feinstaub 2.5')
  parser.add_argument('--pm10', action="store_true", dest="pm10", help='feinstaub 10')
  parser.add_argument('--temperatur', action="store_true", help='Temperatur')
  parser.add_argument('--luftfeuchtigkeit', action="store_true", help='Luftfeuchtigkeit')
  args = parser.parse_args()

  if not args.pm25 and not args.pm10 and not args.temperatur and not args.luftfeuchtigkeit:
    print(printResponse(getFile()))
  #if args.pm25:
  #  print("PM25")

  if args.pm25:
    print(getFile().text.split("PM2.5")[1].split("td class='r'>")[1].split("&nbsp;µg/m³")[0])

  if args.pm10:
    print(getFile().text.split("PM10")[1].split("td class='r'>")[1].split("&nbsp;µg/m³")[0])

  if args.temperatur:
    print(getFile().text.split("Temperatur")[1].split("td class='r'>")[1].split("&nbsp;°C")[0])

  if args.luftfeuchtigkeit:
    print(getFile().text.split("Luftfeuchte")[1].split("td class='r'>")[1].split("&nbsp;%")[0])

#Hole die drei Werteseiten von der STIEBEL ELTRON Steuerunngs Webseite v2.5.6
def getFile():
  r = requests.post(url1, headers={'Connection':'close'})
  return r
  

#gibt die abgefragten Webseiten der Steuerung aus (nur für Testzwecke)
def printResponse(response):
  print("********")
  print(response.text)
  print(response.status_code)





#-----------------------------------------
# MAIN: Hauptprogramm, hier startet alles
#-----------------------------------------
  getFile()    
parseArgs()      #je nach Aufrufparameter (Args) wird dann die Funktion für den Entsprechenden wert aufgerufen



