def new_password():
    return (oldpassword != newpassword and len(newpassword) >= 6 and bool('1' or '2' or '3' or '4' or '5' or '6' or '7'
                                                                      or '8' or '9' or '0' in newpassword))

oldpassword = input('Oude wachtwoord: ')
newpassword = input('Nieuwe wachtwoord: ')
print(new_password())
