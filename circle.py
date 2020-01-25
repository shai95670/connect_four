import pygame
from pygame import gfxdraw


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
      radius = 12

      def __init__(self, color, filled, x_position, y_position, lowest_circle):
          self.color = color
          self.filled = filled # boolean
          self.x_position = x_position
          self.y_position = y_position
          self.lowest_circle = lowest_circle
      
      
      def set_filled(self, boolean_value):
          self.filled = boolean_value
       
              
      def set_lowest_circle(self, boolean_value):
          self.lowest_circle = boolean_value
      
      def set_color(self, color_for_setting):    
          self.color = color_for_setting
                
      # Refactor to one drawing method
      # used once
      def draw_circle(self, surface):
          if not self.filled:
             pygame.draw.circle(surface, self.color, (self.x_position, self.y_position), self.radius)
          elif self.filled:
             pygame.gfxdraw.filled_circle(surface, self.x_position, self.y_position, self.radius, self.color)    
             
            