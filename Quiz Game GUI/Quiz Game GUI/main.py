from question_model import Question 
from quiz_brain import QuizBrain
from ui import UserInterface
from data import question_data

question_bank=[]
for dict in question_data : 
    ques=dict["question"]
    ans=dict["correct_answer"]
    temp=Question(ques,ans)
    question_bank.append(temp)

quiz=QuizBrain(question_bank)
ui=UserInterface(quiz)
