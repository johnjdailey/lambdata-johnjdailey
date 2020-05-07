# my_mod.py

def buyholdsell(n):
    """
    Param n is a number.
    Function will decide if the number is worth buying, holding, or selling.
    """

    if (n) in range(1, 30):
        print("I'm buying")
    elif (n) in range(30, 71):
        print("I'm holding")
    elif (n) in range(90, 101):
        print("I'm selling")
    else:
        print("Your number wasn't in the correct range")

if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print("HELLO")
    y = int(input("Please choose a number between 1 and 100: "))
    buyholdsell(y)