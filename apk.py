#coding: utf-8

from __future__ import division

import curses,time,random,threading,sys,os

"""

Hayo mau apa lu?

mau recode?

yahahaha ga mampu otak nya gk nyampe

kalo ga mampu coding chat w sini biar w ajarin ya wkwkwk

wa : 0821 2506 8665

sfx:* yahahah bocah recode gk ada skill

"""

menu = ["Login","Info","Install Bahan","Hubungi","Join Grup","Exit"]

def print_menu(c,current,yy,xx,menu,title = " TOOLS INSTALLER\n\n\n Author by Tegar ID\n Pilih menu : \n"):

    c.clear()

    tx = xx // 2 - len(title) // 2

    ty = yy // 2 - len(menu)//2 - len(menu) // 2

    c.attron(curses.color_pair(2))

    c.addstr(ty,tx,title)

    c.attroff(curses.color_pair(2))

    for n,i in enumerate(menu):

        x = xx // 2 - len(i)//2

        y = yy // 2 - len(menu)//2 + n

        if current == n:

           c.attron(curses.color_pair(1))

           c.addstr(y,x,i)

           c.attroff(curses.color_pair(1))

        else:

           c.addstr(y,x,i)

        c.refresh()

def print_multiline(c,text_list,yy,xx):

    c.clear()

    c.attron(curses.color_pair(2))

    for n,i in enumerate(text_list):

        x = xx // 2 - len(i) // 2

        y = yy // 2 - len(menu) // 2 + n

        c.addstr(y,x,i)

    c.attroff(curses.color_pair(2))

    c.refresh()

def cur(c,menu,title = " TOOLS INSTALLER\n\n\n Author by Tegar ID\n Pilih menu : \n"):

    yy,xx = c.getmaxyx()

    current = 0

    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_RED)

    curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)

    curses.curs_set(0)

    print_menu(c,current,yy,xx,menu,title = title)

    while True:

      tex = c.getch()

      if tex == curses.KEY_UP:

         current -= 1

      elif tex == curses.KEY_DOWN:

         current += 1

      elif tex == curses.KEY_MOUSE:

         break

      if current < 0:

         current = len(menu)-1

      elif current > len(menu)-1:

         current = 0

      if tex == 10:

         break

      print_menu(c,current,yy,xx,menu,title)

    if menu[current] == "Login":

       cur(c,["Setup-vim","Encript-Html","Encript-Hash","Tema","Chat-Gen","Short-Link","Exit"],title = "Pilih Install")

    elif menu[current] == "Install Bahan":

       print_multiline(c,["Tunggu Proses Install.."],yy,xx)

       time.sleep(2)

       os.system("clear")

       os.system("pkg install wkwk")

       print_multiline(c,["Proses install selesai..","Ketik B/b untuk kembali ke menu"],yy,xx)

       while True:

         cok = c.getch()

         if cok == ord("b") or cok == ord("B"):

            c.clear()

            cur(c,["Login","Info","Install Bahan","Hubungi","Join Grup","Exit"])

            break

    elif menu[current] == "Info":

       print_multiline(c,["Author : Tegar ID","WhatsApp : 082125068665","github : https://github.com/OfficialDarkAngle","instagram : RG4_n0iz","","","Team :","PARANOID CYBER","[RG4] Black Coder","","","","Tekan B atau b untuk kembali ke menu"],yy,xx)

       while True:

          cok = c.getch()

          if cok == ord("b") or cok == ord("B"):

             cur(c,["Login","Info","Install Bahan","Hubungi","Join Grup","Exit"])

             break

    elif menu[current] == "Exit":

         print_multiline(c,["Terimakasih Sudah Menggunakan Tools kami"],yy,xx)

         time.sleep(2)

         return

    elif menu[current] == "Hubungi":

         print_multiline(c,["Ototmatis di tujukan ke kontak chat whatsapp author","Jika Belum Tahu Token nya silahkan Hubungi Author"],yy,xx)

         time.sleep(3)

         os.system("xdg-open 'http:/wa.me/+6282125068665'")

    elif menu[current] == "Encript-Html":

         os.system("clear")

         os.system("git clone https://github.com/OfficialDarkAngle/Encrypt-html")

         print_multiline(c,["Tools Encript Html Sudah Terinstall","Cara Menjalankan Scriptnya Ketik","$ cd Encrypt-html","$ python2 Enkripsi.py","Jika Sudah Paham Ketik Y/y"],yy,xx)

         while True:

            cok = c.getch()

            if cok == ord("Y") or cok == ord("y"):

               return

    elif menu[current] == "Setup-vim":

         os.system("clear")

         os.system("git clone https://github.com/OfficialDarkAngle/Setup-Vim")

         print_multiline(c,["Tools Setup Sudah Terinstall","Cara Menjalankan Scriptnya Ketik","$ cd Setuo-Vim","$ python setup.py","Jika Sudah Paham Ketik Y/y"],yy,xx)

         while True:

            cok = c.getch()

            if cok == ord("Y") or cok == ord("y"):

               return

    elif menu[current] == "Tema":

         os.system("clear")

         os.system("git clone https://github.com/OfficialDarkAngle/Tema")

         print_multiline(c,["Tools Setup Sudah Terinstall","Cara Menjalankan Scriptnya Ketik","$ cd Tema","$ python2 termux.py","Jika Sudah Paham Ketik Y/y"],yy,xx)

         while True:

            cok = c.getch()

            if cok == ord("Y") or cok == ord("y"):

               return

    elif menu[current] == "Ecript-Hash":

         os.system("clear")

         os.system("git clone https://github.com/OfficialDarkAngle/Enkrip")

         print_multiline(c,["Tools Setup Sudah Terinstall","Cara Menjalankan Scriptnya Ketik","$ cd Enkrip","$ sh Enkrip.sh","Jika Sudah Paham Ketik Y/y"],yy,xx)

         while True:

            cok = c.getch()

            if cok == ord("Y") or cok == ord("y"):

               return

    elif menu[current] == "Chat-Gen":

         os.system("clear")

         os.system("git clone https://github.com/OfficialDarkAngle/ChatGen")

         print_multiline(c,["Tools Setup Sudah Terinstall","Cara Menjalankan Scriptnya Ketik","$ cd ChatGen","$ bash ChatGen","Jika Sudah Paham Ketik Y/y"],yy,xx)

         while True:

            cok = c.getch()

            if cok == ord("Y") or cok == ord("y"):

               return

    elif menu[current] == "Short-Link":

         os.system("clear")

         os.system("git clone https://github.com/OfficialDarkAngle/Short")

         print_multiline(c,["Tools Setup Sudah Terinstall","Cara Menjalankan Scriptnya Ketik","$ cd Short","$ bash short.sh","Jika Sudah Paham Ketik Y/y"],yy,xx)

         while True:

            cok = c.getch()

            if cok == ord("Y") or cok == ord("y"):

               return

    elif menu[current] == "Join Grup":

         os.system("clear")

         os.system("xdg-open 'https://chat.whatsapp.com/BgXVHlb5E9XLwg9ezGkFgq'")

curses.wrapper(cur,menu)
