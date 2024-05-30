from flask import Flask, render_template
import ws
import ast

app = Flask(__name__)

@app.route("/")
def launch_word_search():
    # board = ws.create_board(16, 1)

    # use a preloaded board for debugging
    with open('fixed_board.txt', 'r') as f:
        board_string = f.readline()
        board = ast.literal_eval(board_string)
    return render_template('index.html', board=board)