import random
import PySimpleGUI as sg

sg.theme('LightGrey1')

# Define the word list and initial variables
WORDS = ['apple', 'banana', 'cherry', 'durian', 'elderberry', 'fig']
word = random.choice(WORDS)
guesses = set()
max_guesses = 6

# Define the layout for the game window
layout = [[sg.Text('Guess the word:')],
          [sg.Text(' '.join('_' if letter not in guesses else letter for letter in word))],
          [sg.Text('Guess a letter:'), sg.Input(key='-INPUT-')],
          [sg.Button('Guess'), sg.Button('Quit')]]

def update_word_display(word, guesses):
    return ' '.join('_' if letter not in guesses else letter for letter in word)

def main():
    window = sg.Window('Hangman', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit':
            break
        elif event == 'Guess':
            guess = values['-INPUT-']
            if guess in word:
                guesses.add(guess)
                word_display = update_word_display(word, guesses)
                window[1].update(word_display)
                if '_' not in word_display:
                    sg.popup(f'You won! The word was "{word}".')
                    break
            else:
                max_guesses -= 1
                if max_guesses == 0:
                    sg.popup(f'You lost! The word was "{word}".')
                    break
                sg.popup(f'Incorrect guess. You have {max_guesses} guesses left.')
        
    window.close()

if __name__ == '__main__':
    main()
