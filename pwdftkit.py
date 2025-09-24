# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 15:19:46 2025

@author: Shizhe Jiao
"""

import numpy as np
import warnings

# 导入菜单功能
import content

def banner():

    from constant import PWDFT_kit_VERSION as v

    print(
        f"""
                   [-*-   V {v}    -*-]
[Plane-Wave Density Functional Theory Solver Toolbox]
 ____          ____            ____           ____          ____
(    \        /    \          /    \         /    \        /    )     
|  ###########################################################  |
(__#_/        \____/          \____/         \____/        \_#__)        
   #   ______        ______  _____ _____   _   __ _ _______   #
   #  |  _ \ \      / /  _ \|  ___|_   _| | | / /| |__   __|  #
   #  | |_) \ \ /\ / /| | | | |__   | |   | |/ / | |  | |     #
   A  |  __/ \ V  V / | |_| |  __|  | |  -|   |  | |  | |     Z
   #  | |     \_/\_/  |____/| |     | |   | |\ \ | |  | |     #
   #  |./                   |./     |./   |.| \.\|_|  |./     #   
 __#_          ____            ____           ____          _#__
(  # \        /    \          /    \         /    \        / #  )  
|  ###########################################################  |
(____/        \____/          \____/         \____/        \____)

    """
    )

if __name__ == "__main__":
    # Display banner
    banner()
    
    # Show main menu and handle user selection
    while True:
        content.show_menu()
        choice = input("\nPlease enter an option (e.g., 1 or 2, enter q to quit): ")
        
        if choice.lower() == 'q':
            print("Exiting program.")
            break
        
        if content.handle_menu_choice(choice):
            print("Function executed successfully. Exiting program.")
            break


