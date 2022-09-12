#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Alessandro Valitutti

# Last version date: 11 Sep 2022

#########################################################################
#                      IMPORT

import my_regexp

#########################################################################
#                     GLOBAL VARIABLES

global text

##############################################################################
#                      CLASSES
#************************************************************************

#########################################################################
#                      FUNCTIONS
#************************************************************************
#                      change

def change(text):
    step = my_regexp.replace_regexp(text, "([^a-zA-Z]+[pP])o'([^a-zA-Z]+)", '\\1@@@\\2')
    step = my_regexp.replace_regexp(step, "^([pP])o'([^a-zA-Z]+)", '\\1@@@\\2')
    step = my_regexp.replace_regexp(step, "([^a-zA-Z]+[pP])o'$", '\\1@@@')
    step = my_regexp.replace_regexp(step, "a'", 'à')
    step = my_regexp.replace_regexp(step, "e'", 'è')
    step = my_regexp.replace_regexp(step, "i'", 'ì')
    step = my_regexp.replace_regexp(step, "u'", 'ù')
    step = my_regexp.replace_regexp(step, "o'", 'ò')
    step = my_regexp.replace_regexp(step, "@@@", "o'")
    return step

#########################################################################
#                      INSTRUCTIONS
#------------------------------------------------------------------------









