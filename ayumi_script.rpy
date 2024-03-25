## HERE IS THE AYUMI ROUTE

################################################################################
## Parameter Notes
################################################################################

 # define ayumi
 # default ayumi_visits = 0
 # default persistent.ayumi_ending = False

################################################################################
## Ayumi Route
################################################################################

# label calling
label visiting_ayumi:
    if ayumi_visits == 0:
        call  ayumi_day_1
    elif ayumi_visits == 1:
        call  ayumi_day_2
    elif ayumi_visits == 2:
        call  ayumi_day_3
    elif ayumi_visits == 3:
        call  ayumi_day_4
    elif ayumi_visits == 4:
        call  ayumi_day_5
    $ ayumi_visits += 1
    return

# Actual Script
label ayumi_day_1:
    return

label ayumi_day_2:
    return

label ayumi_day_3:
    return

label ayumi_day_4:
    return

label ayumi_day_5:
    return

label ayumi_confession:
    return
