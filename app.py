from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS, cross_origin
import os
from datetime import datetime

app = Flask(__name__)
cors = CORS(app)
app.secret_key = 'your_secret_key'  # Required for session management

# Directory path for question files

# Get a list of question files


@app.route("/lerntypanalyse", methods=["GET", "POST"])
@cross_origin()
def submit():
    question_path = 'lerntyp'
    items = os.listdir(question_path)
    number_of_questions = len(items)
    # Initialize `current_question` and category scores if they don’t already exist in the session
    """if 'current_question' not in session:
        session['current_question'] = 0
    if 'bild' not in session:
        session['bild'] = 0
    if 'auditiv' not in session:
        session['auditiv'] = 0
    if 'lesen' not in session:
        session['lesen'] = 0
    if 'motorisch' not in session:
        session['motorisch'] = 0"""


    current_question = request.args.get('current_question')#session['current_question']
    bild = request.args.get('bild')
    auditiv = request.args.get('auditiv')
    lesen = request.args.get('lesen')
    motorisch = request.args.get('motorisch')

    # Load the current question file
    file_path = f'{question_path}/{current_question}.frage'
    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8') as file:
            content = file.read().splitlines()
        
        frage = content[0]
        option_1 = content[1]
        option_2 = content[3]
        option_3 = content[5]
        option_4 = content[7]

        if request.method == "POST":
            # Retrieve user's selected button
            button_value = request.args.get('button_value')
            index = None

            # Determine which option was selected and update the respective category score
            if button_value == 'button1':
                index = 2
            elif button_value == 'button2':
                index = 4
            elif button_value == 'button3':
                index = 6
            elif button_value == 'button4':
                index = 8
            
            # Update the score in the appropriate category
            if index is not None:
                if content[index] == '1':
                    bild += 1
                elif content[index] == '2':
                    auditiv += 1
                elif content[index] == '3':
                    lesen += 1
                elif content[index] == '4':
                    motorisch += 1
                else:
                    pass

            # Move to the next question or end the quiz
            if current_question < number_of_questions - 1:
                session['current_question'] += 1
                return redirect(url_for('submit'))
            else:
                # Final scores for display
                final_scores = {
                    'bild': bild,
                    'auditiv': auditiv,
                    'lesen': lesen,
                    'motorisch': motorisch
                }
                # Clear session data for a fresh start
                session.clear()
                return {'scores': final_scores} # render_template("result.html", scores=final_scores)

        # Render the question template for GET requests
        return {'frage': frage, 'option_1': option_1, 'option_2': option_2, 'option_3': option_3, 'option_4': option_4, 'bild': bild,
                    'auditiv': auditiv,
                    'lesen': lesen,
                    'motorisch': motorisch, 'current_question': current_question} # render_template("lerntypanalyse.html", frage=frage, option_1=option_1, option_2=option_2, 
                               # option_3=option_3, option_4=option_4)

    # If no questions are available
    # return render_template("index.html")

@app.route("/example", methods=["GET", "POST"])
def example():
    question_path = 'example'
    items = os.listdir(question_path)
    number_of_questions = len(items)
    
    # Initialize `current_question` and category scores if they don’t already exist in the session
    if 'current_question_example' not in session:
        session['current_question_example'] = 0
    if 'punkte_example' not in session:
        session['punkte_example'] = 0
    if 'result_example' not in session:
        session['result_example'] = 0
    if 'correct_result_example' not in session:
        session['correct_result_example'] = 0

    current_question = session['current_question_example']
    score = session['punkte_example']
    correct_result = session['correct_result_example']

    # Load the current question file
    file_path = f'{question_path}/{current_question}.frage'
    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8') as file:
            content = file.read().splitlines()
        
        frage = content[0]
        answer = content[1]
        option_1 = content[2]
        option_2 = content[3]
        option_3 = content[4]
        option_4 = content[5]

        if request.method == "POST":
            # Retrieve user's selected button
            button_value = request.form.get('button_value')
            if button_value == 'button1':
                selected_option = option_1
            elif button_value == 'button2':
                selected_option = option_2
            elif button_value == 'button3':
                selected_option = option_3
            elif button_value == 'button4':
                selected_option = option_4

            # Check if the answer is correct
            if selected_option == answer:
                result = "richtig"
            else:
                result = "falsch"
                correct_result = answer

            # Move to the next question or end the quiz
            if current_question < number_of_questions - 1:
                session['current_question_example'] += 1
                return render_template("example.html", result=result, answer=correct_result)  # Change to 'example' to reflect this function
            else:
                final_score = score
                session.clear()
                return render_template("result_example.html", score=final_score)

        # Render the question template for GET requests
        return render_template("example.html", frage=frage, option_1=option_1, option_2=option_2, 
                               option_3=option_3, option_4=option_4)

    # If no questions are available
    return render_template("index.html", message="No more questions available.")

@app.route("/", methods=["GET", "POST"])
def start():
    current_datetime = datetime.now()
    today = current_datetime.date()

    if 'confirmation' not in session:
        session['confirmation'] = 0
    if 'name' not in session:
        session['name'] = 0
    if 'can_go_home' not in session:
        session['can_go_home'] = 0
    if 'day_until_exam' not in session:
        session['day_until_exam'] = 0

    confirmation = session['confirmation']
    name = session['name']
    can_go_home = session['can_go_home']
    day_until_exam = session['day_until_exam']

    if request.method == "POST":
        name = request.form.get('name')
        notenziel = request.form.get('notenziel')
        day = request.form.get('day')
        month = request.form.get('month')
        year = request.form.get('year')
        date = datetime(int(year), int(month), int(day))
        date = date.date()
        difference = date - today
        day_until_exam = difference.days
        if notenziel:
            confirmation = "gespeichert"
            can_go_home = True
        else:
            confirmation = "nicht gespeichert"
        return {'test': confirmation}#render_template("start.html", confirmation=confirmation, name=name, can_go_home=can_go_home, day_until_exam=day_until_exam)

    return render_template("start.html")

@app.route("/home")
def home():
    # Reset quiz progress on home page load
    session.clear()
    return render_template("index.html")

@app.route("/chatgpt")
def chatgpt():
    return render_template("chatgpt.html")

if __name__ == "__main__":
    app.run(debug=True)
