import csv 
import random
import time
import os
#Ian and Rifah
print("CPSC Quiz\n")
TESTFILE= "TestBank.csv"

def enter_name():
    '''This code takes users first and last name plust their ID as an input. 
    The ID is taken as 5 numbers and adds the A onto it. 
    Each value is returned to the main. If user takes more than 3 times to
    enter a valid ID then the program stops.
    '''
    fname=input("First Name: ")
    lname=input("Last Name: ")
    usr_id=input("Enter ID (5 Numbers) A-")
    attempts = 0
    while len(usr_id) != 5: ## check to see if ID length is of 5 numbers
        usr_id=input("Enter ID (5 Numbers) A-")
        attempts+=1
        if attempts == 2: ##Once the user attempts to enter ID 3 times program stops
            return 
    user_id= 'A'+usr_id
    return fname,lname,user_id

def get_questions(TESTFILE, used_questions):
    '''This function displays the random questions out of the text
    file that is being read from, if a question has been used it is checked and returned and taken out.
    Line from kist is tajen and printed out onto the screen.'''
    if not used_questions:
        print("No more questions available.")
        return None, None
    
    rand_index = random.randrange(len(used_questions))
    rand_question = used_questions.pop(rand_index)
    
    rand_line = rand_question[0]  # Get question provided from first element of list 
    answer = rand_question[4]
    print(rand_question[0])
    print("a.", rand_question[1], "b.", rand_question[2], "c.", rand_question[3])  # Display each of the three choices provided
    return rand_line, answer
    
def make_results(score, elapsed_time, t_questions, t_answers, user_ans, fname, lname, usr_id):
    '''This program takes all of the users info and writes it to a file containing
    their name and ID, these values were all passed from the main function.'''
    with open(usr_id+"_"+fname+"_"+lname+".txt", "w") as outfile:
        outfile.write(f"Student ID: {usr_id}\n")
        outfile.write(f"First Name: {fname}\n")
        outfile.write(f"Last Name: {lname}\n")
        outfile.write(f"Score: {score}/10\n")
        outfile.write(f"Elapsed Time: {elapsed_time} seconds\n\n")
        outfile.write("Selected questions and answers:\n\n")
        for i in range(len(t_questions)):
            outfile.write(f"Question {i+1}: {t_questions[i]}\n")
            outfile.write(f"Correct Answer: {t_answers[i]}\n")
            outfile.write(f"Your Answer: {user_ans[i]}\n\n")
    
def clear():
    '''This function uses the os module in order to clear the users screen.'''
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def main():
    
    all_questions = []
    with open(TESTFILE, 'r') as file:
        reader = csv.reader(file)
        all_questions = list(reader)
        random.shuffle(all_questions)  # Shuffle questions 
    
    while True:
        start_time = time.time()
        fname, lname, user_id = enter_name()
        counter = 0
        score = 0
        t_questions = []
        t_answers = []
        user_ans = []
        num_questions = int(input("Enter number of questions? 10 or 20: "))
        while num_questions != 10 and num_questions != 20:
            num_questions = int(input("Enter number of questions? 10 or 20: "))
        
        used_questions = all_questions[:]
        while counter < num_questions:
            test_question, cor_answ = get_questions(TESTFILE, used_questions)
            if test_question is None:
                break
            t_questions.append(test_question)
            t_answers.append(cor_answ)
            elapsed_time = time.time() - start_time
            if elapsed_time > 600:  # 10 minutes 
                print("Time's up! Quiz terminated.")
                make_results(score, elapsed_time, t_questions, t_answers, user_ans, fname, lname, user_id)
                print(f"Score: {score}/10")
                return 
        
            answ = input("Enter a answer: ")
            while answ != "a" and answ != "b" and answ != "c":
                answ = input("Enter valid answer (a,b,c)?")
            counter += 1
            user_ans.append(answ)
            if answ.upper() == cor_answ and num_questions == 10:
                score += 1
            elif answ.upper() == cor_answ and num_questions == 20:
                score += .5
            if counter == num_questions:  
                print('Score: ', score)
                end_time = time.time()
                elapsed_time = end_time - start_time
                print('Time:', elapsed_time)
                make_results(score, elapsed_time, t_questions, t_answers, user_ans, fname, lname, user_id)
                option = input("Enter Q to quit program or S to clear screen and start new quiz: ")
                if option.lower() == "q":
                    return
                elif option.lower() == "s":
                    clear()
                    continue 
                else:
                    print("Enter a valid command.")


    
if __name__ == "__main__":
    main()
