from tkinter import *
from quiz_brain import QuizBrain

BACKGROUND_COLOR = "#B1DDC6"

class UserInterface :
    def __init__(self,quizbrain : QuizBrain):
        self.quiz=quizbrain

        self.window=Tk()
        self.window.title("QUIZ GAME")
        self.window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
        self.correct_img=PhotoImage(file="Photos/correct.png")
        self.wrong_img=PhotoImage(file="Photos/wrong.png")
        self.white_bg_img=PhotoImage(file="Photos/white_bg.png")

        # CANVAS
        self.canvas=Canvas(self.window,width=500, height=330, highlightthickness=0,bg=BACKGROUND_COLOR)
        self.bg_img=self.canvas.create_image(250,165,image=self.white_bg_img)

        self.question_text=self.canvas.create_text(
            250,
            165,
            width=450,
            font=("Arial",20,"italic"),
            fill="black",
            text="QUESTION"
        )
                                
        self.canvas.grid(row=1,column=0,columnspan=3)

        # BUTTONS
        true_img=PhotoImage(file="Photos/true_button.png")
        self.true_button=Button(image=true_img,highlightthickness=0,border=0,command=self.true_button,bg=BACKGROUND_COLOR)
        self.true_button.grid(row=2,column=0,sticky=E)
        false_img=PhotoImage(file="Photos/false_button.png")
        self.false_button=Button(image=false_img,highlightthickness=0,border=0,command=self.false_button,bg=BACKGROUND_COLOR)
        self.false_button.grid(row=2,column=2,sticky=W)

        # LABELS
        self.score_label=Label(text="SCORE: 0",font=("Cadcadia Case",25,"bold"),bg=BACKGROUND_COLOR)
        self.score_label.grid(row=0,column=0,columnspan=3)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(self.bg_img,image=self.white_bg_img)
        if self.quiz.still_has_questions() :
            self.enable_button()
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text,font=("Arial",20,"italic"),fill="black")
        else :
            self.canvas.itemconfig(self.question_text,text="Quiz Completed")
            self.disable_button()

 
    def true_button(self):
        self.response(self.quiz.check_answer("True"))


    def false_button(self):
        self.response(self.quiz.check_answer("False"))

    def disable_button(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def enable_button(self) :
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
    
    def response(self,is_right) :
        
        if is_right :
            self.canvas.itemconfig(self.bg_img,image=self.correct_img)
            self.score_label.config(text=f"SCORE: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text,text="CORRECT",font=("Arial",30,"bold"),fill="white")
        else :
            self.canvas.itemconfig(self.bg_img,image=self.wrong_img)
            self.canvas.itemconfig(self.question_text,text="WRONG",font=("Arial",30,"bold"),fill="white")
        self.disable_button()
        self.window.after(1000,self.get_next_question)
