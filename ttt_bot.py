import random
import copy


# takes the field and returns a list of all possible Moves
# Each possible move is a touple in the Form (y-coordinate, x-coordinate)
def getPlayableMoves(field):
    playableMoves = []
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] == 0:
                playableMoves.append((i, j))
    return playableMoves


def testForWin(field):
    for i in range(3):
        if field[i][0] == field[i][1] and field[i][1] == field[i][2]:
            if field[i][0] == 1:
                return "lose"
            elif field[i][0] == 2:
                return "win"
        if field[0][i] == field[1][i] and field[1][i] == field[2][i]:
            if field[0][i] == 1:
                return "lose"
            elif field[0][i] == 2:
                return "win"
    if field[0][0] == field[1][1] and field[1][1] == field[2][2]:
        if field[1][1] == 1:
            return "lose"
        elif field[1][1] == 2:
            return "win"
    if field[0][2] == field[1][1] and field[1][1] == field[2][0]:
        if field[1][1] == 1:
            return "lose"
        elif field[1][1] == 2:
            return "win"
    for i in field:
        for j in i:
            if j == 0:
                return 0
    return "draw"


def randomMove(moves):
    randomMove = random.randint(0, len(moves) - 1)
    return moves[randomMove]


def playRandomGame(field, y, x):
    testField = copy.deepcopy(field)
    testField[y][x] = 2
    moves = getPlayableMoves(testField)
    n = len(moves)
    player = 0

    for i in range(n):
        moves = getPlayableMoves(testField)
        # print(getPlayableMoves(testField))
        y, x = randomMove(moves)
        testField[y][x] = player + 1
        if testForWin(testField) != 0:
            return testForWin(testField)
        else:
            player = (player + 1) % 2
        # print(str(testField[0]) + '\n' + str(testField[1]) + '\n' + str(testField[2]))
        # print("---------------" + str(i + 1))
    return 0


# recieves a 3x3 Tik-tak-toe grid where: 0 = Empty, 1 = Player, 2 = Bot
# Field shape = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
def makeMove(field):
    moves = getPlayableMoves(field)
    ratings = []
    best = 0
    for m in moves:
        y, x = m
        count = 0
        for i in range(2000):  # the higher the better
            result = playRandomGame(field, y, x)
            if result == "win":
                count = count + 2
            elif result == "draw":
                count = count + 1
        ratings.append(count)

        currentLargest = 0
        for i in range(len(ratings)):
            if ratings[i] > currentLargest:
                best = i
                currentLargest = ratings[i]            
    #print("------" + str(best) + "-----------")
    #print(ratings)
    return moves[best]
    
