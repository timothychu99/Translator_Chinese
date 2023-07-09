# encoding=utf8
import numpy

class MatrixOfWords:
  def __init__(self, w, h):
    self.mW = w
    self.mH = h
  def matrix(self, cantolist, mandolist):
    matrix = numpy.empty((self.mH, self.mW), dtype=object)
    for i in range(0, len(cantolist)):
      matrix[0][i] = cantolist[i]
    for i in range(0, len(mandolist)):
      matrix[1][i] = mandolist[i]
    
    return matrix

def translateMatrix(width, cantolist, mandolist):
  mtrx = MatrixOfWords(width, 2)
  return mtrx.matrix(cantolist, mandolist)

