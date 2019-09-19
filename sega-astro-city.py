# sega-astro-city.py
# David Kiddell 2019-09-19

# dimensions provided by slagcoin.com
# https://www.slagcoin.com/joystick/layout/sega1_l.png

# python/PDF tutorial written by Mike Driscoll
# http://www.blog.pythonlibrary.org/2018/06/05/creating-pdfs-with-pyfpdf-and-python/

from fpdf import FPDF

# letter size is 8.5 x 11 inches, these are
# helper variables in mm to locate initial joystick location
letter_height = 216 # 8.5 inches in mm
#letter_width = 279 # 11 inches in mm

# start the joystick at 50mm from the left, halfway down the page
joystick_pos_x = 50
joystick_pos_y = letter_height / 2

# Helper function to draw a pretty 30mm hole with 3mm bullseye
# parameters are the pdf to draw to, and x and y coords for the
# center of the circle
def drawButtonHole(pdf, x, y):
	pdf.set_fill_color(0, 0, 0)
	pdf.ellipse(x-15, y-15, 30, 30)
	pdf.ellipse(x-5, y-5, 10, 10, 'F')
	pdf.set_fill_color(255, 255, 255)
	pdf.ellipse(x-1.5, y-1.5, 3, 3, 'F')

# Begin a pdf in landscape orientation, units of mm, and letter size paper
pdf = FPDF(orientation="L", unit="mm", format="letter")

# Create a new page a print a title
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Standard Japanese Arcade Layout, Letter Size", ln=1, align="C")

# draw joystick hole
drawButtonHole(pdf, joystick_pos_x, joystick_pos_y)

# bottom row, leftmost button
draw_b1_x = joystick_pos_x + 59
draw_b1_y = joystick_pos_y + 14
drawButtonHole(pdf, draw_b1_x, draw_b1_y)

# top row, leftmost button
draw_t1_x = draw_b1_x + 7
draw_t1_y = draw_b1_y - 38.5
drawButtonHole(pdf, draw_t1_x, draw_t1_y)

# bottom row, second button
draw_b2_x = draw_b1_x + 33
draw_b2_y = draw_b1_y - 14
drawButtonHole(pdf, draw_b2_x, draw_b2_y)

# top row, second button
draw_t2_x = draw_b2_x + 7
draw_t2_y = draw_t1_y - 14
drawButtonHole(pdf, draw_t2_x, draw_t2_y)

# bottom row, third button
draw_b3_x = draw_b2_x + 36
draw_b3_y = draw_b2_y + 6
drawButtonHole(pdf, draw_b3_x, draw_b3_y)

# top row, third button
draw_t3_x = draw_t2_x + 35.5
draw_t3_y = draw_t2_y + 6
drawButtonHole(pdf, draw_t3_x, draw_t3_y)

# bottom row, fourth button
draw_b4_x = draw_b3_x + 34
draw_b4_y = draw_b3_y + 15
drawButtonHole(pdf, draw_b4_x, draw_b4_y)

# top row, fourth button
draw_t4_x = draw_b4_x + 6.5
draw_t4_y = draw_t3_y + 15
drawButtonHole(pdf, draw_t4_x, draw_t4_y)

pdf.output("sega-astro-city.pdf")