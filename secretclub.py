from colorama import Fore, Back, Style

strength = {
    'name': 10,
    'surname': 20,
    'nickname': 30,
    'alias': 40,
    'aka': 50
}


def short_form(idx, *names, **addons):

    final = ''

    try:
        for name in names:
            final += name[idx]

        for key in addons:
            if key == "prefix":
                final = addons[key] + final

            elif key == "suffix":
                final = final + addons[key]

            else:
                print("You are not good at typing, are you ..."+Fore.RED)

    except TypeError as e:
        print("Wrong data type:"+Fore.RED, e)

    except IndexError as e:
        print("Indexing is going wrong:"+Fore.RED, e)

    except Exception as e:
        print("Something went wrong:"+Fore.RED, e)

    else:
        return final.upper()

    finally:
        print("Hope you managed to pass this stage ...")


def name_strength(**fullname):

    result = 0

    try:
        for key, value in fullname.items():
            result += strength[key] * len(value)

    except KeyError as e:
        print("Perhaps you are giving too many fields:"+Fore.RED, e+Fore.RED)

    else:
        return result


def validate(**prelimdata):

    try:
        assert prelimdata["sc"] != None
        assert prelimdata["ns"] != None

    except KeyError as e:
        print("You are really bad at typing, aren't you?"+Fore.RED)
        print("Validation failed due to"+Fore.RED, e+Fore.RED)

    except AssertionError:
        print("One of the earlier steps has gone wrong."+Fore.RED)
        print("Validation failed"+Fore.RED)

    else:

        print("Looking good so far ..."+ Fore.RED)
        print("Sending for deeper validation"+Fore.RED)
        print("Opening connection to a remote server ..."+Fore.RED)

        try:
            deep_validate()

        except ValueError:
            print("There is something deeply wrong"+Fore.RED)
            print("Validation failed ..."+Fore.RED)

        else:
            print("Congrats ... Validation Successful"+Fore.GREEN)
            print("Welcome to my world!"+Fore.BLUE)

        finally:
            print("Closing connection to the remote server"+Fore.WHITE)


def deep_validate():
    """
    The slides intentionally omit this implementation.
    It randomly succeeds or raises ValueError.
    """
    pass


print(Back.WHITE+Style.DIM+"Welcome to the comrades' club ","\n","Here we will teach you how to fight with the elements, shall you recieve a blessing from the Archons of the God King",'Start your blessing validation')
print(Back.RESET+Fore.RED+Style.BRIGHT+' use these functions to start your blessing','\n'
      ,'short_form(names and adjectives about urself)','\n'
      ,'name_strength(your full name with addons and prefix with suffix)',"\n"
      ,'validate(short_form and name_strength()','\n'
      ,'then deep_validate()')