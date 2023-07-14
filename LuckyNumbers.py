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
import sys

messages = ["are a natural leader", "are a natural peacemaker", "are creative and optimistic", "are a hard worker", "value freedom", "are a carer and provider", "are a thinker", "have diplomatic skills", "are selfless and generous"]

alphabet = "abcdefghijklmnopqrstuvwxyz"
CAPalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

prompts = ["Enter FIRST name here >> ", "Enter LAST name here >> "]



def convert(name: str):
    nameArr = list(name)
    nameVal = 0
    tmp = 0
    for x in range(0, len(name)):
        tmp = alphabet.find(nameArr[x])
        if tmp == -1:
            tmp = CAPalphabet.find(nameArr[x])
            if tmp == -1:
                print("Invalid character " + str(nameArr[x]))
                input('Please try again')
                sys.exit()
                nameVal += (tmp % 9) + 1
                x += 1
    return nameVal


def split_number(lettersum: int):
    while lettersum > 9:
        digAr = list(str(lettersum))
        lettersum = int(digAr[0]) + int(digAr[1])
    return lettersum


def main():
    print('')
    print("Hi there! This program is here to calculate your lucky number and give you its meaning!! Please follow the instructions to find out what our lucky number is! :)")
    print('')

    luckyNumber = split_number(convert(input(str(prompts[0]))) + convert(input(str(prompts[1]))))

    print("Your lucky number is " + str(luckyNumber) + "!! This means that you " + messages[luckyNumber-1])
    input('Press any key to exit')

if __name__ == '__main__':
    main()