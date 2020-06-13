#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 18:52:02 2020

@author: dana
"""

import functions

def test_print_text_section():
    my_list = ["a","b","c"]
    status = functions.print_text_section(my_list)
    assert (status == True)
    
    
def test_click_sections():    
    status = functions.click_sections()
    assert (status == True)
    
    
def test_update_sections():
    position = (0,0)
    status = functions.update_sections(position)
    assert (status == True)
    
def test_expand_screen():
    status = functions.expand_screen()
    assert (status == True)
    
    
def test_update_title(section, color):
    section = 'string'
    color = (0, 0, 0)
    status = functions.update_title(section, color)
    assert (status == True)
    
def test_main_screen():
    status = functions.main_screen()
    assert(status == True)
    
    