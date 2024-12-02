from tkinter import *
import time 
import random

class FlashcardApp:
    score = 0

    def __init__(self):
        # In-memory storage for flashcards
        self.flashcards = []

    def add_flashcard(self):
        add_gui = Tk()
        add_gui.geometry("640x480")
        add_gui.config(bg="#ADD8E6")
        add_gui.title("Add Flashcards")

        Label(add_gui, text="Enter the question:", font=("Arial", 16), bg="#ADD8E6").pack(pady=10)
        question_entry = Entry(add_gui, font=("Arial", 14))
        question_entry.pack(pady=5)
        Label(add_gui, text="Enter the answer:", font=("Arial", 16), bg="#ADD8E6").pack(pady=10)
        answer_entry = Entry(add_gui, font=("Arial", 14))
        answer_entry.pack(pady=5)

        def add_card():
            question = question_entry.get().strip()
            answer = answer_entry.get().strip().lower()
            if question and answer:  
                self.flashcards.append({'question': question, 'answer': answer})
                question_entry.delete(0, END)
                answer_entry.delete(0, END)
                status_label.config(text="Flashcard added!", fg="green")
            else:
                status_label.config(text="Please fill in both fields.", fg="red")

        Button(add_gui, text="Add Flashcard", command=add_card, font=("Arial", 14)).pack(pady=10)

        status_label = Label(add_gui, text="", font=("Arial", 12), bg="#ADD8E6")
        status_label.pack(pady=5)

        def start_quiz():
            if self.flashcards:
                add_gui.destroy()
                random.shuffle(self.flashcards)
                self.start_flashcard_display()
            else:
                status_label.config(text="Please add at least one flashcard.", fg="red")

        Button(add_gui, text="Start Quiz", command=start_quiz, font=("Arial", 14)).pack(pady=10)

        add_gui.mainloop()

    def submit_answer(self, myAnswer, gui, flashcard, btn):
        if myAnswer.get().strip().lower() == flashcard['answer']: # if answer is correct
            m = Label(gui, font=("Arial", 16, "bold"), pady=0,bg="#ADD8E6", text="Correct!") # adds label with answer
            self.score += 1
        else: # if answer is wrong
            m = Label(gui, font=("Arial", 16, "bold"), pady=0, bg="#ADD8E6", text=f"Incorrect! The correct answer is {flashcard['answer']}")

        window_width = 640 #set window dimensions
        window_height = 480
        label_width = m.winfo_reqwidth() #set m's label dimensions
        label_height = m.winfo_reqheight()

        #set m's placement coordinates
        m.place(x=(window_width - label_width) / 2, y=(window_height - label_height) * (0.75))
        btn.forget() # hides button to prevent resubmitting answer

    def show_end_screen(self, gui):
        self.remove_all_from_frame(gui) # clears frame
        totalQuestions= len(self.flashcards)
        score_display = f"Your score is {self.score}/{totalQuestions}"  # format score as "correct/total"
        s = Label(gui, font=("Arial", 16, "bold"), pady=15, text=score_display, bg="#ADD8E6")  # add label with score
        s.pack(expand=True)
        close_btn = Button(gui, text = 'Close', command=gui.destroy) # adds button to close window and end program
        close_btn.pack()
        close_btn.place(x= 300, y=300)

    def remove_all_from_frame(self, gui):
        for w in gui.winfo_children(): # destroys all current widgets
            w.destroy()

    def start_flashcard_display(self):
        gui = Tk()
        gui.geometry("640x480") # sets window size to fixed size
        gui.config(bg="#ADD8E6")
        gui.attributes('-topmost', True)

        currentCardIndex = 0
        for flashcard in self.flashcards: # iterates over all created flashcards

            window_width = 640
            window_height = 480

            currentCardIndex += 1
            q = Label(gui, font=("Arial", 16, "bold"), text=str(flashcard['question']), bg="#ADD8E6") # adds question text

            label_width = q.winfo_reqwidth()
            #label_height = q.winfo_reqheight()
            q.place(x=(window_width - label_width) / 2, y=window_height / 3)

            myAnswer = StringVar()
            e = Entry(gui, textvariable=myAnswer) # adds user input entry, current text added to myAnswer var

            entry_width = e.winfo_reqwidth()
            #entry_height = e.winfo_reqheight()
            e.place(x=(window_width - entry_width) / 2, y=window_height / 2)

            button_frame = Frame(gui)
            button_frame.pack(expand=True, side="bottom")

            sub_btn = Button(gui, text = 'Submit', command=lambda : self.submit_answer(myAnswer, gui, flashcard, sub_btn)) # adds submit button
            sub_btn.place(x=300, y=300)
            if currentCardIndex < len(self.flashcards): # if not last card
                next_btn = Button(gui, text = 'Next Card', command=lambda : self.remove_all_from_frame(gui)) #remove all widgets on click
                next_btn.place(x=window_width - 150, y=300)
            else:
                next_btn = Button(gui, text = 'Test Score', command=lambda : self.show_end_screen(gui)) # go to end screeb on click
                next_btn.place(x=window_width - 150, y=300)
            gui.wait_window(q) # delay progression until question widget is removed

        gui.attributes('-topmost', False)
        gui.mainloop()

app = FlashcardApp()
app.add_flashcard()