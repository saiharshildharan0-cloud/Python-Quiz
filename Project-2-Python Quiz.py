#Python Project-Quiz

print('''----PYTHON QUIZ-----
Welcome to the Python Quiz!!! Thank you for
taking part in this Quiz. Let's test the bright
knowledge you possess.
------------------------------------------------
INSTRUCTIONS:-
--------------
1. The quiz is based on planets and galaxies.
2. The quiz will be divided into three sections:-easy, medium and hard. The first five questions belong to the easy section, the next five to the medium and the last five to the hard section.
3. A total of 15 questions will be asked.
4. Your total score will be displayed after the quiz has ended.
5. All questions are mandatory.
6. Each question has 1 point.
---------------------------------------------------------------------------------------''')

choice=input("Do you wish to still continue? Yes/No:")

answers=list() #List stores the user's answers.
if choice=="Yes":
    print("BEST OF LUCK!!!")
    my_file=open("Questions.txt","r") #The file has questions in it.
    questions=my_file.readlines()
    for question in questions:
        print(question)
        answer=input("Enter your answer:")
        answers.append(answer)
    print("Your answers:-",answers)

my_file2=open("Answers.txt","r") #Contains answers.
answers_1=my_file2.readlines()
modified_answers=list() #Answers are modified after removing spaces and newline chracters.
for answer in answers:
    answer=answer.strip()
    modified_answers.append(answer)
print("Quiz answers:-",modified_answers)

score=0 #Gives the final score.
for i in range(len(modified_answers)):
    if modified_answers[i]==answers[i]:
        score+=1
print("Your final score is",score,"out of",len(modified_answers),".")

print("-----Thanks for playing!!!-----")

my_file.close()
my_file2.close()



    
