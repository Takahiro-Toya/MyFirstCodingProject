
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10056513
#    Student name: Takahiro Toya
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/) [1PT8102].
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  FOUR PIECE JIGSAW PUZZLE
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_attempt".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a jigsaw puzzle whose
#  state of completion is determined by data stored in a list which
#  specifies the locations of the pieces.  You are also required to
#  provide a solution to your particular puzzle.  See the instruction
#  sheet accompanying this file for full details.
#
#  This template file must be used and you will submit
#  your final solution as a single file only.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.


##size_of_pieces = 300 # pixels (excluding any protruding "tabs")
size_of_pieces = 300 # pixels (excluding any protruding "tabs")
half_piece_size = size_of_pieces / 2
max_tab_size = 100 # pixels
box_size = size_of_pieces + (max_tab_size * 2)
half_box_size = box_size / 2
left_border = max_tab_size
gap = max_tab_size
top_bottom_border = max_tab_size
canvas_height = (top_bottom_border + size_of_pieces) * 2
canvas_width = (size_of_pieces * 2 + left_border) * 2
template_centres = [[-(size_of_pieces + half_piece_size), -half_piece_size], # bottom left
                    [-half_piece_size, -half_piece_size], # bottom right
                    [-(size_of_pieces + half_piece_size), half_piece_size], # top left
                    [-half_piece_size, half_piece_size]] # top right
box_centre = [gap + (box_size / 2), 0]

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background for the puzzle, i.e., the template for the
# pieces and the box they're kept in.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up and at its standard width and colour.
#


# Draw the box that contains unused puzzle pieces.  (The box is
# larger than the puzzle pieces to allow for tabs sticking out on
# any of their four sides.)
def draw_box():

    # Determine the position of the box's bottom-left corner
    bottom_left = [box_centre[0] - half_box_size,
                   box_centre[1] - half_box_size]

    # Go to the bottom-left corner and get ready to draw
    penup()
    goto(bottom_left)
    width(5)
    color('black')
    pendown()
    
    # Walk around the box's perimeter
    setheading(0) # point east
    for side in [1, 2, 3, 4]:
        forward(box_size)
        left(90)

    # Reset the pen
    width(1)
    penup()
 

# Draw the individual squares of the jigsaw's template
def draw_template(show_template = False):

    # Only draw if the argument is True
    if show_template:

        # Set up the pen
        width(3)
        color('grey')

        # Draw a box for each centre coordinate
        for centre_x, centre_y in template_centres:
            
            # Determine the position of this square's bottom-left corner
            bottom_left = [centre_x - half_piece_size,
                           centre_y - half_piece_size]

            # Go to the bottom-left corner and get ready to draw
            penup()
            goto(bottom_left)
            pendown()
        
            # Walk around the square's perimeter
            setheading(0) # point east
            for side in [1, 2, 3, 4]:
                forward(size_of_pieces)
                left(90)

        # Reset the pen
        width(1)
        color('black')
        penup()


# As a debugging aid, mark the coordinates of the centres of
# the template squares and the box
def mark_coords(show_coords = False):

    # Only mark the coordinates if the argument is True
    if show_coords:

        # Don't draw lines between the coordinates
        penup()

        # Go to each coordinate, draw a dot and print the coordinate
        color('black')
        for x_coord, y_coord in template_centres + [box_centre]:
            goto(x_coord, y_coord)
            dot(4)
            write(str(x_coord) + ', ' + str(y_coord),
                  font = ('Arial', 12, 'normal'))

    # Reset the pen
    width(1)
    penup()
               
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# jigsaw puzzle pieces:
#
# 1. The name of the piece, from 'Piece A' to 'Piece D'
# 2. The place to put the piece, either in the template, denoted
#    'Top left', 'Top right', 'Bottom left' or 'Bottom right', or
#    in the unused pieces box, denoted 'In box'
#
# Each data set does not necessarily mention all pieces.  Also notice
# that several pieces may be in the box at the same time, in which
# case they should just be drawn on top of each other.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Most importantly, you must write your own data set at the end
# to provide the correct solution to your puzzle.
#

# The following data set doesn't require drawing any jigsaw pieces
# at all.  You may find it useful as a dummy argument when you
# first start developing your "draw_attempt" function.

attempt_00 = []

# Each of the following data sets put just one piece in the box.
# You may find them useful when creating your individual pieces.

attempt_01 = [['Piece A', 'In box']]
attempt_02 = [['Piece B', 'In box']]
attempt_03 = [['Piece C', 'In box']]
attempt_04 = [['Piece D', 'In box']]

# Each of the following data sets put just one piece in a
# location in the template.

attempt_05 = [['Piece A', 'Top left']]
attempt_06 = [['Piece B', 'Bottom right']]
attempt_07 = [['Piece C', 'Top right']]
attempt_08 = [['Piece D', 'Bottom left']]
attempt_09 = [['Piece A', 'Bottom left']]
attempt_10 = [['Piece B', 'Top left']]
attempt_11 = [['Piece C', 'Bottom right']]
attempt_12 = [['Piece D', 'Top right']]

# Each of the following data sets put all four pieces in the
# box, but in different orders.

attempt_13 = [['Piece A', 'In box'], ['Piece B', 'In box'],
              ['Piece C', 'In box'], ['Piece D', 'In box']]
attempt_14 = [['Piece D', 'In box'], ['Piece C', 'In box'],
              ['Piece B', 'In box'], ['Piece A', 'In box']]
attempt_15 = [['Piece C', 'In box'], ['Piece D', 'In box'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]

# Each of the following data sets uses between two and four pieces,
# either in the template or in the box

attempt_16 = [['Piece A', 'Top right'], ['Piece B', 'Bottom left']]
attempt_17 = [['Piece D', 'Bottom right'], ['Piece C', 'In box']]
attempt_18 = [['Piece C', 'Bottom right'], ['Piece A', 'Bottom right']]
attempt_19 = [['Piece B', 'In box'], ['Piece D', 'Top left'],
              ['Piece C', 'In box']]
attempt_20 = [['Piece C', 'Top left'], ['Piece D', 'Top right'],
              ['Piece A', 'Bottom left']]
attempt_21 = [['Piece A', 'In box'], ['Piece D', 'Bottom left'],
              ['Piece C', 'Top right']]
attempt_22 = [['Piece A', 'Bottom left'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom right'], ['Piece D', 'In box']]
attempt_23 = [['Piece D', 'Bottom right'], ['Piece C', 'In box'],
              ['Piece B', 'Top right'], ['Piece A', 'Top left']]
attempt_24 = [['Piece C', 'Bottom right'], ['Piece D', 'Top left'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]
attempt_25 = [['Piece D', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece C', 'Bottom right'], ['Piece A', 'Top right']]
attempt_26 = [['Piece C', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece A', 'Bottom right'], ['Piece D', 'Top right']]
attempt_27 = [['Piece C', 'Bottom left'], ['Piece D', 'In box'],
              ['Piece A', 'Top left'], ['Piece B', 'Top right']]

# Each of the following data sets is a complete attempt at solving
# the puzzle using all four pieces (so there are no pieces left in the box)

attempt_28 = [['Piece A', 'Bottom left'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Top right']]
attempt_29 = [['Piece A', 'Top right'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left']]
attempt_30 = [['Piece A', 'Bottom left'], ['Piece B', 'Top left'],
              ['Piece C', 'Bottom right'], ['Piece D', 'Top right']]
attempt_31 = [['Piece A', 'Bottom right'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom left'], ['Piece D', 'Top left']]
attempt_32 = [['Piece D', 'Top right'], ['Piece A', 'Bottom left'],
              ['Piece B', 'Top left'], ['Piece C', 'Bottom right']]
attempt_33 = [['Piece A', 'Top right'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left']]

# Here you must provide a list which is the correct solution to
# your puzzle.

# ***** Put the solution to your puzzle in this list
solution = [['Piece A', 'Bottom left'], ['Piece B', 'Top left'],
            ['Piece C', 'Top right'] , ['Piece D', 'Bottom right']]

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_attempt" function.
#

# Draw the jigsaw pieces as per the provided data set
def draw_attempt(attempt_file_number):

    # repeat as many times as there are elements in an attemppt list
    for index in range(len(attempt_file_number)):
        
        # check the location to draw a piece
            if attempt_file_number[index][1] == "Bottom left":
                piece_location_x = template_centres[0][0]
                piece_location_y = template_centres[0][1]
            elif attempt_file_number[index][1] == "Bottom right":
                piece_location_x = template_centres[1][0]
                piece_location_y = template_centres[1][1]
            elif attempt_file_number[index][1] == "Top left":
                piece_location_x = template_centres[2][0]
                piece_location_y = template_centres[2][1]
            elif attempt_file_number[index][1] == "Top right":
                piece_location_x = template_centres[3][0]
                piece_location_y = template_centres[3][1]
            elif attempt_file_number[index][1] == "In box":
                piece_location_x = box_centre[0]
                piece_location_y = box_centre[1]
            
        # check the Piece Type to draw
            if attempt_file_number[index][0] == "Piece A":
                piece_a(piece_location_x, piece_location_y)
            elif attempt_file_number[index][0] == "Piece B":
                piece_b(piece_location_x, piece_location_y) 
            elif attempt_file_number[index][0] == "Piece C":
                piece_c(piece_location_x, piece_location_y)
            elif attempt_file_number[index][0]  == "Piece D":
                piece_d(piece_location_x, piece_location_y)

######################################################################
# function to draw beautiful tab

tab_gap = 60 # gap between start of drawing a tab and end of drawing a tab
tab_radius = tab_gap * (1 / sqrt(2))

# Draw a piece's line which has a convex tab
def line_convex():
    forward(half_piece_size - (tab_gap / 2))
    right(45)
    circle(tab_radius, -270)
    right(45)
    forward(half_piece_size - (tab_gap / 2))

# Draw a piece's line whitch has a concave tab    
def line_concave():
    forward(half_piece_size - (tab_gap / 2))
    right(135)
    circle(tab_radius, 270)
    right(135)
    forward(half_piece_size - (tab_gap / 2))

########################################################################

######################################################################## 
   
########################################################################
    
# data to draw a picture on Piece A

elements_a_1 =[[-150.0, 99.0], [-150.0, 150.0], [-53.0, 150.0], \
               [-51.0, 142.0], [-45.0, 139.0], [-39.0, 139.0], \
               [-41.0, 132.0], [-43.0, 125.0], [-42.0, 120.0], \
               [-41.0, 114.0], [-40.0, 106.0], [-39.0, 103.0], \
               [-43.0, 97.0], [-48.0, 92.0], [-54.0, 88.0], \
               [-62.0, 86.0], [-68.0, 85.0], [-75.0, 86.0], \
               [-81.0, 87.0], [-88.0, 89.0], [-94.0, 91.0], \
               [-100.0, 89.0], [-108.0, 87.0], [-115.0, 87.0], \
               [-124.0, 88.0], [-132.0, 89.0], [-138.0, 93.0], \
               [-150.0, 98.0]]  # hand

elements_a_2 =[[23.0, 72.0], [45.0, 69.0], [61.0, 70.0], \
               [96.0, 36.0], [102.0, 26.0], [104.0, 11.0], \
               [113.0, 1.0], [123.0, -4.0], [139.0, -9.0], \
               [140.0, -15.0], [134.0, -13.0], [127.0, -10.0], \
               [118.0, -10.0], [109.0, -10.0], [97.0, -11.0], \
               [89.0, -14.0], [82.0, -19.0], [76.0, -25.0], \
               [69.0, -32.0], [66.0, -40.0], [66.0, -52.0], \
               [61.0, -44.0], [55.0, -36.0], [47.0, -22.0], \
               [40.0, -2.0], [31.0, 25.0], [23.0, 72.0]] # mant

elements_a_3 = [[-40.0, 99.0], [-43.0, 95.0], [-46.0, 90.0], \
                [-51.0, 87.0], [-58.0, 85.0], [-64.0, 83.0], \
                [-7.0, 76.0], [-16.0, 80.0], [-22.0, 83.0], \
                [-28.0, 87.0], [-33.0, 92.0], [-40.0, 99.0]]
                # arm

elements_a_4 = [[-8.0, 78.0], [2.0, 77.0], [10.0, 79.0], [19.0, 81.0], \
                [26.0, 85.0], [30.0, 89.0], [34.0, 91.0], [35.0, 87.0], \
                [42.0, 79.0], [49.0, 75.0], [57.0, 70.0], [48.0, 70.0], \
                [-4.0, 77.0]] # arm

elements_a_5 = [[64.0, 68.0], [76.0, 80.0], [150.0, 88.0]] # body               

elements_a_6 = [[217.0, -2.0], [211.0, -4.0], [211.0, -8.0], \
                [210.0, -12.0], [211.0, -16.0], [213.0, -23.0], \
                [210.0, -29.0], [205.0, -34.0], [185.0, -39.0], \
                [179.0, -40.0], [173.0, -40.0], [168.0, -38.0], \
                [164.0, -36.0], [156.0, -33.0], [151.0, -29.0], \
                [147.0, -24.0], [144.0, -12.0], [142.0, -9.0], \
                [137.0, -7.0], [132.0, -6.0], [127.0, -5.0], \
                [120.0, -2.0], [111.0, 5.0], [108.0, 9.0], \
                [106.0, 22.0], [101.0, 32.0], [96.0, 37.0], \
                [90.0, 43.0], [84.0, 50.0], [76.0, 58.0], [66.0, 65.0]]
                # body

elements_a_7 = [[221.0, -4.0], [220.0, -13.0], [215.0, -21.0], \
                [212.0, -14.0], [212.0, -8.0], [221.0, -4.0]]
                # the small mant part in the right tab
                
elements_a_8 = [[33.0, 89.0], [40.0, 82.0], [48.0, 76.0], \
                 [58.0, 69.0], [65.0, 70.0], [75.0, 72.0], \
                 [78.0, 76.0], [84.0, 69.0], [93.0, 63.0], \
                 [103.0, 58.0], [115.0, 54.0], [122.0, 58.0], \
                 [127.0, 65.0], [134.0, 73.0], [136.0, 79.0], \
                 [140.0, 88.0], [138.0, 101.0], [47.0, 102.0], [33.0, 89.0]]
                # scarf

elements_a_9 = [[-40.0, 147.0], [-33.0, 147.0], [-35.0, 142.0], [-40.0, 147.0]]
                # the small face part near the yellow hand

elements_a_10 = [[150.0, 86.0], [149.0, 85.0], [144.0, 85.0], \
                 [135.0, 85.0], [130.0, 86.0], [127.0, 89.0], \
                 [131.0, 90.0], [137.0, 90.0], [142.0, 91.0],
                 [150.0, 92.0], [150.0, 86.0]]
                # yellow parts around neck

elements_a_11 = [[150.0, 91.0], [150.0, 150.0]] # face

elements_a_12 = [[44.0, 89.0], [50.0, 88.0], [57.0, 85.0], \
                 [64.0, 84.0], [69.0, 84.0], [76.0, 84.0], \
                 [81.0, 84.0], [88.0, 84.0], [93.0, 84.0], \
                 [99.0, 86.0], [105.0, 86.0], [111.0, 86.0], \
                 [119.0, 88.0], [127.0, 88.0], [134.0, 89.0], \
                 [141.0, 91.0], [150.0, 91.0]]
                # face
                
elements_a_13 = [[51.0, 150.0], [61.0, 141.0], [67.0, 135.0], \
                 [75.0, 131.0], [81.0, 128.0], [90.0, 125.0], \
                 [97.0, 124.0], [106.0, 124.0], [114.0, 125.0], \
                 [122.0, 126.0], [129.0, 128.0], [138.0, 131.0], \
                 [147.0, 134.0], [150.0, 135.0], [150.0, 150.0], \
                 [51.0, 150.0]]
                # mouth

elements_a_14 = [[150.0, 66.0], [144.0, 64.0], [141.0, 60.0], \
                 [136.0, 55.0], [134.0, 46.0], [138.0, 38.0], \
                 [145.0, 36.0], [150.0, 34.0], [150.0, 66.0]]
                # smile mark on the body

elements_a_15 = [[98.0, 33.0], [103.0, 32.0], [107.0, 31.0], \
                 [113.0, 30.0], [118.0, 28.0], [122.0, 28.0], \
                 [127.0, 27.0], [132.0, 27.0], [137.0, 28.0], \
                 [142.0, 28.0], [148.0, 28.0], [159.0, 13.0], \
                 [151.0, 12.0], [143.0, 13.0], [134.0, 14.0], \
                 [126.0, 16.0], [120.0, 18.0], [114.0, 20.0], \
                 [105.0, 25.0], [98.0, 33.0]]
                 # yellow belt
                 
elements_a_16 = [[148.0, 28.0], [155.0, 27.0], [160.0, 28.0], \
                 [165.0, 28.0], [171.0, 30.0], [175.0, 32.0], \
                 [179.0, 32.0], [185.0, 34.0], [195.0, 36.0], \
                 [205.0, 32.0], [212.0, 25.0], [207.0, 22.0], \
                 [202.0, 21.0], [193.0, 17.0], [186.0, 15.0], \
                 [179.0, 15.0], [170.0, 14.0], [159.0, 13.0], \
                 [148.0, 28.0]]
                # white belt parts

# elements_a_17 to elements_a_31 are for outline
elements_a_17 = [[-52.0, 147.0], [-48.0, 142.0], [-38.0, 139.0]]
                # outline of right hand

elements_a_18 = [[-40.0, 103.0], [-42.0, 97.0], [-46.0, 93.0], \
                  [-51.0, 89.0], [-56.0, 87.0], [-64.0, 84.0], \
                  [-70.0, 83.0], [-77.0, 85.0], [-84.0, 86.0], \
                  [-90.0, 87.0], [-94.0, 89.0], [-100.0, 87.0], \
                  [-106.0, 86.0], [-113.0, 86.0], [-122.0, 87.0], \
                  [-130.0, 88.0], [-136.0, 90.0], [-141.0, 93.0], \
                  [-147.0, 97.0]] # outline of right hand

elements_a_19 = [[-52.0, 141.0], [-54.0, 135.0], [-58.0, 129.0]]
                    # outline in right hand

elements_a_20 = [[-69.0, 111.0], [-73.0, 108.0], [-76.0, 104.0], \
                  [-81.0, 100.0], [-85.0, 96.0], [-89.0, 93.0], \
                  [-93.0, 91.0]] # outline in right hand 

elements_a_21 = [[33.0, 89.0], [40.0, 82.0], [48.0, 76.0], \
                 [58.0, 69.0], [65.0, 70.0], [75.0, 72.0], \
                 [78.0, 76.0], [84.0, 69.0], [93.0, 63.0], \
                 [103.0, 58.0], [115.0, 54.0], [122.0, 58.0], \
                 [127.0, 65.0], [134.0, 73.0], [136.0, 79.0]]
                    # outline of scarf

elements_a_22 = [[-62.0, 80.0], [-4.0, 75.0], [59.0, 66.0]]
                # outline of right arm

elements_a_23 =[[67.0, 61.0], [74.0, 56.0], [79.0, 52.0], \
                [85.0, 46.0], [97.0, 32.0], [104.0, 23.0], \
                [106.0, 11.0], [113.0, -1.0], [123.0, -7.0], \
                [134.0, -10.0], [143.0, -13.0], [146.0, -22.0], \
                [150.0, -32.0]] # outline of the body

elements_a_24 =[[98.0, 33.0], [108.0, 31.0], [117.0, 28.0], \
                [124.0, 28.0], [132.0, 27.0], [148.0, 28.0], \
                [162.0, 28.0], [172.0, 30.0], [180.0, 32.0], \
                [196.0, 36.0]] # outline of the belt

elements_a_25 = [[105.0, 22.0], [113.0, 18.0], [120.0, 16.0], \
                 [130.0, 14.0], [140.0, 11.0], [152.0, 9.0], \
                 [160.0, 10.0], [172.0, 12.0], [187.0, 13.0], \
                 [199.0, 18.0], [208.0, 20.0], [213.0, 23.0]]
                    # outline of the belt

elements_a_26 = [[148.0, 29.0], [160.0, 10.0]]
                    # outline of the belt

elements_a_27 = [[150.0, 83.0], [143.0, 82.0], [136.0, 82.0], [130.0, 83.0]]
                # outline of the accessory

elements_a_28 = [[-42.0, 148.0], [-35.0, 139.0]] # outline of the face


elements_a_29 = [[32.0, 89.0], [41.0, 86.0], [51.0, 84.0],\
                 [62.0, 81.0], [70.0, 81.0], [80.0, 81.0], \
                 [90.0, 81.0], [100.0, 83.0], [108.0, 83.0], \
                 [116.0, 85.0], [129.0, 85.0], [131.0, 86.0], \
                 [139.0, 87.0], [151.0, 88.0]]
                    # outline of the face

elements_a_30 = [[141.0, -11.0], [151.0, -13.0], [160.0, -13.0], \
                 [170.0, -13.0], [178.0, -12.0], \
                 [186.0, -12.0], [191.0, -7.0], [195.0, 4.0], \
                 [201.0, 6.0], [210.0, 1.0], [219.0, -3.0]]
                # outline between the body and the leg

elements_a_31 = [[150.0, 52.0], [148.0, 53.0], [148.0, 50.0], [150.0, 50.0]]
                # right eye of the smile mark

#------------------------------------------------------------------------------------

# functions to draw Piece A
def piece_a(x_coord, y_coord):

    # piece's corner
    piece_left_bottom = [(x_coord - half_piece_size), (y_coord - half_piece_size)]
    piece_left_top = [(x_coord - half_piece_size), (y_coord + half_piece_size)]
    piece_right_bottom = [(x_coord + half_piece_size), (y_coord - half_piece_size)]
    piece_right_top = [(x_coord + half_piece_size), (y_coord + half_piece_size)]

  # processes to draw picture on Piece A
    
    # make the background
    penup()
    color("Powderblue")
    width(3)
    setheading(90)
    begin_fill()
    goto(piece_left_bottom)
    pendown()
    goto(piece_left_top)
    right(90)
    line_concave()
    right(90)
    line_convex()
    goto(piece_left_bottom)
    penup()
    end_fill()

    # draw the hand
    penup()
    color("Yellow")
    goto(elements_a_1[0][0] + x_coord, y_coord + elements_a_1[0][1])
    pendown()
    begin_fill()
    for element_a_1 in elements_a_1:
        goto(element_a_1[0] + x_coord, element_a_1[1] + y_coord)
    penup()
    end_fill()
    # draw the mant
    color("black")
    goto(elements_a_2[0][0] + x_coord, y_coord + elements_a_2[0][1])
    pendown()
    begin_fill()
    for element_a_2 in elements_a_2:
        goto(element_a_2[0] + x_coord, element_a_2[1] + y_coord)
    penup()
    end_fill()

    # draw the arm
    color("FireBrick")
    goto(elements_a_3[0][0] + x_coord, y_coord + elements_a_3[0][1])
    pendown()
    begin_fill()
    for element_a_3 in elements_a_3:
        goto(element_a_3[0] + x_coord, element_a_3[1] + y_coord)
    penup()
    end_fill()
    goto(elements_a_4[0][0] + x_coord, y_coord + elements_a_4[0][1])
    pendown()
    begin_fill()
    for element_a_4 in elements_a_4:
        goto(element_a_4[0] + x_coord, element_a_4[1] + y_coord)
    penup()
    end_fill()

    # draw the body and the leg
    goto(elements_a_5[0][0] + x_coord, y_coord + elements_a_5[0][1])
    pendown()
    begin_fill()
    for element_a_5 in elements_a_5:
        goto(element_a_5[0] + x_coord, element_a_5[1] + y_coord)
    goto(150.0 + x_coord, (piece_right_top[1] - half_piece_size + (tab_gap / 2)))
    setheading(270)
    right(45)
    circle(tab_radius, -133)
    for element_a_6 in elements_a_6:
        goto(element_a_6[0] + x_coord, element_a_6[1] + y_coord)
    penup()
    end_fill()

    # draw the small mant part (black) in the right tab
    color("black")
    goto(elements_a_7[0][0] + x_coord, y_coord + elements_a_7[0][1])
    pendown()
    begin_fill()
    for element_a_7 in elements_a_7:
        goto(element_a_7[0] + x_coord, element_a_7[1] + y_coord)
    penup()
    end_fill()

    # draw the scarf
    color("SaddleBrown")
    goto(elements_a_8[0][0] + x_coord, y_coord + elements_a_8[0][1])
    pendown()
    begin_fill()
    for element_a_8 in elements_a_8:
        goto(element_a_8[0] + x_coord, element_a_8[1] + y_coord)
    penup()
    end_fill()

    # draw the face part near the hand
    color("BurlyWood")
    goto(elements_a_9[0][0] + x_coord, y_coord + elements_a_9[0][1])
    pendown()
    begin_fill()
    for element_a_9 in elements_a_9:
        goto(element_a_9[0] + x_coord, element_a_9[1] + y_coord)
    penup()
    end_fill()

    # draw the accessory around neck
    color("Yellow")
    goto(elements_a_10[0][0] + x_coord, y_coord + elements_a_10[0][1])
    pendown()
    begin_fill()
    for element_a_10 in elements_a_10:
        goto(element_a_10[0] + x_coord, element_a_10[1] + y_coord)
    penup()
    end_fill()

    # draw the face part
    color("Burlywood")
    goto(elements_a_11[0][0] + x_coord, y_coord + elements_a_10[0][1])
    pendown()
    begin_fill()
    for element_a_11 in elements_a_11:
        goto(element_a_11[0] + x_coord, element_a_11[1] + y_coord)
    goto((piece_right_top[0] - half_piece_size + (tab_gap / 2), 150 + y_coord))
    setheading(135)
    circle(tab_radius, -88)
    for element_a_12 in elements_a_12:
        goto(element_a_12[0] + x_coord, element_a_12[1] + y_coord)
    penup()
    end_fill()
    color("black")
    width(2)

    # draw the mouth
    goto(elements_a_13[0][0] + x_coord, y_coord + elements_a_13[0][1])
    pendown()
    begin_fill()
    fillcolor("Maroon")
    for element_a_13 in elements_a_13:
        goto(element_a_13[0] + x_coord, element_a_13[1] + y_coord)
    penup()
    end_fill()

    # draw the smile mark
    color("yellow")
    goto(elements_a_14[0][0] + x_coord, y_coord + elements_a_14[0][1])
    pendown()
    begin_fill()
    for element_a_14 in elements_a_14:
        goto(element_a_14[0] + x_coord, element_a_14[1] + y_coord)
    penup()
    end_fill()
    color("black")
    goto(elements_a_14[0][0] + x_coord, y_coord + elements_a_14[0][1])
    pendown()
    begin_fill()
    for element_a_14 in elements_a_14:
        goto(element_a_14[0] + x_coord, element_a_14[1] + y_coord)
    penup()

    # draw the belt (yellow part)
    color("yellow")
    goto(elements_a_15[0][0] + x_coord, y_coord + elements_a_15[0][1])
    pendown()
    begin_fill()
    for element_a_15 in elements_a_15:
        goto(element_a_15[0] + x_coord, element_a_15[1] + y_coord)
    penup()
    end_fill()

    # draw the belt (white part)
    color("white")
    goto(elements_a_16[0][0] + x_coord, y_coord + elements_a_16[0][1])
    pendown()
    begin_fill()
    for element_a_16 in elements_a_16:
        goto(element_a_16[0] + x_coord, element_a_16[1] + y_coord)
    penup()
    end_fill()

    # draw the outline
    color("black")
    goto(elements_a_17[0][0] + x_coord, y_coord + elements_a_17[0][1])
    pendown()
    for element_a_17 in elements_a_17:
        goto(element_a_17[0] + x_coord, element_a_17[1] + y_coord)
    penup()
    goto(elements_a_18[0][0] + x_coord, y_coord + elements_a_18[0][1])
    pendown()
    for element_a_18 in elements_a_18:
        goto(element_a_18[0] + x_coord, element_a_18[1] + y_coord)
    penup()
    goto(elements_a_19[0][0] + x_coord, y_coord + elements_a_19[0][1])
    pendown()
    for element_a_19 in elements_a_19:
        goto(element_a_19[0] + x_coord, element_a_19[1] + y_coord)
    penup()       
    goto(elements_a_20[0][0] + x_coord, y_coord + elements_a_20[0][1])
    pendown()
    for element_a_20 in elements_a_20:
        goto(element_a_20[0] + x_coord, element_a_20[1] + y_coord)
    penup()
    goto(elements_a_21[0][0] + x_coord, y_coord + elements_a_21[0][1])
    pendown()
    for element_a_21 in elements_a_21:
        goto(element_a_21[0] + x_coord, element_a_21[1] + y_coord)
    penup()
    goto(elements_a_22[0][0] + x_coord, y_coord + elements_a_22[0][1])
    pendown()
    for element_a_22 in elements_a_22:
        goto(element_a_22[0] + x_coord, element_a_22[1] + y_coord)
    penup()
    goto(elements_a_23[0][0] + x_coord, y_coord + elements_a_23[0][1])
    pendown()
    for element_a_23 in elements_a_23:
        goto(element_a_23[0] + x_coord, element_a_23[1] + y_coord)
    penup()
    goto(elements_a_24[0][0] + x_coord, y_coord + elements_a_24[0][1])
    pendown()
    for element_a_24 in elements_a_24:
        goto(element_a_24[0] + x_coord, element_a_24[1] + y_coord)
    penup()
    goto(elements_a_25[0][0] + x_coord, y_coord + elements_a_25[0][1])
    pendown()
    for element_a_25 in elements_a_25:
        goto(element_a_25[0] + x_coord, element_a_25[1] + y_coord)
    penup() 
    goto(elements_a_26[0][0] + x_coord, y_coord + elements_a_26[0][1])
    pendown()
    for element_a_26 in elements_a_26:
        goto(element_a_26[0] + x_coord, element_a_26[1] + y_coord)
    penup()
    goto(elements_a_27[0][0] + x_coord, y_coord + elements_a_27[0][1])
    pendown()
    for element_a_27 in elements_a_27:
        goto(element_a_27[0] + x_coord, element_a_27[1] + y_coord)
    penup()
    goto(elements_a_28[0][0] + x_coord, y_coord + elements_a_28[0][1])
    pendown()
    for element_a_28 in elements_a_28:
        goto(element_a_28[0] + x_coord, element_a_28[1] + y_coord)
    penup()
    goto(elements_a_29[0][0] + x_coord, y_coord + elements_a_29[0][1])
    pendown()
    for element_a_29 in elements_a_29:
        goto(element_a_29[0] + x_coord, element_a_29[1] + y_coord)
    penup()
    goto(elements_a_30[0][0] + x_coord, y_coord + elements_a_30[0][1])
    pendown()
    for element_a_30 in elements_a_30:
        goto(element_a_30[0] + x_coord, element_a_30[1] + y_coord)
    penup()

    # draw right eye on smile mark
    goto(elements_a_31[0][0] + x_coord, y_coord + elements_a_31[0][1])
    pendown()
    for element_a_31 in elements_a_31:
        goto(element_a_31[0] + x_coord, element_a_31[1] + y_coord)
    penup()    
    
    # draw "Piece A" shape
    penup()
    color("black")
    width(3)
    goto(piece_left_bottom)
    setheading(90)
    pendown()
    goto(piece_left_top)
    right(90)
    line_concave()
    right(90)
    line_convex()
    goto(piece_left_bottom)
    penup()

############################################################
    
# data to draw a picture on Piece B

elements_b_1 = [[-53.0, -137.0], [-61.0, -121.0], [-66.0, -108.0], \
                [-71.0, -90.0], [-73.0, -70.0], [-72.0, -55.0], \
                [-70.0, -38.0], [-68.0, -22.0], [-62.0, -3.0], \
                [-57.0, 9.0], [-48.0, 22.0], [-39.0, 36.0], \
                [-29.0, 48.0], [-17.0, 60.0], [-3.0, 71.0], \
                [15.0, 85.0], [32.0, 91.0], [47.0, 100.0], \
                [65.0, 106.0], [86.0, 110.0], [106.0, 110.0], \
                [122.0, 111.0], [136.0, 110.0], [150.0, 107.0]]
                # face
                
elements_b_2 = [[27.0, -209.0], [13.0, -202.0], [2.0, -197.0], \
                [-6.0, -191.0], [-18.0, -185.0], [-24.0, -178.0], \
                [-31.0, -169.0], [-37, -161], [-31.5, -150], [-43.0, -150]]
                # face

elements_b_3 = [[-136.0, -136.0], [-124.0, -128.0], [-113.0, -124.0], \
                [-102.0, -122.0], [-90.0, -120.0], [-81.0, -122.0], \
                [-72.0, -127.0], [-63.0, -134.0], [-60.0, -138.0], \
                [-56.0, -145.0], [-54.0, -150]]
                # hand

elements_b_4 = [[-37.0, -163.0], [-36.0, -171.0], [-35.0, -178.0], \
                [-36.0, -185.0], [-38.0, -193.0], [-41.0, -188.0], \
                [-41.0, -181.0], [-41.0, -173.0], [-38.0, -163.0]]
                # hand

elements_b_5 = [[-32.0, -172.0], [-24.0, -179.0], [-18.0, -186.0], \
                [-10.0, -191.0], [-1.0, -197.0], [9.0, -202.0], \
                [18.0, -205.0], [29.0, -211.0], [21.0, -216.0], \
                [11.0, -220.0], [-1.0, -221.0], [-11.0, -220.0], \
                [-20.0, -217.0], [-28.0, -212.0], [-32.0, -207.0], \
                [-35.0, -201.0], [-34.0, -192.0], [-38.0, -193.0], \
                [-34.0, -185.0], [-35.0, -177.0], [-37.0, -163.0]] # arm

elements_b_6 = [[-18.0, -123.0], [-26.0, -115.0], [-32.0, -104.0], \
                [-35.0, -94.0], [-35.0, -84.0], [-35.0, -74.0], \
                [-32.0, -64.0], [-29.0, -58.0], [-25.0, -50.0], \
                [-20.0, -45.0], [-14.0, -40.0], [-6.0, -39.0], \
                [4.0, -38.0], [15.0, -39.0], [24.0, -44.0], \
                [33.0, -50.0], [39.0, -59.0], [40.0, -71.0], \
                [45.0, -81.0], [47.0, -91.0], [44.0, -99.0], \
                [40.0, -109.0], [33.0, -115.0], [25.0, -121.0], \
                [18.0, -126.0], [10.0, -130.0], [-3.0, -133.0]]
                # right cheek

elements_b_7 = [[150.0, -59.0], [147.0, -52.0], [145.0, -43.0], \
                [144.0, -35.0], [143.0, -28.0], [146.0, -20.0], \
                [151.0, -12.0], [155.0, -6.0], [160.0, 1.0], \
                [168.0, 7.0], [176.0, 12.0], [183.0, 14.0], \
                [191.0, 15.0], [199.0, 12.0], [207.0, 9.0], \
                [215.0, 6.0], [220.0, 1.0], [220.0, -8.0], \
                [217.0, -17.0], [214.0, -24.0], [208.0, -29.0], \
                [202.0, -34.0], [195.0, -36.0], [188.0, -39.0], \
                [180.0, -40.0], [173.0, -39.0], [166.0, -38.0], \
                [160.0, -35.0], [154.0, -31.0], [150.0, -29.0], \
                [150.0, -38.0], [150.0, -46.0], [150.0, -55.0], \
                [150.0, -59.0]]
                # left cheek

elements_b_8 = [[44.0, -67.0], [44.0, -61.0], [45.0, -52.0], \
                [48.0, -43.0], [52.0, -34.0], [57.0, -28.0], \
                [64.0, -22.0], [71.0, -17.0], [83.0, -13.0], \
                [93.0, -10.0], [104.0, -10.0], [114.0, -13.0], \
                [123.0, -17.0], [131.0, -23.0], [137.0, -33.0], \
                [142.0, -42.0], [143.0, -52.0], [143.0, -64.0], \
                [139.0, -74.0], [132.0, -85.0], [123.0, -93.0], \
                [112.0, -97.0], [100.0, -99.0], [87.0, -102.0], \
                [76.0, -100.0], [64.0, -96.0], [56.0, -89.0], \
                [50.0, -83.0], [47.0, -75.0]] 
                # nose 

elements_b_9 = [[47.0, -144.0], [42.0, -134.0], [40.0, -128.0], \
                [66.0, -120.0], [94.0, -112.0], [150.0, -102.0], \
                [150, -150], [54.0, -150]] # mouth

# elements_b_10 to elements_b_12 are for outline
elements_b_10 = [[-20.0, -42.0], [-13.0, -39.0], [-4.0, -37.0], \
                 [7.0, -37.0], [18.0, -39.0], [26.0, -42.0], \
                 [37.0, -49.0], [41.0, -60.0], [44.0, -68.0], \
                 [46.0, -78.0], [50.0, -84.0], [48.0, -96.0], \
                 [43.0, -106.0], [38.0, -117.0], [31.0, -121.0], \
                 [24.0, -127.0], [10.0, -134.0], [-2.0, -136.0]]
                # outline of the right cheek

elements_b_11 = [[44.0, -67.0], [44.0, -61.0], [45.0, -52.0], \
                 [48.0, -43.0], [52.0, -34.0], [57.0, -28.0], \
                 [64.0, -22.0], [71.0, -17.0], [83.0, -13.0], \
                 [93.0, -10.0], [104.0, -10.0], [114.0, -13.0], \
                 [123.0, -17.0], [131.0, -23.0], [137.0, -33.0], \
                 [142.0, -42.0], [143.0, -52.0], [143.0, -64.0], \
                 [139.0, -74.0], [132.0, -85.0], [123.0, -93.0], \
                 [112.0, -97.0], [100.0, -99.0], [87.0, -102.0], \
                 [76.0, -100.0], [64.0, -96.0], [56.0, -89.0], \
                 [50.0, -83.0], [47.0, -75.0]]
                # outline of the nose

elements_b_12 =[[191.0, 18.0], [178.0, 16.0], [167.0, 10.0], \
                [158.0, 2.0], [149.0, -10.0], [141.0, -28.0], \
                [143.0, -40.0], [146.0, -51.0], [150.0, -62.0]]
                # outline of the left cheek

elements_b_13 = [[-8.0, -7.0], [-9.0, 1.0], [-7.0, 15.0], \
                 [-4.0, 26.0], [0.0, 36.0], [4.0, 45.0], \
                 [10.0, 52.0], [20.0, 58.0], [30.0, 61.0], \
                 [40.0, 60.0], [48.0, 55.0], [54.0, 48.0], \
                 [61.0, 40.0]] # right eyebrow

elements_b_14 = [[83.0, 42.0], [84.0, 50.0], [85.0, 59.0], \
                 [88.0, 67.0], [92.0, 75.0], [97.0, 80.0], \
                 [104.0, 87.0], [112.0, 88.0], [120.0, 88.0], \
                 [127.0, 87.0], [135.0, 85.0], [142.0, 79.0], \
                 [150.0, 71.0]] # left eyebrow

# elements_b_15 to elements_b_19 are for outline
elements_b_15 =[[33.0, -128.0], [55.0, -122.0], [81.0, -115.0], [150.0, -101.0]]
               # outline of the mouth
               
elements_b_16 =[[40.0, -129.0], [43.0, -140.0], [51.0, -150]]
                # outline of the mouth

elements_b_17 = [[-43.0, -150], [-53.0, -137.0], [-61.0, -121.0], \
                 [-66.0, -108.0], [-71.0, -90.0], [-73.0, -70.0], \
                 [-72.0, -55.0], [-70.0, -38.0], [-68.0, -22.0], \
                 [-62.0, -3.0], [-57.0, 9.0], [-48.0, 22.0], \
                 [-39.0, 36.0], [-29.0, 48.0], [-17.0, 60.0], \
                 [-3.0, 71.0], [15.0, 85.0], [32.0, 91.0], \
                 [47.0, 100.0], [65.0, 106.0], [86.0, 110.0], \
                 [106.0, 110.0], [122.0, 111.0], [136.0, 110.0], \
                 [150.0, 107.0]]    # outline of the face


elements_b_18 = [[-150.0, -150.0], [-145.0, -144.0], [-140.0, -137.0], \
                 [-133.0, -133.0], [-124.0, -127.0], [-113.0, -123.0], \
                 [-100.0, -121.0], [-88.0, -120.0], [-78.0, -122.0], \
                 [-69.0, -128.0], [-61.0, -135.0], [-56.0, -145.0], \
                 [-53.0, -150]] # outline of the right hand

elements_b_19 = [[-37.0, -161.0], [-34.0, -166.0], [-28.0, -173.0], \
                 [-22.0, -179.0], [-15.0, -186.0], [-8.0, -191.0], \
                 [1.0, -196.0], [9.0, -200.0], [18.0, -204.0], \
                 [28.0, -208.0]] # outline of the face

elements_b_20 =[[25.0, -8.0], [23.0, -1.0], [23.0, 8.0], [27.0, 15.0], \
                [33.0, 19.0], [39.0, 19.0], [44.0, 16.0], [49.0, 11.0], \
                [50.0, 3.0], [51.0, -7.0], [47.0, -14.0], [41.0, -17.0], \
                [34.0, -18.0], [28.0, -15.0], [25.0, -8.0]] 
                # right eye

elements_b_21 = [[112.0, 17.0], [112.0, 24.0], [112.0, 31.0], \
                 [117.0, 40.0], [124.0, 41.0], [130.0, 41.0], \
                 [135.0, 37.0], [138.0, 28.0], [139.0, 20.0], \
                 [139.0, 13.0], [135.0, 9.0], [130.0, 5.0], \
                 [121.0, 5.0], [118.0, 8.0], [112.0, 17.0]]
                # left eye

# elements_b_22 to elements_b_24 are for white square on the face
elements_b_22 =[[-12.0, -70.0], [-10.0, -84.0], [3.0, -82.0], \
                [1.0, -67.0], [-12, -70]] # square on right cheek

elements_b_23 = [[75.0, -39.0], [78.0, -54.0], [94.0, -52.0], \
                 [92.0, -35.0], [75, -39]] # squaren on the nose

elements_b_24 = [[173.0, -19.0], [177.0, -39.0], [193.0, -36.0], \
                 [190.0, -16.0], [173, -19]] # square on left cheek

elements_b_25 = [[-37.0, -163.0], [-36.0, -171.0], [-35.0, -178.0], \
                [-36.0, -185.0], [-38.0, -193.0], [-41.0, -188.0], \
                [-41.0, -181.0], [-41.0, -173.0], [-38.0, -163.0]]
                # out line of the hand in the bottom tab

#----------------------------------------------------------------------
# function to draw Piece B
def piece_b(x_coord, y_coord):

    # piece's corner 
    piece_left_bottom = [(x_coord - half_piece_size), (y_coord - half_piece_size)]
    piece_left_top = [(x_coord - half_piece_size), (y_coord + half_piece_size)]
    piece_right_bottom = [(x_coord + half_piece_size), (y_coord - half_piece_size)]
    piece_right_top = [(x_coord + half_piece_size), (y_coord + half_piece_size)]

  # processes to draw picture on Piece B

    # make the background
    penup()
    color("PowderBlue")
    width(3)
    setheading(90)
    begin_fill()
    goto(piece_left_bottom)
    pendown()
    goto(piece_left_top)
    goto(piece_right_top)
    setheading(270)
    line_convex()
    right(90)
    line_convex()
    penup()
    end_fill()

    # draw the face
    goto(x_coord - 43, y_coord - 150)
    pendown()
    begin_fill()
    color("BurlyWood")
    for element_b_1 in elements_b_1:
        goto(element_b_1[0] + x_coord, element_b_1[1] + y_coord)
    goto(x_coord + half_piece_size, (piece_right_top[1] - half_piece_size + (tab_gap / 2)))
    setheading(270)
    right(45)
    circle(tab_radius, -270)
    goto(piece_right_bottom)
    setheading(180)
    goto((piece_right_bottom[0] - half_piece_size + (tab_gap / 2)), piece_right_bottom[1])
    right(45)
    circle(tab_radius, -75)
    for element_b_2 in elements_b_2:
        goto((element_b_2[0] + x_coord), element_b_2[1] + y_coord)
    end_fill()
    penup()

    # draw the hand
    goto(piece_left_bottom)
    pendown()
    color("Yellow")
    begin_fill()
    for element_b_3 in elements_b_3:
        goto((element_b_3[0] + x_coord), element_b_3[1] + y_coord)
    penup()
    end_fill()
    goto(x_coord - 37, y_coord - 163)
    pendown()
    begin_fill()
    for element_b_4 in elements_b_4:
        goto(element_b_4[0] + x_coord, element_b_4[1] + y_coord)
    penup()
    end_fill()

    # draw the arm
    goto(x_coord - 37, y_coord - 163)
    pendown()
    color("FireBrick")
    begin_fill()
    for element_b_5 in elements_b_5:
        goto(element_b_5[0] + x_coord, element_b_5[1] + y_coord)
    penup()
    end_fill()

    # draw the cheek
    goto(x_coord - 3, y_coord - 133)
    pendown()
    color("Salmon")
    begin_fill()
    for element_b_6 in elements_b_6:
        goto(element_b_6[0] + x_coord, element_b_6[1] + y_coord)
    penup()
    end_fill()
    goto(x_coord + 150, y_coord - 59)
    pendown()
    begin_fill()
    for element_b_7 in elements_b_7:
        goto(element_b_7[0] + x_coord, element_b_7[1] + y_coord)
    penup()
    end_fill()

    # draw the nose
    goto(x_coord + 45, y_coord - 75)
    pendown()
    color("Crimson")
    begin_fill()
    for element_b_8 in elements_b_8:
        goto(element_b_8[0] + x_coord, element_b_8[1] + y_coord)
    end_fill()
    penup()

    # draw the mouth
    goto(x_coord + 54, y_coord - 150)
    pendown()
    color("Maroon")
    begin_fill()
    for element_b_9 in elements_b_9:
        goto(element_b_9[0] + x_coord, element_b_9[1] + y_coord)
    end_fill()
    penup()

    # draw the outline
    goto(elements_b_10[0][0] + x_coord, y_coord + elements_b_10[0][1])
    pendown()
    color("black")
    width(2)
    for element_b_10 in elements_b_10:
        goto(element_b_10[0] + x_coord, element_b_10[1] + y_coord)
    penup()
    goto(elements_b_11[0][0] + x_coord, y_coord + elements_b_11[0][1])
    pendown()
    for element_b_11 in elements_b_11:
        goto(element_b_11[0] + x_coord, element_b_11[1] + y_coord)
    penup()
    goto(elements_b_12[0][0] + x_coord, y_coord + elements_b_12[0][1])
    pendown()
    for element_b_12 in elements_b_12:
        goto(element_b_12[0] + x_coord, element_b_12[1] + y_coord)
    penup()

    # draw the eyebrows
    goto(elements_b_13[0][0] + x_coord, y_coord + elements_b_13[0][1])
    pendown()
    for element_b_13 in elements_b_13:
        goto(element_b_13[0] + x_coord, element_b_13[1] + y_coord)
    penup()
    goto(elements_b_14[0][0] + x_coord, y_coord + elements_b_14[0][1])
    pendown()
    for element_b_14 in elements_b_14:
        goto(element_b_14[0] + x_coord, element_b_14[1] + y_coord)
    penup()

    # draw the outline
    goto(elements_b_15[0][0] + x_coord, y_coord + elements_b_15[0][1])
    pendown()
    for element_b_15 in elements_b_15:
        goto(element_b_15[0] + x_coord, element_b_15[1] + y_coord)
    penup()
    goto(elements_b_16[0][0] + x_coord, y_coord + elements_b_16[0][1])
    pendown()
    for element_b_16 in elements_b_16:
        goto(element_b_16[0] + x_coord, element_b_16[1] + y_coord)
    penup()
    goto(elements_b_17[0][0] + x_coord, y_coord+ elements_b_17[0][1])
    pendown()
    for element_b_17 in elements_b_17:
        goto(element_b_17[0] + x_coord, element_b_17[1] + y_coord)
    penup()
    goto(elements_b_18[0][0] + x_coord, y_coord + elements_b_18[0][1])
    pendown()
    for element_b_18 in elements_b_18:
        goto(element_b_18[0] + x_coord, element_b_18[1] + y_coord)
    penup()
    goto(elements_b_19[0][0] + x_coord, y_coord + elements_b_19[0][1])
    pendown()
    for element_b_19 in elements_b_19:
        goto(element_b_19[0] + x_coord, element_b_19[1] + y_coord)
    penup()

    # draw the eyes
    goto(elements_b_20[0][0] + x_coord, y_coord + elements_b_20[0][1])
    pendown()
    begin_fill()
    for element_b_20 in elements_b_20:
        goto(element_b_20[0] + x_coord, element_b_20[1] + y_coord)
    penup()
    end_fill()
    goto(elements_b_21[0][0] + x_coord, y_coord + elements_b_21[0][1])
    pendown()
    begin_fill()
    for element_b_21 in elements_b_21:
        goto(element_b_21[0] + x_coord, element_b_21[1] + y_coord)
    penup()
    end_fill()

    # draw the white squares
    goto(elements_b_22[0][0] + x_coord, y_coord + elements_b_22[0][1])
    pendown()
    color("white")
    begin_fill()
    for element_b_22 in elements_b_22:
        goto(element_b_22[0] + x_coord, element_b_22[1] + y_coord)
    penup()
    end_fill()
    goto(elements_b_23[0][0] + x_coord, y_coord + elements_b_23[0][1])
    pendown()
    begin_fill()
    for element_b_23 in elements_b_23:
        goto(element_b_23[0] + x_coord, element_b_23[1] + y_coord)
    penup()
    end_fill()
    goto(elements_b_24[0][0] + x_coord, y_coord + elements_b_24[0][1])
    pendown()
    begin_fill()
    for element_b_24 in elements_b_24:
        goto(element_b_24[0] + x_coord, element_b_24[1] + y_coord)
    penup()
    end_fill()

    # draw outline of the hand in the bottom tab
    color("black")
    goto(elements_b_25[0][0] + x_coord, y_coord + elements_b_25[0][1])
    pendown()
    for element_b_25 in elements_b_25:
        goto(element_b_25[0] + x_coord, element_b_25[1] + y_coord)
    penup()
    
# draw the "Piece B" shape
    penup()
    color("black")
    width(3)
    setheading(90)
    penup()
    goto(piece_left_bottom)
    pendown()
    goto(piece_left_top)
    goto(piece_right_top)
    setheading(270)
    line_convex()
    right(90)
    line_convex()
    penup()
    
################################################################

# data to draw Piece C
elements_c_1_1 = [[-150.0, 106.0], [-144.0, 105.0], [-137.0, 104.0], \
               [-130.0, 103.0], [-124.0, 100.0], [-115.0, 97.0], \
               [-105.0, 93.0], [-97.0, 88.0], [-87.0, 83.0], \
               [-78.0, 76.0], [-70.0, 70.0], [-62.0, 64.0], \
               [-55.0, 56.0], [-48.0, 47.0], [-41.0, 39.0], \
               [-35.0, 29.0], [-29.0, 20.0], [-24.0, 9.0], \
               [-19.0, -2.0], [-16.0, -16.0], [-14.0, -29.0], \
               [-12.0, -37.0], [-12.0, -50.0], [-12.0, -63.0], \
               [-14.0, -76.0], [-15.0, -88.0], [-18.0, -101.0], \
               [-25.0, -119.0], [-28.0, -126.0], [-35.0, -139.0], \
               [-43.0, -150.0], [-150, -150]] 
                # face

elements_c_1_2 = [[-150.0, 106.0], [-144.0, 105.0], [-137.0, 104.0], \
               [-130.0, 103.0], [-124.0, 100.0], [-115.0, 97.0], \
               [-105.0, 93.0], [-97.0, 88.0], [-87.0, 83.0], \
               [-78.0, 76.0], [-70.0, 70.0], [-62.0, 64.0], \
               [-55.0, 56.0], [-48.0, 47.0], [-41.0, 39.0], \
               [-35.0, 29.0], [-29.0, 20.0], [-24.0, 9.0], \
               [-19.0, -2.0], [-16.0, -16.0], [-14.0, -29.0], \
               [-12.0, -37.0], [-12.0, -50.0], [-12.0, -63.0], \
               [-14.0, -76.0], [-15.0, -88.0], [-18.0, -101.0], \
               [-25.0, -119.0], [-28.0, -126.0], [-35.0, -139.0], \
               [-43.0, -150.0]] # face line
                
elements_c_2_1 = [[-24.0, -120.0], [-42.0, -150.0]]
                # arm

elements_c_2_2 = [[-38.0, -197.0], [-26.0, -192.0], [-16.0, -187.0], \
                  [-7.0, -180.0], [2.0, -175.0], [14.0, -167.0], \
                  [31.0, -154.0], [29.0, -152.0], [35.0, -147.0], \
                  [28.0, -148.0], [19.0, -148.0], [10.0, -147.0], \
                  [-2.0, -143.0], [-12.0, -137.0], [-18.0, -132.0], \
                  [-22.0, -122.0]]  # arm
                
elements_c_3_1 = [[-18.0, -101.0], [-21.0, -94.0], [-23.0, -87.0], \
                [-24.0, -81.0], [-24.0, -72.0], [-21.0, -63.0], \
                [-18.0, -55.0], [-13.0, -49.0], [-6.0, -44.0], \
                [1.0, -39.0], [10.0, -36.0], [20.0, -33.0], \
                [29.0, -33.0], [39.0, -33.0], [48.0, -34.0], \
                [59.0, -36.0], [68.0, -40.0], [77.0, -45.0], \
                [84.0, -50.0], [91.0, -58.0], [95.0, -64.0], \
                [98.0, -73.0], [100.0, -82.0], [101.0, -92.0], \
                [99.0, -99.0], [95.0, -107.0], [89.0, -113.0], \
                [83.0, -117.0], [75.0, -121.0], [67.0, -124.0], \
                [61.0, -126.0], [56.0, -127.0], [52.0, -134.0], \
                [47.0, -140.0], [41.0, -144.0], [35.0, -146.0], \
                [28.0, -147.0], [19.0, -146.0], [10.0, -145.0], \
                [2.0, -142.0], [-5.0, -139.0], [-12.0, -135.0], \
                [-17.0, -130.0], [-23.0, -119.0], [-18.0, -101.0]]
                # hand

elements_c_3_2 = [[-10.0, -111.0], [-2.0, -117.0], [8.0, -122.0], \
                  [18.0, -125.0], [31.0, -127.0], [40.0, -129.0], \
                  [50.0, -129.0]] # hand(inside) line
                
elements_c_4 = [[-52.0, -150.0], [-50.0, -147.0], [-45.0, -144.0], \
                [-40.0, -140.0], [-36.0, -140.0], [25.0, -158.0], \
                [37.0, -164.0], [41.0, -172.0], [42.0, -180.0], \
                [42.0, -186.0], [13.0, -169.0], [-28.0, -150.0], \
                [-51.0, -150.0]] # mant

elements_c_5_1 = [[-24.0, -120.0], [-42.0, -150.0]]
                # arm outline

elements_c_5_2 = [[-38.0, -197.0], [-26.0, -192.0], [-16.0, -187.0], \
                  [-7.0, -180.0], [2.0, -175.0], [14.0, -167.0], \
                  [31.0, -154.0], [29.0, -152.0], [35.0, -147.0]]
    
                
elements_c_6 = [[38.0, -163.0], [28.0, -158.0]]
                 # mant line

elements_c_7 = [[-76.0, -2.0], [-68.0, -7.0], \
                [-63.0, -18.0], [-59.0, -29.0], [-59.0, -41.0], \
                [-61.0, -53.0], [-63.0, -63.0], [-67.0, -70.0], \
                [-74.0, -78.0], [-81.0, -83.0], [-88.0, -85.0], \
                [-97.0, -86.0], [-102.0, -86.0], [-107.0, -85.0], \
                [-116.0, -82.0], [-125.0, -80.0], [-130.0, -77.0], \
                [-136.0, -74.0], [-139.0, -70.0], [-143.0, -67.0],
                [-150.0, -60.0]]
                # cheek

elements_c_8 = [[-150.0, -60.0], [-142.0, -72.0], [-135.0, -77.0], \
               [-126.0, -82.0], [-118.0, -84.0], [-108.0, -88.0], \
               [-98.0, -88.0], [-93.0, -87.0], [-84.0, -86.0]]
                # cheek line

elements_c_9 = [[-113.0, -93.0], [-112.0, -101.0], [-112.0, -109.0], \
                [-113.0, -117.0], [-116.0, -125.0], [-119.0, -133.0], \
                [-122.0, -138.0], [-126.0, -144.0], [-133.0, -150.0], \
                [-150.0, -152.0], [-150.0, -102.0], [-113.0, -93.0], \
                [-106.0, -91.0]] # mouth

elements_c_10 = [[-36.0, -201.0], [-28.0, -203.0], [-20.0, -206.0], \
                 [-12.0, -210.0], [-5.0, -217.0], [-2.0, -223.0], \
                 [-7.0, -223.0], [-14.0, -221.0], [-21.0, -218.0], \
                 [-27.0, -214.0], [-31.0, -210.0], [-36.0, -201.0]]   # body part in the bottom tab

#-------------------------------------------------------------------------

# functions to draw Piece C
def piece_c(x_coord, y_coord):
    
    # piece's corner
    piece_left_bottom = [(x_coord - half_piece_size), (y_coord - half_piece_size)]
    piece_left_top = [(x_coord - half_piece_size), (y_coord + half_piece_size)]
    piece_right_bottom = [(x_coord + half_piece_size), (y_coord - half_piece_size)]
    piece_right_top = [(x_coord + half_piece_size), (y_coord + half_piece_size)]

  # processes to draw the picture on Piece C

    # make the background
    penup()
    color("Powderblue")
    width(3)
    setheading(90)
    begin_fill()
    goto(piece_left_bottom)
    pendown()
    line_concave()
    goto(piece_right_top)
    goto(piece_right_bottom)
    setheading(180)
    line_convex()
    end_fill()
    penup()

    # draw the face
    goto(elements_c_1_1[0][0] + x_coord, elements_c_1_1[0][1] + y_coord)
    pendown()
    color("BurlyWood")
    begin_fill()
    for element_c_1_1 in elements_c_1_1:
        goto(element_c_1_1[0] + x_coord, element_c_1_1[1] + y_coord)
    setheading(90)
    line_concave()
    penup()
    end_fill()

    # draw the face outline
    goto(elements_c_1_2[0][0] + x_coord, elements_c_1_2[0][1] + y_coord)
    pendown()
    color("black")
    width(2)
    for element_c_1_2 in elements_c_1_2:
        goto(element_c_1_2[0] + x_coord, element_c_1_2[1] + y_coord)
    penup()
    goto(piece_left_bottom[0] + half_piece_size - (tab_gap / 2), piece_left_bottom[1])
    pendown()
    begin_fill()
    setheading(0)
    right(135)
    circle(tab_radius, 220)
    goto(piece_left_bottom[0] + half_piece_size - (tab_gap / 2), piece_left_bottom[1])
    end_fill()

    # draw the mant
    goto(elements_c_4[0][0] + x_coord, elements_c_4[0][1] + y_coord)
    pendown()
    color("SaddleBrown")
    begin_fill()
    for element_c_4 in elements_c_4:
        goto(element_c_4[0] + x_coord, element_c_4[1] + y_coord)
    penup()
    end_fill()

    # draw the arm
    goto(elements_c_2_1[0][0] + x_coord, elements_c_2_1[0][1] + y_coord)
    pendown()
    color("FireBrick")
    begin_fill()
    for element_c_2_1 in elements_c_2_1:
        goto(element_c_2_1[0] + x_coord, element_c_2_1[1] + y_coord)   
    goto(piece_left_bottom[0] + half_piece_size - (tab_gap / 2), piece_left_bottom[1])
    setheading(0)
    right(135)
    circle(tab_radius, 75)
    for element_c_2_2 in elements_c_2_2:
        goto(element_c_2_2[0] + x_coord, element_c_2_2[1] + y_coord)
    end_fill()
    penup()

    # draw the hand
    goto(elements_c_3_1[0][0] + x_coord, elements_c_3_1[0][1] + y_coord)
    pendown()
    color("yellow")
    begin_fill()
    for element_c_3_1 in elements_c_3_1:
        goto(element_c_3_1[0] + x_coord, element_c_3_1[1] + y_coord)
    penup()
    end_fill()

    # draw the hand inside line
    color("black")
    width(2)
    goto(elements_c_3_1[0][0] + x_coord, elements_c_3_1[0][1] + y_coord)
    pendown()
    for element_c_3_1 in elements_c_3_1:
        goto(element_c_3_1[0] + x_coord, element_c_3_1[1] + y_coord)
    penup()
    goto(elements_c_3_2[0][0] + x_coord, elements_c_3_2[0][1] + y_coord)
    pendown()
    for element_c_3_2 in elements_c_3_2:
        goto(element_c_3_2[0] + x_coord, element_c_3_2[1] + y_coord)
    penup()

    # draw the arm outline
    goto(elements_c_5_1[0][0] + x_coord, elements_c_5_1[0][1] + y_coord)
    pendown()
    color("black")
    for element_c_5_1 in elements_c_5_1:
        goto(element_c_5_1[0] + x_coord, element_c_5_1[1] + y_coord)
    penup()

    # draw the mant outline
    goto(elements_c_6[0][0] + x_coord, elements_c_6[0][1] + y_coord)
    pendown()
    color("black")
    for element_c_6 in elements_c_6:
        goto(element_c_6[0] + x_coord, element_c_6[1] + y_coord)
    penup()

    # draw the left cheek
    goto(-150.0 + x_coord, -60.0 + y_coord)
    setheading(90)
    goto(piece_left_bottom[0], piece_left_bottom[1] + half_piece_size - (tab_gap / 2))
    pendown()
    color("Salmon")
    begin_fill()
    right(135)
    circle(tab_radius, 135)
    for element_c_7 in elements_c_7:
        goto(element_c_7[0] + x_coord, element_c_7[1] + y_coord)
    end_fill()

    # draw the left cheek outine
    penup()
    goto(elements_c_8[0][0] + x_coord, elements_c_8[0][1] + y_coord)
    pendown()
    color("black")
    for element_c_8 in elements_c_8:
        goto(element_c_8[0] + x_coord, element_c_8[1] + y_coord)
    penup()

    # draw the mouth
    color("black")
    goto(elements_c_9[0][0] + x_coord, elements_c_9[0][1] + y_coord)
    pendown()
    begin_fill()
    fillcolor("Maroon")
    for element_c_9 in elements_c_9:
        goto(element_c_9[0] + x_coord, y_coord + element_c_9[1])
    penup()
    end_fill()

    # draw the body part in the bottom tab
    fillcolor("FireBrick")
    goto(elements_c_10[0][0] + x_coord, elements_c_10[0][1] + y_coord)
    pendown()
    begin_fill()
    for element_c_10 in elements_c_10:
        goto(element_c_10[0] + x_coord, element_c_10[1] + y_coord)
    end_fill()
    penup()
    
    # draw the shape of "Piece C"
    penup()
    color("black")
    width(3)
    setheading(90)
    goto(piece_left_bottom)
    pendown()
    line_concave()
    goto(piece_right_top)
    goto(piece_right_bottom)
    setheading(180)
    line_convex()
    penup()

    
#####################################################################    

# data to draw picture on piece D

elements_d_1 = [[43.0, 116.0], [41.0, 106.0], [39.0, 100.0], \
                    [35.0, 94.0], [29.0, 88.0], [22.0, 84.0], \
                    [14.0, 79.0], [6.0, 77.0], [-1.0, 77.0], \
                    [-8.0, 78.0], [-15.0, 79.0], [-20.0, 41.0], \
                    [-8.0, 14.0], [-2.0, 13.0], [2.0, 12.0], \
                    [8.0, 12.0], [15.0, 12.0], [22.0, 12.0], \
                    [25.0, 13.0], [31.0, 14.0], [35.0, 16.0], \
                    [40.0, 19.0], [43.0, 22.0], [47.0, 27.0], \
                    [50.0, 31.0], [53.0, 36.0], [56.0, 42.0], \
                    [59.0, 48.0], [64.0, 60.0], [68.0, 65.0], \
                    [73.0, 69.0], [78.0, 73.0], [84.0, 76.0], \
                    [89.0, 79.0], [93.0, 80.0], [100.0, 80.0], \
                    [113.0, 78.0], [97.0, 100.0], [67.0, 116.0], \
                    [43.0, 116.0]] # mant (black & main)

elements_d_2 = [[-77.0, 5.0], [-58.0, 8.0], [-55.0, -10.0], \
                [-59.0, -13.0], [-65.0, -16.0], [-79.0, -17.0], \
                [-77.0, -11.0], [-77.0, -6.0], [-79.0, 5.0]]
                    # mant (black & minor)

elements_d_3 = [[39.0, 136.0], [41.0, 130.0], [43.0, 123.0], \
                [42.0, 112.0], [49.0, 109.0], [57.0, 105.0], \
                [65.0, 102.0], [73.0, 98.0], [80.0, 94.0], \
                [87.0, 90.0], [95.0, 86.0], [101.0, 82.0], \
                [106.0, 79.0], [112.0, 75.0], [119.0, 70.0], \
                [127.0, 64.0], [138.0, 55.0], [150.0, 44.0], \
                [150.0, 89.0], [146.0, 92.0], [142.0, 96.0], \
                [136.0, 100.0], [130.0, 104.0], [124.0, 107.0], \
                [116.0, 111.0], [108.0, 114.0], [100.0, 118.0], \
                [93.0, 120.0], [69.0, 128.0], [39.0, 136.0]]
                # mant (brown)

elements_d_4 = [[-77.0, -4.0], [-72.0, -3.0], [-68.0, -1.0], \
                [-62.0, 1.0], [-56.0, -9.0], [-51.0, -13.0], \
                [-45.0, -14.0], [-40.0, -14.0], [-33.0, -13.0], \
                [-26.0, -12.0], [-21.0, -7.0], [-17.0, -2.0], \
                [-13.0, 1.0], [-10.0, 5.0], [-7.0, 12.0], \
                [-5.0, 19.0], [-5.0, 25.0], [-4.0, 31.0], \
                [-6.0, 37.0], [-11.0, 42.0], [-7.0, 48.0], \
                [-4.0, 55.0], [-2.0, 63.0], [-1.0, 68.0], \
                [0.0, 77.0]] # body and leg

elements_d_5 = [[-150.0, 97.0], [-142.0, 85.0], [-137.0, 81.0], \
                [-129.0, 80.0], [-121.0, 78.0], [-114.0, 78.0], \
                [-106.0, 78.0], [-99.0, 79.0], [-92.0, 82.0], \
                [-87.0, 87.0], [-84.0, 93.0], [-81.0, 100.0], \
                [-80.0, 105.0], [-73.0, 105.0], [-64.0, 108.0], \
                [-58.0, 111.0], [-55.0, 115.0], [-50.0, 122.0], \
                [-46.0, 128.0], [-43.0, 136.0], [-41.0, 141.0], \
                [-41.0, 150.0], [-61.0, 150.0], [-150.0, 97.0]]
                # scarf

elements_d_6 = [[-150.0, 82.0], [-146.0, 83.0], [-141.0, 85.0], \
                [-136.0, 87.0], [-132.0, 89.0], [-129.0, 94.0], \
                [-132.0, 95.0], [-132.0, 100.0], [-139.0, 99.0], \
                [-150.0, 97.0], [-150.0, 81.0]] # yellow accessory on neck

elements_d_7 = [[-150.0, 88.0], [-144.0, 89.0], [-138.0, 91.0], \
                [-132.0, 92.0], [-126.0, 95.0], [-119.0, 96.0], \
                [-113.0, 100.0], [-108.0, 102.0], [-102.0, 104.0], \
                [-95.0, 108.0], [-89.0, 112.0], [-84.0, 114.0], \
                [-79.0, 119.0], [-73.0, 122.0], [-68.0, 126.0], \
                [-63.0, 130.0], [-60.0, 134.0], [-53.0, 150.0], \
                [-150.0, 150.0], [-150.0, 88.0]] # face

elements_d_8 = [[-150.0, 35.0], [-143.0, 36.0], [-138.0, 38.0], \
                [-132.0, 40.0], [-128.0, 42.0], [-123.0, 45.0], \
                [-119.0, 48.0], [-116.0, 51.0], [-115.0, 54.0], \
                [-115.0, 57.0], [-118.0, 64.0], [-122.0, 66.0], \
                [-128.0, 67.0], [-134.0, 68.0], [-141.0, 68.0], \
                [-150.0, 66.0], [-150.0, 35.0]] # smile mark

elements_d_9 = [[-150.0, 41.0], [-144.0, 40.0], [-140.0, 41.0], \
                [-136.0, 43.0], [-132.0, 46.0], [-131.0, 49.0]]
                # smile mark

elements_d_10 = [[-32.0, 90.0], [-33.0, 87.0], [-35.0, 83.0], \
                 [-38.0, 78.0], [-41.0, 74.0], [-46.0, 69.0], \
                 [-50.0, 65.0], [-55.0, 62.0], [-60.0, 57.0], \
                 [-65.0, 54.0], [-73.0, 49.0], [-77.0, 47.0], \
                 [-82.0, 45.0], [-87.0, 43.0], [-78.0, 27.0], \
                 [-71.0, 30.0], [-65.0, 33.0], [-60.0, 35.0], \
                 [-54.0, 39.0], [-49.0, 44.0], [-44.0, 50.0], \
                 [-37.0, 55.0], [-35.0, 59.0], [-31.0, 65.0], \
                 [-29.0, 70.0], [-27.0, 74.0], [-25.0, 82.0], \
                 [-32.0, 90.0]] # belt (yellow part)

elements_d_11 = [[-87.0, 43.0], [-92.0, 40.0], [-100.0, 37.0], \
                 [-92.0, 30.0], [-86.0, 23.0], [-78.0, 27.0], \
                 [-87.0, 43.0]] # belt (white part)

elements_d_12 = [[-12.0, 44.0], [-16.0, 40.0], [-19.0, 35.0], \
                 [-22.0, 30.0], [-26.0, 25.0], [-30.0, 21.0], \
                 [-35.0, 17.0], [-40.0, 14.0], [-45.0, 11.0], \
                 [-50.0, 9.0], [-55.0, 5.0], [-63.0, 1.0]]
                # the boundary line between the body and the leg

elements_d_13 = [[-150.0, -32.0], [-138.0, -59.0], [-141.0, -61.0], \
                 [-143.0, -66.0], [-144.0, -75.0], [-143.0, -84.0], \
                 [-142.0, -92.0], [-141.0, -101.0], [-138.0, -109.0], \
                 [-134.0, -116.0], [-129.0, -120.0], [-123.0, -122.0], \
                 [-118.0, -123.0], [-111.0, -123.0], [-103.0, -120.0], \
                 [-94.0, -116.0], [-90.0, -112.0], [-85.0, -107.0], \
                 [-82.0, -102.0], [-77.0, -95.0], [-74.0, -89.0], \
                 [-72.0, -82.0], [-70.0, -76.0], [-69.0, -68.0], \
                 [-68.0, -62.0], [-69.0, -53.0], [-70.0, -47.0], \
                 [-71.0, -41.0], [-74.0, -36.0], [-77.0, -32.0], \
                 [-80.0, -30.0], [-83.0, -26.0], [-86.0, -28.0], \
                 [-91.0, -33.0], [-96.0, -37.0], [-101.0, -39.0], \
                 [-107.0, -42.0], [-114.0, -43.0], [-121.0, -43.0], \
                 [-129.0, -42.0], [-134.0, -41.0], [-140.0, -38.0], \
                 [-150.0, -32.0]] # right foot

elements_d_14 = [[-53.0, -14.0], [-31.0, -40.0], [-34.0, -37.0], \
                 [-32.0, -49.0], [-30.0, -56.0], [-28.0, -61.0], \
                 [-24.0, -69.0], [-20.0, -75.0], [-15.0, -80.0], \
                 [-9.0, -85.0], [-3.0, -91.0], [4.0, -93.0], \
                 [10.0, -94.0], [19.0, -95.0], [27.0, -94.0], \
                 [35.0, -90.0], [39.0, -83.0], [41.0, -78.0], \
                 [44.0, -70.0], [45.0, -60.0], [44.0, -50.0], \
                 [44.0, -42.0], [43.0, -35.0], [41.0, -27.0], \
                 [37.0, -20.0], [35.0, -15.0], [32.0, -11.0], \
                 [28.0, -7.0], [23.0, -1.0], [16.0, 4.0], \
                 [12.0, 7.0], [8.0, 10.0], [6.0, 11.0], \
                 [1.0, 12.0], [-5.0, 12.0], [-7.0, 9.0], \
                 [-9.0, 5.0], [-12.0, 1.0], [-15.0, -3.0], \
                 [-18.0, -5.0], [-23.0, -11.0], [-28.0, -14.0], \
                 [-35.0, -14.0], [-41.0, -16.0], [-53.0, -14.0]]
                # left foot

elements_d_15 = [[-150.0, 135.0], [-146.0, 137.0], [-142.0, 140.0], \
                 [-138.0, 144.0], [-133.0, 150.0], [-150.0, 150.0], \
                 [-150.0, 135.0]] # mouth

#-------------------------------------------------------------------------

# function to draw Piece D
def piece_d(x_coord, y_coord):

    # piece's corner
    piece_left_bottom = [(x_coord - half_piece_size), (y_coord - half_piece_size)]
    piece_left_top = [(x_coord - half_piece_size), (y_coord + half_piece_size)]
    piece_right_bottom = [(x_coord + half_piece_size), (y_coord - half_piece_size)]
    piece_right_top = [(x_coord + half_piece_size), (y_coord + half_piece_size)]

  # process to draw the picture on piece D

    # make the background
    penup()
    color("Powderblue")
    width(3)
    setheading(90)
    begin_fill()
    goto(piece_left_bottom)
    pendown()
    line_concave()
    right(90)
    line_concave()
    goto(piece_right_bottom)
    goto(piece_left_bottom)
    end_fill()
    penup()

    # draw the mant (black)
    color("black")
    goto(elements_d_1[0][0] + x_coord, elements_d_1[0][1] + y_coord)
    begin_fill()
    for element_d_1 in elements_d_1:
        goto(element_d_1[0] + x_coord, element_d_1[1] + y_coord)
    end_fill()
    goto(elements_d_2[0][0] + x_coord, elements_d_2[0][1] + y_coord)
    begin_fill()
    for element_d_2 in elements_d_2:
        goto(element_d_2[0] + x_coord, element_d_2[1] + y_coord)
    end_fill()

    # draw the mant (brown)
    goto(elements_d_3[0][0] + x_coord, elements_d_3[0][1] + y_coord)
    width(2)
    fillcolor("SaddleBrown")
    pendown()
    begin_fill()
    for element_d_3 in elements_d_3:
        goto(element_d_3[0] + x_coord, element_d_3[1] + y_coord)
    end_fill()
    penup()

    # draw the body and the leg
    goto(piece_left_top)
    fillcolor("FireBrick")
    pendown()
    begin_fill()
    goto(-150 + x_coord, 150 + y_coord - half_piece_size + (tab_gap / 2))
    setheading(225)
    circle(tab_radius, -135)
    for element_d_4 in elements_d_4:
        goto(element_d_4[0] + x_coord, element_d_4[1] + y_coord)
    setheading(0)
    circle(tab_radius, -135)
    goto(piece_left_top)
    end_fill()
    penup()

    # draw the scarf
    goto(elements_d_5[0][0] + x_coord, elements_d_5[0][1] + y_coord)
    fillcolor("SaddleBrown")
    pendown()
    begin_fill()
    for element_d_5 in elements_d_5:
        goto(element_d_5[0] + x_coord, element_d_5[1] + y_coord)
    end_fill()
    penup()

    # draw the yellow accessory around the neck
    goto(elements_d_6[0][0] + x_coord, elements_d_6[0][1] + y_coord)
    fillcolor("Yellow")
    pendown()
    begin_fill()
    for element_d_6 in elements_d_6:
        goto(element_d_6[0] + x_coord, element_d_6[1] + y_coord)
    end_fill()    
    penup()

    # draw the face
    goto(elements_d_7[0][0] + x_coord, elements_d_7[0][1] + y_coord)
    fillcolor("BurlyWood")
    pendown()
    begin_fill()
    for element_d_7 in elements_d_7:
        goto(element_d_7[0] + x_coord, element_d_7[1] + y_coord)
    end_fill()     
    penup()

    # draw the smile mark
    goto(elements_d_8[0][0] + x_coord, elements_d_8[0][1] + y_coord)
    color("black")
    fillcolor("Yellow")
    pendown()
    begin_fill()
    for element_d_8 in elements_d_8:
        goto(element_d_8[0] + x_coord, element_d_8[1] + y_coord)
    end_fill()
    penup()

    goto(elements_d_9[0][0] + x_coord, elements_d_9[0][1] + y_coord)
    pendown()
    for element_d_9 in elements_d_9:
        goto(element_d_9[0] + x_coord, element_d_9[1] + y_coord)
    penup()
    goto(-135.0 + x_coord, 59.0 + y_coord)
    dot(3)
    goto(-135.0 + x_coord, 57.0 + y_coord)
    dot(3)

    # draw the belt (yellow part)
    goto(elements_d_10[0][0] + x_coord, elements_d_10[0][1] + y_coord)
    pendown()
    begin_fill()
    for element_d_10 in elements_d_10:
        goto(element_d_10[0] + x_coord, element_d_10[1] + y_coord)
    end_fill()
    penup()

    # draw the belt (yellow part)
    goto(elements_d_11[0][0] + x_coord, elements_d_11[0][1] + y_coord)
    fillcolor("white")
    pendown()
    begin_fill()
    for element_d_11 in elements_d_11:
        goto(element_d_11[0] + x_coord, element_d_11[1] + y_coord)
    end_fill()
    penup()

    # draw the boundary line between the body and the leg 
    goto(elements_d_12[0][0] + x_coord, elements_d_12[0][1] + y_coord)
    pendown()
    for element_d_12 in elements_d_12:
        goto(element_d_12[0] + x_coord, element_d_12[1] + y_coord)
    penup()

    # draw the right foot
    goto(elements_d_13[0][0] + x_coord, elements_d_13[0][1] + y_coord)
    fillcolor("yellow")
    pendown()
    begin_fill()
    for element_d_13 in elements_d_13:
        goto(element_d_13[0] + x_coord, element_d_13[1] + y_coord)
    end_fill()
    penup()

    # draw the left foot
    goto(elements_d_14[0][0] + x_coord, elements_d_14[0][1] + y_coord)
    fillcolor("yellow")
    pendown()
    begin_fill()
    for element_d_14 in elements_d_14:
        goto(element_d_14[0] + x_coord, element_d_14[1] + y_coord)
    end_fill()
    penup()

    # draw the mouth
    goto(elements_d_15[0][0] + x_coord, elements_d_15[0][1] + y_coord)
    fillcolor("Maroon")
    pendown()
    begin_fill()
    for element_d_15 in elements_d_15:
        goto(element_d_15[0] + x_coord, element_d_15[1] + y_coord)
    end_fill()
    penup()    

    # draw the shape of "Piece C"
    penup()
    color("black")
    width(3)
    setheading(90)
    goto(piece_left_bottom)
    pendown()
    line_concave()
    right(90)
    line_concave()
    goto(piece_right_bottom)
    goto(piece_left_bottom)
    penup()




#

#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing canvas
setup(canvas_width, canvas_height)

# Give the canvas a neutral background colour
# ***** You can change the background colour if necessary to ensure
# ***** good contrast with your puzzle pieces
bgcolor('light grey')

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by solving your puzzle
title('Four Piece Jigsaw Puzzle - anpanman (Japanese most famous character among children)')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Draw the box that holds unused jigsaw puzzle pieces
draw_box()

# Draw the template that holds the jigsaw pieces
# ***** If you don't want to display the template change the
# ***** argument below to False
draw_template(False)

# Mark the centres of the places where jigsaw puzzle pieces must
# be drawn
# ***** If you don't want to display the coordinates change the
# ***** argument below to False
mark_coords(True)

# Call the student's function to display the attempted solution
# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_attempt(solution)

# Exit gracefully by hiding the cursor and releasing the window
tracer(False)
hideturtle()
done()

#
#--------------------------------------------------------------------#

