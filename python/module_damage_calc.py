print('Welcome to the Module Damage Calc')
damage = input('Please enter the damage modifier (e.g. 1.02): ')
duration = input('Please enter the rate of fire bonus in percent (e.g. 6): ')
print(f'The damage increase of the module is: {float(damage) / (1 - float(duration)/100)}')
input("Press enter to exit;")