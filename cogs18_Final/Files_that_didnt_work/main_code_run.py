#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:26:51 2020

@author: dana
"""

import pygame
import time
import functions_v2 as functions

# Inititaized pygame window 




def main():
    """ Runs Program  
    

    Returns
    -------
    None.

    """
    
    running = True
    clock = pygame.time.Clock()
         
    while running:
        for event in pygame.event.get():
            print(pygame.QUIT)
            if event.type == pygame.QUIT:  
                running = False
       
    functions.main_screen()
    
    pygame.display.flip()
    
    # Sets delay 
    time.sleep(8)
            
    functions.click_sections()

    # Limits while loop to 60 times/s 
    clock.tick(60)
    
    pygame.quit()

main()
