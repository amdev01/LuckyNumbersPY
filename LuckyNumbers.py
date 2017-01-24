print('Licensed under the Apache License, Version 2.0 (the "License");')
print('you may not use this file except in compliance with the License.')
print('You may obtain a copy of the License at')
print('')
print('     http://www.apache.org/licenses/LICENSE-2.0')
print('')
print('Unless required by applicable law or agreed to in writing, software')
print('distributed under the License is distributed on an "AS IS" BASIS,')
print('WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.')
print('See the License for the specific language governing permissions and')
print('limitations under the License.')

#============================================================================
# Name        : LuckyNumbers.cpp
# Author      : Adam Myczkowski
# Version     : 2.4
# Description : Lucky number calculator
#============================================================================

#==========CHEATSHEET================
#	1	2	3	4	5	6	7	8	9
#	a	b	c	d	e	f	g	h	i
#	j	k	l	m	n	o	p	q	r
#	s	t	u	v	w	x	y	z
#====================================

lucky1 = "are a natural leader"
lucky2 = "are a natural peacemaker"
lucky3 = "are creative and optimistic"
lucky4 = "are a hard worker"
lucky5 = "value freedom"
lucky6 = "are a carer and provider"
lucky7 = "are a thinker"
lucky8 = "have diplomatic skills"
lucky9 = "are selfless and generous"

alphabet = "abcdefghijklmnopqrstuvwxyz"
CAPalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

FrNmVal = 0
LstNmVal = 0
tmp = 0

print('')
print("Hi there! This program is here to calculate your lucky number and give you its meaning!! Please follow the instructions to find out what our lucky number is! :)")
print('')

FrNm = input(str('Enter FIRST name here >> '))
FrNmAr = list(FrNm)

LstNm = input(str('Enter FIRST name here >> '))
LstNmAr = list(LstNm)

for x in range(0, len(FrNm)):
    tmp = alphabet.find(FrNmAr[x])
    if tmp == -1:
        tmp = CAPalphabet.find(FrNmAr[x])
        if tmp == -1:
            print("Invalid character" + str(FrNmAr[x]))
            break
    FrNmVal += (tmp % 9) + 1
    x += 1

for x in range(0, len(LstNm)):
    tmp = alphabet.find(LstNmAr[x])
    if tmp == -1:
        tmp = CAPalphabet.find(LstNmAr[x])
        if tmp == -1:
            print("Invalid character" + str(LstNmAr[x]))
            break
    LstNmVal += (tmp % 9) + 1
    x += 1

while FrNmVal > 9:
    digAr = list(str(FrNmVal))
    FrNmVal = int(digAr[0]) + int(digAr[1])

while LstNmVal > 9:
    digAr = list(str(LstNmVal))
    LstNmVal = int(digAr[0]) + int(digAr[1])

LuckyNumber = FrNmVal + LstNmVal

while LuckyNumber > 9:
    digAr = list(str(LuckyNumber))
    LuckyNumber = int(digAr[0]) + int(digAr[1])

Output = "Your lucky number is " + str(LuckyNumber) + "!! This means that you "

if LuckyNumber == 1:
    Output += lucky1
elif LuckyNumber == 2:
    Output += lucky2
elif LuckyNumber == 3:
    Output += lucky3
elif LuckyNumber == 4:
    Output += lucky4
elif LuckyNumber == 5:
    Output += lucky5
elif LuckyNumber == 6:
    Output += lucky6
elif LuckyNumber == 7:
    Output += lucky7
elif LuckyNumber == 8:
    Output += lucky8
elif LuckyNumber == 9:
    Output += lucky9

print(Output)
input('Press any key to exit')
