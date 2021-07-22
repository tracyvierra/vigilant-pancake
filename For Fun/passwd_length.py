username = input('Enter user name: ')
passwd = input('Enter your password: ')
passwd_hidden = '*' * len(passwd)
passwd_len = len(passwd)

print(f'{username}, your password of {passwd_hidden} is {passwd_len} characters long.')