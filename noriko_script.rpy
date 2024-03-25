## HERE IS THE NORIKO ROUTE

################################################################################
## Parameter Notes
################################################################################

 # define noriko
 # default noriko_visits = 0
 # default persistent.noriko_ending = False

################################################################################
## Noriko Route
################################################################################

# label calling
label visiting_noriko:
    if noriko_visits == 0:
        call  noriko_day_1
    elif noriko_visits == 1:
        call  noriko_day_2
    elif noriko_visits == 2:
        call  noriko_day_3
    elif noriko_visits == 3:
        call  noriko_day_4
    elif noriko_visits == 4:
        call  noriko_day_5
    $ noriko_visits += 1
    return

# Actual Script
label noriko_day_1:
    return

label noriko_day_2:
    return

label noriko_day_3:
    return

label noriko_day_4:
    return

label noriko_day_5:
    return

label noriko_confession:
    return
