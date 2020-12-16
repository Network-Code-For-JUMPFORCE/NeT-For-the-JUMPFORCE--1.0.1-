import socket
import time
import _thread
import smtplib
import random
#lid=[]
#lem=[]
#rang, dost, sen
#lvyf=[]
#lfc=[]
#lpa=[]
#0=first name, 1=lastname
#lfl=[]
kolet=[[],[],[],[],[],[]]
#0= online ya na 1= conn if on 
onof=[[],[]]
def sendmail (to,subject,message):
        from_em='jumpforcehelligames@gmail.com'
        cc=[""]
        header  = "From: %s\n" %from_em
        header += "To: %s\n" %",".join(to)
        header += "CC: %s\n" %",".join(cc)
        header += "Subject: %s\n\n" % subject
        message = header + message
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(from_em,*******)
        problems = server.sendmail(from_em,to,message)
        server.quit()
        return (problems)

def good (conn,sh):
        



def nf (conn):
        global kolet
	global onof
        t=len(kolet[4])
        pk=kolet[4]
        ek=kolet[1]
        ik=kolet[0]
        f=-1
        vs=conn.recv(1024)
        vs=vs.decode("utf-8")
        p=conn.recv(1024)
        p=p.decode("utf-8")
        if vs in ik:
                for tt in range (t):
                        if ik[tt]==vs:
                                f=tt
                                break
        elif vs in ek :
                for tt in range (t):
                        if ek[tt]==vs:
                                f=tt
                                break
        if f!=-1 and pk[f]==p:
                conn.send(('1').encode("utf-8"))
                (onof[0])[f]=1
                (onof[1])[f]=conn
                _thread_start_new_thread(good,(conn,f))
                return
        conn.send(('0').encode("utf-8"))
	time.sleep(7)
        _thread_start_new_thread(vorodf,(conn))
        return
def yf (conn):
        global kolet
        rang = (kolet[2])[0]
        dost = (kolet[2])[1]
        sen  = (kolet[2])[2]
        r=conn.recv(1024)
        r=r.decode("utf-8")
        d=conn.recv(1024)
        d=d.decode("utf-8")
        s=conn.recv(1024)
        s=s.decode("utf-8")
        f=-1
        t=len(rang)
        if r in rang :
                for i in range (t):
                        if rang[i]==r:
                                f=i
	f=str(f)
        conn.send(f.encode("utf-8"))
        f=int(f)
	ff=f
        if f==-1:
                time.sleep (7)
                _thread_start_new_thread(vorodf,(conn))
                return
        if f!=-1:
                if dost[f]!=d or sen[f]!=s:
                        f=-1
                else:
                        f=1
        f=str(f)
        conn.send(f.encode("utf-8"))
        f=int(f)
	fff=0
        if f==1:
                code = random.randint(10000,99999)
		payamcode="salam rafigh gol. \n behemoon gofti ke ramzeto faramosh kardi, age ke gofti, bashe, inam code vorodet,\n"+ str(code) + "\n amma age az hichi khabar nadari, ye e-mail be hamin address bezan. albate, kolan ma dost darim ke baz khord shoma ro beshnavim, pas in e-mailo be onvan pol ertebati ma va khodet, dar nazar begir. \n ba tashako, JUMPFORCE GROUP. \n helli 3" 
		bb=sendmail  ((kolet[1])[ff],"ramzeto faramoosh kardi??(jumpforce game)",payamcode)
                if bb!={}:
                        print ((kolet[1])[ff], bb)
                        conn.send(("0").encode("utf-8"))
                        conn.close()
                        return
                conn.send(("1").encode("utf-8"))
                ccc=conn.recv(1024)
		ccc=ccc.decode("utf-8")
		ccc=int(ccc)
		if ccc==code:
			fff=1
        if f==-1:
                time.sleep(7)
                _thread_start_new_thread(vorodf,(conn))
                return
	conn.send(((str(fff)).encode("utf-8"))
	fff=int(fff)
        hispas=0
	if fff==1:
		hispas = (kolet[4])[ff]
		conn.send(((str(hispas)).encode("utf-8"))
                _thread_start_new_thread(vorodf,(conn))
                return
	if fff==0:
		time.sleep(15)
		_thread_start_new_thread(vorodf,(conn))
	return 

def vorodf (conn):     
        #f4=vorodf
        vs=conn.recv(1024)
        vs=vs.decode("utf-8")
        vs=int(vs)
        if vs == 1:
                #nf
                _thread_start_new_thread(nf,(conn))
        if vs == 2:
                #yf
                _thread_start_new_thread(yf,(conn))
        return
def sakhtf (conn):
	global onof
        global kolet
        i=conn.recv(1024)
        i=i.decode("utf-8")
        e=conn.recv(1024)
        e=e.decode("utf-8")
        fc=conn.recv(1024)
        fc=fc.decode("utf-8")
        p=conn.recv(1024)
        p=p.decode("utf-8")
        fi=conn.recv(1024)
        fi=fi.decode("utf-8")
        la=conn.recv(1024)
        la=la.decode("utf-8")
        r=conn.recv(1024)
        r=r.decode("utf-8")
        d=conn.recv(1024)
        d=d.decode("utf-8")
        s=conn.recv(1024)
        s=vs.decode("utf-8")
        f='0'
        if i in (kolet(0)) :
                f='20'
                conn.send(f.encode("utf-8"))
                _thread_start_new_thread(sakhtf,(conn))
                return
        if e in (kolet(1)) :
                f='21'
                conn.send(f.encode("utf-8"))
                _thread_start_new_thread(sakhtf,(conn))       
                return
	if r in ((kolet(2))[0]) :
                f='23'
                conn.send(f.encode("utf-8"))
                _thread_start_new_thread(sakhtf,(conn))       
                return
	if d in ((kolet(2))[1]):
		f='24'
                conn.send(f.encode("utf-8"))
                _thread_start_new_thread(sakhtf,(conn))       
                return
	if s in ((kolet(2))[2]):
		f='25'
                conn.send(f.encode("utf-8"))
                _thread_start_new_thread(sakhtf,(conn))       
                return
			  
        #chek nemiconim ke first name va last na,e tekrari beshe
        conn.send(f.encode("utf-8"))
        code = random.randint(10000,99999)
        payam="SALAM rafigh gol! \n mamanoon ke mikhay ye account bezany va jumpforce bazi kony! \n in code tayidete:  "+str(code)+"\n age to az hichi khabar nadari, ye e-mail be hamin adress bezan.mamanoon (: \n ba tashakor, ravabet omomi jumpforce. \n rah ertebati ma va shoma: hamin e=mail. \n HELLIGAMES company."
        d=sendmail(e,"jumpforce-Creat an account",payam)
        tot=0
        if d!={}:
                print(d)
                conn.send(("0").encode("utf-8"))
                conn.close()
                return
        else:
                conn.send(("1").encode("utf-8"))
                codev=conn.recv(1024)
                codev=int(codev.decode("utf-8"))
                if codev==code:
                        conn.send(("1").encode("utf-8"))
                        (kolet[0]).append(i)
                        (kolet[1]).append(e)
                        ((kolet[2])[0]).append(r)
                        ((kolet[2])[1]).append(d)
                        ((kolet[2])[2]).append(s)
                        (kolet[3]).append(fc)
                        (kolet[4]).append(p)
                        ((kolet[5])[0]).append(fi)
                        ((kolet[5])[1]).append(la)
                        (onof[0]).append(0)
                        (onof[1]).append(0)
                        _thread_start_new_thread(vorodf,(conn))
                        return
                else:
                        conn.send(("0").encode("utf-8"))
                        time.sleep(15)
                        _thread_start_new_thread(sakhtf,(conn))
                        return
def kolf (conn):
        vs=conn.recv(1024)
        vs=vs.decode("utf-8")
        vs=int(vs)
        if vs==1:
                _thread_start_new_thread(vorodf,(conn))
        if vs==2:
                _thread_start_new_thread(sakhtf,(conn))
        return
def listento ():
        global s
        conn, addr = s.accept()
        print (str(addr[0])+" cnnected")
        _thread_start_new_thread(listento,())
        return (kolf(conn))
# creat a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(host)
port=1234
s.bind((host,port))
s.listen(120)
_thread_start_new_thread(listento,())
time.sleep('modat baz boodan server(second)')
s.close()
