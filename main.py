from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    # Random number chosen
    random_number = random.randint(1, 100)
    if request.method == 'POST':
        user_guess = request.form['guess']
        guess = int(user_guess)
        if guess < 1 or guess > 100:
            return '<h1> Your guess must be between 1 and 100. </h1>' \
                   '<img src="https://media.giphy.com/media/8L0Pky6C83SzkzU55a/giphy.gif">'
        elif guess > random_number:
            return '<h1> The guess is too high. </h1>' \
                   '<img src="https://media.giphy.com/media/l4pLY0zySvluEvr0c/giphy.gif">'
        elif guess < random_number:
            return '<h1> The guess is too low. </h1>' \
                   '<img src="https://media.giphy.com/media/l4pLY0zySvluEvr0c/giphy.gif">'
        else:
            return '<h1> Correct guess, Well done </h1>' \
                '<br/> <img src="https://media.giphy.com/media/MEdXzJwmTvjpw79Gig/giphy.gif">'
    return render_template('index.html', number=random_number)


if __name__ == "__main__":
    app.run(debug=True)
