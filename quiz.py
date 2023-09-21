from random import shuffle
from question import Question
from quiz_questions import question_data
class Quiz:
    def __init__(self):
        self.questions = [Question(q["text"], q["answer"]) for q in question_data]
        self.score = 0
        self.current_question_index = 0
        self.shuffle_questions()

    def shuffle_questions(self):
        shuffle(self.questions)

    def next_question(self):
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        else:
            return None

    def do_questions_remain(self):
        return self.current_question_index < len(self.questions)

    def check_answer(self, user_answer):
        current_question = self.next_question()
        if current_question:
            if current_question.check_answer(user_answer):
                self.score += 2
            else:
                self.score -= 1
            self.current_question_index += 1

    def display_score(self):
        print(f"Your final score is: {self.score}")

if __name__ == "__main__":
    quiz = Quiz()
    while quiz.do_questions_remain():
        current_question = quiz.next_question()
        print(f"Question: {current_question.text}")
        user_answer = input("True or False? ").strip()
        quiz.check_answer(user_answer)

    quiz.display_score()
