import circle
#from pygame.locals import *

connect_four_grid = []

# will mark on the gui available dropping spaces
# in color
# highest row which has zeros as values in it
# start looping through connect_four_gui from the last index
# check for each (not circle_object.filled)
# return a list of strings of the format 'row:column'
# which can then be used to check for the correct
# circle_object to color for the user 
# so that he knows available circles to click

def check_row_for_unfilled_circles(grid_row):
    for index in range(len(grid_row)):
        if not grid_row[index].circle_object.filled:
           return index 
     
def check_for_lowest_available_space(game_grid):
    lowest_available_spaces = []
    
    if len(lowest_available_spaces) == 7:
        return lowest_available_spaces
    
    for row in range(len(game_grid), 0, -1):
        check_row_for_unfilled_circles(game_grid[row])

# when circle clicked update the relevent circle_object
# filled attribute to True
# invoke once every click
def update_grid():
    pass

# start checking after four turns
# then check after each move by a player
def check_winner():
    pass

# Create the connect four circles at the start of the game
# since they are there at the start
# they should all have their attribute filled as false
# 640X400
# called once at the start
def create_board_circle_objects(game_grid):
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

create_board_circle_objects(connect_four_grid)
# get the currect circle object currently being clicked on the game gui
# by getting the mouse coordinates and checking with in which circle has the
# compute the distance between the mouse pos and each center of one of the 42
# board circle objects (x, y) coordinates
# compute each value and add it to a list
# sort that list
# get the first element of that list, thats the closest circle
# then check if that distance is less then the circles coordinates + radius
# if it is then the circle was clicked 
def set_clicked_circle_to_filled(game_grid):
    #pygame.mouse.get_pos()
    pass

# should be called every few sec
def draw_board_circles(game_grid):
    for row in game_grid:
        for circle_object in row:
            circle_object.draw_circle()
        
# class App:
#     def __init__(self):
#         self._running = True
#         self._display_surf = None
#         self.size = self.weight, self.height = 640, 400

#     def on_init(self):
#         pygame.init()
#         self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
#         self._running = True

#     def on_event(self, event):
#         if event.type == pygame.QUIT:
#             self._running = False

#     def on_loop(self):
#         pass

#     def on_render(self):
#         pass

#     def on_cleanup(self):
#         pygame.quit()

#     def on_execute(self):
#         if self.on_init() == False:
#             self._running = False

#         while (self._running):
#             for event in pygame.event.get():
#                 self.on_event(event)
#             self.on_loop()
#             self.on_render()
#         self.on_cleanup()


# if __name__ == "__main__":
#     theApp = App()
#     theApp.on_execute()
