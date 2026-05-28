#O Despertar do Objeto Errante
import posix
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import random
import math

class Coordenadas():
  def __init__(self):
    self.x = 0
    self.y = 0

coord = Coordenadas()

def desenhar_triangulo():
  gl.glBegin(gl.GL_TRIANGLES)
  gl.glVertex3f(0, 0.4, 0)
  gl.glVertex3f(-0.4, -0.4, 0)
  gl.glVertex3f(0.4, -0.4, 0)
  gl.glEnd()

def teclado(tecla, x, y):
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  match tecla[0]:
  #Tecla S
    case 115:
      coord.y -= 0.05
  #Tecla W
    case 119:
      coord.y += 0.05
  #Tecla A
    case 97:
      coord.x -= 0.05
  #Tecla D
    case 100:
      coord.x += 0.05
  gl.glShadeModel(gl.GL_FLAT)
  gl.glColor3f(1, 1, 1, 1)
  desenhar_triangulo()
  gl.glTranslatef(coord.x, coord.y, 0)
  glut.glutSwapBuffers()
  coord.x = 0
  coord.y = 0

def display():
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glShadeModel(gl.GL_FLAT)
  gl.glColor3f(1, 1, 1, 1)
  desenhar_triangulo()
  glut.glutSwapBuffers()


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
