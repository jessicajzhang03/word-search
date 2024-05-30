from flask import Flask, render_template
import ws
from random import randint
# import ast

app = Flask(__name__)

@app.route("/")
def launch_word_search():
    board, words = ws.create_board(16, randint(35,39))
    word_list = [word[0] for word in words]
    word_list.sort()

    # use a preloaded board for debugging
    # with open('fixed_board.txt', 'r') as f:
    #     board_string = f.readline()
    #     board = ast.literal_eval(board_string)
    return render_template('index.html', board=board, word_list=word_list)