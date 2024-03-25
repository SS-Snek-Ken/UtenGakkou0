## HERE IS THE SHIZUKA ROUTE

################################################################################
## Parameter Notes
################################################################################

 # define shizuka
 # default shizuka_visits = 0
 # default persistent.shizuka_ending = False

################################################################################
## Shizuka Route
################################################################################

# label calling
label visiting_shizuka:
    if shizuka_visits == 0:
        call  shizuka_day_1
    elif shizuka_visits == 1:
        call  shizuka_day_2
    elif shizuka_visits == 2:
        call  shizuka_day_3
    elif shizuka_visits == 3:
        call  shizuka_day_4
    elif shizuka_visits == 4:
        call  shizuka_day_5
    $ shizuka_visits += 1
    return

# Actual Script
label shizuka_day_1:
    return

label shizuka_day_2:
    return

label shizuka_day_3:
    return

label shizuka_day_4:
    return

label shizuka_day_5:
    return

label shizuka_confession:
    return
