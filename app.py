from flask import Flask, render_template, jsonify, request
from Reversi import beginning_board, is_valid_move, change_discs, red, black

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['GET'])
def start_game():
    board = beginning_board()
    return jsonify(board=board, player=red)

@app.route('/make_move', methods=['POST'])
def make_move():
    data = request.json
    board = data['board']
    row = data['row']
    col = data['col']
    player = data['player']
    
    if is_valid_move(board, row, col, player):
        board[row][col] = player
        change_discs(board, row, col, player)
        player = 3 - player
        return jsonify(board=board, player=player, valid=True)
    else:
        return jsonify(valid=False)

if __name__ == '__main__':
    app.run(debug=True)
