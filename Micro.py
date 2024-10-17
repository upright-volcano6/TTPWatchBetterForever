password_make = input('you: make a temporary password for micro: ')
print('Micro: I think ' + password_make + ' is a good temporary password')

password_test = input('you: password: ')
if password_test == password_make:
  print('Micro: Correct')
elif password_test != password_make:
  print('Micro: Incorrect!')
