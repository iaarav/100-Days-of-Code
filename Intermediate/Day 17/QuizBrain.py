class Brain:
    def __init__(self, questionNo, questionList):
        self.questionNo = questionNo
        self.score = 0
        self.questionList = questionList

    def questionsRemaining(self):
        if self.questionNo < len(self.questionList):
            return True
        else:
            return False

    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNo]
        self.questionNo += 1
        userAnswer = input(f"Q. {self.questionNo}: {currentQuestion.text} (True/False): ").lower()

        self.checkAnswer(userAnswer=userAnswer, correctAnswer=currentQuestion.answer)

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer == correctAnswer.lower():
            self.score += 1
            print("You got it right!!")
        else:
            print("You got it wrong!!")

            print(f"The correct answer was {correctAnswer}")
        print(f"The score is: {self.score}/{self.questionNo}")
