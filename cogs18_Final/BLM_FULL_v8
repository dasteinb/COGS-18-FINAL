#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:23:22 2020

@author: dana
"""


"""
Created on Fri Jun 12 10:26:51 2020

@author: dana
"""

import pygame
import time

# Inititaized pygame window 
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define screen dimensions 
SCREEN_WIDTH = 870
SCREEN_HEIGHT = 870

# Define sections
row_1 = ['About', 'History', 'Actions']
row_2 = ['Learn', 'Petitions', 'Current News'] 
row_3 = ['Donate', 'Social Media', 'Merch']
     
# Defines font
font = pygame.font.SysFont('Ariel', 50, True, False)
font2 = pygame.font.SysFont('Ariel', 20, True, False)

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
     
# Set title of pygame window
pygame.display.set_caption("BLM Info")

# Definingn Functions 
def print_text_section(my_list):
        """Displays text of each section

        Parameters
        ----------
        my_list : list
            list of strings to be displayed.

        Returns
        -------
        None.

        """
        def print_text(text):
            """
            prints out text on panel  
    
            Parameters
            ----------
            text : string
                string to be printed on screen.
    
            Returns
            -------
            None.
    
            """
            temp_text = font2.render(text, True, WHITE)
            screen.blit(temp_text, [900, n])
            
        # Starting y coordinate for text
        n = 120
        
        # For loop that prints out text 
        for i in my_list:
            print_text(i)
            n= n + 20 

def about_info():
    """Fills in info for about section 

    Returns
    -------
    None.

    """
    # Text strings 
    about_text_1 = "BlackLivesMatter was founded in 2013 in response" 
    about_text_2 = "to the acquittal of Trayvon Martin’s murderer." 
    about_text_3 = "Black Lives Matter Foundation, Inc is a global" 
    about_text_4 = "organization in the US, UK, and Canada, whose" 
    about_text_5 = "mission is to eradicate white supremacy and" 
    about_text_6 = "build local power to intervene in violence"
    about_text_7 = "inflicted on Black communities by the state and" 
    about_text_8 = "vigilantes. By combating and countering act of"
    about_text_9 = "violence,creating space for Black imagination"
    about_text_10 = "and innovation, and centering Black joy, we are winning"
    about_text_11 = "immediate improvements in our lives."
    about_text_12 = "Taken from https://blacklivesmatter.com/about/"
                    
    # List of Text strings
    about_texts = [about_text_1, about_text_2, about_text_3, about_text_4,
                   about_text_5, about_text_6, about_text_7, about_text_8,
                   about_text_9, about_text_10, about_text_11, about_text_12]
    
    print_text_section(about_texts)

    #Updates display
    pygame.display.update()

def history_info(): 
    """Fills in info for history section 

    Returns
    -------
    None.

    """
    history_text_1 = "In 2013, three radical Black organizers —"
    history_text_2 = "Alicia Garza, Patrisse Cullors, and Opal"
    history_text_3 = "Tometi — created a Black-centered political" 
    history_text_4 = "will and movement building project called" 
    history_text_5 = "#BlackLivesMatter. It was in response"
    history_text_6 = "to the acquittal of Trayvon Martin’s"
    history_text_7 = "murderer, George Zimmerman."
    history_text_8 =  "                           "
    history_text_9 = "The project is now a member-led global" 
    history_text_10 = "network of more than 40 chapters. Our"
    history_text_11 = "members organize and build local power"                   
    history_text_12 = "to intervene in violence inflicted on Black"
    history_text_13 = "communities by the state and vigilantes."
    history_text_14 = "Black Lives Matter is an ideological and" 
    history_text_15 = "political intervention in a world where" 
    history_text_16 = "Black lives are systematically and" 
    history_text_17 = "intentionally targeted for demise. It is an" 
    history_text_18 = "affirmation of Black folks’ humanity, our" 
    history_text_19 = "contributions to this society, and our"
    history_text_20 = "resilience in the face of deadly oppression."
    history_text_21 = "Taken from : https://blacklivesmatter.com/herstory/"
                 
    history_texts = [history_text_1, history_text_2, history_text_3, 
                     history_text_4, history_text_5, history_text_6,
                     history_text_7, history_text_8, history_text_9, 
                     history_text_10, history_text_11, history_text_12, 
                     history_text_13, history_text_14, history_text_15, 
                     history_text_16, history_text_17, history_text_18, 
                     history_text_19, history_text_20, history_text_21]                
                      
    print_text_section(history_texts)                 
   
    #Updates display
    pygame.display.update()                  
                                   
def actions_info():
    """Fills in info for actions section 

    Returns
    -------
    None.

    """
    actions_text_1 = "February 2019: #Free21Savage: Following Shéyaa Bin" 
    actions_text_2 = "Abraham-Joseph’s detainment by the Immigration" 
    actions_text_3 = "Customs and Enforcement (ICE) agency, Black Lives" 
    actions_text_4 = "Matter Global Network joined with a consortium of" 
    actions_text_5 = "nearly 60 celebrities, top human rights organizations" 
    actions_text_6 = "(including Color of Change, BAJI, UndocuBlack Network," 
    actions_text_7 = "Define American, and United We Dream), and"
    actions_text_8 = "communications and legal teams to advocate for the"
    actions_text_9 = "release of Abraham-Joseph, to continue to pressure"
    actions_text_10 = "ICE, and to draw attention to the need for"
    actions_text_11 = "immigration reform — the unfair targeting of Black"
    actions_text_12 = "immigrants and the 600,000 undocumented Black"
    actions_text_13 = "immigrants in the US."
    actions_text_14 = "                                             " 
    actions_text_15 = "September 2018: Stephon Clark: Marking the six-month" 
    actions_text_16 = "anniversary of the murder of Stephon Clark, Black" 
    actions_text_17 = "Lives Matter Global Network activists used 175"
    actions_text_18 = "caskets to represent these lives and to magnify the"
    actions_text_19 = "impact that hese fatalities have on our community."
    actions_text_20 = "This action was intended to highlight the violence"
    actions_text_21 = "inflicted upon Black bodies by the police force and"      
    actions_text_22 = "the urgent need to transform policing in America," 
    actions_text_23 = "and to call for justice, transparency, and" 
    actions_text_24 = "accountability. We demanded an increased interest"
    actions_text_25 = "in investing in our communities including promoting"
    actions_text_26 = "education and resources an divesting from" 
    actions_text_27 = "over-policing. BLM activists were joined by: Women"
    actions_text_28 = "or Equality, Voices of the Youth, APTP, PICO, BSU"
    actions_text_29 = "Sacramento City, AGNT, NAACP, SURJ, HIP, Immigration"
    actions_text_30 = "Brown Berets, and a host of others."
    actions_text_31 = "From https://blacklivesmatter.com/global-actions/"                    
                       
    actions_texts = [actions_text_1, actions_text_2, actions_text_3, 
                     actions_text_4, actions_text_5, actions_text_6, 
                     actions_text_7, actions_text_8, actions_text_9, 
                     actions_text_10, actions_text_11, actions_text_12,
                     actions_text_13, actions_text_14, actions_text_15,
                     actions_text_16, actions_text_17, actions_text_18,
                     actions_text_19, actions_text_20, actions_text_21,
                     actions_text_22, actions_text_23, actions_text_23,
                     actions_text_24, actions_text_25, actions_text_26, 
                     actions_text_27, actions_text_28, actions_text_29,
                     actions_text_30, actions_text_31] 
    
                       
    print_text_section(actions_texts)    

    #Updates display
    pygame.display.update()
    
def learn_info():
    """Fills in info for learn section 

    Returns
    -------
    None.

    """
    learn_text_1 = "BLM has a series called 'What Matters.' There are"
    learn_text_2 = "currently 4 episodes: (1) Exploring the Media's Role" 
    learn_text_3 = "in COVID-19 with Marc Lamont Hill, (2) Say Her Name "
    learn_text_4 = "- Breonna Taylor, a Connnversationn with Tamika"
    learn_text_5 = "Mallory and Taylor Family Attorney Lonita Baker, (3)" 
    learn_text_6 = "Coronavirus- Answering Public Health Concern with"
    learn_text_7 = "Dr. Cedric Dark, (4) Black Lives Matter's South Bend" 
    learn_text_8 = "Members - Communinty Organizers. You can find these"
    learn_text_9 = "episodes at https://blacklivesmatter.com/whatmatters/"
    
    learn_texts = [learn_text_1, learn_text_2, learn_text_3, learn_text_4,
                   learn_text_5, learn_text_6, learn_text_7, learn_text_8,
                   learn_text_9]

    print_text_section(learn_texts)    

    #Updates display
    pygame.display.update()
                    
def petition_info():
    """Fills in info for petitions section 

    Returns
    -------
    None.

    """
    petition_text_1 = "#DefundThePolice: Enough is enough. Our pain, our"
    petition_text_2 = "cries, and our need to be seen and heard resonate" 
    petition_text_3 = "throughout this entire country.We demand"
    petition_text_4 = "acknowledgment and accountability for the devaluation"
    petition_text_5 = "and dehumanization of Black life at the hands of"
    petition_text_6 = "the police. We call for radical, sustainable"
    petition_text_7 = "solutions that affirm the prosperity of Black lives."
    petition_text_8 = "George Floyd’s violent death was a breaking point— "
    petition_text_9 = "an all too familiar reminder that, for Black people,"
    petition_text_10 = "law enforcement doesn’t protect or save our lives." 
    petition_text_11 = "They often threaten and take them. Right now," 
    petition_text_12 = "Minneapolis and cities across our country are on"
    petition_text_13 = "fire, and our people are hurting — the violence" 
    petition_text_14 = "against Black bodies felt in the ongoing mass"
    petition_text_15 = "disobedience, all while we grapple with a pandemic" 
    petition_text_16 = "that is disproportionately affecting, infecting, and"
    petition_text_17 = "killing us. We call for an end to the systemic"                  
    petition_text_18 = "racism that allows this culture of corruption to go" 
    petition_text_19 = "unchecked and our lives to be taken. We call for a" 
    petition_text_20 = "national defunding of police. We demand investment in"                  
    petition_text_21 = "our communities and the resources to ensure Black" 
    petition_text_22 = "people not only survive, but thrive. If you’re"
    petition_text_23 = "with us, add your name to the petition right now and"                  
    petition_text_24 = "help us spread the word. Sign petition @"
    petition_text_25 = "https://blacklivesmatter.com/defundthepolice/ "                
                      
    petition_texts = [petition_text_1, petition_text_2, petition_text_3,
                       petition_text_4, petition_text_5, petition_text_6,
                       petition_text_7, petition_text_8, petition_text_9,
                       petition_text_10, petition_text_11, petition_text_12,
                       petition_text_13, petition_text_14, petition_text_15,
                       petition_text_16, petition_text_17, petition_text_18,
                       petition_text_19, petition_text_20, petition_text_21,
                       petition_text_22, petition_text_23, petition_text_24, 
                       petition_text_25]               
   
    print_text_section(petition_texts)    

    #Updates display
    pygame.display.update()                 
                      
def current_news_info():
    """Fills in info for current news section 

    Returns
    -------
    None.

    """
    current_news_text_1 = "June 11th: Black Lives Matter Global Network"
    current_news_text_2 = "Foundation Announces $6.5 Million Fund to Support" 
    current_news_text_3 = "Organizing Work "
    current_news_text_4 = "                                          "
    current_news_text_5 = "June 5th: Happy Birthday, Breonna"
    current_news_text_6 = "                                          "
    current_news_text_7 = "June 4th: A Moment of Silence for George Floyd"
    current_news_text_8 = "                                          "
    current_news_text_9 = "June 2nd: What Matters Ep. 4: Black Lives"
    current_news_text_10 = "Matter’s South Bend Members – Community"
    current_news_text_11 = "Organizers"
    current_news_text_12 = "                                          "                     
    current_news_text_13 = "May 30th: #DefundThePolice"  
    current_news_text_14 = "Articles and more news can be found @"
    current_news_text_15 = "https://blacklivesmatter.com/news/"
                          
    current_news_texts = [current_news_text_1, current_news_text_2,
                         current_news_text_3, current_news_text_4,
                         current_news_text_5, current_news_text_6,
                         current_news_text_7, current_news_text_8,
                         current_news_text_9, current_news_text_10,
                         current_news_text_11, current_news_text_12,
                         current_news_text_13, current_news_text_14,
                         current_news_text_15]
   
    print_text_section(current_news_texts)    

    #Updates display
    pygame.display.update()   
    
def donate_info():
    """Fills in info for donate section 

    Returns
    -------
    None.

    """
    donate_text_1 = "You can donate to the Black Lives Matter Movement @"
    donate_text_2 = "https://secure.actblue.com/donate/ms_blm_homepage_2019"
    
    donate_texts= [donate_text_1, donate_text_2]
    
    
    print_text_section(donate_texts)    

    #Updates display
    pygame.display.update()   
    
    
def social_media_info():
    """Fills in info for social media section 

    Returns
    -------
    None.

    """
    social_media_text_1 = "Facebook:"
    social_media_text_2 = "https://www.facebook.com/BlackLivesMatter/" 
    social_media_text_3 = "Twitter: @Blklivesmatter"
    social_media_text_4 = "Instagram: @Blklivesmatter"
    
    social_media_texts = [social_media_text_1, social_media_text_2, 
                          social_media_text_3, social_media_text_4
                          ]
    
    
    print_text_section(social_media_texts)    

    #Updates display
    pygame.display.update() 
def merch_info():
    """Fills in info for merch section 

    Returns
    -------
    None.

    """
    merch_text_1 = "You have find T-shirts, hats, stickers, longsleeves," 
    merch_text_2 = "sweatshirts, masks, pins, bracelets, and flags @"
    merch_text_3 = "https://store.blacklivesmatter.com/store/"
                    
    merch_texts = [merch_text_1, merch_text_2, merch_text_3]
    
     
    print_text_section(merch_texts)    

    #Updates display
    pygame.display.update() 
    
    
    
def click_sections():
    """Sets up info panels for each section when click it 

    Returns
    -------
    position

    """
    
    position = (0, 0)
    
    event = pygame.event.get()
    
    # Gets position of mouse when click
    for ev in event:
        if ev.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            print(position)
        update_sections(position)
  
def update_sections(position):
    """Updates the side of the screen with information of selection section
    

    Returns
    -------
    None.

    """
   
    
    def expand_screen():
        """Expands the screen (to fill in with info) 
    
        Parameters
        ----------
        width : TYPE
            DESCRIPTION.
    
        Returns
        -------
        None.
    
        """
        
        screen = pygame.display.set_mode((1300, 870))
        
        # Updates display
        pygame.display.flip()
        
    def update_title(section, color):
        """Updates the title of the expanded screen based on section clicked
    
        Parameters
        ----------
        section : string
             section being referenced.
        color : TYPE
            list corresponding to a colot (pre-defined).
    
        Returns
        -------
        None.
    
        """
        
        main_screen()
        
        
        # Creates new title with input parameters
        temp_text = font.render(section, True, color)
        screen.blit(temp_text, [1050, 75])
    
        #Updates display
        pygame.display.update()
            
   
    
    # Checks if mouse is in... 
    if (position[0] > 0 and position[0] < 280):
        # About section 
        if (position[1] > 0 and position[1] < 280):
            expand_screen()
            update_title(row_1[0], BLUE)
            about_info()
            
        # Learn Section
        elif (position[1] > 290 and position[1] < 570):
             expand_screen()
             update_title(row_2[0], RED)
             learn_info()
            
        # Donate section
        else:
             expand_screen()
             update_title(row_3[0], GREEN)
             donate_info()
            
    if (position [0] > 290 and position [0] < 570): 
        # History section 
         if (position[1] > 0 and position[1] < 280):
             expand_screen()
             update_title(row_1[1], BLUE)
             history_info()
             
        # Petitions section 
         elif (position[1] > 290 and position[1] < 570):
             expand_screen()
             update_title(row_2[1], RED)
             petition_info()
            
         # Social Media section 
         else:
             expand_screen()
             update_title(row_3[1], GREEN)
             social_media_info()
            
    if (position [0] > 580) : 
        # Actions section
          if (position[1] > 0 and position[1] < 280):
             expand_screen()
             update_title(row_1[2], BLUE)
             actions_info()
             
        # Currnt News section
          elif (position[1] > 290 and position[1] < 570):
             expand_screen()
             update_title(row_2[2], RED)
             current_news_info()
             
         # Merch section
          else:
             expand_screen()
             update_title(row_3[2], GREEN)
             merch_info()
    
def main_screen():
    """Creates the main interface of the game/info panel, segemented
    

    Returns
    -------
    None.

    """
    # sets up screen
    screen.fill(BLACK)
        
        
    # Draws boxes for sections
    pygame.draw.rect(screen, BLUE, [0, 0, 280, 280], 2)
    pygame.draw.rect(screen, BLUE, [290, 0, 280, 280], 2)
    pygame.draw.rect(screen, BLUE, [580, 0, 280, 280], 2)
    pygame.draw.rect(screen, RED, [0, 290, 280, 280], 2)
    pygame.draw.rect(screen, RED, [290, 290, 280, 280], 2)
    pygame.draw.rect(screen, RED, [580, 290, 280, 280], 2)
    pygame.draw.rect(screen, GREEN, [0, 580, 280, 280], 2)
    pygame.draw.rect(screen, GREEN, [290, 580, 280, 280], 2)
    pygame.draw.rect(screen, GREEN, [580, 580, 280, 280], 2)
            
           
    # Set text titles for Row 1
    text_1 = font.render(row_1[0], True, WHITE)
    screen.blit(text_1, [100, 125])
    text_2 = font.render(row_1[1], True, WHITE)
    screen.blit(text_2, [355, 125])
    text_3 = font.render(row_1[2], True, WHITE)
    screen.blit(text_3, [650, 125])
        
    # Set text titles for Row 2
    text_4 = font.render(row_2[0], True, WHITE)
    screen.blit(text_4, [100, 400])
    text_5 = font.render(row_2[1], True, WHITE)
    screen.blit(text_5, [355, 400])
    text_6 = font.render(row_2[2], True, WHITE)
    screen.blit(text_6, [590, 400])
        
    # Set text titles for Row 3 
    text_7 = font.render(row_3[0], True, WHITE)
    screen.blit(text_7, [80, 700])
    text_8 = font.render(row_3[1], True, WHITE)
    screen.blit(text_8, [310, 700])
    text_9 = font.render(row_3[2], True, WHITE)
    screen.blit(text_9, [650, 700])

def main():
    """Runs Program 
    
    """
    
    running = True
    clock = pygame.time.Clock()
     
    while running:
        for event in pygame.event.get():
            print(pygame.QUIT)
            if event.type == pygame.QUIT:  
                    running = False
       
        main_screen()
        pygame.display.flip()
        time.sleep(8)
            
            
        click_sections()
        
        
 
        
    #limits while loop to 60 times/s 
    clock.tick(60)
    
    pygame.quit()

main()
