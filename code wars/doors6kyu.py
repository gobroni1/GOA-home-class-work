#change every 0/1 on index % i == 0

n=5
def get_issuer(number):
    number = str(number)
    if number[0]=="3" and len(number) == 15:
        return 'AMEX'
    elif number[0]=="6" and len(number) ==16:
        return 'Discover'
    elif number[0]==4 and 13 == len(number):
        return 'VISA'
    elif number[0]==4 and 16 == len(number):
        return 'VISA'
    elif number[0]=="51" or number[0]=="52" or number[0]=="5" and len(number) ==16:
        return 'Mastercard'
    else:
        return 'Unknown'

    
        
