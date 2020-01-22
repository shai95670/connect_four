import circle, math, pygame
#from pygame.locals import *

connect_four_grid = []
dict_of_bounderies = {0: 52, 52: 112, 112: 172, 172: 232, 232: 292, 292: 352, 352: 412}
current_player = 'red'
NUMBER_OF_CIRCLES_TO_WIN = 4
number_of_turns = 0
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


# will mark on the gui available dropping spaces
# in color
# highest row which has zeros as values in it
# start looping through connect_four_gui from the last index
# check for each (not circle_object.filled)
# return a list of strings of the format 'row:column'
# which can then be used to check for the correct
# circle_object to color for the user 
# so that he knows available circles to click
def get_lowest_available_row(game_grid, column_number_to_search):
    list_of_circle_objects_to_search = [value[column_number_to_search] for value in game_grid]
    
    for index in range(len(list_of_circle_objects_to_search)-1, 0, -1):
        is_lowest_circle = list_of_circle_objects_to_search[index].lowest_circle
        is_filled = (not list_of_circle_objects_to_search[index].filled)
        if is_lowest_circle and is_filled:
           return index    
        
           
# Create the connect four circles at the start of the game
# since they are there at the start
# they should all have their attribute filled as false
# 640X400
# called once at the start
def create_board_circle_objects(game_grid):
    row_of_circle_objects = []
    x = 40
    y = 40

    for index in range(43):
        if index % 7 == 0 and index > 6:
           y += 60 # incresse y
           x = 40
           game_grid.append(row_of_circle_objects)
           row_of_circle_objects = []

        row_of_circle_objects.append(circle.BoardCirlce(WHITE, False, x, y, False))
        x += 60


# called once at the start of the game        
def set_first_seven_lowest_circles(game_grid):
    # Set last rows lowest_circle attribute to True
    for circle_object in game_grid[5]:
        circle_object.lowest_circle = True              


# TODO: REFACTOR THIS FUNCTION
# loop through the first row of circle objects
# based on where the user clicked get the coordinates
# check at which column the user clicked and return it?
# run through a single list and not a 2d list
# improvment from o(n)2
# call the function get_clicked_column ?
# key:value pairs where key is left boundery
# right is right boundery ie 30:40
def get_number_of_clicked_column(bounderies):
    index = 0
    mouse_x_y_positions = pygame.mouse.get_pos()
    for key, value in bounderies.items():
        if mouse_x_y_positions[0] >= key and mouse_x_y_positions[0] <= value:
           return index
        index += 1                


"""
 Refactor check_four_in_a_row_verticaly and check_four_in_a_row_horizantly and
 check_four_in_a_row_diagnoly into one function
"""
def check_four_in_a_row_verticaly(circle_object, current_row, current_column, game_grid):
    if (circle_object.color != game_grid[current_row-1][current_column].color and
        not circle_object.color == (255, 255, 255)):
        return False
    
    circles_in_a_row = 1 # always assume we start with one 
    column_to_decrement = current_column
    
    for index in range(3):
        column_to_decrement -= 1
        if (circle_object.color == game_grid[current_row][column_to_decrement].color and
            not circle_object.color == (255, 255, 255)):
           circles_in_a_row += 1
    if circles_in_a_row == NUMBER_OF_CIRCLES_TO_WIN:
       return True
    else:
       return False        
   
      
def check_four_in_a_row_horizantly(circle_object, current_row, current_column, game_grid):
    if (circle_object.color != game_grid[current_row][current_column+1].color and
        not circle_object.color == (255, 255, 255)):
        return False
     
    circles_in_a_row = 1 # always assume we start with one
    column_to_increment = current_column
    for index in range(3):
        column_to_increment += 1
        print(current_row, column_to_increment)
        if (circle_object.color == game_grid[current_row][column_to_increment].color and
            not circle_object.color == (255, 255, 255) and not column_to_increment > 6):
            circles_in_a_row += 1
    
    if circles_in_a_row == NUMBER_OF_CIRCLES_TO_WIN:
       return True
    else:
       return False 
            
                   
def check_four_in_a_row_diagnoly(circle_object, current_row, current_column, game_grid):            
    if (circle_object.color != game_grid[current_row-1][current_column+1].color and
        not circle_object.color == (255, 255, 255)):
        return False
    
    circles_in_a_row = 1 # always assume we start with one
    column_to_increment = current_column
    row_to_decrement = current_row
    for index in range(3):
        column_to_increment += 1
        row_to_decrement -= 1
        if (circle_object.color == game_grid[row_to_decrement][column_to_increment].color and
            not circle_object.color == (255, 255, 255)):
           circles_in_a_row += 1
        if column_to_increment == 6 or row_to_decrement == 0:
           break    
    
    if circles_in_a_row == NUMBER_OF_CIRCLES_TO_WIN:
       return True
    else:
       return False 
  
        
# start checking after four turns
# then check after each move by a player
# return '' if no winner or return color of winner
def check_winner(game_grid):
    
    for row in range(len(game_grid)-1, 0, -1):
        for column in range(len(game_grid[row])):
            if (check_four_in_a_row_horizantly(game_grid[row][column], row, column, connect_four_grid) or
                check_four_in_a_row_verticaly(game_grid[row][column], row, column, connect_four_grid) or
                check_four_in_a_row_diagnoly(game_grid[row][column], row, column, connect_four_grid) and 
                game_grid[row][column].filled):
               return game_grid[row][column].color
    return ''           

           
def set_color_for_circle(game_grid, column_to_set, row_to_set, color=YELLOW):
    game_grid[row_to_set][column_to_set].set_color(color)    


def fill_circle(game_grid, column_to_fill, row_to_fill):
    game_grid[row_to_fill][column_to_fill].set_filled(True)

def set_lowest_circle(game_grid, column_to_set, row_to_set):
    game_grid[row_to_set][column_to_set].set_lowest_circle(False)
    game_grid[row_to_set - 1][column_to_set].set_lowest_circle(True)


# game_grid[clicked_circles_row][clicked_circles_column].fill_circle(players_color)

 
# should be called every few sec
def draw_board_circles(game_grid, game_surface):
    for row in game_grid:
        for circle_object in row:
            circle_object.draw_circle(game_surface)
 
          
class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.weight, self.height = 440, 440
        self.clock = None


    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('connect_four')
        self.set_fps()
       
        
    def set_fps(self):
        self.clock = pygame.time.Clock()
    
     
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONUP:
           column_clicked = get_number_of_clicked_column(dict_of_bounderies)
           row_of_circle = get_lowest_available_row(connect_four_grid, column_clicked) 
           global current_player, number_of_turns  
           if current_player == 'red':
              set_color_for_circle(connect_four_grid, column_clicked, row_of_circle, RED)
              current_player = 'yellow'
           else:
              # run with default yellow argument 
              set_color_for_circle(connect_four_grid, column_clicked, row_of_circle) 
              current_player = 'red'                  
           set_lowest_circle(connect_four_grid, column_clicked, row_of_circle)
           fill_circle(connect_four_grid, column_clicked, row_of_circle)
           number_of_turns += 1
           
           if number_of_turns == 4:
              print(check_winner(connect_four_grid))
        
    def on_render(self):
        draw_board_circles(connect_four_grid, self.screen)
        

    def on_cleanup(self):
        pygame.quit()


    def on_execute(self):
        self.on_init()

        while (self._running): # main game loop                                                                                                                                           
            for event in pygame.event.get():
                self.on_event(event)
            self.screen.fill(BLUE)
            self.on_render()
            
            pygame.display.update()
            self.clock.tick(60)
            
        self.on_cleanup()


if __name__ == "__main__":
    create_board_circle_objects(connect_four_grid)
    set_first_seven_lowest_circles(connect_four_grid)
    theApp = App()
    theApp.on_execute()
