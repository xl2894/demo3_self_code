#!/usr/bin/env python
import sys
import re
import codecs
import numpy

# majority of the code has been removed.
# For adcademic integrity reason, only a small fraction
# of the code remains.
class Context(object): 
    """
    Represent a single input word with context.
    """
    
    def __init__(self, cid, word_form, lemma, pos): 
        self.cid = cid
        self.word_form = word_form
        self.lemma = lemma
        self.pos = pos


    def __repr__(self):
        return None