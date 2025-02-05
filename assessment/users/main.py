def load_data(filename):
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
    f = open(filename, 'r')
    data_list = f.readlines()
    f.close()
    
    return data_list


def create_user_dict(data_list):
    '''
    A function that takes output from load_data() and returns
    a dictionary of user information represented with a dictionary.
    
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
        users[f'user {index}']['balance'] = float(data[3])
    
    return users


def get_username():
    '''
    A function that prompts the user for a name.
    
    Returns:
        name
    '''
    return input('Enter Name: ')


def get_password():
    '''
    A function that prompts the user for a password.
    
    Returns:
        password
    '''
    return input('Enter Password: ')


def validate_user(username, password, data_dict):
    '''
    A function that loops through the user data_dict searching
    for a user with matching name and password.
    
    Returns:
        the username (string) if the username exists
    '''
    for user, information in data_dict.items():
        if information['username'] == username and information['password'] == password:
            return user # username and password match, return user


def accrue_interest(rate, data_dict):
    '''
    A function that loops through the user data_dict
    and adds an amount of interest to every users' balance.
    Rate should be given as a percent, i.e. 0.10 is equal to 10%.
    
    Returns:
        NA
    '''
    print(f'All Accounts Accruing {rate * 100} % Interest')
    for user, information in data_dict.items():
        information['balance'] += information['balance'] * rate


def deposit(username, password, data_dict, amount):
    '''
    A function that increases a validated users balance
    by amount.
    
    Returns:
        NA
    '''
    user = validate_user(username, password, data_dict)
    
    if user:
        print(f"Depositing ${amount} into {data_dict[user]['full_name']}'s Account")
        data_dict[user]['balance'] += amount
        

def withdraw(username, password, data_dict, amount):
    '''
    A function that decreases a validated users balance
    by amount, if amount less than the current balance.
    
    Returns:
        NA
    '''
    user = validate_user(username, password, data_dict)
    
    if user:
        if amount <= data_dict[user]['balance']:
            print(f"Withdrawing ${amount} from {data_dict[user]['full_name']}'s Account")
            data_dict[user]['balance'] -= amount
        else:
            print('Withdrawal amount exceeds available balance.')


def main():
    
    # load data
    data_list = load_data('data.txt')
    data_dict = create_user_dict(data_list)
    
    # log all users
    print('Starting Balances')
    for user in data_dict.items():
        print(user)
    print('\n')

    # get login information
    username = get_username()
    password = get_password()
    # validate
    user = validate_user(username, password, data_dict)
    if user:
        print(f"Name: {data_dict[user]['full_name']}")
        print(f"Balance: {data_dict[user]['balance']}")
    else:
        print('User name and password not found.')
        
    # S T R E T C H ---
    print('\nStretch Goals: ')
    # accrue interest
    accrue_interest(0.10, data_dict)
    # deposit
    deposit(username, password, data_dict, 1000)
    # withdraw
    withdraw(username, password, data_dict, 5)
    
    # log all users
    print('\n')
    print('Ending Balances')
    for user in data_dict.items():
        print(user)
        
main()

