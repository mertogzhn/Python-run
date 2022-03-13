from traceback import print_tb


class Question:
    def __init__(self,text,choices,answer) -> None:
        self.text= text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        return self.answer==answer

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text} ")

        for q in question.choices:
            print("-" + q)

        answer = input("cevap : ")
        print(question.checkAnswer(answer))
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question=self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()
    
    def showScore(self):
        print('score: ', self.score)


q1=Question("en iyi programla dili hangisidir?",["c#","python","java","js"],"python")
q2=Question("en popüler programla dili hangisidir?",["java","c#","python","js"],"python")
q3=Question("en çok kazandiran programla dili hangisidir?",["c#","java","js","python"],"python")

questions=[q1,q2,q3]

quiz=Quiz(questions)

quiz.displayQuestion()

