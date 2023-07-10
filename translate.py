# encoding=utf8
from mtranslate import translate
from matrix import translateMatrix
import pinyin_jyutping_sentence
from gtts import gTTS
import playsound
import os

class Translate:
  text1 = ""
  text2 = ""
  counter = 0
  translation = ""

  def __init__(self, a, b):
    self.text1 = a
    self.text2 = b
  
  def transret():
    return Translate.translation
     
  def translatePhrase(self, eng_phrase):
    trans = translate(eng_phrase, 'zh-TW') 
    Translate.translation = trans  
    canto = pinyin_jyutping_sentence.jyutping(trans)
    mando = pinyin_jyutping_sentence.pinyin(trans)
    words = canto.split(" ")
    words2 = mando.split(" ")
    return translateMatrix(len(words), words, words2)

def frtrans(inputs):
  hi = Translate(3,3)
  return hi.translatePhrase(inputs)

def frtrans2(inputs):
  translation = translate(inputs, 'zh-TW')
  translation2 = translate(inputs, 'zh-CN')
  texts1 = translation + "\n" + translation2
  translationEng = translate(translation2, 'en')
  texts2 = translationEng
  return texts1 + "\n" + texts2

def frtrans3(ini):
  return ini + "\n" + translate(ini, 'en')

def frtrans4(ini):
  return pinyin_jyutping_sentence.jyutping(ini) + "\n" + pinyin_jyutping_sentence.pinyin(ini)

def transer():
  return Translate.transret()

def count():
  Translate.counter += 1
  return Translate.counter

def voice(input, counter):
  tts = gTTS(text= input, lang='zh')
  x = str(counter)
  filename = os.path.dirname(__file__) + '\\' + input + x + '.mp3'
  tts.save(filename)
  playsound.playsound(filename)
  os.remove(filename)
