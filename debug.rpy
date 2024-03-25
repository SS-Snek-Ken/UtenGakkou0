################################################################################
## Debug Menu
################################################################################
menu debug_menu:
    "Day 1":
        jump day_1_debug
    "Day 2":
        jump day_2_debug
    "Day 3":
        jump day_3_debug
    "Day 4":
        jump day_4_debug
    "Day 5":
        jump day_5_debug
    "Ending":
        jump ending_debug
    "Return":
        jump debug_access


menu day_1_debug:
    "Start":
        call day_1_start
    "Menu":
        call day_1_menu
    "End":
        call day_1_end
    "Back":
        jump debug_menu

menu day_2_debug:
    "Start":
        call day_2_start
    "":
        pass
    "End":
        call day_2_end
    "Back":
        jump debug_menu


menu day_3_debug:
    "Start":
        call day_3_start
    "":
        pass
    "End":
        call day_3_end
    "Back":
        jump debug_menu


menu day_4_debug:
    "Start":
        call day_4_start
    "":
        pass
    "End":
        call day_4_end
    "Back":
        jump debug_menu


menu day_5_debug:
    "Start":
        call day_5_start
    "":
        pass
    "End":
        call day_5_end
    "Back":
        jump debug_menu


menu ending_debug:
    "":
        pass
    "":
        pass
