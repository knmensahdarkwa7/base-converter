# main_branch ask whether u want to continue with the program
# base_ branch ask which type of conversion you would want to use
#


print('Welcome to my base converter')

active = False
main_branch = input('Do u want to continue[q to quit]: ')
if main_branch == 'y':
    active = True
elif main_branch == 'n':
    active = False

# Canging from paths
while active:
    base_branch = input(
        'Choose 1 if you are converting from other bases[2,5,8,16] to decimal\nChoose 2 if you are converting from decimal to other bases\n: ')
    if base_branch == '1':
        init_num = input('Enter desired number: ')
        base = int(input('What base is it in: '))

        # checking for validity for base two
        # Converting from base 2 to 10
        if base == 2 and all(char in '01' for char in init_num):
            def base2_to_base10():
                formula = 0
                power = len(init_num) - 1
                for num in init_num:
                    formula += int(num) * pow(base, power)
                    power -= 1
                print(f'{init_num} in base {base} is: {formula.__float__()}')


            base2_to_base10()
        elif base == 2:
            print('This is not a base two digit')

        # checking for validity for base 5
        # Converting from base 5 to 10
        if base == 5 and all(char in '01234' for char in init_num):
            def base5_to_base10():
                power = len(init_num) - 1
                formula = 0
                for num in init_num:
                    formula += int(num) * pow(base, power)
                    power -= 1
                print(f'{init_num} in base {base} is: {formula.__float__()}')


            base5_to_base10()
        elif base == 5:
            print('This is not a base five digit')

        # checking for validity for base 8
        # Converting from base 8 to 10
        if base == 8 and all(char in '01234567' for char in init_num):
            def base8_to_base10():
                power = len(init_num) - 1
                formula = 0
                for num in init_num:
                    formula += int(num) * pow(base, power)
                    power -= 1
                print(f'{init_num} in base {base} is: {formula.__float__()}')


            base8_to_base10()
        elif base == 8:
            print('This is not a base eight digit')

        # checking for validity for base 16
        # Converting from base 16 to 10
        ####################################################################################
        ####################Still under development#######################################3
        ######################################################################################
        if base == 16 and all(char in '0123456789ABCDEF' for char in init_num):
            def base16_to_base10():
                power = len(init_num) - 1
                formula = 0
                for num in init_num:
                    formula += int(num) * pow(base, power)
                    power -= 1
                print(f'{init_num} in base {base} is: {formula.__float__()}')


            base16_to_base10()
        elif base == 16:
            print('This is not a base sixteen digit')

    elif base_branch == '2':
        base10_num = int(input('Enter the number: '))
        base_conversion = int(input('Enter the base you are converting into: '))


        def base10_to_others():
            formula = 0
            formula += base10_num % base_conversion






    else:
        print('Nigga, what are u doing')  ############Don't for get to change NIGGA
        main_branch = input('Why do you want to quit? ')
        if main_branch == 'y':
            active = False
            print('Byeeeeee')
            break
        elif main_branch == 'n':
            pass

else:
    print('byeeeee')
