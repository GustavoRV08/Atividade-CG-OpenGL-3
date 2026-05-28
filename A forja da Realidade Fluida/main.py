#A Forja da Realidade Fluida
import posix
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

class Pontos:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.z = 0


class Faces:
  def __init__(self):
    self.pontos = []
    self.r = 0
    self.g = 0
    self.b = 0
    self.a = 0

  def add_ponto(self, ponto):
    self.pontos.append(ponto)

fator_cis = 0

def criar_pontos():
  pontos = []

  p1 = Pontos()
  p1.x = -0.2
  p1.y = 0
  p1.z = 0.3

  p2 = Pontos()
  p2.x = 0.2
  p2.y = 0
  p2.z = 0.3

  p3 = Pontos()
  p3.x = 0.2
  p3.y = 0
  p3.z = -0.3

  p4 = Pontos()
  p4.x = -0.2
  p4.y = 0
  p4.z = -0.3

  p5 = Pontos()
  p5.x = -0.2
  p5.y = 0.5
  p5.z = 0.3

  p6 = Pontos()
  p6.x = 0.2
  p6.y = 0.5
  p6.z = 0.3

  p7 = Pontos()
  p7.x = 0.2
  p7.y = 0.5
  p7.z = -0.3

  p8 = Pontos()
  p8.x = -0.2
  p8.y = 0.5
  p8.z = -0.3

  pontos.append(p1)
  pontos.append(p2)
  pontos.append(p3)
  pontos.append(p4)
  pontos.append(p5)
  pontos.append(p6)
  pontos.append(p7)
  pontos.append(p8)
  return pontos

def criar_faces():
  faces = []
  face1 = Faces()
  face1.add_ponto(pontos[0])
  face1.add_ponto(pontos[1])
  face1.add_ponto(pontos[5])
  face1.add_ponto(pontos[4])

  face2 = Faces()
  face2.add_ponto(pontos[0])
  face2.add_ponto(pontos[1])
  face2.add_ponto(pontos[2])
  face2.add_ponto(pontos[3])

  face3 = Faces()
  face3.add_ponto(pontos[1])
  face3.add_ponto(pontos[2])
  face3.add_ponto(pontos[6])
  face3.add_ponto(pontos[5])

  face4 = Faces()
  face4.add_ponto(pontos[2])
  face4.add_ponto(pontos[3])
  face4.add_ponto(pontos[7])
  face4.add_ponto(pontos[6])

  face5 = Faces()
  face5.add_ponto(pontos[0])
  face5.add_ponto(pontos[3])
  face5.add_ponto(pontos[7])
  face5.add_ponto(pontos[4])

  face6 = Faces()
  face6.add_ponto(pontos[4])
  face6.add_ponto(pontos[5])
  face6.add_ponto(pontos[6])
  face6.add_ponto(pontos[7])

  faces.append(face1)
  faces.append(face2)
  faces.append(face3)
  faces.append(face4)
  faces.append(face5)
  faces.append(face6)
  return faces


pontos = criar_pontos()
faces = criar_faces()



def desenhar_faces():
  for i in range(len(faces)):
    gl.glBegin(gl.GL_LINE_LOOP)
    for j in range(len(faces[i].pontos)):
      gl.glVertex3f(faces[i].pontos[j].x+faces[i].pontos[j].y*fator_cis, 
                    faces[i].pontos[j].y, 
                    faces[i].pontos[j].z)
    gl.glEnd()

def teclado(tecla, x, y):
  global fator_cis
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  match tecla[0]:
    case 104:
      fator_cis += 0.1
    case 72:
      fator_cis -= 0.1
    case 122:
      fator_cis = 0
  desenhar_faces()
  glut.glutSwapBuffers()


def display():
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glShadeModel(gl.GL_FLAT)
  glu.gluPerspective(60, 1, 0, 10)
  glu.gluLookAt(0, 0.25, -1,
                 0, 0.25, 0,
                 0, 1, 0)
  desenhar_faces()
  glut.glutSwapBuffers()




glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Gustavo Rodrigues Viana')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
