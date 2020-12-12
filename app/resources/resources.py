from enum import Enum


class ExpClass(Enum):
    # should such class be documented?
    # """ class does this and that """
    X0 = {"exp_class": "X0", "concrete_class": "C12/15", "max_wc": None, "min_cem": None,
          "remarks": "No corrosion risk"}
    # different naming of keys?
    # Todo Add values for other classes if template accepted
    XC1 = {"exp_class": "XC1", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XC2 = {"exp_class": "XC2", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XC3 = {"exp_class": "XC3", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XC4 = {"exp_class": "XC4", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XD1 = {"exp_class": "XD1", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XD2 = {"exp_class": "XD2", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XD3 = {"exp_class": "XD3", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XS1 = {"exp_class": "XS1", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XS2 = {"exp_class": "XS2", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XS3 = {"exp_class": "XS3", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XF1 = {"exp_class": "XF1", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XF2 = {"exp_class": "XF2", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XF3 = {"exp_class": "XF3", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XF4 = {"exp_class": "XF4", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XA1 = {"exp_class": "XA1", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XA2 = {"exp_class": "XA2", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}
    XA3 = {"exp_class": "XA3", "concrete_class": None, "max_wc": None, "min_cem": None,
           "remarks": None}


class ConcreteClass(Enum):
    C12_15 = {"concrete_class": "C12/15", "fck": 12, "fck_cube": 15, "fcm": 20, "fctm": 1.6, "fctk_0.05": 1.1,
              "fctk_0.95": 2.0, "Ecm": 27}
    # Todo Add values for other classes if template accepted


class SteelClass(Enum):
    # different structure of classes? e.g. 35G2Y = {class = AIII}, 34GS = {class = AIII}, ...
    A_III = {"type": {
        # keep diameters as range object, list comprehension, generator object, or simple list?
        "35G2Y": {"type_name": "35G2Y", "diameters": range(6, 22, 2), "fyk": 410, "fyd": 350, "ftk": 550},
        # keep fyd inside each type or in class only?
        "34GS": {"type_name": "34GS", "diameters": [n for n in range(6, 34, 2)], "fyk": 410, "fyd": 350, "ftk": 550},
        "RB400": {"type_name": "RB400", "diameters": (n for n in range(6, 42, 2)), "fyk": 400, "fyd": 350, "ftk": 440},
        "RB400W": {"type_name": "RB400W",
                   "diameters": [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40], "fyk": 400,
                   "fyd": 350, "ftk": 440}
    }}
    # Todo Add values for other classes if template accepted


# keep all resources as enum class objects, generator object of enum attributes, list of enum attributes?
resources = {
    "exp_classes": ExpClass,
    "concrete_classes": (concrete_class for concrete_class in ConcreteClass),
    "steel_classes": [steel_class for steel_class in SteelClass]
}

# save file template prototype
file = {
    "element": {
        "plate": {
            "exp_class": str,
            "concrete_class": str,
            "concrete_cover": float,
            "steel_class": str,
            "bar_diam": int,
            "thickness": float,
            "moment": float
        },
        "beam": {
            "exp_class": str,
            "concrete_class": str,
            "concrete_cover": float,
            "steel_class": str,
            "bar_diam": int,
            "height": float,
            "width": float,
            "support_section": bool,
            "flange_thickness": float,
            "flange_width": float,
            "moment": float
        },
        "column": {
            "exp_class": str,
            "concrete_class": str,
            "concrete_cover": float,
            "steel_class": str,
            "bar_diam": int,
            "height": float,
            "width": float,
            "moment": float,
            "vertical": float
        },
        "foot": {
            "exp_class": str,
            "concrete_class": str,
            "concrete_cover": float,
            "steel_class": str,
            "bar_diam": int,
            "column_bar_diam": int,
            "foot_height": float,
            "foot_width": float,
            "foot_length": float,
            "column_height": float,
            "column_width": float,
            "vertical": float
        }
    },
    "remarks": str,
    "results": str
}
