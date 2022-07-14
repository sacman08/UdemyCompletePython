"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
quiz_questions = open('questions.txt', 'r')
my_quiz_questions = [line.strip() for line in quiz_questions.readlines()]
quiz_questions.close()

score = 0
total_score = len(my_quiz_questions)

for question in my_quiz_questions:
    my_question = question.split('=')
    my_answer = input(f'{my_question[0]}=')
    if my_answer == my_question[1]:
        score += 1

final_score_file = open('results.txt', 'w')
final_score_file.write(f'Your final score is {score}/{total_score}')
final_score_file.close()
