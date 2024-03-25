## HERE IS THE BANTER WITH TOMOE BASED

################################################################################
## Parameter Notes
################################################################################

 # define tomoe =
 # default day_number = 0
 # default visited_tomoe = False

################################################################################
## Tomoe Banter (Keep convos short and to the point as much as possible)
################################################################################

# label calling
label visiting_tomoe:
    $ visited_tomoe = True
    if day_number == 1:
        call  tomoe_day_1
    elif day_number == 2:
        call  tomoe_day_2
    elif day_number == 3:
        call  tomoe_day_3
    elif day_number == 4:
        call  tomoe_day_4
    elif day_number == 5:
        call  tomoe_day_5
    return

# Actual Script
label tomoe_day_1:
    return

label tomoe_day_2:
    return

label tomoe_day_3:
    return

label tomoe_day_4:
    return

label tomoe_day_5:
    return
