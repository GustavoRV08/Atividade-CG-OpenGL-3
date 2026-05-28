#Os Eixos da Eternidade
import posix
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import random
import math

def teclado(tecla, x, y):
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  match tecla[0]:
  #Tecla x
    case 120:
      gl.glRotatef(-5, 1, 0, 0)
  #Tecla X
    case 88:
      gl.glRotatef(5, 1, 0, 0)
  #Tecla y
    case 121:
      gl.glRotatef(-5, 0, 1, 0)
  #Tecla Y
    case 89:
      gl.glRotatef(5, 0, 1, 0)
  #Tecla z
    case 122:
      gl.glRotatef(-5, 0, 0, 1)
  #Tecla Z
    case 90:
      gl.glRotatef(5, 0, 0, 1)
  gl.glColor3f(1, 1, 1, 1)
  glut.glutWireCube(0.5)
  glut.glutSwapBuffers()

def display():
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glShadeModel(gl.GL_FLAT)
  glu.gluPerspective(60, 1, 0, 10)
  glu.gluLookAt(0, 0, -1,
               0, 0, 0,
               0, 1, 0)
  gl.glColor3f(1, 1, 1, 1)
  glut.glutWireCube(0.5)
  glut.glutSwapBuffers()


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
