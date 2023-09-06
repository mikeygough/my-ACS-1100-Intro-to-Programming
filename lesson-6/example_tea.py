''' You want to write a program that will suggest the ideal temperature for the type of tea the user provides. 
If the tea is green tea display 150-180 F, 
if the tea is oolong 190 - 200 F, 
and if the tea is black tea 180 - 212 F. 
In all other cases display the phrase, 
“I don’t recognize that tea.” '''

'''

GET tea_type

IF tea_type == "green":
    DISPLAY "150-180 F"
ELSE IF tea_type == "oolong":
    DISPLAY "190 - 200 F"
ELSE IF tea_type == "black":
    DISPLAY "180 - 212 F"
ELSE
    DISPLAY “I don’t recognize that tea.”
END IF

'''