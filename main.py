import random

MAX_LINES = 3  # defined a global constant.
MAX_BET = 150
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "🎃":2,
    "🎋":4,
    "😉":6,
    "🍒":8
}

symbol_values = {
    "🎃":5,
    "🎋":4,
    "😉":3,
    "🍒":2
}


def check_winnings(columns, lines, bet, values):
    winning = 0 # stores betting amount
    winning_lines = [] # stores no. of line on which we won
    for line in range(lines):   # loops thru every line
        symbol = columns[0][line] # takes the first symbol as reference and checks the other symbols
        for column in columns:
            symbol_to_check = column[line] # the first symbol of every column
            if symbol_to_check != symbol:
                break
        else:
            winning += values[symbol] * bet
            winning_lines.append(line + 1)

    return winning, winning_lines

def spinning_slotmachine(rows, cols, symbols):
    all_symbols = []    #empty list to store all the symbols
    for symbol, symbol_count in symbols.items():    # .items() --> returns key-value pairs from the dictionary.
        for _ in range(symbol_count):   #Iterated for all the symbols.
            all_symbols.append(symbol)  #every symbol was added(appended) to the all_symbols list

    columns = []  #Initialize an empty list to store all columns.

    for _ in range(cols):  #Loop to create each col_1.
        col_1 = []  #Initialize an empty list for the current col_1.
        current_symbols = all_symbols[:]  #Make a copy of all_symbols to prevent modifying the original list.

        for _ in range(rows):  #Loop through each row in the col_1.
            value = random.choice(current_symbols)  #Pick a random symbol from the available symbols.
            current_symbols.remove(value)  #Remove the chosen symbol to avoid duplicates in this col_1.
            col_1.append(value)  #Add the chosen symbol to the current col_1.

        columns.append(col_1)  #Add the completed col_1 to the list of columns.

    return columns  #Return the final list of columns.

def print_slotmachine(columns):
    for row in range(len(columns[0])):  #loop runs for every row, len(columns[0]) gives the no. of rows, columns[0] is the first row
        for i, col_1 in enumerate(columns):    #enumerate(columns) loops through each col_1, while also tracking its index (i).
            if i != len(columns) - 1:
                print(col_1[row],end=" | ")
            else:
                print(col_1[row],)

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit($): ")
        if amount.isdigit():        # to check if the input is a digit or not
            amount = float(amount)  # converted the input to float type
            if amount > 0:
                break   # amount > 0, then break the loop
            else:
                print("The deposit must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def choose_no_of_lines():
    while True:
        lines = input("enter the no. of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")  #Added max. lines in the sentence, by converting it to a string.
        if lines.isdigit():        # to check if the input is a digit or not
            lines = int(lines)  # converted the input to int type
            if 0 <= lines <= MAX_LINES:
                break   # amount > 0, then break the loop
            else:
                print("Enter valid no. of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bets():
    while True:
        amount = input("Enter the amount you want to bet per line($): ")
        if amount.isdigit():        # to check if the input is a digit or not
            amount = float(amount)  # converted the input to float type
            if MIN_BET <= amount <= MAX_BET:
                break   # amount > 0, then break the loop
            else:
                print(f' {amount} is not between {MIN_BET} and {MAX_BET}.')
        else:
            print("Please enter a number.")

    return amount

def game(balance):
    lines = choose_no_of_lines()
    while True:
        bet = get_bets()
        total_bet = lines * bet

        if total_bet > balance:
            print("You don't have enough money. Your balance is ", balance)
        else:
            break

        print(f'You are betting ${bet} on {lines} lines. Total bet =  ${total_bet}.')

    slots = spinning_slotmachine(ROWS, COLS, symbol_count)
    print_slotmachine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f'You won {winnings}')
    print(f'You won on line no. {winning_lines}.')
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f'Current balance is  ${balance}')
        spin = input("Press enter to spin (q to quit): ")
        if spin == 'q':
            break
        balance += game(balance)

    print(f'You are left with ${balance}')



main()