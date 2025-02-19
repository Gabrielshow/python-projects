'''
Speed Typing Test
-------------------------------------------------------------
'''

# there is still a lot to add
# to add wpm
# the text scrolling or moving for longer texts
# typing sections
# if possible build your electron equivalent of this app

import tkinter
from timeit import default_timer as timer
import random

def speed_test():
    # List of sentences for the typing test
    speed_test_sentences = [
        'This is a random sentence to check speed.',
        'Speed, I am lightning mcqueen.',
        'Typing tests can help you improve your speed and accuracy.',
        'The quick brown fox jumps over the lazy dog.'
    ]

    sentence = random.choice(speed_test_sentences)
    start = None  # Timer start time will be set when user starts typing
    game_over = False  # Game over flag to stop the timer after completion

    main_window = tkinter.Tk()
    main_window.geometry('600x400')
    main_window.configure(bg='lightblue')  # Set background color

    # Display the sentence
    label_1 = tkinter.Label(main_window, text=sentence, font='Helvetica 16', bg='lightblue')
    label_1.place(x=150, y=10)

    label_2 = tkinter.Label(main_window, text='Start Typing:', font='Helvetica 14', bg='lightblue')
    label_2.place(x=10, y=120)

    entry = tkinter.Entry(main_window)
    entry.place(x=280, y=125)

    label_3 = tkinter.Label(main_window, text='', font='times 20', bg='lightblue')
    label_3.place(x=10, y=300)

    def update_timer():
        nonlocal game_over, start
        if not game_over:
            current_time = round(timer() - start, 2)
            label_3.configure(text=f'Time: {current_time}s')
            main_window.after(100, update_timer)  # Update every 100ms

    def highlight_errors(typed_text: str):
        # Highlight wrong characters in red
        highlighted_text = ""
        for i, char in enumerate(typed_text):
            if i < len(sentence) and char != sentence[i]:
                highlighted_text += f"<span style='color:red'>{char}</span>"
            else:
                highlighted_text += char
        label_1.configure(text=highlighted_text)

    def start_timer(event):
        nonlocal start
        if start is None:  # Start timer only once user starts typing
            start = timer()
            update_timer()

    def check_result():
        nonlocal game_over
        typed_text = entry.get()
        error_indices = [i for i, (t, s) in enumerate(zip(typed_text, sentence)) if t != s]

        if typed_text == sentence:
            game_over = True
            end = timer()
            time_taken = round(end - start, 2)
            words = len(typed_text.split())
            wpm = round(words / (time_taken / 60), 2)
            label_3.configure(text=f'Time: {time_taken}s | WPM: {wpm}')
        else:
            error_message = f'Errors at positions: {error_indices}'
            label_3.configure(text=f'Wrong Input. {error_message}')
        
        highlight_errors(typed_text)  # Highlight errors after the result

    # Buttons with hover effect
    def on_hover(event):
        event.widget.config(bg="lightgreen")

    def reset_game():
        main_window.destroy()  # Destroy the current window
        speed_test()  # Start a new game

    button_1 = tkinter.Button(main_window, text='Done', command=check_result, width=12, bg='grey')
    button_1.place(x=150, y=180)
    button_1.bind("<Enter>", on_hover)

    button_2 = tkinter.Button(main_window, text='Try Again', command=reset_game, width=12, bg='grey')
    button_2.place(x=250, y=180)
    button_2.bind("<Enter>", on_hover)

    entry.bind("<KeyPress>", start_timer)  # Start timer when user starts typing

    main_window.mainloop()

if __name__ == '__main__':
    speed_test()
