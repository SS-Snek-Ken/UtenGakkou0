## GAME BEGINS HERE, NOT AT MAIN. ALL PARAMETERS TO BE PLACED HERE

################################################################################
## Characters
################################################################################
# Establish all character shortcuts and customisations (Does not work with Live2D)

# Player input character
define player = Character("[playername]")
# Female characters
define tomoe = Character("友恵(ともえ)") # ,image="tomoe"
define shizuka = Character("静香(しずか)")
define noriko = Character("則子(のりこ)")
define ayumi = Character("亜由美(あゆみ)")
define ayame = Character("文芽(あやめ)")

define e = Character("Eileen") #temp

################################################################################
## Visit Tracking
################################################################################

# Used for regular tomoe visits
default day_number = 0
default repeated = 0

# Used to determine which character event to call
default visited_tomoe = False
default noriko_visits = 0
default shizuka_visits = 0
default ayumi_visits = 0
default ayame_visits = 0

# Used to end day 1
default day_1_visits = 0  # max = 5

# Check for lolharem ending conditions
default balanced = False

# Track query count for secret ending
default ask_tomoe = 0

################################################################################
## Ending Flags Initialization
################################################################################

# Ordinary ending flags
default persistent.noriko_ending = False
default persistent.shizuka_ending = False
default persistent.ayumi_ending = False
default persistent.ayame_ending = False
default persistent.lolharem_ending = False
default persistent.normal_ending = False

# Almost complete flag
default persistent.unlock_flag = True if persistent.noriko_ending and persistent.shizuka_ending and persistent.ayumi_ending and persistent.ayame_ending and persistent.lolharem_ending and persistent.normal_ending else False

# Secret Route Flag (unlock Gallery?)
default persistent.tomoe_ending = False

# testing flag (To remove)
default persistent.testingflag = False

################################################################################
## Debug Mode
################################################################################

# To quickly debug certain sequences
default debug_mode = False

### Dev Notes
# Ruby text only works on dialogue, not anywhere else.

################################################################################
## Secret Codes
################################################################################

# Locked folder code
default password = [ "_" if persistent.noriko_ending == False else "R", \
                    "_" if persistent.shizuka_ending == False else "O", \
                    "_" if persistent.ayumi_ending == False else "U", \
                    "_" if persistent.ayame_ending == False else "T", \
                    "_" if persistent.lolharem_ending == False else "E", \
                    "_" if persistent.normal_ending == False else "7"]

default hidden_code = "547196" # omake folder code

################################################################################
## Sound Effects & BGM
################################################################################

# Will not utilise
define audio.alarm = "audio/SE/alarm.mp3"


################################################################################
################################################################################
###########################    Start of Game    ################################
################################################################################
################################################################################

label start:

    ##### Dream Intro Sequence #####
    scene bg dark

    ###################################
    ## Developer Tools
    ###################################
    narrator "The following should be developer only."

    narrator "Adjust flag for testing."
    menu flag_test:
        "True":
            $ persistent.testing_flag = True
        "False":
            $ persistent.testing_flag = False

    narrator "Begin Debugging?"
    menu debug_access:
        "Debug":
            $ debug_mode = True
            jump debug_menu
        "End":
            $ debug_mode = False
            return
        "Continue":
            $ debug_mode = False
            pass

    ###################################
    ###################################
    "製作者" """
    ！ご注意です！{p}

    """

    show darkfigure with dissolve
    narrator "{rb}勇者様{/rb}{rt}ゆうしゃさま{/rt}...よく来たぞ...\n{rb}名{/rb}{rt}な{/rt}を教えてくれ。"

    # Player Name Input
    python:
        playername = renpy.input("あなたの名前は？", length=16)
        if not playername:
            playername = "タレオ"

    narrator "{rb}勇者{/rb}{rt}ゆうしゃ{/rt}[player]、{rb}頼{/rb}{rt}たの{/rt}む...{rb}世界{/rb}{rt}せかい{/rt}を{rb}助{/rb}{rt}たす{/rt}けてください。"

    # Code to access the locked zip file for way to access Tomoe Route
    default code = " ".join(password)
    extend "旅に出る前に、この呪文良く覚えておけ...{p}[code]"

    hide darkfigure with dissolve
    ##### Dream Sequence END #####

    # Sound Effect test
    play sound alarm volume 0.5
    player "..."
    stop sound

    # Long single person text example
    player"""
    最近...{w=0.7}レトロなRPGゲームやりすぎたかも...{p=0.7}夢まで出るなんって...

    今なん時？ん...まだ大丈夫みたい。

    でも今起きないと、さすがに遅刻する...{w=0.7}よいしょ。
    """

    jump day_1_start
