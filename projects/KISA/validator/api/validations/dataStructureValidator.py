'''
this module validates data against a defined data structure
'''

def throw(exception):
    raise Exception(exception)

def validateData(data, structure, path='$'):
    if type(structure) == type(type):
        if not isinstance(data, structure):
            throw(f'{path}: expected  {structure}, got {type(data)}')
    else:
        if type(structure)!= type(data):
            throw(f'{path}: expected  {type(structure)}, got {type(data)}')

        if isinstance(structure,dict):
            _path = path
            for key in structure:
                path = f'{_path}->{key}'
                if key not in data:
                    throw(f'{path}: missing key <{key}>  in dictionary')
                validateData(data[key], structure[key], path)
        elif isinstance(structure, (list,tuple)):
            _path = path
            for index,item in enumerate(structure):
                path = f'{_path}[#{index}]'
                if index > len(data)-1:
                    throw(f'{path}: item at index {index} missing')
                validateData(data[index],item, path)
                

if __name__=='__main__':
    print(validateData({
        'age':13,
        'name':'douglas',
        'weight':56.0,
        'other':[67,90.8,{
            'complex':(
                [],
                {'one':17.0},
                {'k':'7','k2':9, 'h':65},
                {'k':54}
            )
        }]
    },
    {
        'age':int,
        'name':str,
        'weight':float,
        'other':[int,float,{
            'complex':(
                list,
                {
                    'one':float
                },
                {'k':str},
                {'k':int}
            )
        }]
    }))

