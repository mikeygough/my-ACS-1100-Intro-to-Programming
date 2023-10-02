def load_data():
    '''
    A function that reads a text file of data and returns 
    a list of strings where each string represents data from that row.
    
    Returns:
        list of strings
        example: ['aman,1234,Andy Allman,1000\n', 
                 'betho,pa$$word,Beth Beto,2000\n'.
                 ...
                 ]
        
    '''
    f = open('data.txt', 'r')
    data_list = f.readlines()
    f.close()
    
    return data_list


def create_user_dict(data_list):
    '''
    A function that takes output from load_data() and returns
    a dictionary of user information represented with a dictionary
    
    Returns:
        dictionary of user dictionaries
        example: {'user 1': {'username': 'aman', 'password': '1234', 'full_name': 'Andy Allman', 'balance': '1000\n'},
                  'user 2': {'username': 'betho', 'password': 'pa$$word', 'full_name': 'Beth Beto', 'balance': '2000\n'},
                  ...
                 }
    '''
    users = {}
    
    for index, data in enumerate(data_list, start=1):
        data = data.split(',')
        users[f'user {index}'] = {}
        users[f'user {index}']['username'] = data[0] 
        users[f'user {index}']['password'] = data[1] 
        users[f'user {index}']['full_name'] = data[2] 
        users[f'user {index}']['balance'] = data[3] 
    
    return users


def get_username():
    '''
    A function that prompts the user for a name
    
    Returns:
        name
    '''
    return input('Enter Name: ')


def get_password():
    '''
    A function that prompts the user for a password
    
    Returns:
        password
    '''
    return input('Enter Password: ')


def validate_user(username, password, data_dict):
    '''
    A function that loops through the user data_dict searching
    for a user with matching name and password
    
    Returns:
        True if the user exists
        False if the user does not exist
    '''
    for user, information in data_dict.items():
        if information['username'] == username and information['password'] == password:
            return True # username and password match
    return False # no match

data_list = load_data()
data_dict = create_user_dict(data_list)

username = get_username()
password = get_password()

print(validate_user(username=username, password=password, data_dict=data_dict))
