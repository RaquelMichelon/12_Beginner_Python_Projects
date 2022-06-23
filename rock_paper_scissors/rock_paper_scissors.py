import random

# r > s; s > p; p > r;

def play():
    user = input("What`s your choice? Enter (r) for rock, (p) for paper or (s) for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return f"You won! {user} win to {computer}"
    
    return f"You lost! {user} lost to {computer}"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or(player == 'p' and opponent == 'r'):
        return True


print(play())
