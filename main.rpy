## NON-BRANCHING STORY BASED HERE

################################################################################
## Reused Labels (usually for repeated menus)
################################################################################

### DO NOT JUMP, ONLY CALL
label location_menu:  # for days 2,3,4,5
    # Give Player menu
    menu locations:
        "パソコン室" if visited_tomoe == False:
            call visiting_tomoe
        "生徒会室":
            call visiting_noriko
        "図書館":
            call visiting_shizuka
        "美術室":
            call visiting_ayumi
        "教室":
            call visiting_ayame
    # if-else to repeat menu after visiting tomoe
    if visited_tomoe == True and repeated == 0:
        $ repeated = 1
        call location_menu
    return

################################################################################
## Start of main script
################################################################################

label day_1_start:
    $ day_number = 1
    scene bg school

    player "はぁぁ...{w=1}{rb}眠{/rb}{rt}ねむ{/rt}い..."

    "???" "{rb}睡眠不足{/rb}{rt}すいみんふそく{/rt}みたいな、{rb}先輩{/rb}{rt}せんぱい{/rt}。{p}また夜遅くゲームしてったか？"

    player "{i}この声は…{/i}{p}そうだったら何が、{rb}友恵{/rb}{rt}ともえ{/rt}？"

    show tomoe normal
    tomoe "何って、やめた方がいいよ。"

    player "{i}彼女は私の後輩、友恵。幼馴染じゃないけど、長い時間の知り合いなのでなかなか仲良しだ。{/i}"

    tomoe "そこまで続ければ疲れすぎて学校無理そうだぞ。あなたの成績のせいで来年あなたと同級生になるのいやだからな。"
    tomoe "考えだけで体が震える。"

    player "そんなに嫌なの？傷ついた。{p}って、先輩の扱いひどいなぁ、あんた。"

    tomoe "いつも通りでしょう。"

    player "…{w}ねぇ、友恵ちゃん。あんたって他の生徒のことよく知ってるよね。「情報人」と呼ばれるし。"
    tomoe "「情報人」は勝手に押し付けられたあだ名だ、私が別に情報を掘り出すわけじゃないし。{p}ただあっちこっちで人話を聞いてるだけだ、だから人に関しては少し知ってるだけ。"

    tomoe "っで、何？誰かのこと質問があるの？"
    player "…彼女が{w=0.7}欲しい…"

    tomoe "…え？{p}まじにいってる？"
    player "…うん…"

    tomoe "冗談でしょう⁉ いきなりに？ {p}先輩ギャルゲーやってて変な考えが頭に入ったとかかな？"
    tomoe "いいや待って、やっぱり私の正気のために聞かない方がいい。"
    tomoe "っで、私からおすすめの人聞くつもりか？"

    player "頼む。これに関しては手伝える最も有能な知り合いはあんたしかないんだ。"

    tomoe "お前の知り合いは私だけだけどな。"
    player "おい。"

    tomoe "さてさて、彼氏いないの女子… {p}先輩のこと耐える人…"

    player "{i}こいつ無視だけじゃない、悪口まで…{/i}"

    tomoe "… {w}先輩チャンスがある女子、4人思いついた。"
    player "４？"

    # e "{b}{color=#f00}{font=fonts/onryou.ttf}ホラーフォントテスト{/font}{/color}{/b}"


    $ asked = False

    menu character_query:
        "静香":
            $ asked = True
            show tomoe data
            tomoe""
            tomoe""
            jump character_query
        "亜由美":
            $ asked = True
            show tomoe data
            tomoe ""
            tomoe ""
            jump character_query
        "文芽":
            $ asked = True
            show tomoe data
            tomoe ""
            tomoe ""
            jump character_query
        "則子":
            $ asked = True
            show tomoe data
            tomoe ""
            tomoe ""
            jump character_query
        "わかった":
            if asked == False:
                tomoe "何が「わかった」だよ、何も聞いてねぇじゃねか！{p}もういいよ…"
            else:
                pass

    # Update query count once player ends query
    $ ask_tomoe += 1

    tomoe "これでわかったか？ちゃんと覚えてる？"

    # Ask player if they want to repeat query
    menu after_query:
        "大丈夫だ": # Refuse
            jump finish_query
        "もう一回": # Repeat
            if ask_tomoe == 1:
                call repeat_query_1
            elif ask_tomoe == 2:
                call repeat_query_2
            elif ask_tomoe_3:
                jump repeat_query_finish
            jump character_query

    ############################################
    # Labels to call based on times repeat query
    label repeat_query_1:
        # First repeat text

        return

    label repeat_query_2:
        # Second repeat text

        return

    label repeat_query_final:

        menu:
            "test": # Positive
                jump secret_day_1
            "test2": # Negative
                # Insert text
                pass

    ############################################

    # Finish using the query
    label finish_query:
        pass

    # Continue text

# jump beginning_of_the_end

label day_1_repeater:
    call day_1_menu
    if day_1_visits < 5:
        jump day_1_menu
    else:
        jump day_1_end

menu day_1_menu:
    "パソコン室" if visited_tomoe == False:
        call visiting_tomoe
    "生徒会室" if noriko_visits == 0:
        call visiting_noriko
    "図書館" if shizuka_visits == 0:
        call visiting_shizuka
    "美術室" if ayumi_visits == 0:
        call visiting_ayumi
    "教室" if ayame_visits == 0:
        call visiting_ayame

label day_1_end:


############################################
label day_2_start:
    $ day_number = 2
    $ repeated == 0
    $ visited_tomoe = False

    call location_menu

label day_2_end:

############################################
label day_3_start:
    $ day_number = 3
    $ repeated == 0
    $ visited_tomoe = False

    call location_menu

label day_3_end:

############################################
label day_4_start:
    $ day_number = 4
    $ repeated == 0
    $ visited_tomoe = False

    call location_menu

label day_4_end:

###########################################
label day_5_start:
    $ day_number = 5
    $ repeated == 0
    $ visited_tomoe = False

    call location_menu

label day_5_end: #confession point
    # Check all visit parameters, next dialogue changes accordingly
    if noriko_visits == 5:
        pass # noriko ending
    elif shizuka_visits == 5:
        pass # shizuka ending
    elif ayumi_visits == 5:
        pass # ayumi ending
    elif ayame_visits == 5:
        pass # ayame ending
    # else move on to next label

###########################################

# All checks failed, continuation
label route_fail:
    player "この一週間、色々やったなー。"

    show tomoe
    tomoe "いやいや、先輩はただ普段関わらない人と知り合いになっただけですよ。 {p}別に色々やってないから。"

    player "...{w}ねぇ、友恵。"

    tomoe "なーにー？"

    player "...たまに俺の味方にしてくれないか？"

    tomoe "...{w}嫌だもん～"

    player "..."

    tomoe "ってか、先輩は彼女作るつもりだったじゃないか？ {p}今までなにやってんの？"
    tomoe "私の視点から、完全に友達作りの行動になってるけど？" # Suspicious text

    player "そうかもしれないね..."

    tomoe "っで、彼女のことどうすんの？"

    # Check for lolharem conditions
    if noriko_visits == 2 and shizuka_visits == 2 and ayumi_visits == 2 and ayame_visits == 2:
        $ balanced = True

    # Ending choice with conditions
    menu normal_ending_choice:
        "{rb}諦{/rb}{rt}あきら{/rt}める":
            jump normal_ending
        "... {rb}告白{/rb}{rt}こくはく{/rt}する" if balanced == True:
            jump lolharem_ending

###########################################

label normal_ending:
    player "やっぱり、5日内で知らない相手を彼女にするが無茶だった。"

    tomoe "お！先輩やっと正気に戻ったね～{p}彼女作るの先輩には無理だ～って、私最初から知ってた。"

    player "やめてー、とどめ刺さないでー"

    tomoe "まぁいいじゃないか。先輩はまだ...{w}私がいるでしょう～"

    player "そうだね、俺はまだこの有能後輩親友がいる。"

    tomoe @ sad "..."
    extend "そうだよぉ～"

    tomoe "んじゃ、これは失恋みたいの状況だから..."
    tomoe "この大切な後輩が先輩とどっかで元気になろうよぉ！ {p}さぁ、行こう！"

    player "相変わらずだね、友恵..."

    scene bg sky #maybe
    player "{i}...今回失敗したが、なんか次ならいける感じがする。{p}その時頑張ろうか。{/i}"
    # Normal Ending
    $ persistent.normal_ending = True
    return

###########################################

label lolharem_ending:
    tomoe "...え？"

    player "俺は{w}今日で{w}告白する。"

    tomoe "えぇ！誰に？"

    player "...全人。"

    tomoe "噓でしょう[player]先輩？！{w=0.7}これはギャルゲーじゃないんだよ！{w=0.7}現実だよ！"
    tomoe "なにやっても失敗するよ！{w=0.7}バッドエンドだよ！"

    player "俺はやめない。"

    hide tomoe with dissolve
    tomoe "先輩？{w=0.7}せんぱい？{w=0.7}センパイィィィ！" # gradually make text smaller

    # Scene change
    # Show all 4 girls
    player ""

    # Knockout
    scene bg black
    # Tomoe suspicious text
    tomoe "こういう結末...{size -= 17}つ{/size}何考えてる、ふざけてるのか？{p}...はぁ...いつもみたいにわからないままだな。"
    # こういう結末...あの作者め、あいつ一体何考えてる、ふざけてるのか？...はぁ...いつもみたいにわからないままだな。

    # Wake up

    tomoe "お。起きたか、[player]先輩。{p}上手くボコられたね。{w=0.7}そのままで私の膝の上でじいとして。"
    tomoe "まったく、四人同時に告白なんて、{w=1.0}一体何考えてるの？{w=0.7}後で病院行く？"
    tomoe "これは完全に{rb}事項自得{/rb}{rt}じこうじとく{/rt}ですよ。まさか最初からこれを狙ってたか？"
    tomoe "まぁ、この状態の先輩がなにも言い返せないし、動けるまで休め。"

    $ persistent.lolharem_ending = True
    return
