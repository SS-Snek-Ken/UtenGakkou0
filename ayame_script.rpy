## HERE IS THE AYAME ROUTE

################################################################################
## Parameter Notes
################################################################################

 # define ayame
 # default ayame_visits = 0
 # default persistent.ayame_ending = False

################################################################################
## Ayame Route
################################################################################

# label calling
label visiting_ayame:
    if ayame_visits == 0:
        call  ayame_day_1
    elif ayame_visits == 1:
        call  ayame_day_2
    elif ayame_visits == 2:
        call  ayame_day_3
    elif ayame_visits == 3:
        call  ayame_day_4
    elif ayame_visits == 4:
        call  ayame_day_5
    $ ayame_visits += 1
    return

# Actual Script
label ayame_day_1:
    return

label ayame_day_2:
    return

label ayame_day_3:
    return

label ayame_day_4:
    return

label ayame_day_5:
    return

label ayame_confession:
    return
