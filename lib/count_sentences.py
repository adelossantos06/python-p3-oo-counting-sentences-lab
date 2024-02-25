#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if not isinstance(value, str):
      print("The value must be a string.")
    else:
      self._value = value

  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else:
      return False
    
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False

  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False

  def count_sentences(self):
    sentences =  re.split('[.!?]', self.value)
    sentences = list(filter(None, sentences))
    print(sentences)
    return len(sentences)
