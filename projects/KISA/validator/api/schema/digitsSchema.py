def _integerIsValid(d,schema):
    '''
    this function validates an integer with %d as the schema for validating digits as integers and returns boelean
    '''
    if "%d" in schema:
        if isinstance(d,int):
            return True
        return False 

print(_integerIsValid(4546.6,'%d'))

def _floatIsValid(d,schema):

    '''
    this function validates a float  with %f as the schema for validating digits as integers and returns boolean
    '''
    if "%f" in schema:
        if isinstance(d,float):
            return True
        return False 
print(_floatIsValid(4546.6,'%f'))

def _decimalPlacesIsValid(d, schema):
    '''
    this function validates decimal Places  with in a float  and limitimg them 
    to onw would like , *() as the schema. which takes 2 arguments the first argument is the float value 
    and the 2nd argumet is the maximum number of decimal places 
    '''
    if _floatIsValid(d,'%f'):
        if schema.startswith('*(') and schema.endswith(')'):
            arguments = schema[2:-1].split(',')
            if len(arguments) == 2:
                    rounded_d = round(float(arguments[0]), int(arguments[1]))
                    if rounded_d == float(arguments[0]):
                        return True
        return False
    return False
                  



def digitIsValid(d, schema):
    '''
    this is the main function for validating digits 
    '''
    schemaParts = schema.split('`')
    results = {}

    for part in schemaParts:
        if part == "%d":
            if not  _integerIsValid(d, part):
                return False
        elif part == "%f":
            if not _floatIsValid(d, part):
                return False
        elif part.startswith("*(") and part.endswith(")"):
            if not  _decimalPlacesIsValid(d, part):
                return False
    return True


def _range(d,schema):
    '''
    this function validates a range of digits 
    '''
    if _integerIsValid(d,'%d'):
        if schema.startswith('[') and schema.endswith(']'):
            arguments = schema[1:-1].split(',')
            if len(arguments) == 2:
                if d >= int(arguments[0]) and d <= int(arguments[1]) and d == arguments[2]:
                    return True
        return False
    return False


# data = {

#     33.33:"*(33.33,4)"
# }
# for d, schema in data.items():
#     validationResults = digitIsValid(d, schema)
    
#     print(f"digit: {d}")
#     for part, isValid in validationResults.items():
#         validity = 'True' if isValid else 'False'
#         print(f"{part}: {validity}")
#     print("\n")
