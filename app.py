import circle, math
from pygame.locals import *

connect_four_grid = []
POTENTIAL_CLICKED_CIRCLE_COORDINATES = None
NUMBER_OF_CIRCLES_TO_WIN = 4

# will mark on the gui available dropping spaces
# in color
# highest row which has zeros as values in it
# start looping through connect_four_gui from the last index
# check for each (not circle_object.filled)
# return a list of strings of the format 'row:column'
# which can then be used to check for the correct
# circle_object to color for the user 
# so that he knows available circles to click
def check_for_lowest_available_space(game_grid):
    lowest_available_spaces = []
    
    
    for row in range(len(game_grid)-1, 0, -1):
        if len(lowest_available_spaces) == 7:
           break
        for column in range(len(game_grid[row])):
            if not game_grid[row][column].filled and game_grid[row][column].lowest_circle:
               lowest_available_spaces.append(str(row)  + ':' + str(column))

    
    return lowest_available_spaces
    
    
# Create the connect four circles at the start of the game
# since they are there at the start
# they should all have their attribute filled as false
# 640X400
# called once at the start
def  (game_grid):
    row_of_circle_objects = []
    x = 0
    y = 0

    for index in range(43):
        if index % 7 == 0 and index > 6:
           y += 50 # incresse y
           x = 0
           game_grid.append(row_of_circle_objects)
           row_of_circle_objects = []

        row_of_circle_objects.append(circle.BoardCirlce('white', False, x, y, False))
        x += 70

# called once at the start of the game        
def set_first_seven_lowest_circles(game_grid):
    # Set last rows lowest_circle attribute to True
    for circle_object in game_grid[5]:
        circle_object.lowest_circle = True              


# create_board_circle_objects(connect_four_grid)
# set_first_seven_lowest_circles(connect_four_grid)
# check_for_lowest_available_space(connect_four_grid)
def is_circle_clicked(game_grid):
    distance_dict = {}
    
    mouse_x_y_positions = pygame.mouse.get_pos()
    for row in range(len(game_grid)-1, 0, -1):
        for column in range(len(game_grid[row])):
            distance_x = math.pow((game_grid[row][column].x_position - mouse_x_y_positions[1]), 2)
            distance_y = math.pow((game_grid[row][column].y_position - mouse_x_y_positions[0]), 2)
            distance_between_points = math.sqrt(distance_x + distance_y)
            distance_dict[distance_between_points] = str(row) + ':' + str(column)
    
    
    sorted_distances_list = list(distance_dict.keys()).sort()
    POTENTIAL_CLICKED_CIRCLE_COORDINATES = distance_dict[sorted_distances_list[0]].split(sep=':')
    if sorted_distances_list[0] < game_grid[0][0].radius:
       return True
    else:
       return False        

"""
 Refactor check_four_in_a_row_verticaly and check_four_in_a_row_horizantly and
 check_four_in_a_row_diagnoly into one function
"""
def check_four_in_a_row_verticaly(circle_object, current_row, current_column, game_grid):
    if circle_object.color != game_grid[current_row-1][current_column].color:
       return False
    
    circles_in_a_row = 1 # always assume we start with one 
    for index in range(4):
        current_column -= 1
        if circle_object.color == game_grid[current_row][current_column].color:
           circles_in_a_row += 1
    if circles_in_a_row == NUMBER_OF_CIRCLES_TO_WIN:
       return True
    else:
       return False        
   
      
def check_four_in_a_row_horizantly(circle_object, current_row, current_column, game_grid):
    if circle_object.color != game_grid[current_row][current_column+1].color:
       return False
     
    circles_in_a_row = 1 # always assume we start with one
    for index in range(4):
        current_column += 1
        if circle_object.color == game_grid[current_row][current_column].color:
           circles_in_a_row += 1
    
    if circles_in_a_row == NUMBER_OF_CIRCLES_TO_WIN:
       return True
    else:
       return False 
            

                   
def check_four_in_a_row_diagnoly(circle_object, current_row, current_column, game_grid):            
    if circle_object.color != game_grid[current_row-1][current_column+1].color:
       return False
    
    circles_in_a_row = 1 # always assume we start with one 
    for index in range(4):
        current_colum += 1
        current_row -= 1
        if circle_object.color == game_grid[current_row][current_column].color:
           circles_in_a_row += 1
    
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
            if check_four_in_a_row_horizantly(game_grid[row][column], row, column, connect_four_grid) or
               check_four_in_a_row_verticaly(game_grid[row][column], row, column, connect_four_grid) or
               check_four_in_a_row_diagnoly(game_grid[row][column], row, column, connect_four_grid):
               return game_grid[row][column].color
    return ''           
               
               


# if circle has been clicked then invoke this function
def run_when_circle_clicked(clicked_circles_row, clicked_circles_column, game_grid, players_color):
    # when circle clicked update the relevent circle_object
    # filled attribute to True
    # color the clicked circle with the correct players color either
    # yellow or red
    # change circle to no longer lowest spot
    # invoke once every click
    game_grid[clicked_circles_row][clicked_circles_column].filled = True
    game_grid[clicked_circles_row][clicked_circles_column].lowest_circle = False
    game_grid[clicked_circles_row][clicked_circles_column].fill_circle(players_color)
 

# should be called every few sec
def draw_board_circles(game_grid):
    for row in game_grid:
        for circle_object in row:
            circle_object.draw_empthy_circle()
        
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        draw_board_circles(connect_four_grid)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
            
        create_board_circle_objects(connect_four_grid)
        set_first_seven_lowest_circles(connect_four_grid)
        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
