# This is Dry code

from typing import Tuple
savings = 1096.25
checking = 1590.80
def process_transaction(transactions):
    global checking
    global savings
    if transactions>0:
        checking += (transactions * .85)
        savings += (transactions * .15)
    elif transactions<0:
        checking += transactions




if __name__ == "__main__":
    transations = [300.00, -50.00, -5.00, -20, 15.72, 2083.93, -1034.00, -420.00, -5.23, -15.93, -72.90]
    new_balance = (transations)
    print("Your new checking balance is:", '${:.2f}'.format(round(new_balance[0], 2)), "\nYour new savings balance is: ", '${:.2f}'.format(round(new_balance[1], 2)))