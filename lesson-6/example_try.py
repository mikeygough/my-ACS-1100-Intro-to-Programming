''' You need a system that asks for an input number. 
Since input allows strings and converting some strings to numbers fails you 
should use try: except: like this. '''

'''

n = input("Give me a number: ") # “two”
try:
   n = int(n) # “two” -> ERROR
 # do something with n
except:
   # try again

'''
   
'''
calculate_area:
    PROMPT "Give me a number:"

    GET n

    TRY:
        SET n = int n
        DISPLAY n times n
    EXCEPT:
        DISPLAY "Try again"
        RUN calculate_area
    END TRY
END calculate_area

RUN calculate_area
'''

def calculate_area():
    n = input("Give me a number: ")
    
    try:
        n = float(n)
        area = n * n
        print(f"Area: {area:.2f}")
    except:
        print("Try again with an integer, for example, 5.")
        calculate_area()
    
calculate_area()