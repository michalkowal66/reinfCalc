from enum import Enum


class ExpClass(Enum):
    """Enum Class containing concrete exposition classes

    Exposition classes are stored as class attributes referring to dictionaries with related values and remarks
    in accordance to PN-EN 1992-1-1:2008/NA: 2010

    Each attribute holds fixed number of keys that represent values of concrete properties:
        exp_class: exposition class,
        concrete_class: minimum concrete class that may be used with given exposition class,
        max_wc: maximum water/cement ration
        min_cem: minimum content of cement [kg/m^3]
        remarks: remarks about exposition class
    """
    X0 = {"exp_class": "X0", "concrete_class": "C12/15", "max_wc": None, "min_cem": None,
          "remarks": "No corrosion risk"}
    XC1 = {"exp_class": "XC1", "concrete_class": "C20/25", "max_wc": 0.65, "min_cem": 260,
           "remarks": "Corrosion due to carbonation hazard"}
    XC2 = {"exp_class": "XC2", "concrete_class": "C25/30", "max_wc": 0.6, "min_cem": 280,
           "remarks": "Corrosion due to carbonation hazard"}
    XC3 = {"exp_class": "XC3", "concrete_class": "C30/37", "max_wc": 0.55, "min_cem": 280,
           "remarks": "Corrosion due to carbonation hazard"}
    XC4 = {"exp_class": "XC4", "concrete_class": "C30/37", "max_wc": 0.5, "min_cem": 300,
           "remarks": "Corrosion due to carbonation hazard"}
    XD1 = {"exp_class": "XD1", "concrete_class": "C30/37", "max_wc": 0.55, "min_cem": 300,
           "remarks": "Corrosion due to chlorides hazard"}
    XD2 = {"exp_class": "XD2", "concrete_class": "C30/37", "max_wc": 0.55, "min_cem": 300,
           "remarks": "Corrosion due to chlorides hazard"}
    XD3 = {"exp_class": "XD3", "concrete_class": "C35/45", "max_wc": 0.45, "min_cem": 320,
           "remarks": "Corrosion due to chlorides hazard"}
    XS1 = {"exp_class": "XS1", "concrete_class": "C30/37", "max_wc": 0.5, "min_cem": 300,
           "remarks": "Corrosion due to sea water chlorides hazard"}
    XS2 = {"exp_class": "XS2", "concrete_class": "C35/45", "max_wc": 0.45, "min_cem": 320,
           "remarks": "Corrosion due to sea water chlorides hazard"}
    XS3 = {"exp_class": "XS3", "concrete_class": "C35/45", "max_wc": 0.45, "min_cem": 340,
           "remarks": "Corrosion due to sea water chlorides hazard"}
    XF1 = {"exp_class": "XF1", "concrete_class": "C30/37", "max_wc": 0.55, "min_cem": 300,
           "remarks": "Freeze and thaw hazard"}
    XF2 = {"exp_class": "XF2", "concrete_class": "C25/30", "max_wc": 0.55, "min_cem": 300,
           "remarks": "Freeze and thaw hazard"}
    XF3 = {"exp_class": "XF3", "concrete_class": "C30/37", "max_wc": 0.5, "min_cem": 320,
           "remarks": "Freeze and thaw hazard"}
    XF4 = {"exp_class": "XF4", "concrete_class": "C30/37", "max_wc": 0.45, "min_cem": 340,
           "remarks": "Freeze and thaw hazard"}
    XA1 = {"exp_class": "XA1", "concrete_class": "C30/37", "max_wc": 0.55, "min_cem": 300,
           "remarks": "Chemical hazard"}
    XA2 = {"exp_class": "XA2", "concrete_class": "C30/37", "max_wc": 0.5, "min_cem": 320,
           "remarks": "Chemical hazard"}
    XA3 = {"exp_class": "XA3", "concrete_class": "C35/45", "max_wc": 0.45, "min_cem": 360,
           "remarks": "Chemical hazard"}


class ConcreteClass(Enum):
    """ Enum Class containing concrete classes

    Concrete classes are stored as class attributes referring to classes' characteristic values
    in accordance to PN-EN 1992-1-1:2008/NA: 2010

    Each attribute holds fixed number of keys that represent values of concrete properties:
        concrete_class: concrete class,
        fck: characteristic compressive strength of cylinder sample [MPa],
        fck_cube: characteristic compressive strength of cube sample [MPa],
        fcm: mean compressive strength of cylinder sample [MPa],
        fctm: mean tensile strength [MPa],
        fctk_0.05: 5% fractile tensile strength [MPa],
        fctk_0.95: 95% fractile tensile strength [MPa],
        Ecm: Elastic modulus [GPa]
     """
    C12_15 = {"concrete_class": "C12/15", "fck": 12, "fck_cube": 15, "fcm": 20, "fctm": 1.6, "fctk_0.05": 1.1,
              "fctk_0.95": 2.0, "Ecm": 27}
    C16_20 = {"concrete_class": "C16/20", "fck": 16, "fck_cube": 20, "fcm": 24, "fctm": 1.9, "fctk_0.05": 1.3,
              "fctk_0.95": 2.5, "Ecm": 29}
    C20_25 = {"concrete_class": "C20/25", "fck": 20, "fck_cube": 25, "fcm": 28, "fctm": 2.2, "fctk_0.05": 1.5,
              "fctk_0.95": 2.9, "Ecm": 30}
    C25_30 = {"concrete_class": "C25/30", "fck": 25, "fck_cube": 30, "fcm": 33, "fctm": 2.6, "fctk_0.05": 1.8,
              "fctk_0.95": 3.3, "Ecm": 31}
    C30_37 = {"concrete_class": "C30/37", "fck": 30, "fck_cube": 37, "fcm": 38, "fctm": 2.9, "fctk_0.05": 2.0,
              "fctk_0.95": 3.8, "Ecm": 33}
    C35_45 = {"concrete_class": "C35/45", "fck": 35, "fck_cube": 45, "fcm": 43, "fctm": 3.2, "fctk_0.05": 2.2,
              "fctk_0.95": 4.2, "Ecm": 34}
    C40_50 = {"concrete_class": "C40/50", "fck": 40, "fck_cube": 50, "fcm": 48, "fctm": 3.5, "fctk_0.05": 2.5,
              "fctk_0.95": 4.6, "Ecm": 35}
    C45_55 = {"concrete_class": "C45/55", "fck": 45, "fck_cube": 55, "fcm": 53, "fctm": 3.8, "fctk_0.05": 2.7,
              "fctk_0.95": 4.9, "Ecm": 36}
    C50_60 = {"concrete_class": "C50/60", "fck": 50, "fck_cube": 60, "fcm": 58, "fctm": 4.1, "fctk_0.05": 2.9,
              "fctk_0.95": 5.3, "Ecm": 37}


class RebarClass(Enum):
    """ Enum Class containing steel classes

    Steel classes are stored as class attributes referring to classes' characteristic values
    in accordance to PN-B-03264:2002

    Each attribute holds fixed number of keys that represent values of concrete properties:
        steel_class: steel class,
        fyd: design yield strength of steel class
    """
    A_III = {
        "steel_class": "A-III", "fyd": 350
    }
    A_IIIN = {
        "steel_class": "A-IIIN", "fyd": 420
    }


resources = {
    "exp_class": ExpClass,
    "concrete_class": ConcreteClass,
    "steel_class": RebarClass,
    "diameters": [n for n in range(6, 42, 2)]
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
