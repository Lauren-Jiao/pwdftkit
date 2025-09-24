# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 15:28:55 2025

@author: Shizhe Jiao
"""

PWDFT_kit_VERSION = "1.0"

# ---------------------------------------------------------------------------------
BOHR2ANG = 0.529177249
ANG2BOHR = 1 / 0.529177249

HARTREE2EV = 27.21138602
EV2HARTREE = 1 / 27.21138602

# Ground State Parameters
ground_state_params = """Mixing_Variable       : potential
Mixing_Type          : broyden
Mixing_MaxDim        : 8
Mixing_StepLength    : 0.7
# Temperature        : 300.0
# Smearing_Scheme    : FD
# Extra_Electron     : 0.0
Calculate_Force_Each_SCF : 0
Temperature          : 0
SCF_Outer_MaxIter    : 999
SCF_Outer_Tolerance  : 1e-5
SCF_Phi_MaxIter      : 499
SCF_Phi_Tolerance    : 1e-7
SCF_Inner_MaxIter    : 5
SCF_Inner_Tolerance  : 1e-6
Eig_MaxIter          : 5
Eig_Tolerance        : 1e-13
XC_Type              : XC_GGA_XC_PBE
PW_Solver            : PPCG
Ecut_Wavefunction    : 15
FFT_Number_Type      : even
Output_Density       : 0
Restart_Density      : 0
# VDW_Type           : DFT-D2
# Spin_Type          : 1
# Spin_Orbit_Coupling  : 0
# Spin_Axis            : [0, 0, 1]"""

# Hybrid Functional Parameters
hybrid_functional_params = """Mixing_Variable       : potential
Mixing_Type          : broyden
Mixing_MaxDim        : 8
Mixing_StepLength    : 0.7
# Temperature        : 300.0
# Smearing_Scheme    : FD
# Extra_Electron     : 0.0
Calculate_Force_Each_SCF : 0
Temperature          : 0
SCF_Outer_MaxIter    : 999
SCF_Outer_Tolerance  : 1e-5
SCF_Phi_MaxIter      : 499
SCF_Phi_Tolerance    : 1e-7
SCF_Inner_MaxIter    : 5
SCF_Inner_Tolerance  : 1e-6
Eig_MaxIter          : 5
Eig_Tolerance        : 1e-13
PW_Solver            : PPCG
Ecut_Wavefunction    : 15
FFT_Number_Type      : even
Output_Density       : 0
Restart_Density      : 0
# VDW_Type           : DFT-D2
XC_Type              : XC_HYB_GGA_XC_HSE06
Hybrid_ACE           : 1
# Hybrid_Mixing_Type : nested
# Hybrid_DF          : 1
# Hybrid_DF_Num_Mu   : 7.0
# Hybrid_DF_Num_GaussianRandom : 2.0
# Hybrid_DF_Tolerance : 1e-20
# Spin_Type          : 1
# Spin_Orbit_Coupling  : 0
# Spin_Axis            : [0, 0, 1]"""

# Molecular Dynamics Parameters
molecular_dynamics_params = """Ion_Move                  : verlet
MD_Time_Step              : 40
Ion_Max_Iter              : 1100
Ion_Temperature           : 300
MD_Extrapolation_Type     : linear
MD_Extrapolation_Variable : wavefun
MD_SCF_Outer_MaxIter      : 999
MD_SCF_Phi_MaxIter        : 499"""

# Pseudopotential Parameters
pseudopotential_params = """# Pseudopotential
# HGH
# PeriodTable        : HGH_Si_O.bin
# Pseudo_Type        : HGH

# ONCV
Pseudo_Type          : ONCV
Use_VLocal           : 1
Use_Atom_Density     : 1
UPF_File:
"""

def test_print_ground_state():
    """测试打印Ground State参数"""
    print("==================== Ground State Parameters ====================")
    print(ground_state_params)
    print("===============================================================")

# ---------------------------------------------------------------------------------
"""
Periodic table. The table currently is of size 110 by 12. 
Each row is a atom with the corresponding atom number. 
And the columns represent anum, mass, venum, iloc, occs, occp, occd, iso, ic, 
isref, ipref, idref in the corresponding order. 
The explainations of these notations are given in the following tables.
"""
NaN = -1

PERIODIC_TABLE_DICT = {
    "brief": {
        "H"  : 1,
        "He" : 2,
        "Li" : 3,
        "Be" : 4,
        "B"  : 5,
        "C"  : 6,
        "N"  : 7,
        "O"  : 8,
        "F"  : 9,
        "Ne" : 10,
        "Na" : 11,
        "Mg" : 12,
        "Al" : 13,
        "Si" : 14,
        "P"  : 15,
        "S"  : 16,
        "Cl" : 17,
        "Ar" : 18,
        "K"  : 19,
        "Ca" : 20,
        "Sc" : 21,
        "Ti" : 22,
        "V"  : 23,
        "Cr" : 24,
        "Mn" : 25,
        "Fe" : 26,
        "Co" : 27,
        "Ni" : 28,
        "Cu" : 29,
        "Zn" : 30,
        "Ga" : 31,
        "Ge" : 32,
        "As" : 33,
        "Se" : 34,
        "Br" : 35,
        "Kr" : 36,
        "Rb" : 37,
        "Sr" : 38,
        "Y"  : 39,
        "Zr" : 40,
        "Nb" : 41,
        "Mo" : 42,
        "Tc" : 43,
        "Ru" : 44,
        "Rh" : 45,
        "Pd" : 46,
        "Ag" : 47,
        "Cd" : 48,
        "In" : 49,
        "Sn" : 50,
        "Sb" : 51,
        "Te" : 52,
        "I"  : 53,
        "Xe" : 54,
        "Cs" : 55,
        "Ba" : 56,
        "La" : 57,
        "Ce" : 58,
        "Pr" : 59,
        "Nd" : 60,
        "Pm" : 61,
        "Sm" : 62,
        "Eu" : 63,
        "Gd" : 64,
        "Tb" : 65,
        "Dy" : 66,
        "Ho" : 67,
        "Er" : 68,
        "Tm" : 69,
        "Yb" : 70,
        "Lu" : 71,
        "Hf" : 72,
        "Ta" : 73,
        "W"  : 74,
        "Rr" : 75,
        "Os" : 76,
        "Ir" : 77,
        "Pt" : 78,
        "Au" : 79,
        "Hg" : 80,
        "Tl" : 81,
        "Pb" : 82,
        "Bi" : 83,
        "Po" : 84,
        "At" : 85,
        "Rn" : 86,
        "Fr" : 87,
        "Ra" : 88,
        "Ac" : 89,
        "Th" : 90,
        "Pa" : 91,
        "U"  : 92,
        "Np" : 93,
        "Pu" : 94,
        "Am" : 95,
        "Cm" : 96,
        "Bk" : 97,
        "Cf" : 98,
        "Es" : 99,
        "Fm" : 100,
        "Md" : 101,
        "No" : 102,
        "Lr" : 103,
        "Rf" : 104,
        "Db" : 105,
        "Sg" : 106,
        "Bh" : 107,
        "Hs" : 108,
        "Mt" : 109,
        "Ds" : 110,
        "Rg" : 111,
        "Cn" : 112,
        "Uut": 113,
        "Fl" : 114,
        "Uup": 115,
        "Lv" : 116,
        "Uus": 117,
        "Uuo": 118
    },
    
    "details": [
        #anum     amass   venum  iloc   occs occp occd iso  ic  isref ipref idref
        [1  ,    1.0079 ,   1,    1,    1,   0,   0,   0,   0,   1,   0,   1], 
        [2  ,    4.0026 ,   2,    1,    2,   0,   0,   0,   0,   1,   1,   1],
        [3  ,    6.9390 ,   1,    1,    1,   0,   0,   0,   0,   1,   1,   1],
        [4  ,    9.0122 ,   2,    1,    2,   0,   0,   0,   0,   1,   1,   1],
        [5  ,   10.811  ,   3,    1,    2,   1,   0,   0,   0,   1,   1,   1],
        [6  ,   12.0112 ,   4,    1,    2,   2,   0,   0,   0,   1,   1,   1],
        [7  ,   14.0067 ,   5,    1,    2,   3,   0,   0,   0,   1,   1,   1],
        [8  ,   15.9994 ,   6,    2,    2,   4,   0,   0,   0,   1,   1,   1],
        [9  ,   18.9984 ,   7,    1,    2,   5,   0,   0,   0,   0,   1,   1],
        [10 ,   20.183  ,   8,    1,    2,   6,   0,   0,   0,   1,   1,   1],
        [11 ,   22.9898 ,   1,    2,    1,   0,   0,   0,   0,   1,   1,   1],
        [12 ,   24.312  ,   2,    1,    2,   0,   0,   0,   0,   1,   1,   1],
        [13 ,   26.9815 ,   3,    1,    2,   1,   0,   0,   0,   1,   1,   1],
        [14 ,   28.086  ,   4,    1,    2,   2,   0,   0,   0,   1,   1,   1],
        [15 ,   30.9738 ,   5,    1,    2,   3,   0,   0,   0,   1,   1,   1],
        [16 ,   32.064  ,   6,    1,    2,   4,   0,   0,   0,   1,   1,   1],
        [17 ,   35.453  ,   7,    1,    2,   5,   0,   0,   0,   1,   1,   1],
        [18 ,   39.948  ,   8,    1,    2,   6,   0,   0,   0,   1,   1,   1],
        [19 ,   39.0983 ,   1,    1,    1,   0,   0,   0,   1,   1,   1,   1],
        [20 ,   40.08   ,   2,    1,    2,   0,   0,   0,   0,   1,   1,   1],
        [21 ,   44.956  ,   3,    1,    2,   0,   1,   1,   0,   1,   1,   1],
        [22 ,   47.90   ,   4,    1,    2,   0,   2,   1,   0,   1,   1,   1],
        [23 ,   50.9415 ,   5,    1,    2,   0,   3,   1,   0,   1,   1,   1],
        [24 ,   51.996  ,   6,    1,    1,   0,   5,   1,   0,   1,   1,   1],
        [25 ,   54.938  ,   7,    1,    2,   0,   5,   1,   0,   1,   1,   1],
        [26 ,   55.847  ,   8,    1,    2,   0,   6,   1,   0,   1,   1,   1],
        [27 ,   58.993  ,   9,    1,    2,   0,   7,   1,   0,   1,   1,   1],
        [28 ,   58.71   ,  10,    1,    2,   0,   8,   0,   0,   1,   1,   1],
        [29 ,   63.546  ,  11,    1,    1,   0,  10,   1,   0,   1,   1,   1],
        [30 ,   65.38   ,  12,    1,    2,   0,  10,   1,   0,   0,   1,   1],
        [31 ,   69.723  ,   3,    1,    2,   1,   0,   1,   1,   1,   1,   1],
        [32 ,   72.64   ,   4,    2,    2,   2,   0,   1,   1,   1,   1,   1],
        [33 ,   74.921  ,   5,    3,    2,   3,   0,   1,   1,   1,   1,   1],
        [34 ,   78.96   ,   6,    3,    2,   4,   0,   1,   0,   1,   1,   1],
        [35 ,   79.904  ,   7,    3,    2,   5,   0,   1,   0,   1,   1,   1],
        [36 ,   83.798  ,   8,    3,    2,   6,   0,   1,   0,   1,   1,   1],
        [37 ,   85.467  , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [38 ,   87.62   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [39 ,   88.905  , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [40 ,   91.224  , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [41 ,   92.906  , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [42 ,   95.96   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [43 ,   97.907  , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [44 ,  101.07   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [45 ,  102.9    , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [46 ,  106.42   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [47 ,  107.86   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [48 ,  112.41   ,  12,    1,    2,   0,  10,   1,   1,   1,   1,   1],
        [49 ,  114.81   ,   3,    1,    2,   1,   0,   1,   1,   1,   1,   1],
        [50 ,  118.71   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [51 ,  121.76   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [52 ,  127.6    ,   6,    1,    2,   4,   0,   1,   1,   1,   1,   1],
        [53 ,  126.9    , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [54 ,  131.29   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [55 ,  132.90   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [56 ,  137.32   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [57 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [58 ,   NaN     ,  10,    1,    2,   0,   1,   1,   1,   1,   1,   1],
        [59 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [60 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [61 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [62 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [63 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [64 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [65 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [66 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [67 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [68 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [69 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [70 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [71 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [72 ,  178.49   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [73 ,  180.94   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [74 ,  183.84   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [75 ,  186.20   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [76 ,  190.23   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [77 ,  192.21   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [78 ,  195.078  ,  10,    1,    1,   0,   9,   1,   0,   1,   1,   1],
        [79 ,  196.96   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [80 ,  200.59   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [81 ,  204.38   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [82 ,  207.2    , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [83 ,  208.98   ,   5,    2,    2,   3,   0,   1,   1,   1,   1,   1],
        [84 ,  208.98   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [85 ,  208.98   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [86 ,  222.01   , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [87 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [88 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [89 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [90 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [91 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [92 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [93 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [94 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [95 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [96 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [97 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [98 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [99 ,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [100,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [101,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [102,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [103,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [104,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [105,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [106,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [107,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [108,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [109,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [110,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [111,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [112,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [113,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [114,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [115,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [116,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [117,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
        [118,   NaN     , NaN,  NaN,  NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN],
    ],
}

# ---------------------------------------------------------------------------------

# 测试打印Ground State参数
if __name__ == "__main__":
    test_print_ground_state()