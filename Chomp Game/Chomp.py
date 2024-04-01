import pygame
import time
robot_img = pygame.image.load("robot.jpg") 
human_img = pygame.image.load("human.jpg")  


rows = 6
col = 6

class Chomp:
    def __init__(self, board, poisoned, rows, col, Humanscore, AIscore, GameState,turn):
        self.board = board
        self.poisoned = poisoned
        self.rows = rows
        self.col = col
        self.board[poisoned[0]][poisoned[1]] = False
        self.Humanscore = Humanscore
        self.AIscore = AIscore
        self.GameState = GameState
        self.turn=turn

def Displayboard(chompy):
    print("---------------------------------")
    for i in range(chompy.rows):
        for j in range(chompy.col):
            print(chompy.board[i][j], "\t", end="")
        print("\n")
    print("Human Score is: ", chompy.Humanscore)
    print("AI Score is: ", chompy.AIscore)

def CheckMoveValidity(board, i, j):
    i = int(i)  
    j = int(j)  

    if i == len(board) - 1 and j == 0:
        print("You have eaten the Poisoned Chocolate")
        return -1

    if 0 <= i < len(board) and 0 <= j < len(board[0]):
        return True 
    
    print("You have entered an invalid move, Try Again")
    return False

def EatChoccy(chompy, i, j, turn):
    for x in range(i, -1, -1):
        for y in range(j, len(chompy.board[0])):
            if CheckMoveValidity(chompy.board, x, y):
                if turn == "Human" and chompy.board[x][y]==True:
                    chompy.board[x][y] = "H_Ate"
                    chompy.Humanscore += 1
                elif turn == "AI" and chompy.board[x][y]==True:
                    chompy.board[x][y] = "A_Ate"
                    chompy.AIscore += 1

def Minimax(chompy):
    possible_moves = []
    for i in range(chompy.rows):
        for j in range(chompy.col):
            if chompy.board[i][j]:
                possible_moves.append((i, j))
    
    choices = []
    highscore = 0
    X_Cord = 0
    Y_Cord = 0

    while possible_moves:
        move = possible_moves.pop()
        i, j = move[0], move[1]
        score = 0

        for x in range(i, -1, -1):
            for y in range(j, len(chompy.board[0])):
                if CheckMoveValidity(chompy.board, x, y) and chompy.board[x][y]==True:
                    score += 1
        choices.append((move, score))

        if highscore < score:
            highscore = score
            X_Cord = i
            Y_Cord = j
    
    print(choices)
    if highscore == 0:
        X_Cord = chompy.rows - 1
        Y_Cord = 0
        return -1
    EatChoccy(chompy, X_Cord, Y_Cord, "AI")  

    return None  




def initialize_pygame(chompy):
    pygame.init()
    chompy.screen = pygame.display.set_mode((chompy.col * 100, chompy.rows * 100))
    pygame.display.set_caption("Chomp Game")

def draw_board(chompy):
    chompy.screen.fill((245, 245, 245))  

    for i in range(chompy.rows):
        for j in range(chompy.col):
            if chompy.board[i][j] == True or chompy.board[i][j] == False:
                color = (153, 102, 51)
                pygame.draw.circle(chompy.screen, color, (j * 100 + 50, i * 100 + 50), 30, 0)  # Draw a circle with anti-aliasing
            elif chompy.board[i][j] == "H_Ate":
                color=(0, 204, 153)  # Dark brown for human
                pygame.draw.circle(chompy.screen, color, (j * 100 + 50, i * 100 + 50), 30, 0)  # Draw a circle with anti-aliasing
            elif chompy.board[i][j] == "A_Ate":
                color=(255, 102, 153)
                pygame.draw.circle(chompy.screen, color, (j * 100 + 50, i * 100 + 50), 30, 0)  # Draw a circle with anti-aliasing

    pygame.display.flip()  # Update the display


      


def handle_events(chompy):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            chompy.GameState = "Quit"
            return False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // 100
            col = x // 100

            if row == chompy.rows - 1 and col == 0:
                chompy.GameState = "Lost"
                draw_board(chompy)
                Displayboard(chompy)
                return False
            
            if chompy.board[row][col] != True:
                print("Please select an unselected cell.")
                return True
            
            if chompy.GameState != "Won" and chompy.GameState != "Lost":
                if chompy.turn == "Human":
                    EatChoccy(chompy, row, col, "Human")
                    chompy.turn = "AI"  
                    draw_board(chompy)
                    Displayboard(chompy)

                if chompy.turn == "AI":
                    ans = Minimax(chompy)

                    if ans == -1:
                        chompy.GameState = "Won"
                        draw_board(chompy)
                        Displayboard(chompy)
                        return False
                    else:
                        draw_board(chompy)
                        Displayboard(chompy)
                        chompy.turn = "Human"
    pygame.display.flip()
    return True




board = [[True for _ in range(col)] for _ in range(rows)]
chompy = Chomp(board, (rows - 1, 0), rows, col, 0, 0, None,"Human")
initialize_pygame(chompy)
draw_board(chompy)
running = True
while running:
    running = handle_events(chompy)


if(chompy.GameState=="Won"):
    print("You Won")
    chompy.screen.fill((245, 245, 245))
    font = pygame.font.Font(None, 50)
    text = font.render("You Won", True, (255, 0, 0))
    text_rect = text.get_rect(center=(chompy.col * 50, chompy.rows * 50))
    chompy.screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(3)

    scaled_human_img = pygame.transform.scale(human_img, (600, 600))  
    chompy.screen.blit(scaled_human_img, (0, 0))  
    pygame.display.flip()
    time.sleep(3)
else:
    print("You Lost")
    
    chompy.screen.fill((245, 245, 245))
    font = pygame.font.Font(None, 50)
    text = font.render("You Lost", True, (255, 0, 0))
    text_rect = text.get_rect(center=(chompy.col * 50, chompy.rows * 50))
    chompy.screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(3)

    scaled_robot_img = pygame.transform.scale(robot_img, (600, 600))  
    chompy.screen.blit(scaled_robot_img, (0, 0))  
    pygame.display.flip()
    time.sleep(3)


pygame.quit()
