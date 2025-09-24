# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 11:15:41 2025

@author: Shizhe Jiao

"""
import numpy as np
import warnings
import os
import sys
import shutil
sys.path.append(os.path.dirname(__file__))
import constant

def read_vasp_file():
    """Read VASP input file and extract lattice and atomic coordinate information"""
    # Get all files in current directory
    files = os.listdir('.')
    
    # Find POSCAR file or files ending with .vasp
    vasp_files = [f for f in files if f == 'POSCAR' or f.endswith('.vasp')]
    
    if not vasp_files:
        print("Error: No POSCAR file or .vasp files found in current directory.")
        return None
    
    # If only one VASP file found, use it directly
    if len(vasp_files) == 1:
        filename = vasp_files[0]
        print(f"Found VASP file: {filename}")
    else:
        # If multiple VASP files found, let user choose
        print("Multiple VASP files found:")
        for i, f in enumerate(vasp_files):
            print(f"{i+1}. {f}")
        
        while True:
            try:
                choice = int(input("Please enter the number of the file you want to use: "))
                if 1 <= choice <= len(vasp_files):
                    filename = vasp_files[choice-1]
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    # Read the selected VASP file
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except IOError:
        print(f"Error: Cannot read file {filename}")
        return None
    
    # Parse the file content
    # Store first line as system_name
    system_name = lines[0].strip()
    
    # Store second line as factor
    factor = float(lines[1].strip())
    
    # Store lines 3-5 as lattice
    lattice = []
    for i in range(2, 5):
        lattice.append([float(x) for x in lines[i].split()])
    lattice = np.array(lattice)
    
    # Store sixth line as elements
    elements = lines[5].split()
    
    # Store seventh line as atom_number
    atom_number = [int(x) for x in lines[6].split()]
    
    # Store eighth line as DorC (Direct or Cartesian)
    DorC = lines[7].strip()
    
    # Store lines starting from ninth line as coordinates
    coordinates = []
    for i in range(8, len(lines)):
        if lines[i].strip():  # Skip empty lines
            coordinates.append([float(x) for x in lines[i].split()])
    coordinates = np.array(coordinates)
    
    # Print extracted information
    print("\nExtracted information:")
    print(f"System name: {system_name}")
    print(f"Scaling factor: {factor}")
    print("Lattice vectors:")
    for i, vec in enumerate(lattice):
        print(f"  a{i+1}: {vec}")
    print(f"Elements: {elements}")
    print(f"Number of atoms: {atom_number}")
    print(f"Coordinate type: {DorC}")
    print("Atomic coordinates:")
    for i, coord in enumerate(coordinates):
        print(f"  {i+1}: {coord}")
    
    # Return all extracted information
    return {
        'system_name': system_name,
        'factor': factor,
        'lattice': lattice,
        'elements': elements,
        'atom_number': atom_number,
        'DorC': DorC,
        'coordinates': coordinates
    }

def generate_pwdft_input(vasp_data, params):
    """Generate pwdft.in file with VASP structure data and specified parameters"""
    # Extract necessary information from vasp_data
    elements = vasp_data['elements']
    atom_number = vasp_data['atom_number']
    lattice = vasp_data['lattice']
    coordinates = vasp_data['coordinates']
    DorC = vasp_data['DorC']
    
    # Get atom types with atomic numbers
    atom_types = []
    for element in elements:
        if element in constant.PERIODIC_TABLE_DICT["brief"]:
            atom_types.append(constant.PERIODIC_TABLE_DICT["brief"][element])
        else:
            print(f"Warning: Element {element} not found in periodic table dictionary.")
            atom_types.append(0)  # Default to 0 if not found
    
    # Generate the pwdft.in content
    pwdft_content = f"{params}\n\n"
    pwdft_content += "# Structure information from VASP file\n"
    
    # Add Super_Cell in the required format (only diagonal elements without brackets)
    pwdft_content += "begin Super_Cell\n"
    # 修改为将三个对角线元素写在同一行上，并乘以ANG2BOHR常量
    pwdft_content += f"  {lattice[0][0]*constant.ANG2BOHR:.6f}  {lattice[1][1]*constant.ANG2BOHR:.6f}  {lattice[2][2]*constant.ANG2BOHR:.6f}\n"
    pwdft_content += "end Super_Cell\n\n"
    
    # Add Atom_Types_Num
    pwdft_content += f"Atom_Types_Num: {len(atom_types)}\n\n"
    
    # Add Atom_Type and corresponding Atom_Red
    coord_index = 0
    for i, (element, atom_type, num_atoms) in enumerate(zip(elements, atom_types, atom_number)):
        # Add Atom_Type
        pwdft_content += f"Atom_Type: {atom_type}  # {element}\n"
        
        # Add Atom_Red for this element type (without brackets)
        pwdft_content += "begin Atom_Red\n"
        for j in range(num_atoms):
            if coord_index < len(coordinates):
                coord = coordinates[coord_index]
                pwdft_content += f"  {coord[0]:.6f}  {coord[1]:.6f}  {coord[2]:.6f}\n"
                coord_index += 1
        pwdft_content += "end Atom_Red\n\n"
    
    # Write to pwdft.in file
    with open('pwdft.in', 'w') as f:
        f.write(pwdft_content)
    
    print("pwdft.in file generated successfully!")
    print("\nGenerated pwdft.in content:")
    # print(pwdft_content)


def generate_config_yaml(vasp_data, params):
    """Generate config.yaml file with VASP structure data and specified parameters"""
    # Extract necessary information from vasp_data
    elements = vasp_data['elements']
    atom_number = vasp_data['atom_number']
    lattice = vasp_data['lattice']
    coordinates = vasp_data['coordinates']
    DorC = vasp_data['DorC']
    
    # Get atom types with atomic numbers
    atom_types = []
    for element in elements:
        if element in constant.PERIODIC_TABLE_DICT["brief"]:
            atom_types.append(constant.PERIODIC_TABLE_DICT["brief"][element])
        else:
            print(f"Warning: Element {element} not found in periodic table dictionary.")
            atom_types.append(0)  # Default to 0 if not found
    
    # Calculate Super_Cell from lattice diagonals and multiply by ANG2BOHR
    super_cell = [abs(lattice[i][i])*constant.ANG2BOHR for i in range(3)]
    
    # Create Atom_Red list based on coordinates
    atom_red = []
    for coord in coordinates:
        atom_red.append(f"  [  {coord[0]:.6f}  {coord[1]:.6f}  {coord[2]:.6f}  ]")
    
    # Check if pseudopotential_params is already included in params
    if "# Pseudopotential" in params:
        # Generate the config.yaml content without adding pseudopotential_params again
        config_content = f"{params}\n\n"
        config_content += "# Structure information from VASP file\n"
        config_content += f"Atom_Types_Num : {len(atom_types)}\n"
        
        # Add Atom_Type in new format
        config_content += f"Atom_Type      : [  {',  '.join(map(str, atom_types))}  ]\n"
        
        # Add Super_Cell in new format
        config_content += f"Super_Cell     : [  {super_cell[0]:.6f},  {super_cell[1]:.6f},  {super_cell[2]:.6f}  ]\n"
        
        # Add Atom_Num in new format
        config_content += f"Atom_Num       : [  {', '.join(map(str, atom_number))}  ]\n"
        
        # Add Atom_Red in new format
        config_content += "Atom_Red       :\n"
        for atom_coord in atom_red:
            config_content += f"- {atom_coord}\n"
        
        # Add UPF_File entries for each element (pseudopotential section is already included in params)
        # Find the position to add UPF files
        lines = config_content.split('\n')
        insert_index = len(lines)  # Default to end
        for i, line in enumerate(lines):
            if line.strip() == "UPF_File:":
                insert_index = i + 1
                break
        
        # Add UPF_File entries for each element
        upf_entries = []
        for element in elements:
            upf_entries.append(f"  -  {element}_ONCV_PBE-1.0.upf")
        
        # Insert UPF entries at the correct position
        lines = lines[:insert_index] + upf_entries + lines[insert_index:]
        config_content = '\n'.join(lines)
    else:
        # Generate the config.yaml content (original behavior)
        config_content = f"{params}\n\n"
        config_content += "# Structure information from VASP file\n"
        config_content += f"Atom_Types_Num : {len(atom_types)}\n"
        
        # Add Atom_Type in new format
        config_content += f"Atom_Type      : [  {',  '.join(map(str, atom_types))}  ]\n"
        
        # Add Super_Cell in new format
        config_content += f"Super_Cell     : [  {super_cell[0]:.6f},  {super_cell[1]:.6f},  {super_cell[2]:.6f}  ]\n"
        
        # Add Atom_Num in new format
        config_content += f"Atom_Num       : [  {', '.join(map(str, atom_number))}  ]\n"
        
        # Add Atom_Red in new format
        config_content += "Atom_Red       :\n"
        for atom_coord in atom_red:
            config_content += f"- {atom_coord}\n"
        
        # Add Pseudopotential parameters
        config_content += "\n"
        config_content += constant.pseudopotential_params
        
        # Add UPF_File entries for each element
        for element in elements:
            config_content += f"  -  {element}_ONCV_PBE-1.0.upf\n"
    
    # Write to config.yaml file
    with open('config.yaml', 'w') as f:
        f.write(config_content)
    
    print("config.yaml file generated successfully!")
    print("\nGenerated config.yaml content:")
    # print(config_content)
    
    # Copy UPF files from ppdata folder to current directory
    ppdata_path = os.path.join(os.path.dirname(__file__), 'ppdata')
    if os.path.exists(ppdata_path):
        for element in elements:
            upf_filename = f"{element}_ONCV_PBE-1.0.upf"
            source_path = os.path.join(ppdata_path, upf_filename)
            dest_path = os.path.join('.', upf_filename)
            
            if os.path.exists(source_path):
                shutil.copy2(source_path, dest_path)
                print(f"Copied {upf_filename} to current directory.")
            else:
                print(f"Warning: {upf_filename} not found in ppdata folder.")
    else:
        print("Warning: ppdata folder not found.")

# Example usage (uncomment to test)
# if __name__ == "__main__":
#     result = read_vasp_file()


