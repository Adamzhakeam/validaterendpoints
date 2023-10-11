'''
this  is module that handles validation of emails 
'''
# def _formatIsValid(email:str)->bool:
#     '''
#     this function checks if the email  format is valid
#     '''
#     AtSymbolIndex = email.find('@')
#     if AtSymbolIndex != -1 and email.find('@') < len(email) - 1:
#         dotIndex = email.find('.', AtSymbolIndex + 1)
#         if dotIndex != -1:
#             return True
#     return False

def _formatIsValid(email: str) -> bool:
    '''
    This function checks if the email format is valid.
    '''
    atSymbolIndex = email.find('@')
    dotIndex = email.find('.', atSymbolIndex + 1)
    return atSymbolIndex != -1 and dotIndex != -1 and dotIndex < len(email) - 1


def _firstCharacterIsValid(email:str) -> bool:
    '''
    this function is to check if the first character of 
    the email is (-) hyphen or dot (.)
    '''
    return email[0].isalpha() or email[0].isdigit()

def _lastCharacterOfLocalEmailPartIsValid(email:str)->bool:
    '''
    function validates the last character of the local email part
    '''
    localEmailPart = email[:email.index('@')]
    return localEmailPart[len(localEmailPart)-1].isalpha() or localEmailPart[len(localEmailPart)-1].isdigit()

# def _localEmailPartCharactersAreValid(email:str) -> bool:
#     '''
#     function to validate local part of the email
#     '''
#     allowedCharactersInLocalEmailPart = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!#$%&'*+-/=?^_`{|}~"
#     #localEmailPart = email[:email.index('@')]
#     for character in email[:email.index('@')]:
#         if  character not in allowedCharactersInLocalEmailPart :
#             return False
#     return True 

def _localEmailPartCharactersAreValid(email: str) -> bool:
    '''
    Function to validate the local part of the email.
    '''
    allowedCharactersInLocalEmailPart = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!#$%&'*+-/=?^_`{|}~"
    return all(character in allowedCharactersInLocalEmailPart for character in email[:email.index('@')])

    
# def _checkForConsectiveDots(email:str)->bool:
#     '''
#     this function checks for consective dots in the  email
#     '''
#     dot = ('.')
#     for character in range (0,len(email)-1):
#         if email[character] == dot and email[character + 1] == dot:
#             return False
#     return True

# def _checkForSpaces(email:str) -> bool:
#     '''
#     function checks for spaces in email
#     '''
#     spaces = " " 
#     if spaces in email:
#         return False
#     else:
#         return True


def _firstCharacterOfDomainNameIsValid(email:str)->bool:
    '''
    checks whether the first character of domain part
    is valid
    '''
    domainEmailPart = email.split('@',1)[1]                            
    return domainEmailPart[0].isalpha() or domainEmailPart[0].isdigit()

def _lastCharacterOfDomainIsValid(email:str)->bool:
    '''
    function checks if last character of  domain is valid 
    '''
    atSymbolIndex = email.rfind('@')
    withoutLocalPart = email[atSymbolIndex+1:]
    fullStopIndex = withoutLocalPart.rfind('.')
    emailDomain = withoutLocalPart[:fullStopIndex+0]
    return emailDomain[len(emailDomain)-1].isalpha() or emailDomain[len(emailDomain)-1].isdigit()

def _domainLengthIsValid(email:str) -> bool:
    '''
    function validates the length of the email domain
    '''
    character = '@'
    characterIndex = email.rfind(character)
    withoutLocalEmailPart = email[characterIndex+1:]
    dotIndex = withoutLocalEmailPart.rfind('.')
    return len(withoutLocalEmailPart[:dotIndex+0]) >=2 and len(withoutLocalEmailPart[:dotIndex+0]) <= 255

def _domainCharactersAreValid(email:str) -> bool:
    '''
    function validates the characters of domain 
    '''
    symbolIndex = email.rfind('@')
    withoutLocalPart = email[symbolIndex+1:]
    fullStopIndex = withoutLocalPart.rfind('.')
    #emailDomain = withoutLocalPart[:fullStopIndex+0]
    allowedCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-."
    return all(character in allowedCharacters for character in  withoutLocalPart[:fullStopIndex+0])
    # for characters in emailDomain:
    #     if characters not in allowedCharacters:
    #         return False
    # return True 
    
# def _emailIsNotFilled(email:str)->bool:
#     '''
#     function to validate email is filled 
#     '''
#     return len(email) !=0

def _firstCharacterOfTopLevelDomainIsValid(email:str)->bool:
    '''
    checks whether the first character of top level domain part
    is valid
    '''
    characterIndex = email.rfind('.')
    emailDomain = email[characterIndex+1:]
    return emailDomain[0].isdigit() or emailDomain[0].isalpha()
    
# def _topLevelDomainCharactersAreValid(email:str)-> bool:
#     '''
#     function that validates charactes in top level domain
#     '''
#     theDotIndex = email.rfind('.')
#     if theDotIndex !=0:
#          allowedCharactersInTopLevelDomain = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-"
#          for topLevelDomainCharacter in  email[theDotIndex+1:]:
#               if topLevelDomainCharacter not in allowedCharactersInTopLevelDomain:
#                   return False
#     return True

def _topLevelDomainCharactersAreValid(email: str) -> bool:
    '''
    Function that validates characters in the top-level domain.
    '''
    theDotIndex = email.rfind('.')
    if theDotIndex == 0:
        return False
    allowedCharactersInTopLevelDomain = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-"
    return all(character in allowedCharactersInTopLevelDomain for character in email[theDotIndex + 1:])

    
def _lengthOfTopLevelDomainIsValid(email:str)->bool:
    '''
    checks for top level domain length is valid 
    '''
    dotIndex = email.rfind('.')
    return len(email[dotIndex+1:]) >= 2  and len(email[dotIndex+1:]) <= 63
    
def _lastCharacterOfTopLevelDomainIsValid(email:str)->bool:
    '''
    checks whether the last character of domain part
    is valid
    '''
    return  email[len(email)-1].isalpha()

def _ifAtSymbolIsMoreThanOne (email:str) -> bool:
    '''
    check email if @ is more than one 
    '''
    return email.count("@") == 1
      
def isValid(email:str) -> bool:
    return _formatIsValid(email)  and _firstCharacterIsValid(email) and _lastCharacterOfLocalEmailPartIsValid(email) and\
        _localEmailPartCharactersAreValid(email) and _firstCharacterOfDomainNameIsValid(email) and  _lastCharacterOfDomainIsValid(email) and\
    _domainLengthIsValid(email) and _firstCharacterOfTopLevelDomainIsValid(email) and \
    _lengthOfTopLevelDomainIsValid(email) and _domainCharactersAreValid(email) and  \
     _lastCharacterOfTopLevelDomainIsValid(email) and _topLevelDomainCharactersAreValid(email) and\
     _ifAtSymbolIsMoreThanOne(email)
     

# if __name__ == "__main__":
#     for testCase , testResponse in [
#         ('john.doe@example.com',True),('jane.smith123@gmail.com',True),('info@companywebsite.net',True),
#         ('support@123site.info',True),('user-name@email-provider.co.uk',True),('contact_us@my-website.org',True),
#         ('contact_us@my-website.org',True),('mary+joe@emailserver.edu',True),('sales@mycompany.io',True),
#         ('newsletter-subscriber@email-service.com', True),('webmaster@email-domain.travel',True),
#         ('invalid.email@.com',False),('@example.com',False),('us er@.org ',False),('user@domain',False),
#         ('user@.',False),('user@invalid@domain.com',False),('user@domain..com',False),('user@domain com',False),
#         ('user@domain#email.com',False),('user@domain_with_very_long_name_that_exceeds_maximum_characters_allowed_in_domain.com',False),
#         ('gacepef101@vikinoko.com',True),('pifodi8325@trazeco.com',True),('wibike3093@xgh6.com',True),('megin91106@vikinoko.com',True),
#         ('bofoxe9291@wlmycn.com',True),('danovi6218@vikinoko.com',True),('mocag57481@xgh6.com',True),('pecotov674@trazeco.com',True),
#         ('dokolo9181@trazeco.com',True),('wowim88732@xgh6.com',True),
#         ('lol㋡@gmail.com',False), ('    @gmail.com',False),('@gmail.com',False), ('lol.3@@gmail.com.uk--ol',False),
#         ('isaac.magambo@students.mak.ac.ug',True),("2200807411@std.kyu.ac.ug", True)
#         ,('hssnkizz@gmail.com', True), ('123',False),  ('123.xyz',False), ('123.xyz@1.',False), ('123.xyz@g',False),
#         ('x123.xyz@b.com',False),(' ',False),("valid_email1@example.com", True),("valid_email2@gmail.com", True),("valid_email3@outlook.com", True),("valid_email4@yahoo.com", True),
#         ("valid_email5@email.co.uk", True),("invalid_email1", False),("invalid_email2@", False),("invalid_email3@.com", False),("invalid_email4@com", False),
#         ("invalid_email5@@", False),("valid_email6@hotmail.com", True),
#        ("valid_email7@example.co", True),("valid_email8@example.co.uk", True),("invalid_email6@example..com", False),("invalid_email7@.co.uk", False),("valid_email9@example.org", True),("valid_email10@gmail.co", True),
#        ("valid_email11@subdomain.example.com", True),("invalid_email8@example.c", False),
#         ("invalid_email9@-example.com", False)

#     ]:
#         assert isValid(testCase) == testResponse, f"failed test for arg {testCase}"
#     print('all is well')
