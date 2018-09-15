from random import randint as r
from os import system as s
board=[" "," "," "," "," "," "," "," "," "," "]
win=False
click=True
print('\t*****************************')
print('\t*\tTIC TOC Game\t    *')
print('\t*\t Created By\t    *')
print('\t*\tOmar Faruk.OM\t    *')
print('\t*****************************')
word=""
def sbord():
    print(f"{board[1]}" + " |" + f" {board[2]}" + " |" + f" {board[3]}")
    print("- + - + -")
    print(f"{board[4]}" + " |" + f" {board[5]}" + " |" + f" {board[6]}")
    print("- + - + -")
    print(f"{board[7]}" + " |" + f" {board[8]}" + " |" + f" {board[9]}")
def intro():
	global word
	ask=int(input("What Do You Want?\n1.[X]\n2.[O]\n3.Coustom Words\n>"))
	if ask==1:
		word=("X","O")
	elif ask==2:
		word=("O","X")
	elif ask==3:
		while True:
			st,cd=input("Enter Your and oponent Word{separeted by ','}:").split(',')
			if len(st)>1 or len(cd)>1:
				print('Please Enter One Letter')
			else:
				word=(st,cd)
				break
	return word

ask1=int(input('1.Single Player\n2.Dobule Player\n>>>'))
if ask1==1:
	intro()
	s('clear')
	while True:
		sbord()
		try:
			put=int(input("Enter 1-9 :"))
			if put<1 or put>9:
				print('\nwrong Input\n')
				continue
			elif not put:
				print('\nDont Empty\n')
				continue
			if board[put]!=" ":
				print('\nits already filled\n')
				continue
			board[put]=word[0]
			sbord()
			if board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " " and board[9] != " ":
				s('clear')
				print("\nMatch Draw\n")
				break
			if (word[0]+word[0]+word[0]==board[1]+board[2]+board[3] or word[0]+word[0]+word[0]==board[4]+board[5]+board[6] or word[0]+word[0]+word[0]==board[9]+board[7]+board[8] or word[0]+word[0]+word[0]==board[1]+board[4]+board[7] or word[0]+word[0]+word[0]==board[2]+board[5]+board[8] or word[0]+word[0]+word[0]==board[3]+board[6]+board[9] or word[0]+word[0]+word[0]==board[1]+board[5]+board[9] or word[0]+word[0]+word[0]==board[3]+board[5]+board[7]):
				s('clear')
				sbord()
				print("\nYou Won\n")
				break
			while True:
				ran=r(1,9)
				if board[ran]==" ":
					board[ran]=word[1]
					break
			if (word[1]+word[1]+word[1]==board[1]+board[2]+board[3] or word[1]+word[1]+word[1]==board[4]+board[5]+board[6] or word[1]+word[1]+word[1]==board[9]+board[7]+board[8] or word[1]+word[1]+word[1]==board[1]+board[4]+board[7] or word[1]+word[1]+word[1]==board[2]+board[5]+board[8] or word[1]+word[1]+word[1]==board[3]+board[6]+board[9] or word[1]+word[1]+word[1]==board[1]+board[5]+board[9] or word[1]+word[1]+word[1]==board[3]+board[5]+board[7]):
				s('clear')
				sbord()
				print("\nComputer Won\n")
				break
			s('clear')
		except Exception as e:
			print(f'\nYou Got {e} error plz take care\n')
elif ask1==2:
	intro()
	s('clear')
	while True:
		if board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " " and board[9] != " ":
			sbord()
			print("Match Draw")
			break
		if click==True:
			sbord()
			try:
				put=int(input('1st player Enter 1-9:'))
				if 1>put or put>9:
					print('\nwrong input\n')
					continue
				elif board[put]!=" ":
					print('\nAlredy enter\n')
					continue
				elif not type(put) == int:
					print("\nPlz Set Int value\n")
				else:
					pass
				board[put]=word[0]
				if (word[0]+word[0]+word[0]==board[1]+board[2]+board[3] or word[0]+word[0]+word[0]==board[4]+board[5]+board[6] or word[0]+word[0]+word[0]==board[9]+board[7]+board[8] or word[0]+word[0]+word[0]==board[1]+board[4]+board[7] or word[0]+word[0]+word[0]==board[2]+board[5]+board[8] or word[0]+word[0]+word[0]==board[3]+board[6]+board[9] or word[0]+word[0]+word[0]==board[1]+board[5]+board[9] or word[0]+word[0]+word[0]==board[3]+board[5]+board[7]):
					s('clear')
					sbord()
					print("\n1st player Won\n")
					break
				s('clear')
				click=False
			except Exception as e:
				print(f'\nYou Got {e} error plz take care\n')
		elif click==False:
			sbord()
			try:
				put1=int(input('2ndplayer Enter 1-9:'))
				if put1>9 or put1<1:
					print('\nwrong Input\n')
					continue
				elif board[put1]!=" ":
					print('\nYour input is already taken\n')
					continue
				board[put1]=word[1]
				if (word[1]+word[1]+word[1]==board[1]+board[2]+board[3] or word[1]+word[1]+word[1]==board[4]+board[5]+board[6] or word[1]+word[1]+word[1]==board[9]+board[7]+board[8] or word[1]+word[1]+word[1]==board[1]+board[4]+board[7] or word[1]+word[1]+word[1]==board[2]+board[5]+board[8] or word[1]+word[1]+word[1]==board[3]+board[6]+board[9] or word[1]+word[1]+word[1]==board[1]+board[5]+board[9] or word[1]+word[1]+word[1]==board[3]+board[5]+board[7]):
					s('clear')
					sbord()
					print("\n2nd Player Won\n")
					break
				s('clear')
				click=True
			except Exception as e:
				print(f'\nYou Got {e} error plz take care\n')