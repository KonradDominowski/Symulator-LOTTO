from random import shuffle

all_numbers = [i for i in range(1, 50)]

def choose_numbers(n):
    """
    Pick numbers to be drawn.

    n numbers will be picked.
    """

    user_numbers = []

    for i in range(n):
        while True:
            try:
                guess = int(input('Enter a number 1 to 49: '))
                if guess not in all_numbers:
                    raise ValueError
                if guess in user_numbers:
                    print("Number already picked. Pick another number.")
                    continue
                break
            except ValueError:
                print("Enter a whole number from 1 to 49")

        user_numbers.append(guess)

    return sorted(user_numbers)


def draw():
    user_numbers = choose_numbers(6)
    print('Your numbers:')
    print(*user_numbers)

    input('Press Enter to start a draw')
    shuffle(all_numbers)
    drawn_numbers = all_numbers[:6]

    print('Numbers drawn:')
    print(*drawn_numbers)

    correct_numbers = 0
    for i in user_numbers:
        if i in drawn_numbers:
            correct_numbers += 1

    if correct_numbers == 1:
        print(f'You hit {correct_numbers} number, try again next time')
    elif correct_numbers >= 3:
        print(f'You hit {correct_numbers} numbers, you can collect your prize')
    else:
        print(f'You hit {correct_numbers} numbers, try again next time')


draw()