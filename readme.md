Arcade controls in PDF format
=============================

The arcade layouts [available at slagcoin.com][1] are a fantastic resource but
they're all in raster format which is not ideal for printing. This is a perfect
use case for the PDF file format which defines a layout in real-world units.

I've taken the dimensions from slagcoin's standard japanese layout and converted
them to a python script that will spit out a dimensionally correct PDF using the
python FPDF library. The python script should be easily adaptable to other layouts,
or A4 paper rather than letter size.

[1]: https://www.slagcoin.com/joystick/layout.html