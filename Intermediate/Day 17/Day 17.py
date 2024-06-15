from data import questionData
from QuestionModel import Question
from QuizBrain import Brain

questionBank = []

for question in questionData:
    questionBank.append(
        Question(
            question["text"],
            question["answer"]
        )
    )

brain = Brain(0, questionBank)

while brain.questionsRemaining():
    brain.nextQuestion()

print("You've completed the quiz")
print(f"Your final score is : {brain.score}")
