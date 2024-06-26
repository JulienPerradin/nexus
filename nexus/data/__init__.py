import numpy as np

__all__ = [
    "correlation_length",
    "atomic_masses",
    "atomic_numbers",
    "atomic_names",
    "chemical_symbols",
]

correlation_lengths = np.array(
    [
        -3.7390,  # H
        np.nan,  # He
        -1.90,  # Li
        7.79,  # Be
        5.30,  # B
        6.6460,  # C
        9.36,  # N
        5.803,  # O
        5.654,  # F
        4.566,  # Ne
        3.63,  # Na
        5.375,  # Mg
        3.449,  # Al
        4.149,  # Si
        5.13,  # P
        2.847,  # S
        9.5770,  # Cl
        1.909,  # Ar
        3.67,  # K
        4.70,  # Ca
        12.29,  # Sc
        -3.438,  # Ti
        -0.3824,  # V
        3.635,  # Cr
        -3.73,  # Mn
        9.45,  # Fe
        2.49,  # Co
        10.3,  # Ni
        7.718,  # Cu
        5.680,  # Zn
        7.288,  # Ga
        8.185,  # Ge
        6.58,  # As
        7.970,  # Se
        6.795,  # Br
        7.81,  # Kr
        7.09,  # Rb
        7.02,  # Sr
        7.75,  # Y
        7.16,  # Zr
        7.054,  # Nb
        6.715,  # Mo
        np.nan,  # Tc
        7.03,  # Ru
        5.88,  # Rh
        5.91,  # Pd
        5.922,  # Ag
        4.87,  # Cd
        4.065,  # In
        6.225,  # Sn
        5.57,  # Sb
        5.80,  # Te
        5.28,  # I
        4.92,  # Xe
        5.42,  # Cs
        5.07,  # Ba
        8.24,  # La
        4.84,  # Ce
        4.58,  # Pr
        7.69,  # Nd
        np.nan,  # Pm
        0.80,  # Sm
        7.22,  # Eu
        6.5,  # Gd
        7.38,  # Tb
        16.9,  # Dy
        8.01,  # Ho
        7.79,  # Er
        7.07,  # Tm
        12.43,  # Yb
        7.21,  # Lu
        7.7,  # Hf
        6.91,  # Ta
        4.86,  # W
        9.2,  # Re
        10.7,  # Os
        10.6,  # Ir
        9.60,  # Pt
        7.63,  # Au
        12.692,  # Hg
        12.692,  # Tl
        9.405,  # Pb
        8.532,  # Bi
        np.nan,  # Po
        np.nan,  # At
        np.nan,  # Rn
        np.nan,  # Fr
        np.nan,  # Ra
        np.nan,  # Ac
        10.31,  # Th
        9.1,  # Pa
        8.417,  # U
        np.nan,  # Np
        np.nan,  # Pu
        np.nan,  # Am
        np.nan,  # Cm
        np.nan,  # Bk
        np.nan,  # Cf
        np.nan,  # Es
        np.nan,  # Fm
        np.nan,  # Md
        np.nan,  # No
        np.nan,  # Lr
        np.nan,  # Rf
        np.nan,  # Db
        np.nan,  # Sg
        np.nan,  # Bh
        np.nan,  # Hs
        np.nan,  # Mt
        np.nan,  # Ds
        np.nan,  # Rg
        np.nan,  # Cn
        np.nan,  # Nh
        np.nan,  # Fl
        np.nan,  # Mc
        np.nan,  # Lv
        np.nan,  # Ts
        np.nan,  # Og
    ]
)

chemical_symbols = np.array(
    [
        "H",
        "He",
        "Li",
        "Be",
        "B",
        "C",
        "N",
        "O",
        "F",
        "Ne",
        "Na",
        "Mg",
        "Al",
        "Si",
        "P",
        "S",
        "Cl",
        "Ar",
        "K",
        "Ca",
        "Sc",
        "Ti",
        "V",
        "Cr",
        "Mn",
        "Fe",
        "Co",
        "Ni",
        "Cu",
        "Zn",
        "Ga",
        "Ge",
        "As",
        "Se",
        "Br",
        "Kr",
        "Rb",
        "Sr",
        "Y",
        "Zr",
        "Nb",
        "Mo",
        "Tc",
        "Ru",
        "Rh",
        "Pd",
        "Ag",
        "Cd",
        "In",
        "Sn",
        "Sb",
        "Te",
        "I",
        "Xe",
        "Cs",
        "Ba",
        "La",
        "Ce",
        "Pr",
        "Nd",
        "Pm",
        "Sm",
        "Eu",
        "Gd",
        "Tb",
        "Dy",
        "Ho",
        "Er",
        "Tm",
        "Yb",
        "Lu",
        "Hf",
        "Ta",
        "W",
        "Re",
        "Os",
        "Ir",
        "Pt",
        "Au",
        "Hg",
        "Tl",
        "Pb",
        "Bi",
        "Po",
        "At",
        "Rn",
        "Fr",
        "Ra",
        "Ac",
        "Th",
        "Pa",
        "U",
        "Np",
        "Pu",
        "Am",
        "Cm",
        "Bk",
        "Cf",
        "Es",
        "Fm",
        "Md",
        "No",
        "Lr",
        "Rf",
        "Db",
        "Sg",
        "Bh",
        "Hs",
        "Mt",
        "Ds",
        "Rg",
        "Cn",
        "Nh",
        "Fl",
        "Mc",
        "Lv",
        "Ts",
        "Og",
    ]
)


atomic_numbers = {symbol: Z for Z, symbol in enumerate(chemical_symbols)}

atomic_masses = np.array( #iupac2016
    [
        1.008,  # H [1.00784, 1.00811]
        4.002602,  # He
        6.94,  # Li [6.938, 6.997]
        9.0121831,  # Be
        10.81,  # B [10.806, 10.821]
        12.011,  # C [12.0096, 12.0116]
        14.007,  # N [14.00643, 14.00728]
        15.999,  # O [15.99903, 15.99977]
        18.998403163,  # F
        20.1797,  # Ne
        22.98976928,  # Na
        24.305,  # Mg [24.304, 24.307]
        26.9815385,  # Al
        28.085,  # Si [28.084, 28.086]
        30.973761998,  # P
        32.06,  # S [32.059, 32.076]
        35.45,  # Cl [35.446, 35.457]
        39.948,  # Ar
        39.0983,  # K
        40.078,  # Ca
        44.955908,  # Sc
        47.867,  # Ti
        50.9415,  # V
        51.9961,  # Cr
        54.938044,  # Mn
        55.845,  # Fe
        58.933194,  # Co
        58.6934,  # Ni
        63.546,  # Cu
        65.38,  # Zn
        69.723,  # Ga
        72.630,  # Ge
        74.921595,  # As
        78.971,  # Se
        79.904,  # Br [79.901, 79.907]
        83.798,  # Kr
        85.4678,  # Rb
        87.62,  # Sr
        88.90584,  # Y
        91.224,  # Zr
        92.90637,  # Nb
        95.95,  # Mo
        97.90721,  # 98Tc
        101.07,  # Ru
        102.90550,  # Rh
        106.42,  # Pd
        107.8682,  # Ag
        112.414,  # Cd
        114.818,  # In
        118.710,  # Sn
        121.760,  # Sb
        127.60,  # Te
        126.90447,  # I
        131.293,  # Xe
        132.90545196,  # Cs
        137.327,  # Ba
        138.90547,  # La
        140.116,  # Ce
        140.90766,  # Pr
        144.242,  # Nd
        144.91276,  # 145Pm
        150.36,  # Sm
        151.964,  # Eu
        157.25,  # Gd
        158.92535,  # Tb
        162.500,  # Dy
        164.93033,  # Ho
        167.259,  # Er
        168.93422,  # Tm
        173.054,  # Yb
        174.9668,  # Lu
        178.49,  # Hf
        180.94788,  # Ta
        183.84,  # W
        186.207,  # Re
        190.23,  # Os
        192.217,  # Ir
        195.084,  # Pt
        196.966569,  # Au
        200.592,  # Hg
        204.38,  # Tl [204.382, 204.385]
        207.2,  # Pb
        208.98040,  # Bi
        208.98243,  # 209Po
        209.98715,  # 210At
        222.01758,  # 222Rn
        223.01974,  # 223Fr
        226.02541,  # 226Ra
        227.02775,  # 227Ac
        232.0377,  # Th
        231.03588,  # Pa
        238.02891,  # U
        237.04817,  # 237Np
        244.06421,  # 244Pu
        243.06138,  # 243Am
        247.07035,  # 247Cm
        247.07031,  # 247Bk
        251.07959,  # 251Cf
        252.0830,  # 252Es
        257.09511,  # 257Fm
        258.09843,  # 258Md
        259.1010,  # 259No
        262.110,  # 262Lr
        267.122,  # 267Rf
        268.126,  # 268Db
        271.134,  # 271Sg
        270.133,  # 270Bh
        269.1338,  # 269Hs
        278.156,  # 278Mt
        281.165,  # 281Ds
        281.166,  # 281Rg
        285.177,  # 285Cn
        286.182,  # 286Nh
        289.190,  # 289Fl
        289.194,  # 289Mc
        293.204,  # 293Lv
        293.208,  # 293Ts
        294.214,  # 294Og
    ]
)
