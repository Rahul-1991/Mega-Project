from random import randint

class QuizMaker(object):

    def __init__(self):
        self.file_handle = None
        self.question_list = list()

    def get_quiz_info(self):
        file_name = raw_input('Enter quiz file name with path : ')
        num_question = raw_input('Enter number of questions for quiz : ')
        return file_name, int(num_question)

    def get_file_handle(self, file_name):
        self.file_handle = open(file_name)

    def get_question_list(self):
        self.question_list = self.file_handle.readlines()

    def get_question_count(self):
        return len(self.question_list)

    def prepare_question_set(self):
        filename, num_question = self.get_quiz_info()
        self.get_file_handle(filename)
        self.get_question_list()
        total_question_count = len(self.question_list)
        quiz_question = list()
        for i in range(num_question):
            while True:
                question = self.question_list[randint(0, total_question_count-1)]
                if question not in quiz_question:
                    quiz_question.append(question)
                    break
        return quiz_question

    def print_question_for_quiz(self):
        quiz_question = self.prepare_question_set()
        for question in quiz_question:
            print question.strip()

quizmaker = QuizMaker()
quizmaker.print_question_for_quiz()
