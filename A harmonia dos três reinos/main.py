#A harmonia dos três reinos
import posix
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def desenhar_triangulo():
  gl.glBegin(gl.GL_TRIANGLES)
  gl.glColor3f(1, 0, 0, 1)
  gl.glVertex3f(-0.6, 0.2, 0)
  gl.glVertex3f(-0.4, -0.2, 0)
  gl.glVertex3f(-0.8, -0.2, 0)
  gl.glEnd()

def desenhar_quadrado():
  gl.glBegin(gl.GL_QUADS)
  gl.glColor3f(0, 1, 0, 1)
  gl.glVertex3f(-0.2, 0.2, 0)
  gl.glVertex3f(0.2, 0.2, 0)
  gl.glVertex3f(0.2, -0.2, 0)
  gl.glVertex3f(-0.2, -0.2, 0)
  gl.glEnd()

def desenhar_pentagono():
  gl.glBegin(gl.GL_POLYGON)
  gl.glColor3f(0, 0, 1, 1)
  gl.glVertex3f(0.4, 0, 0)
  gl.glVertex3f(0.6, 0.2, 0)
  gl.glVertex3f(0.8, 0, 0)
  gl.glVertex3f(0.8, -0.2, 0)
  gl.glVertex3f(0.4, -0.2, 0)
  gl.glEnd()

def teclado(tecla, x, y):
  gl.glLoadIdentity()
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  match tecla[0]:
    case 49:
      desenhar_quadrado()
      desenhar_pentagono()
      gl.glScalef(0.7, 0.7, 0)
      desenhar_triangulo()
    case 50:
      desenhar_triangulo()
      desenhar_pentagono()
      gl.glScalef(0.7, 0.7, 0)
      desenhar_quadrado()
    case 51:
      desenhar_triangulo()
      desenhar_quadrado()
      gl.glScalef(0.7, 0.7, 0)
      desenhar_pentagono()
  glut.glutSwapBuffers()

def display():
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glShadeModel(gl.GL_FLAT)
  desenhar_triangulo()
  desenhar_quadrado()
  desenhar_pentagono()
  glut.glutSwapBuffers()


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
