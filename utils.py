
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def stroke_output(x, y, format_str, *args):
    buffer = format_str % args
    glPushMatrix()
    glTranslatef(-2.5, y, 0)
    glScalef(0.003, 0.005, 0.005)
    for char in buffer:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(char))
    glPopMatrix()
