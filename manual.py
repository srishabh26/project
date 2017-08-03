#!/usr/bin/python

print "Content-Type:text/html"
print
import commands
import operator
import os
import cgi
import cgitb
cgitb.enable()
t=commands.getstatusoutput("nmap -sP 192.168.56.0-255 | grep 'Nmap scan'| awk '{print $5}'")
commands.getstatusoutput("touch /now/file1.txt")
f1=open("/now/file1.txt",'wrt')
f1.write(t[1])
f2=open("/now/file1.txt",'r')
f1.close()
l=f2.readlines()
l1=[]
for x in l:

		p=x.strip()
		l1.append(p)


mydict=dict()
for x in l1:
	print x
	if (x=='192.168.56.1' or x=='192.168.56.100' or x=='192.168.56.101'):
		pass
	else:
		t=commands.getstatusoutput("sshpass -p a ssh -l root "+x+" free -m |awk 'NR==2{print $2}'")	
		
					
		mydict[x]=int(t[1])
		mydict.update()

sorted_mydict=sorted(mydict.items(),key=operator.itemgetter(1))
ind=0
cnt=1
for i in sorted_mydict:
	if cnt==1:
		print """<table border="1">
		 <th>IP OF SYSTEM</th>
		 <th>FREE-RAM</th>"""
	print """<tr>
	<td>%s </td>"""%sorted_mydict[ind][0]
	print """<td>%s</td>"""%sorted_mydict[ind][1]
	print """</tr>"""
	cnt=cnt+1
	ind=ind+1

print """<form action='http://192.168.56.101/cgi-bin/rishabh.py'>
	 Namenode-ip<input type="text" name='nn' /><br />
	 Job-Tracker<input type="text" name='jt' /><br /> 
      """

for i in range(0,(len(sorted_mydict)-2),1):
	print """ Datanode<input type="text" name='dn' /><br/>"""
print """<input type="submit" /></form>"""
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy