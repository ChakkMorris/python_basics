# function which asks user for input number, returns odd or even

def odd_or_even():
    num = int(input("enter number please\n"))
    
    if num%4 == 0:
        print('Even number which devides by 4')
 
    elif num%2 == 1:
        print('Odd number')
    else:
        print(num , 'Even number')
        
odd_or_even()



# divisor functions -returns list of an input number's divisors
def divisor(num):
    division_list=[]
    for digit in range(1,num+1):
        if num%digit==0:
            division_list.append(digit)
    return division_list

l = divisor(39)

for i in l:
    print(i)
    
    
    
  # function which returns whether an input string is a palindrome
def is_palindrome(string):

    s=0
    e=len(string)-1
    
    while s<e:

    #   print(string[s],' ',string[-(1+s)])
        if string[s]!=string[e]:
            print(string, 'is not a palindrome')
            return

        s +=1
        e -=1
        
    print(string,'Is a palindrome')

is_palindrome('morrrrom')
is_palindrome('morom')
is_palindrome('moro')
is_palindrome('14541')  




# function recieves list, returns a new list only with even numbers from list
def even_list(list):
    
    return_list=[]
    for item in list:
        if item%2 ==0:
            return_list.append(item)
    return return_list


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = even_list(a)

for item in b:
    print(item)
    
    
    
   
# list comprehension : item for item in list_a if item not in list_b.
import random
numlist = []
list_length = random.randint(5,15)

while len(numlist) < list_length:
    numlist.append(random.randint(1,75))
    
evenlist = [number for number in numlist if number % 2 == 0] 
print(numlist)
print(evenlist)
    
    
    
    
    
#rock paper scissors game
def check_inputs(list):
    acceptable = ['R','P','S']
    count=0
    
    for item in list: 
        if item in acceptable:
            count+=1
        
    return count
    
def winner(list):
    if list[0]==list[1]:
        print('Draw, try again')
        return 0
    
    elif list[0]== 'R' and list[1]=='P':
        print('player 2 wins! well done')
    elif list[0]== 'R' and list[1]=='S':
        print('player 1 wins! well done')
    elif list[0]== 'P' and list[1]=='S':
        print('player 2 wins! well done')
    elif list[0]== 'P' and list[1]=='R':
        print('player 2 wins! well done')
    elif list[0]== 'S' and list[1]=='P':
        print('player 1 wins! well done')
    elif list[0]== 'S' and list[1]=='R':
        print('player 2 wins! well done')
        
    return 1


while 1:
    player_1 = (input('Player 1: Enter "r" for rock, "s" for Scissors, "p" for paper\n')).upper()
    player_2 = (input('Player 2: Enter "r" for rock, "s" for Scissors, "p" for paper\n')).upper()
    
    answers = [player_1,player_2]
    
    check = check_inputs(answers)
    if check == 2:
        if winner(answers) == 0:
            continue
        break
    print('wrong inputs. try again')
    
    
    
    
    
 #  Function which recieves 2 lists, and returns list of common items
def list_compare(l_1, l_2):
    
    new_list=[]
    
    for item in l_1:
        if item not in l_2:
            new_list.append(item)
    
    return set(new_list)

            
l = list_compare(a, b)

for i in l:
    print(i)
    
    
    
    
    
    
    
#Function which returns a list that contains only the elements that are common between several lists 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 'lev','chakk']
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,'lev','bob',4,13]
c = [3,'lev',22,4565,5,4,89,5,8]
d = [3, 5, 8, 'lev', 11, 'analyst']
e = [3, 5, 8, 'lev', 11, 'analyst', 'data']

sample_lists = [a,b,c,c,d,e]

def list_overlap(lists):
    
    overlap = lists[0]
    count_lists = len(sample_lists)
    
    #print(count_lists)
    for i in range(1,count_lists):
        return_list = []
        
        for j in range(0,len(overlap)):
            if overlap[j] in lists[i]:
                return_list.append(overlap[j])
            
        overlap = return_list
        
    return overlap
    

        
check_list = list_overlap(sample_lists)
print(check_list)


    
