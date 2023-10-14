import random 

def generate_random_number(limit):
    random_num = random.randint(0, limit)
    
    while(random_num < limit):
        if(random_num % 7 == 0):
            return random_num
        
        else:
            random_num +=1


if __name__ == '__main__':
    limit = int(input('enter a limitation number: '))
    print(generate_random_number(limit))
    




