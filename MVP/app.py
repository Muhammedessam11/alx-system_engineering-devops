from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for workouts
workouts = []

@app.route('/')
def index():
    return render_template('index.html', workouts=workouts)

@app.route('/add_workout', methods=['POST'])
def add_workout():
    workout_name = request.form['workout_name']
    duration = request.form['duration']
    calories = request.form['calories']
    workouts.append({'workout_name': workout_name, 'duration': duration, 'calories': calories})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
