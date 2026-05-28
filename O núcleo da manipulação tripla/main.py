#O Núcleo da Manipulação Tripla
import posix
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def desenhar_paralelepipedo():
  #face1
  gl.glBegin(gl.GL_LINE_LOOP)
  gl.glColor(1, 1, 1, 1)
  gl.glVertex3f(-0.2, 0, 0.3)
  gl.glVertex3f(0.2, 0, 0.3)
  gl.glVertex3f(0.2, 0, -0.3)
  gl.glVertex3f(-0.2, 0, -0.3)
  gl.glEnd()
  #face2
  gl.glBegin(gl.GL_LINE_LOOP)
  gl.glColor(1, 1, 1, 1)
  gl.glVertex3f(-0.2, 0, -0.3)
  gl.glVertex3f(0.2, 0, -0.3)
  gl.glVertex3f(0.2, 0.5, -0.3)
  gl.glVertex3f(-0.2, 0.5, -0.3)
  gl.glEnd()
  #face3
  gl.glBegin(gl.GL_LINE_LOOP)
  gl.glColor(1, 1, 1, 1)
  gl.glVertex3f(0.2, 0, -0.3)
  gl.glVertex3f(0.2, 0, 0.3)
  gl.glVertex3f(0.2, 0.5, 0.3)
  gl.glVertex3f(0.2, 0.5, -0.3)
  gl.glEnd()
  #face4
  gl.glBegin(gl.GL_LINE_LOOP)
  gl.glColor(1, 1, 1, 1)
  gl.glVertex3f(0.2, 0, 0.3)
  gl.glVertex3f(-0.2, 0, 0.3)
  gl.glVertex3f(-0.2, 0.5, 0.3)
  gl.glVertex3f(0.2, 0.5, 0.3)
  gl.glEnd()
  #face5
  gl.glBegin(gl.GL_LINE_LOOP)
  gl.glColor(1, 1, 1, 1)
  gl.glVertex3f(-0.2, 0, 0.3)
  gl.glVertex3f(-0.2, 0, -0.3)
  gl.glVertex3f(-0.2, 0.5, -0.3)
  gl.glVertex3f(-0.2, 0.5, 0.3)
  gl.glEnd()
  #face6
  gl.glBegin(gl.GL_LINE_LOOP)
  gl.glColor(1, 1, 1, 1)
  gl.glVertex3f(-0.2, 0.5, 0.3)
  gl.glVertex3f(0.2, 0.5, 0.3)
  gl.glVertex3f(0.2, 0.5, -0.3)
  gl.glVertex3f(-0.2, 0.5, -0.3)
  gl.glEnd()

def teclado(tecla, x, y):
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  desenhar_paralelepipedo()
  match tecla[0]:
    #tecla t
    case 116:
      gl.glTranslatef(-0.1, 0, 0)
    #tecla T
    case 84:
      gl.glTranslatef(0.1, 0, 0)
    #tecla y
    case 121:
      gl.glRotatef(5, 0, 1, 0)
    #tecla Y
    case 89:
      gl.glRotatef(-5, 0, 1, 0)
    #tecla e
    case 101:
      gl.glScalef(0.9, 1, 1)
    #tecla E   
    case 69:
      gl.glScalef(1.1, 1, 1)

  glut.glutSwapBuffers()

def display():
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glShadeModel(gl.GL_FLAT)
  glu.gluPerspective(60, 1, 0, 10)
  glu.gluLookAt(0, 0.25, -1,
               0, 0.25, 0,
               0, 1, 0)
  desenhar_paralelepipedo()
  glut.glutSwapBuffers()


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
