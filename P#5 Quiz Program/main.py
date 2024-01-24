quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer":"Paris"},

    "question2": {
        "question":"What is the capital of Germany?",
        'answer':'Berlin'},

    'question3': {
        'question':'What is the capital of Georgia?',
        'answer':'Tbilisi'},

    'question4': {
        'question':'What is the capital of Spain?',
        'answer':'Madrid'},

    'question5': {
        'question':'What is the capital of Italy?',
        'answer':'Rome'},

    'question6': {
        'question':'What is the capital of Russia?',
        'answer':'Moscow'}
}
correct = 0
wrong = 0
score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        correct = correct + 1
        score = correct
        print('Your score is: ', score)

    else:
        print('Wrong')
        print('The answer is: ' + value['answer'])
        wrong = wrong + 1
        score = correct
        print('Your score is: ', score)

print('You have', correct, 'out of 6 question correctly')
print('Your percentage is ', int((correct/6)*100), '%')





















