# some of this thieved from
# https://medium.com/@msgold/creating-a-word-search-puzzle-b499533e938
# hahaha. i am a THIEF. uh oh!

import requests
import random
import string



def word_placements(board, word):
    placed = False
    tries = 0

    placements = []
    # element is a list consisting of:
    #   an ordered pair (row, col)
    #   an orientation: negative means ``backwards''
    #   the number of crossings

    max_crossings = 0

    for orientation in range(1, 5):
        # TODO: ADD DIAGONALS!!!
        if orientation == 1: # horizontal
            for row in range(len(board)):
                for col in range(len(board)-len(word)+1):
                    left_to_right = True
                    left_to_right_crossings = 0
                    right_to_left = True
                    right_to_left_crossings = 0

                    for i, c in enumerate(range(col, col+len(word))):
                        if board[row][c] != '-':
                            if board[row][c] != word[i]:
                                left_to_right = False
                                break
                            left_to_right_crossings += 1

                    for i, c in enumerate(range(col, col+len(word))):
                        if board[row][c] != '-':
                            if board[row][c] != word[-i-1]:
                                right_to_left = False
                                break
                            right_to_left_crossings += 1

                    if left_to_right:
                        if left_to_right_crossings == max_crossings:
                            placements.append((row, col, 1, left_to_right_crossings))
                        elif left_to_right_crossings > max_crossings:
                            placements = [(row, col, 1, left_to_right_crossings)]
                            max_crossings = left_to_right_crossings
                    if right_to_left:
                        if right_to_left_crossings == max_crossings:
                            placements.append((row, col, -1, right_to_left_crossings))
                        elif right_to_left_crossings > max_crossings:
                            placements = [(row, col, -1, right_to_left_crossings)]
                            max_crossings = right_to_left_crossings

        if orientation == 2: # vertical
            for row in range(len(board)-len(word)+1):
                for col in range(len(board)):
                    top_to_bottom = True
                    top_to_bottom_crossings = 0
                    bottom_to_top = True
                    bottom_to_top_crossings = 0

                    for i, r in enumerate(range(row, row+len(word))):
                        if board[r][col] != '-':
                            if board[r][col] != word[i]:
                                top_to_bottom = False
                                break
                            top_to_bottom_crossings += 1

                    for i, c in enumerate(range(col, col+len(word))):
                        if board[r][col] != '-':
                            if board[r][col] != word[-i-1]:
                                bottom_to_top = False
                                break
                            bottom_to_top_crossings += 1

                    if top_to_bottom:
                        if top_to_bottom_crossings == max_crossings:
                            placements.append((row, col, 2, top_to_bottom_crossings))
                        elif top_to_bottom_crossings > max_crossings:
                            placements = [(row, col, 2, top_to_bottom_crossings)]
                            max_crossings = top_to_bottom_crossings
                    if bottom_to_top:
                        if bottom_to_top_crossings == max_crossings:
                            placements.append((row, col, -2, bottom_to_top_crossings))
                        elif bottom_to_top_crossings > max_crossings:
                            placements = [(row, col, -2, bottom_to_top_crossings)]
                            max_crossings = bottom_to_top_crossings

        if orientation == 3:
            for row in range(len(board)-len(word)+1):
                for col in range(len(board)-len(word)+1):
                    nw_to_se = True
                    nw_to_se_crossings = 0
                    se_to_nw = True
                    se_to_nw_crossings = 0

                    for i, (r,c) in enumerate(zip(range(row, row+len(word)),
                                                  range(col, col+len(word)))):
                        if board[r][c] != '-':
                            if board[r][c] != word[i]:
                                nw_to_se = False
                                break
                            nw_to_se_crossings += 1

                    for i, (r,c) in enumerate(zip(range(row, row+len(word)),
                                                  range(col, col+len(word)))):
                        if board[r][c] != '-':
                            if board[r][c] != word[-i-1]:
                                se_to_nw = False
                                break
                            se_to_nw_crossings += 1

                    if nw_to_se:
                        if nw_to_se_crossings == max_crossings:
                            placements.append((row, col, 3, nw_to_se_crossings))
                        elif nw_to_se_crossings > max_crossings:
                            placements = [(row, col, 3, nw_to_se_crossings)]
                            max_crossings = nw_to_se_crossings

                    if se_to_nw:
                        if se_to_nw_crossings == max_crossings:
                            placements.append((row, col, -3, se_to_nw_crossings))
                        elif se_to_nw_crossings > max_crossings:
                            placements = [(row, col, -3, se_to_nw_crossings)]
                            max_crossings = se_to_nw_crossings

        if orientation == 4:
            for row in range(len(word)-1, len(board)):
                for col in range(len(board)-len(word)+1):
                    sw_to_ne = True
                    sw_to_ne_crossings = 0
                    ne_to_sw = True
                    ne_to_sw_crossings = 0

                    for i, (r,c) in enumerate(zip(range(row, row-len(word), -1),
                                                  range(col, col+len(word)))):
                        if board[r][c] != '-':
                            if board[r][c] != word[i]:
                                sw_to_ne = False
                                break
                            sw_to_ne_crossings += 1

                    for i, (r,c) in enumerate(zip(range(row, row-len(word), -1),
                                                  range(col, col+len(word)))):
                        if board[r][c] != '-':
                            if board[r][c] != word[-i-1]:
                                ne_to_sw = False
                                break
                            ne_to_sw_crossings += 1

                    if sw_to_ne:
                        if sw_to_ne_crossings == max_crossings:
                            placements.append((row, col, 4, sw_to_ne_crossings))
                        elif sw_to_ne_crossings > max_crossings:
                            placements = [(row, col, 4, sw_to_ne_crossings)]
                            max_crossings = sw_to_ne_crossings

                    if ne_to_sw:
                        if ne_to_sw_crossings == max_crossings:
                            placements.append((row, col, -4, ne_to_sw_crossings))
                        elif se_to_nw_crossings > max_crossings:
                            placements = [(row, col, -4, ne_to_sw_crossings)]
                            max_crossings = ne_to_sw_crossings


    if placements:
        # placements.sort(key=lambda placement:placement[-1], reverse=True)
        # return placements[0]
        return random.choice(placements)

    return False

def place_word(board, word, row, col, orientation):
    if orientation == 1:
        for i, c in enumerate(range(col, col+len(word))):
            board[row][c] = word[i]
    elif orientation == 2:
        for i, r in enumerate(range(row, row+len(word))):
            board[r][col] = word[i]
    elif orientation == 3:
        for i, (r,c) in enumerate(zip(range(row, row+len(word)),
                                      range(col, col+len(word)))):
            board[r][c] = word[i]
    elif orientation == 4:
        for i, (r,c) in enumerate(zip(range(row, row-len(word), -1),
                                      range(col, col+len(word)))):
            board[r][c] = word[i]

def fill_empty(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == '-':
                board[row][col] = random.choice(string.ascii_uppercase)

def create_word_search(words, size, max_words=float('inf')):
    board = [['-' for _ in range(size)] for _ in range(size)]

    word_list = []
    words_placed = 0
    words_since_last_placed = 0

    for word in words:
        original_word = word
        words_since_last_placed += 1

        # placement of word with maximal crossings
        placement = word_placements(board, word)

        if placement:
            row, col, orientation, max_crossings = placement
            if max_crossings >= 3 or (words_since_last_placed >= 10):
                if orientation < 0:
                    word = word[::-1]
                    orientation = -orientation
                place_word(board, word, row, col, orientation)
                words_since_last_placed = 0
                word_list.append([original_word, placement])
                words_placed += 1

        if words_placed == max_words:
            break

    # fill_empty(board)

    for i in range(len(word_list)):
        word_info = word_list[i]
        print(f'{i+1}. {word_info[0]} at ({word_info[1][0]}, {word_info[1][1]}) with {word_info[1][3]} crossings in direction {word_info[1][2]}')

    return board

def display_board(board):
    for row in board:
        print(' '.join(row))

def create_board(size, max_words=float('inf'), word_list_length=1000):
    url = f'https://random-word-api.herokuapp.com/word?number={word_list_length}'
    response = requests.get(url)
    words = [word.upper() for word in response.json() if size >= len(word) >= 4]
    print(words)
    print(f'total words: {len(words)}')
    board = create_word_search(words, size, max_words)
    return board

if __name__ == '__main__':
    board = create_board(16, 40)
    display_board(board)


# 20x20 grid comes with roughly 60 words if trying 1000
# 16x16 grid comes with roughly 40 words if trying 1000
