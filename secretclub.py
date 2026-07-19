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
                print("You are not good at typing, are you ...")

    except TypeError as e:
        print("Wrong data type:", e)

    except IndexError as e:
        print("Indexing is going wrong:", e)

    except Exception as e:
        print("Something went wrong:", e)

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
        print("Perhaps you are giving too many fields:", e)

    else:
        return result


def validate(**prelimdata):

    try:
        assert prelimdata["sc"] != None
        assert prelimdata["ns"] != None

    except KeyError as e:
        print("You are really bad at typing, aren't you?")
        print("Validation failed due to", e)

    except AssertionError:
        print("One of the earlier steps has gone wrong.")
        print("Validation failed")

    else:

        print("Looking good so far ...")
        print("Sending for deeper validation")
        print("Opening connection to a remote server ...")

        try:
            deep_validate()

        except ValueError:
            print("There is something deeply wrong")
            print("Validation failed ...")

        else:
            print("Congrats ... Validation Successful")
            print("Welcome to my world!")

        finally:
            print("Closing connection to the remote server")


def deep_validate():
    """
    The slides intentionally omit this implementation.
    It randomly succeeds or raises ValueError.
    """
    pass


print("Welcome to the comrades' club ","\n","Here we will teach you how to fight with the elements, shall you recieve a blessing from the archons of the god king",'Start you blessing validation')
print(' us these functions to start your blessing','\n'
      ,'short_form(names and adjectives about urself)','\n'
      ,'name_strength(your full name with addons and prefix with suffix)',"\n"
      ,'validate(short_form and name_strength)','\n'
      ,'then deep_validate()')