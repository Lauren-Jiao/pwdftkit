# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 11:15:41 2025

@author: Shizhe Jiao

"""

# Import function1 module to use VASP file reading functionality
import sys
import os
sys.path.append(os.path.dirname(__file__))
import function1 as func

# Import constant module to access parameter strings
import constant

# Global variable to store VASP data
stored_vasp_data = None

def show_menu():
    """Display main menu"""
    print("\n==================== PWDFT-kit ====================")
    print("1. Input file")
    print("2. Electronic Structure")
    print("=======================================================")

def show_submenu_input_file():
    """Display Input File submenu"""
    print("\n------------------ Input File Submenu ------------------")
    print("1.1 VASPtoPWDFT")
    print("-------------------------------------------------------")

def show_submenu_vasp_to_pwdft():
    """Display VASP to PWDFT submenu"""
    print("\n---------------- VASP to PWDFT Submenu -----------------")
    print("1.1.1 config.yaml")
    print("1.1.2 pwdft.in")
    print("-------------------------------------------------------")

def show_submenu_config_yaml():
    """Display config.yaml submenu"""
    print("\n---------------- config.yaml Submenu -----------------")
    print("a) Ground State")
    print("b) Hybrid Functional")
    print("c) Ab initio Molecular Dynamics")
    print("-------------------------------------------------------")

def show_submenu_pwdft_in():
    """Display pwdft.in submenu"""
    print("\n---------------- pwdft.in Submenu -----------------")
    print("a) Ground State")
    print("b) Hybrid Functional")
    print("c) Ab initio Molecular Dynamics")
    print("-------------------------------------------------------")

def show_submenu_electronic_properties():
    """Display Electronic Structure submenu"""
    print("\n------------- Electronic Structure Submenu -------------")
    print("2.1 Energy Levels ()")
    print("2.2 Density of States (DOS)")
    print("2.3 Dielectric Properties")
    print("-------------------------------------------------------")

def handle_menu_choice(choice):
    """Handle main menu selection"""
    # Check if it's a direct submenu option
    if choice == "1.1.1":
        handle_direct_submenu_option(choice)
        return True  
    elif choice == "1.1.2":
        handle_direct_submenu_option(choice)
        return True  
    elif choice == "1":
        # 当用户输入1时，显示子菜单并处理
        show_submenu_input_file()
        sub_choice = input("Please enter submenu option (e.g., 1.1): ")
        result = handle_submenu_input_file_choice(sub_choice)
        return result  
    elif choice.startswith("1."):
        show_submenu_input_file()
        sub_choice = input("Please enter submenu option (e.g., 1.1): ")
        result = handle_submenu_input_file_choice(sub_choice)
        return result  
    elif choice.startswith("2."):
        show_submenu_electronic_properties()
        sub_choice = input("Please enter submenu option (e.g., 2.1): ")
        result = handle_submenu_electronic_properties_choice(sub_choice)
        return result  
    else:
        print("Invalid option, please try again.")
        return False

def handle_direct_submenu_option(choice):
    """Handle direct submenu option input"""
    global stored_vasp_data
    if choice in ["1.1.1", "1.1.2"]:
        print("Executing VASPtoPWDFT conversion function...")
        # Call VASP file reading function
        print("Reading VASP input file...")
        stored_vasp_data = func.read_vasp_file()
        if stored_vasp_data:
            print("VASP file read successfully!")
            # Process based on the direct option
            if choice == "1.1.1":
                handle_submenu_vasp_to_pwdft_choice("1.1.1")
            elif choice == "1.1.2":
                handle_submenu_vasp_to_pwdft_choice("1.1.2")
        else:
            print("Failed to read VASP file.")

def handle_submenu_input_file_choice(choice):
    """Handle Input_file submenu selection"""
    global stored_vasp_data
    if choice == "1.1":
        print("Executing VASPtoPWDFT conversion function...")
        # Call VASP file reading function
        print("Reading VASP input file...")
        stored_vasp_data = func.read_vasp_file()
        if stored_vasp_data:
            print("VASP file read successfully!")
            # Code to process vasp_data can be added here
            
            # 显示子菜单供进一步选择
            show_submenu_vasp_to_pwdft()
            sub_choice = input("Please enter submenu option (e.g., 1.1.1): ")
            result = handle_submenu_vasp_to_pwdft_choice(sub_choice)
            return result  
        else:
            print("Failed to read VASP file.")
            return False
    else:
        print("Invalid option, please try again.")
        return False

def handle_submenu_vasp_to_pwdft_choice(choice):
    """Handle VASP to PWDFT submenu selection"""
    if choice == "1.1.1":
        print("Generating config.yaml file...")
        # config.yaml Menu
        show_submenu_config_yaml()
        sub_choice = input("Please select calculation type (a/b/c): ")
        result = handle_submenu_config_yaml_choice(sub_choice)
        return result  
    elif choice == "1.1.2":
        print("Generating pwdft.in file...")
        # pwdft.in Menu
        show_submenu_pwdft_in()
        sub_choice = input("Please select calculation type (a/b/c): ")
        result = handle_submenu_pwdft_in_choice(sub_choice)
        return result
    else:
        print("Invalid option, please try again.")
        return False

def handle_submenu_config_yaml_choice(choice):
    """Handle config.yaml submenu selection"""
    global stored_vasp_data
    if choice == "a":
        print("Generating config.yaml for Ground State calculation...")
        # Check if VASP data is available
        if stored_vasp_data:
            # Generate config.yaml with VASP data and Ground State parameters
            func.generate_config_yaml(stored_vasp_data, constant.ground_state_params)
            return True  
        else:
            print("Error: No VASP data available. Please read a VASP file first.")
            return False
    elif choice == "b":
        print("Generating config.yaml for Hybrid Functional calculation...")
        # Check if VASP data is available
        if stored_vasp_data:
            # Generate config.yaml with VASP data and Hybrid Functional parameters
            # Combine hybrid_functional_params with pseudopotential_params
            hybrid_params = constant.hybrid_functional_params + "\n\n" + constant.pseudopotential_params
            func.generate_config_yaml(stored_vasp_data, hybrid_params)
            return True  
        else:
            print("Error: No VASP data available. Please read a VASP file first.")
            return False
    elif choice == "c":
        print("Generating config.yaml for Ab initio Molecular Dynamics calculation...")
        # Check if VASP data is available
        if stored_vasp_data:
            # Generate config.yaml with VASP data and Molecular Dynamics parameters
            # Combine molecular_dynamics_params with ground_state_params and pseudopotential_params
            md_params = constant.molecular_dynamics_params + "\n\n" + constant.ground_state_params + "\n\n" + constant.pseudopotential_params
            func.generate_config_yaml(stored_vasp_data, md_params)
            return True  
        else:
            print("Error: No VASP data available. Please read a VASP file first.")
            return False
    else:
        print("Invalid option, please try again.")
        return False

def handle_submenu_pwdft_in_choice(choice):
    """Handle pwdft.in submenu selection"""
    global stored_vasp_data
    if choice == "a":
        print("Generating pwdft.in for Ground State calculation...")
        # Check if VASP data is available
        if stored_vasp_data:
            # Generate pwdft.in with VASP data and Ground State parameters
            func.generate_pwdft_input(stored_vasp_data, constant.ground_state_params)
            return True  
        else:
            print("Error: No VASP data available. Please read a VASP file first.")
            return False
    elif choice == "b":
        print("Generating pwdft.in for Hybrid Functional calculation...")
        # Check if VASP data is available
        if stored_vasp_data:
            # Generate pwdft.in with VASP data and Hybrid Functional parameters
            # Combine hybrid_functional_params with pseudopotential_params
            hybrid_params = constant.hybrid_functional_params + "\n\n" + constant.pseudopotential_params
            func.generate_pwdft_input(stored_vasp_data, hybrid_params)
            return True  
        else:
            print("Error: No VASP data available. Please read a VASP file first.")
            return False
    elif choice == "c":
        print("Generating pwdft.in for Ab initio Molecular Dynamics calculation...")
        # Check if VASP data is available
        if stored_vasp_data:
            # Generate pwdft.in with VASP data and Molecular Dynamics parameters
            # Combine molecular_dynamics_params with ground_state_params and pseudopotential_params
            md_params = constant.molecular_dynamics_params + "\n\n" + constant.ground_state_params + "\n\n" + constant.pseudopotential_params
            func.generate_pwdft_input(stored_vasp_data, md_params)
            return True  
        else:
            print("Error: No VASP data available. Please read a VASP file first.")
            return False
    else:
        print("Invalid option, please try again.")
        return False

def handle_submenu_electronic_properties_choice(choice):
    """Handle electronic properties submenu selection"""
    if choice == "2.1":
        print("Calculating energy levels...")
        # Actual function calls can be added here
        return True 
    elif choice == "2.2":
        print("Calculating density of states...")
        # Actual function calls can be added here
        return True  
    elif choice == "2.3":
        print("Calculating dielectric properties...")
        # Actual function calls can be added here
        return True 
    else:
        print("Invalid option, please try again.")
        return False