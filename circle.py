import pygame

WHITE = ''


"""
Connect Four (also known as Four Up, Plot Four, Find Four,
Four in a Row, Four in a Line, Drop Four,
and Gravitrips (in Soviet Union)) is a two-player connection game in which the players first choose a color and then take turns dropping one colored disc from the top into a seven-column,
six-row vertically suspended grid. The pieces fall straight down,
occupying the lowest available space within the column.
The objective of the game is to be the first to form a horizontal,
vertical, or diagonal line of four of one's own discs. Connect Four is a solved game.
The first player can always win by playing the right moves.
"""

class BoardCirlce:
      surface = None  # Connect_Board Object
      radius = 6

      def __init__(self, color, filled, x_position, y_position, lowest_circle):
          self.color = color
          self.filled = filled # boolean
          self.x_position = x_position
          self.y_position = y_position
          self.lowest_circle = lowest_circle
          
      
      # Refactor to one drawing method
      # used once
      def draw_circle(self):
          if self.filled:
             pygame.gfxdraw.filled_circle(self.surface, self.x_position, self.y_position, self.radius, self.color)
          pygame.draw.circle(self.surface, WHITE, self.radius, [self.x_position, self.y_position])   
 