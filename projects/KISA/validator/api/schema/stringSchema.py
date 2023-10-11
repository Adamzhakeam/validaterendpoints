'''

str(argument,argument)takes two arguments can both be integers 
if its one argument it takes the range of the length of the string if the 
the are 2 arguments the 1st is te minimum length and the second is te maximum length of
te string or the can be the minimum length of the string and the second argument can e ++
meaning increment by one till infinity

W*(TAKE ONE ARGUMENT OR more SEPERATED B A COMMA)in this it can take either integers or
alphabet characters or special characters what goes in tese parethensis
is what some wiuld specificall want te string to start with 
if its more tan one argument onl one at ago can bein te string not all of tem at once

*W ()this is the opposite of    W*

[AZ,Az,az] represents for case sesitivity te square brackets can one or all the
3 arguments AZ meaning all letters of te string are capital
Az meaming first letter of ever word is capital 
az meaning all letters are not capital

%s for alphabet characters

A-Z represensts alphabets from  A to z



0-9 represents numbers from 0 to 9

$(none,exp)this represents special characters and te argument none means no special character allowed 
exp means exeption meaning exeption of te special charcter one would define then it can also take
one argument of a special character

@()takes 1 or more  arguments it takes in integengers refering to te index of the argument 
that will be put in te parenthis

* this mutlplies with thw integer on its right to for the required  alphabets or integers depending 
on the condition

#s represents space

$s(none) no spaces allow in string 

.repesents AND

|represents or

%d represents integer

%f represensts float

` this represents seperater after a a module 

++ represents increment by one till maximum if it  is there 


&()this represents excluded in the parenthis one can put 
the arguments that the do no to want in the string

A-Z(none) represents that alphabets are not allowed in the string

0-9(none) represents thats digits are not allowed in 

#() this takes two arguments the first argument is either a digit ,alphabet are special character and the second 
argument is an integer that restricts the number of times a character should be consectively stated 

@s() this takes 3 arguments the first is the index the is the %sthe alphabet identifier then lastly is the
the alphabet you ould ant at that spcific index 

@d() this takes 3 arguments the first is the index the is the %d the digit identifier then lastly is the
the digit you ould ant at that spcific index

@$() this takes 2 argumengts the 1st on is the index and then the other is special characer specified at that
index they 2 argments are seperated by a comma ','

*()

\c() this takes in 2 arguments .. areguments[0] is anycharecter that one would like to limit its occurence
arguments[1] is an integer potraying the maximum occurencies of arguemnts[0] the arguments are seperarted by a comma(',')

'''
def _spaceModule(s, schema):
    if  "#s(none)" in schema:
        return ' ' not in s  
    elif schema == "#s":
        return ' ' in s  # Return True if there are spaces in the string
    else:
        return False  
def _stringLengthModule(s, schema):
    schema = schema.strip()  
    if '(' in schema and ')' in schema:
        arguments = schema[schema.index('(') + 1:schema.index(')')].split(',')
        if len( arguments) == 1:
            return len(s) == int(arguments[0])
        elif len( arguments) == 2:
            minLength = int( arguments[0])
            maxLength =  arguments[1].strip()
            if maxLength.isdigit():
                return minLength <= len(s) <= int(maxLength)
            elif maxLength == "++":
                return minLength <= len(s)
    return False


    

def _caseSensitivity(s, schema):
    if not isinstance(s, str):
        # Check if 's' is a string; if not, return False
        return False

    if 'AZ' in schema:
        # Check if the entire string is in uppercase
        return s.isupper()
    elif 'Az' in schema:
        # Check if the first character of each word is in uppercase
        words = s.split()
        return all(word[0].isupper() for word in words)
    elif 'az' in schema:
        # Check if the entire string is in lowercase
        return s.islower()
    return False

def _excludeCharacterModule(s, schema):
    '''
    defines the &() the exclusion of characters

    '''

    schema = schema[2:-1]  
    excludedCharacters = schema.split(',')

    for char in excludedCharacters:
        if char in s:
            return False

    return True

def _integerModule(s, schema):
  '''
  integer module
  '''
  return "%d" in schema and len(s) == 1 and s.isdigit()


def _startingCharacter(s, schema):

    '''
    defines the module for dictating the first character
    '''
 
    if '(' in schema and ')' in schema:
        startChars = schema[schema.index('(') + 1:schema.index(')')]
        startChars = startChars.split(',')
        
        for startChar in startChars:
            if startChar.isdigit():
                
                if s.startswith(startChar):
                    return True
            elif startChar.isalpha():
               
                if s.startswith(startChar):
                    return True
            elif len(startChar) == 1:
                
                if s.startswith(startChar):
                    return True
            elif schema == "W*(%s)" and s and s[0].isalpha():
                    return True
            elif schema == "W*(%d)" and s and s[0].isdigit():
                    return True    

    return False

def _lastCharacter(s, schema):
    '''
    defines the module for the last character
    '''
    if '(' in schema and ')' in schema:
        endChars = schema[schema.index('(') + 1:schema.index(')')]
        endChars = endChars.split(',')
        
        for endChar in endChars:
            if endChar.isdigit():
               
                if s.endswith(endChar):
                    return True  
            elif endChar.isalpha():
                
                if s.endswith(endChar):
                    return True  
            elif len(endChar) == 1:
                
                if s.endswith(endChar):
                    return True
            if schema == "*W(%s)" and s and s[-1].isalpha():
                return True
            if schema == "*W(%d)" and s and s[-1].isdigit():
                return True    
    return False


def _specialCharacterModule(s, schema):
    '''
    special character module for exempting special characters fro a string
    '''
    specialChars = "!@#$%^&*\/|()_-+=<>?"
    
    if schema == '$(none)':
        return not any(char in specialChars for char in s)
    
    parts = schema.split(',')

    allowedChars = []

    for part in parts:
        if part.startswith('(') and part.endswith(')'):
            allowedChars.update(part[1:-1])

    return all(char in allowedChars or char not in specialChars for char in s)

def _alphabetsModule(s, schema):
    if "A-Z(none)" in schema:
        return not any(char.isalpha() for char in s)
    elif "A-Z" in schema:
        return all(char.isalpha() or char.isdigit() for char in s)
    else:
        return False


def _astericModule(s, schema):
    #this function asigns the astric character as a incrementer 

    if len(schema) >= 4 and schema[2] == '*' and schema[3:].isdigit():
       
        if schema.startswith('%d'):
            return sum(1 for char in s if char.isdigit()) == int(schema[3:])
        elif schema.startswith('%s'):
            return sum(1 for char in s if char.isalpha()) == int(schema[3:])

def _atIndexModule(S, schema):
    # Split the schema into parts using '@' as the delimiter
    schemaParts = schema.split('@')[1:]
    
    for part in schemaParts:
        try:
            indexString, dataType = part.strip('()').split(',')
            index = int(indexString)
        except ValueError:
            return False
        
        if 0 <= index < len(S):
            if dataType == '%d':
                # Check if the character at the specified index is a digit
                if not S[index].isdigit():
                    return False
            elif dataType == '%s':
                # Check if the character at the specified index is an alphabet character
                if not S[index].isalpha():
                    return False
            elif dataType.isalpha():
                # Check if the character at the specified index is an alphabet character
                if not S[index].isalpha():
                    return False
            elif dataType == '#s':
                # Check if the character at the specified index is an alphabet character
                if not S[index]!= '':
                    return False
            else:  
                return False
        else:
            return False
    return True


def _alphabetModule(s, schema):
    '''
    alphabet module
    '''
    return "%s" in schema and len(s) >= 1 and 'a' <= 'z'

def _digitsModule(s, schema):
    if "0-9(none)" in schema:
        return not any(char.isdigit() for char in s)
    elif "0-9" in schema:
        return all(char.isdigit() for char in s)
    else:
        return 
        



def _consecutiveRepeatsModule(s, schema):
    # Extract the character/number and repeat count from the schema
    if len(schema) < 4 or schema[0] != '#' or schema[1] != '(' or schema[-1] != ')':
           return False #Invalid schema format. It should be '#(character/number n)'")

    schemaParts = schema[2:-1].split(',')
    if len(schemaParts) != 2:
        return False #("Invalid schema format. It should be '#(character/number n)'")

    charcterOrNumber, repeatCountString = schemaParts
    try:
        repeat_count = int(repeatCountString)
    except ValueError:
        return False #("Invalid repeat count in the schema. It should be an integer.")

    # Check for consecutive repeats of the character/number
    consenctiveCount = 0
    previousCharacter = None

    for character in s:
        if character == charcterOrNumber:
            consenctiveCount += 1
            if consenctiveCount == repeat_count:
                return False
        else:
            consenctiveCount = 0

        previousCharacter = character

    return True

def _atIndexDigitsOnlyModule(S, schema):
    # THIS MODULE IS RESPONSIBLE FOR SPECIFIC DIGITS AT SPECIFIC INDEX
    schemaParts = schema.split('@d')[1:]
    digitsToCheck = {}
    
    for part in schemaParts:
        try:
            indexString, dataAndCustomType = part.strip('()').split(',')
            index = int(indexString)
        except ValueError:
            return False
        
        dataType, customType = dataAndCustomType.split('|')
        
        if dataType == '%d':
            digitsToCheck[index] = customType
    
   
    for index, digit in digitsToCheck.items():
        if 0 <= index < len(S):
            if S[index] != digit:
                return False
        else:
         
            return False
    
    return True

def _atIndexAlphabetsOnlyModule(S, schema):
    #this module responsible for putting a specifc alphabet at a speified index
    schemaParts = schema.split('@s')[1:]
    lettersToCheck = {}
    
    for part in schemaParts:
        try:
            indexString, dataAndCustomType = part.strip('()').split(',')
            index = int(indexString)
        except ValueError:
            return False
            
        
        dataType, customType = dataAndCustomType.split('|')
        
        if dataType == '%s':
            lettersToCheck[index] = customType
    
    for index, letter in lettersToCheck.items():
        if 0 <= index < len(S):
            if S[index] != letter:
                return False
        else:
            return False
    return True

def _atIndexSpecialCharactersModule(S, schema):
    # this module secifies index at a which a specific character 
    schemaParts = schema.split('@$')[1:]
    specialCharactersToCheck = {}
    specialCharacters = "!@#$%^&*()_-+=<>,'/|][`?"
    
    for part in schemaParts:
        try:
            indexString, specialCharacter = part.strip('()').split(',')
            index = int(indexString)
        except ValueError:
            return False
        
        if specialCharacter in specialCharacters:
            specialCharactersToCheck[index] = specialCharacter
        else:
            return False
    for index, value in specialCharactersToCheck.items():
        if 0 <= index < len(S):
            if S[index] != value:
                return False
        else:
            return False
    return True

def _characterOccurrence(s,schema ):
    if schema.startswith('\c(') and schema.endswith(')'):
        arguments = schema[3:-1].split(',')
        if len(arguments) == 2:
            characterCount = s.count(arguments[0].strip())
            if characterCount > int(arguments[1].strip()):
                return  False
            return True

def stringIsValid(s, schema):
    schemaParts = schema.split('`')
    
    for part in schemaParts:
        if part == "#s" or part == "#s(none)":
            if not _spaceModule(s, part):
                return False
        elif part.startswith("str(") and part.endswith(")"):
            if not _stringLengthModule(s, part):
                return False
        elif part in ['AZ', 'Az', 'az']:
            if not _caseSensitivity(s, part):
                return False
        elif part == "A-Z(none)" or part == "0-9(none)" or part == "A-Z" or part == "0-9":
            if not _alphabetsModule(s, part):
                return False
        elif part.startswith("W*(") and part.endswith(")"):
            if not _startingCharacter(s, part):
                return False
        elif part.startswith("*W(") and part.endswith(")"):
            if not _lastCharacter(s, part):
                return False
        elif part.startswith("&(") and part.endswith(")"):
            if not _excludeCharacterModule(s, part):
                return False
        elif part == "%d" or part == "%s" or part.startswith("%d*") or part.startswith("%s*"):
            if not _integerModule(s, part) and not _alphabetModule(s, part):
                return False
        elif part.startswith("@(") and part.endswith(")"):
            if not _atIndexModule(s, part):
                return False
        elif part.startswith("@d(") and part.endswith(")"):
            if not _atIndexDigitsOnlyModule(s, part):
                return False
        elif part.startswith("@s(") and part.endswith(")"):
            if not _atIndexAlphabetsOnlyModule(s, part):
                return False
        elif part.startswith("$(") and part.endswith(")"):
            if not _specialCharacterModule(s, part):
                return False
        elif part.startswith('#(') and part.endswith(')'):
            if not _consecutiveRepeatsModule(s, part):
                return False
        elif part.startswith('@$(') and part.endswith(')'):
            if not _atIndexSpecialCharactersModule(s, part):
                return False
        elif part.startswith('\c(') and part.endswith(')'):
            if not _characterOccurrence(s, part):
                return False
    
    return True

# def stringIsValid(s, schema):
#     schemaParts = schema.split('`')
#     results = {}

#     for part in schemaParts:
#         if part == "#s":
#             results[part] = _spaceModule(s, part)
#         elif part == "#s(none)":
#             results[part] = _spaceModule(s, part)
#         elif part.startswith("str(") and part.endswith(")"):
#             results[part] = _stringLengthModule(s, part)
#         elif part in ['AZ', 'Az', 'az']:
#             results[part] = _caseSensitivity(s, part)
#         elif part == "A-Z(none)" :  
#             results[part] = _alphabetsModule(s, part)
#         elif  part == "0-9(none)":  
#             results[part] = _digitsModule(s, part)
#         elif part == "A-Z":
#             results[part] = _alphabetsModule(s, part)
#         elif part == "0-9" :
#             results[part] = _digitsModule(s, part)
#         elif part.startswith("W*(") and part.endswith(")"):
#             results[part] = _startingCharacter(s, part)
#         elif part.startswith("*W(") and part.endswith(")"):
#             results[part] = _lastCharacter(s, part)
#         elif part.startswith("&(") and part.endswith(")"):
#             results[part] = _excludeCharacterModule(s, part)
#         elif part == "%d":
#             results[part] = _integerModule(s, part)
#         elif part == "%s":
#             results[part] = _alphabetModule(s, part)
#         elif part.startswith("%d*") or part.startswith("%s*"):
#             results[part] = _astericModule(s, part)
#         elif part.startswith("@(") and part.endswith(")"):
#             results[part] = _atIndexModule(s, part)
#         elif part.startswith("@d(") and part.endswith(")"):
#             results[part] = _atIndexDigitsOnlyModule(s, part)
#         elif part.startswith("@s(") and part.endswith(")"):
#             results[part] =  _atIndexAlphabetsOnlyModule(s, part)
#         elif part.startswith("$(") and part.endswith(")"):
#             results[part] = _specialCharacterModule(s, part)
#         elif part.startswith('#(') and part.endswith(')'):
#             results[part] = _consecutiveRepeatsModule(s, part)
#         elif part.startswith('@$(') and part.endswith(')'):
#             results[part] = _atIndexSpecialCharactersModule(s, part) 
#         elif part.startswith('\c(') and part.endswith(')'):
#             results[part] = _characterOccurrence(s,part )

#     return results








# data = {
#     "UBF 000F": "W*(U)`@(1,%s)`@(2,%s)`@(4,%d)`@(5,%d)`@(6,%d)`*W(%s)`&(I,O)`AZ`str(8,8)`#(0,3)",
#     "UP 0244": "str(7)`W*(UP)`@(2,#s)`@(3,%d)`@(4,%d)`@(5,%d)`@(6,%d)`&(I,O)`AZ`#s`$(none)",#popo plate
#     "!adamKata":"str(6,8)`#s(none)`&(!,#,$,%,^,&,*,(,),_,-,+,=,<,>,?)",#username
#     "RF12AL57DDJE4W":"str(14)`W*(CM,CF,RF)`@(2,%d)`@(3,%d)`$(none)`#s(none)`AZ",#NIN
#     "1234 3451 3466 3754":"str(16)`@(0,%d)`@(1,%d)`@(2,%d)`@(3,%d)`@(4,#s)`@(5,%d)`@(6,%d)`@(7,%d)`@(8,%d)`@(9,#s)`\
#     `@(10,%d)`@(11,%d)`@(12,%d)`@(13,%d)`@(14,#s)`*W(%d)`$(none)`A-Z(none)",#creditCard number
#     "20/X/3461/EVE":"str(12,13)`W*(20,21,22,23)`@$(2,/)`@s(3,%s|U)`@(5,%d)`@(6,%d)`@(7,%d)`@(8,%d)`*W(PS,EVE,DAY)`\c(/,3)`AZ`#s(none)`&(!,@,#,$,%,^,&,*,(,),_,-,+,=,<,>,?)",
#     "UG 0244G":"str(8)`W*(UG)`@(2,#s)`@(3,%d)`@(4,%d)`@(5,%d)`@(6,%d)`&(I,O)`AZ`*W(%s)`$(none)",#ug plate
#     "H4DF123":"W*(H)`@d(1,%d|4)"
    





# }


# for s, schema in data.items():
#     validationResults = stringIsValid(s, schema)
    
#     print(f"String: {s}")
#     for part, isValid in validationResults.items():
#         validity = 'True' if isValid else 'False'
#         print(f"{part}: {validity}")
#     print("\n")