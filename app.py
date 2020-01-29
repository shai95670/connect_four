import circle, math, pygame, time
from pygame.locals import *

connect_four_grid = []
dict_of_bounderies = {0: 52, 52: 112, 112: 172, 172: 232, 232: 292, 292: 352, 352: 412}
current_player = 'red'
number_of_turns = 0
winners_color = None

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
NUMBER_OF_CIRCLES_TO_WIN = 4


def get_lowest_available_row(game_grid, column_number_to_search):
    list_of_circle_objects_to_search = [value[column_number_to_search] for value in game_grid]
    print(list_of_circle_objects_to_search)

    for index in range(len(list_of_circle_objects_to_search) - 1, -1, -1):
        # is_lowest_circle = list_of_circle_objects_to_search[index].lowest_circle
        is_filled = list_of_circle_objects_to_search[index].filled
        if not is_filled:
           return index


def get_number_of_clicked_column(bounderies):
    index = 0
    mouse_x_y_positions = pygame.mouse.get_pos()
    for key, value in bounderies.items():
        if mouse_x_y_positions[0] >= key and mouse_x_y_positions[0] <= value:
           return index
        index += 1


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
            y += 60  # incresse y
            x = 40
            game_grid.append(row_of_circle_objects)
            row_of_circle_objects = []

        row_of_circle_objects.append(circle.BoardCirlce(WHITE, False, x, y))
        x += 60


# called once at the start of the game        
def set_first_seven_lowest_circles(game_grid):
    # Set last rows lowest_circle attribute to True
    for circle_object in game_grid[5]:
        circle_object.lowest_circle = True

    # TODO: REFACTOR THIS FUNCTION


def check_if_color_white(circle_object):
    return circle_object.color == (255, 255, 255)


def check_four_in_a_row(current_row, current_column, game_grid):
    # check current circle being checked if its white
    if (check_if_color_white(game_grid[current_row][current_column])):
       return False
    
    first_circle_in_a_row = game_grid[current_row][current_column]    
    circles_in_a_row_horizontal = 1
    circles_in_a_row_verticaly = 1
    circles_in_a_diagnoly = 1
    for number in range(1, 4): # horizontal (5, 6)
        if ((not current_column + number > 6) and
            (first_circle_in_a_row.color == game_grid[current_row][current_column + number].color)):
            circles_in_a_row_horizontal += 1
        else:
            break
               
    for number in range(1, 4): # vertically        
        if ((not current_row - number < 0) and
            (first_circle_in_a_row.color == game_grid[current_row - number][current_column].color)):
            circles_in_a_row_verticaly += 1
        else:
            break   
    for number in range(1, 4):
        if ((not current_row - number < 0) and
            (not current_column + number > 6) and 
            (first_circle_in_a_row.color == game_grid[current_row - number][current_column + number].color)):
            circles_in_a_row_verticaly += 1
        else:
            break   
    
    if (circles_in_a_row_horizontal == 4 or
        circles_in_a_row_verticaly == 4):
        return True
    return False 


# then check after each move by a player
# return '' if no winner or return color of winner
# check edge cases
def check_winner(game_grid):
    for row in range(len(game_grid) - 1, 0, -1):
        for column in range(len(game_grid[row])):
            if (check_four_in_a_row(row, column, game_grid)):
                return game_grid[row][column].color
    return ''


def set_color_for_circle(game_grid, column_to_set, row_to_set, color=YELLOW):
    game_grid[row_to_set][column_to_set].set_color(color)


def fill_circle(game_grid, column_to_fill, row_to_fill):
    game_grid[row_to_fill][column_to_fill].set_filled(True)


# should be called every few sec
def draw_board_circles(game_grid, game_surface):
    for row in game_grid:
        for circle_object in row:
            circle_object.draw_circle(game_surface)

# run both of those functions once
def unfill_all_circles(game_grid):
    for row in game_grid:
        for circle_object in row:
            circle_object.filled = False

def whiten_all_circles(game_grid):
    for row in game_grid:
        for circle_object in row:
            circle_object.color = WHITE




class App:
    def __init__(self):
        #self._running = True
        self.screen = None
        self.size = self.weight, self.height = 440, 440
        self.clock = None
        self._running = False
        self.game_over = False

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('connect_four')
        self.set_fps()
        self._running = True

    def set_fps(self):
        self.clock = pygame.time.Clock()

    def on_event(self, event):
        if event.type == pygame.QUIT:
           self._running = False
        if event.type == pygame.KEYDOWN:   
           if event.key == pygame.K_p:
              unfill_all_circles(connect_four_grid)
              whiten_all_circles(connect_four_grid)
              self.game_over = False
              self.screen = None  
              self.on_execute()
        if event.type == pygame.MOUSEBUTTONUP and not self.game_over:
            column_clicked = get_number_of_clicked_column(dict_of_bounderies)
            row_of_circle = get_lowest_available_row(connect_four_grid, column_clicked)
            global current_player, number_of_turns, winners_color
            if row_of_circle is None:
               return 
            if current_player == 'red':
                set_color_for_circle(connect_four_grid, column_clicked, row_of_circle, RED)
                current_player = 'yellow'
            else:
                # run with default yellow argument
                set_color_for_circle(connect_four_grid, column_clicked, row_of_circle)
                current_player = 'red'
            #set_lowest_circle(connect_four_grid, column_clicked, row_of_circle)
            fill_circle(connect_four_grid, column_clicked, row_of_circle)
            number_of_turns += 1

            if number_of_turns >= 4:
               winners_color = check_winner(connect_four_grid)
               if winners_color:
                  self.game_over = True


    def on_render(self):
        draw_board_circles(connect_four_grid, self.screen)

    def on_cleanup(self):
        pygame.quit()
             
    def set_game_winner_logo(self):
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        # now print the text
        text_surface = font.render('Winner', False, (0, 0, 0))
        self.screen.blit(text_surface, dest=(190,370))
        
        pygame.draw.rect(self.screen, winners_color, [200, 400, 40, 20])

    def on_execute(self):
        self.on_init()
        create_board_circle_objects(connect_four_grid)
        set_first_seven_lowest_circles(connect_four_grid)
        
        while (self._running):  # main game loop
            for event in pygame.event.get():
                self.on_event(event)
                 
            self.screen.fill(BLUE)
            self.on_render()
            
            if self.game_over:
               self.set_game_winner_logo()    
                     
            pygame.display.update()
            self.clock.tick(60)
            
        self.on_cleanup()    
            
               
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
