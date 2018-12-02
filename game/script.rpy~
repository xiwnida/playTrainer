init python:
    
#==============================================================ФУНКЦИИ=========
    

#==============================================================ФУНКЦИЯ РАНДОМНЫХ ПРИМЕРОВ В МАТЕМАТИКЕ======
    import random
    def matematika():
        global num1
        global num2
        global operate
        global right_answer
        operate=random.randint(1,2) #1 - сложение. 2 - вычитание.
        num1=random.randint(1,9)
        num2=random.randint(1,9)
        if operate==1:
            while num1+num2>=10:
                num1=random.randint(1,9)
                num2=random.randint(1,9)
            operate='+'
            right_answer=str(num1+num2)
        elif operate==2:
            while num1<num2:
                num1=random.randint(1,9)
                num2=random.randint(1,9)
            operate='-'
            right_answer=str(num1-num2)
        num1=str(num1)
        num2=str(num2)
        
#==============================================================ФУНКЦИЯ РАНДОМНОГО ЧИСЛА ДЛЯ КОМБИНАЦИЙ ЛАМП=========
        
    def random_number():
        global num1
        global lamp_storage
        num1=random.randint(1,4)
        lamp_storage.append(num1)
        
#==============================================================ФУНКЦИЯ РАНДОМНЫХ ПЯТИ ЗАГАДОК=====
        
    def zagadki():
        global zagadki_array
        global zagadki_round
        zagadki_array=[i for i in range(1,27)]
        for i in range(5):
            a=random.randint(0,len(zagadki_array)-1)
            zagadki_round.append(zagadki_array[a])
            zagadki_array.pop(a)
            
#==============================================================ФУНКЦИЯ, ПОДБИРАЮАЩАЯ ПРАВИЛЬНЫЙ ОТВЕТ И ТРИ РАНДОМНЫХ.===== ЕЩЕ РАЗМЕШИВАЕТ ИХ В СЛУЧАЙНОМ ПОРЯДКЕ========
            
    def answers():
        global zagadki_answers
        global zagadki_round
        global circle_num
        zagadki_array=[i for i in range(1,27)]
        zagadki_array.remove(zagadki_round[circle_num])
        b=[]
        b.append(zagadki_round[circle_num])
        for i in range(3):
            a=random.randint(0,len(zagadki_array)-1)
            b.append(zagadki_array[a])
            zagadki_array.pop(a)
        for i in range(3):
            a=random.randint(0,len(b)-1)
            zagadki_answers.append(b[a])
            b.pop(a)
        zagadki_answers.append(b[0])
        
#==============================================================ПЕРЕМЕННЫЕ========
        
init:
    $ cub_bronz=0
    $ cub_priz_bronz=False
    $ cub_priz_silver=False
    $ cub_priz_gold=False
    $ cub_mat=0
    $ cub_mat_bronz=False
    $ cub_mat_silver=False
    $ cub_mat_gold=False
    $ cub_mem=0
    $ cub_mem_bronz=False
    $ cub_mem_silver=False
    $ cub_mem_gold=False
    $ cub_wis=0
    $ cub_wis_bronz=False
    $ cub_wis_silver=False
    $ cub_wis_gold=False
    $ cub_gold=0
    $ cub_win_bronz=False
    $ cub_win_silver=False
    $ cub_win_gold=False
    $ num1=0 # Первое число для математики и рандомный номер для ламп
    $ num2=0 # Второе число для математики
    $ operate=0 # Сложение или вычитание
    $ answer='' # Хранит в себе ответ пользователя на пример
    $ right_answer='' # Хранит в себе правильный ответ
    $ circle_num=0 # Считает количество прохождений цикла
    $ right_num=0 # Считает количество правильных ответов
    $ first_game=0 # Определяет, во сколько разных игр играл пользователь
    $ mat=False
    $ mem=False
    $ zag=False
    $ lamp_circle=0 # Считает, сколько нужно зажечь ламп
    $ lamp_circle2=0 # Считает, сколько раз пользователь зажег лампу
    $ lamp_storage=[] # Хранит порядок зажигания ламп
    $ choosen_lamp=0 # Хранит значение выбранной лампы
    $ zagadki_array=[] # Хранит в себе все загадки
    $ zagadki_round=[] # Хранит в себе пять загадок на раунд
    $ zagadki_answers=[] # Хранит в себе варианты ответа на раунд
    $ zagadka_answer=0 # Хранит в себе ответ пользователя на загадку
    
#===============================================================================ЭКРАНЫ С ТЕКСТАМИ======

# Экраны
screen text1:
    imagebutton:
        idle "text1_idle"
        hover "text1_hover"
        focus_mask True
        action Play("sound", "music/book2.ogg"), Jump("text2")
        
screen text2:
    imagebutton:
        idle "text2_idle"
        hover "text2_hover"
        focus_mask True
        action Play("sound", "music/book2.ogg"), Jump("text3")

screen text3:
    imagebutton:
        idle "text3_idle"
        hover "text3_hover"
        focus_mask True
        action Play("sound", "music/book2.ogg"), Jump("game_start")
        
screen matema_text:
    imagebutton:
        idle "text1_idle"
        hover "text1_hover"
        focus_mask True
        action Play("sound", "music/book2.ogg"), Jump("matema2")
        
screen lamp_text:
    imagebutton:
        idle "text1_idle"
        hover "text1_hover"
        focus_mask True
        action Play("sound", "music/book2.ogg"), Jump("lamps2")
        
screen zagadka_text:
    imagebutton:
        idle "text1_idle"
        hover "text1_hover"
        focus_mask True
        action Play("sound", "music/book2.ogg"), Jump("zagadki2")

screen good:
    imagebutton:
        idle "text1_idle"
        hover "text1_hover"
        focus_mask True
        action Play("sound", "music/book2.ogg"), Jump("game_start")
        
#==============================================================ЭКРАН НАВИГАЦИИ ПО ГЛАВНОМУ МЕНЮ=========
        
        
screen main_menu_screen:
    imagebutton:
        idle "but1_idle"
        hover "but1_hover"
        focus_mask True
        hovered Play('sound', 'music/select.wav')
        action Play("sound", "music/save.wav"), Jump("matem")
        
    imagebutton:
        idle "but2_idle"
        hover "but2_hover"
        focus_mask True
        hovered Play('sound', 'music/select.wav')
        action Play("sound", "music/save.wav"), Jump("lamps")
        
    imagebutton:
        idle "but3_idle"
        hover "but3_hover"
        focus_mask True
        hovered Play('sound', 'music/select.wav')
        action Play("sound", "music/save.wav"), Jump("zagadki")
        
    imagebutton:
        idle 'exit_idle.png'
        hover 'exit_hover.png'
        focus_mask True
        hovered Play('sound', 'music/select.wav')
        action Quit(confirm=not main_menu)
    
    if cub_gold>0:
        imagebutton:
            if cub_gold>4:
                idle "cub_win_gold"
                hover "cub_win_gold_hover"
            elif cub_gold>2:
                idle "cub_win_silver"
                hover "cub_win_silver_hover"
            elif cub_gold>0:
                idle "cub_win_bronz"
                hover "cub_win_bronz_hover"
            focus_mask True
            action Jump("start_game2")    
    
    if cub_bronz>0:
        imagebutton:
            if cub_bronz>4:
                 idle "cub_priz_gold"
                 hover "cub_priz_gold_hover"
            elif cub_bronz>2:
                 idle "cub_priz_silver"
                 hover "cub_priz_silver_hover"
            elif cub_bronz>0:
                 idle "cub_priz_bronz"
                 hover "cub_priz_bronz_hover"
            focus_mask True
            action Jump("start_game2")
    
    if cub_mat>0:
        imagebutton:
            if cub_mat>4:
                idle "cub_mat_gold"
                hover "cub_mat_gold_hover"
            elif cub_mat>2:
                idle "cub_mat_silver"
                hover "cub_mat_silver_hover"
            elif cub_mat>0:
                idle "cub_mat_bronz"
                hover "cub_mat_bronz_hover"
            focus_mask True
            action Jump("start_game2")
        
    if cub_mem>0:
        imagebutton:
            if cub_mem>4:
                idle "cub_mem_gold"
                hover "cub_mem_gold_hover"
            elif cub_mem>2:
                idle "cub_mem_silver"
                hover "cub_mem_silver_hover"
            elif cub_mem>0:
                idle "cub_mem_bronz"
                hover "cub_mem_bronz_hover"
            focus_mask True
            action Jump("start_game2")
        
    if cub_wis>0:       
        imagebutton:
            if cub_wis>4:
                idle "cub_wis_gold"
                hover "cub_wis_gold_hover"
            elif cub_wis>2:
                idle "cub_wis_silver"
                hover "cub_wis_silver_hover"
            elif cub_wis>0:
                idle "cub_wis_bronz"
                hover "cub_wis_bronz_hover"
            focus_mask True
            action Jump("start_game2")
            
#==============================================================ЭКРАН НАВИГАЦИИ ПО МАТЕМАТИКЕ========
            
screen matema_number:
    imagebutton:
        xpos 350 ypos 280
        idle "1.png"
        hover "1_hover.png"
        action Jump("one")
        
    imagebutton:
        xpos 503 ypos 280
        idle "2.png"
        hover "2_hover.png"
        action Jump("two")
        
    imagebutton:
        xpos 656 ypos 280
        idle "3.png"
        hover "3_hover.png"
        action Jump("three")
        
    imagebutton:
        xpos 350 ypos 408
        idle "4.png"
        hover "4_hover.png"
        action Jump("four")
        
    imagebutton:
        xpos 503 ypos 408
        idle "5.png"
        hover "5_hover.png"
        action Jump("five")
        
    imagebutton:
        xpos 656 ypos 408
        idle "6.png"
        hover "6_hover.png"
        action Jump("six")
        
    imagebutton:
        xpos 350 ypos 536
        idle "7.png"
        hover "7_hover.png"
        action Jump("seven")
        
    imagebutton:
        xpos 503 ypos 536
        idle "8.png"
        hover "8_hover.png"
        action Jump("eight")
        
    imagebutton:
        xpos 656 ypos 536
        idle "9.png"
        hover "9_hover.png"
        action Jump("nine")
        
    imagebutton:
        xpos 784 ypos 536
        idle "0.png"
        hover "0_hover.png"
        action Jump("zero")
        
    imagebutton:
        idle "matema_idle.png"
        hover "matema_hover.png"
        focus_mask True
        action Jump("matema_decide")
        
    imagebutton:
        idle 'stop_idle.png'
        hover 'stop_hover.png'
        focus_mask True
        action Play("sound", "music/cancel.wav"), Jump('in_menu_stop')
        
#==============================================================ЭКРАН НАВИГАЦИИ ПО ЛАМПАМ=======
        
screen lamps:
    imagebutton:
        idle 'lamp_off1'
        hover 'lamp1_hover'
        focus_mask True
        action Jump('lamp1')
        
    imagebutton:
        idle 'lamp_off2'
        hover 'lamp2_hover'
        focus_mask True
        action Jump('lamp2')
        
    imagebutton:
        idle 'lamp_off3'
        hover 'lamp3_hover'
        focus_mask True
        action Jump('lamp3')
        
    imagebutton:
        idle 'lamp_off4'
        hover 'lamp4_hover'
        focus_mask True
        action Jump('lamp4')
        
    imagebutton:
        idle 'stop_idle.png'
        hover 'stop_hover.png'
        focus_mask True
        action Play("sound", "music/cancel.wav"), Jump('in_menu_stop')
        
#==============================================================ЭКРАН НАВИГАЦИИ ПО ЗАГАДКАМ=======
        
screen zagadki():
    imagebutton:
        xpos 360 ypos 353
        idle 'otvet_'+str(zagadki_answers[0])+'.png'
        hover 'otvet_'+str(zagadki_answers[0])+'h.png'
        action Jump('zagadka1')
        
    imagebutton:
        xpos 360 ypos 499
        idle 'otvet_'+str(zagadki_answers[1])+'.png'
        hover 'otvet_'+str(zagadki_answers[1])+'h.png'
        action Jump('zagadka2')
        
    imagebutton:
        xpos 664 ypos 353
        idle 'otvet_'+str(zagadki_answers[2])+'.png'
        hover 'otvet_'+str(zagadki_answers[2])+'h.png'
        action Jump('zagadka3')
        
    imagebutton:
        xpos 664 ypos 499
        idle 'otvet_'+str(zagadki_answers[3])+'.png'
        hover 'otvet_'+str(zagadki_answers[3])+'h.png'
        action Jump('zagadka4')
        
    imagebutton:
        idle 'stop_idle.png'
        hover 'stop_hover.png'
        focus_mask True
        action Play("sound", "music/cancel.wav"), Jump('in_menu_stop')
        
#==============================================================================ВСТУПЛЕНИЕ====
        
label start:

    scene menu_down with fade 
    show text1 with dissolve
    call screen text1

label text2:
    scene menu_buttons with dissolve
    show text2 with dissolve
    call screen text2
    
label text3:
    scene menu_cubs with dissolve
    show text3 with dissolve
    call screen text3
    
label game_start:
    
#==============================================================================КУБКИ
    
    scene menu_cubs   # Сначала меню с кнопками, если вдруг нужно получить кубок

    if cub_priz_gold:   # Показать все изображения кубков, если они уже были получены ранее
        show cub_priz_gold
    elif cub_priz_silver:
        show cub_priz_silver
    elif cub_priz_bronz:
        show cub_priz_bronz
    if cub_mat_gold:
        show cub_mat_gold
    elif cub_mat_silver:
        show cub_mat_silver
    elif cub_mat_bronz:
        show cub_mat_bronz
    if cub_mem_gold:
        show cub_mem_gold
    elif cub_mem_silver:
        show cub_mem_silver
    elif cub_mem_bronz:
        show cub_mem_bronz
    if cub_wis_gold:
        show cub_wis_gold
    elif cub_wis_silver:
        show cub_wis_silver
    elif cub_wis_bronz:
        show cub_wis_bronz
    if cub_win_gold:
        show cub_win_gold
    elif cub_win_silver:
        show cub_win_silver
    elif cub_win_bronz:
        show cub_win_bronz
    with dissolve
     
    if cub_bronz==1:        # Добавить кубки с эффектом появления, если они были получены только что
        play sound 'music/Applause2.ogg'
        $renpy.pause(1)
        show cub_priz_bronz with zoomin
        $ cub_bronz=2
        $ cub_priz_bronz=True
    elif cub_bronz==3:
        play sound 'music/Applause2.ogg'
        $renpy.pause(1)
        show cub_priz_silver with zoomin
        $ cub_bronz=4
        $ cub_priz_silver=True
    elif cub_bronz==5:
        play sound 'music/Applause2.ogg'
        $renpy.pause(1)
        show cub_priz_gold with zoomin
        $ cub_bronz=6
        $ cub_priz_gold=True
    if cub_mat==1:
        play sound 'music/Applause2.ogg'
        $renpy.pause(1)
        show cub_mat_bronz with zoomin
        $ cub_mat=2
        $ cub_mat_bronz=True
    elif cub_mat==3:
        play sound 'music/Applause2.ogg'
        $renpy.pause(1)
        show cub_mat_silver with zoomin
        $ cub_mat=4
        $ cub_mat_silver=True
    elif cub_mat==5:
        play sound 'music/Applause2.ogg'
        $renpy.pause(1)
        show cub_mat_gold with zoomin
        $ cub_mat=6
        $ cub_mat_gold=True
    if cub_mem==1:
        play sound 'music/Applause2.ogg'
        $renpy.pause(1)
        show cub_mem_bronz with zoomin
        $ cub_mem=2
        $ cub_mem_bronz=True
    elif cub_mem==3:
        play sound 'music/Applause2.ogg'
        $renpy.pause(1)
        show cub_mem_silver with zoomin
        $ cub_mem=4
        $ cub_mem_silver=True
    elif cub_mem==5:
        play sound 'music/Applause2.ogg'
        $renpy.pause(1)
        show cub_mem_gold with zoomin
        $ cub_mem=6
        $ cub_mem_gold=True
    if cub_wis==1:
        play sound 'music/Applause2.ogg'
        $renpy.pause(1)
        show cub_wis_bronz with zoomin
        $ cub_wis=2
        $ cub_wis_bronz=True
    elif cub_wis==3:
        play sound 'music/Applause2.ogg'
        $renpy.pause(1)
        show cub_wis_silver with zoomin
        $ cub_wis=4
        $ cub_wis_silver=True
    elif cub_wis==5:
        play sound 'music/Applause2.ogg'
        $renpy.pause(1)
        show cub_wis_gold with zoomin
        $ cub_wis=6
        $ cub_wis_gold=True
    if cub_gold==1:
        play sound 'music/Applause1.ogg'
        $renpy.pause(1)
        show cub_win_bronz with zoomin
        $ cub_gold=2
        $ cub_win_bronz=True
    elif cub_gold==3:
        play sound 'music/Applause1.ogg'
        $renpy.pause(1)
        show cub_win_silver with zoomin
        $ cub_gold=4
        $ cub_win_silver=True
    elif cub_gold==5:
        play sound 'music/Applause1.ogg'
        $renpy.pause(1)
        show cub_win_gold with zoomin
        $ cub_gold=6
        $ cub_win_gold=True
        
#====================================================================================ВЫБОР====ИГРЫ====
    
label start_game2:   # Метка для перехода, если игрок нажимает на кубки
    scene menu_main
    call screen main_menu_screen  # Вызов основного экрана, который отвечает за навигацию по меню
    
#==============================================================СЛОЖЕНИЕ===И===ВЫЧИТАНИЕ====

    
label matem:
    scene menu_down
    show matema_text with dissolve
    call screen matema_text
label matema2:
    hide matema_text 
    show matema_board
    show expression "right_"+str(right_num)+'.png'
    with dissolve
    while circle_num<5:
        $matematika()
        show expression num1+'.png':
            xpos 320 ypos 100
        show expression operate+'.png':
            xpos 448 ypos 100
        show expression num2+'.png':
            xpos 576 ypos 100
        show expression '=.png':
            xpos 704 ypos 100
        label matema3:
            hide expression answer+'.png '
            if answer:
                show expression answer+'.png ':
                    xpos 822 ypos 100
            call screen matema_number
    
        label one:
            $answer='1'
            jump matema3
        label two:
            $answer='2'
            jump matema3
        label three:
            $answer='3'
            jump matema3
        label four:
            $answer='4'
            jump matema3
        label five:
            $answer='5'
            jump matema3
        label six:
            $answer='6'
            jump matema3
        label seven:
            $answer='7'
            jump matema3
        label eight:
            $answer='8'
            jump matema3
        label nine:
            $answer='9'
            jump matema3
        label zero:
            $answer='0'
            jump matema3
    
        label matema_decide:
    
            if answer==right_answer:
                $ right_num+=1
                play sound 'music/chime1.ogg'
                show expression "right_"+str(right_num)+'.png'
                show smile with dissolve
                $renpy.pause(1)
                hide smile with dissolve
            else:
                play sound 'music/buzzer2.ogg'
                show sad with dissolve
                $renpy.pause(1)
                hide sad with dissolve
            $ answer=''
            $ circle_num+=1
          
    if right_num>=5 and cub_mat<5:
        $cub_mat=5
    elif right_num>=3 and cub_mat<3:
        $cub_mat=3
    elif right_num>=1 and cub_mat<1:
        $cub_mat=1
        
    if not mat:
        $ first_game+=1
        if first_game==1:
            $cub_bronz=1
        elif first_game==2:
            $cub_bronz=3
        elif first_game==3:
            $cub_bronz=5
        $ mat=True
      
    jump in_menu
    
#==============================================================ЗАЖГИ===ЛАМПОЧКИ=====
    
label lamps:
    scene menu_down
    show lamp_text with dissolve
    call screen lamp_text
label lamps2:
    hide lamp_text
    show lamps
    show right_answer
    show expression 'right_'+str(right_num)+'.png'
    show expression 'stop.png'
    with dissolve
    
    while circle_num !=5:
        show lamp_look 
        $renpy.pause(0.5)
        while lamp_circle != circle_num+1: # Зажигает от одной до пяти ламп в зависимости от уровня внешнего цикла
            $ random_number()
            show expression 'lamp_on'+str(num1) with dissolve
            $renpy.pause(0.2)
            hide expression 'lamp_on'+str(num1) with dissolve
            $ lamp_circle+=1
        $renpy.pause(0.5)
        hide lamp_look
        show lamp_go
        
        while lamp_circle2 !=circle_num+1: # Позволяет пользователю одну за другой нажимать лампы. В случае ошибки обрывает цикл.
            hide lamps
            
            call screen lamps

            label lamp1:
                show lamps
                $ choosen_lamp=1
                jump lamp5
            label lamp2:
                show lamps
                $ choosen_lamp=2
                jump lamp5
            label lamp3:
                show lamps
                $ choosen_lamp=3
                jump lamp5
            label lamp4:
                show lamps
                $ choosen_lamp=4
                jump lamp5
        
            label lamp5:
                if choosen_lamp==lamp_storage[lamp_circle2]:
                    $ lamp_circle2+=1
                    show expression 'lamp_on'+str(choosen_lamp) with dissolve
                    $renpy.pause(0.2)
                    hide expression 'lamp_on'+str(choosen_lamp) with dissolve
                    if lamp_circle2 ==circle_num+1:
                        $ right_num+=1
                        show expression 'right_'+str(right_num)+'.png'
                        play sound 'music/chime1.ogg'
                        show smile with dissolve
                        $renpy.pause(1)
                        hide smile with dissolve
                else:
                    play sound 'music/buzzer2.ogg'
                    show expression 'lamp_wrong'+str(choosen_lamp) with dissolve
                    $renpy.pause(0.2)
                    hide expression 'lamp_wrong'+str(choosen_lamp) with dissolve
                    show sad with dissolve
                    $renpy.pause(1)
                    hide sad with dissolve
                    $ lamp_circle2=circle_num+1
                    
        $ lamp_circle=0
        $ lamp_circle2=0
        $ circle_num+=1
        $lamp_storage=[]
        $renpy.pause(0.5)
        hide lamp_go

    if right_num>=5 and cub_mem<5:
        $cub_mem=5
    elif right_num>=3 and cub_mem<3:
        $cub_mem=3
    elif right_num>=1 and cub_mem<1:
        $cub_mem=1
        
    if not mem:
        $ first_game+=1
        if first_game==1:
            $cub_bronz=1
        elif first_game==2:
            $cub_bronz=3
        elif first_game==3:
            $cub_bronz=5
        $ mem=True
        
    jump in_menu
    
#==================================================================УГАДАЙ===ЗАГАДКУ======
    
label zagadki:
    scene menu_down
    show zagadka_text with dissolve
    call screen zagadka_text
label zagadki2:
    hide zagadka_text
    show zagadka_board
    show right_answer
    show expression 'right_'+str(right_num)+'.png'
    with dissolve
    $ zagadki()
    while circle_num !=5:
        $ answers()
        show expression 'zagadka_'+str(zagadki_round[circle_num])+'.png'
        
        call screen zagadki
            
        label zagadka1:
            $zagadka_answer=zagadki_answers[0]
            jump zagadka5
        label zagadka2:
            $zagadka_answer=zagadki_answers[1]
            jump zagadka5
        label zagadka3:
            $zagadka_answer=zagadki_answers[2]
            jump zagadka5
        label zagadka4:
            $zagadka_answer=zagadki_answers[3]
            jump zagadka5
        label zagadka5:
            
            show expression 'otvet_'+str(zagadki_answers[0])+'.png':   # Чтобы надписи не пропадали после нажатия на кнопку
                xpos 360 ypos 353
            show expression 'otvet_'+str(zagadki_answers[1])+'.png':
                xpos 360 ypos 499
            show expression 'otvet_'+str(zagadki_answers[2])+'.png':
                xpos 664 ypos 353
            show expression 'otvet_'+str(zagadki_answers[3])+'.png':
                xpos 664 ypos 499
                
            if zagadka_answer==zagadki_round[circle_num]:
                $ right_num+=1
                play sound 'music/chime1.ogg'
                show expression 'right_'+str(right_num)+'.png'
                show smile with dissolve
                $renpy.pause(1)
                hide smile with dissolve
            else:
                play sound 'music/buzzer2.ogg'
                show sad with dissolve
                $renpy.pause(1)
                hide sad with dissolve
                
        $ circle_num+=1
        $ zagadki_answers=[]
        
        hide expression 'otvet_'+str(zagadki_answers[0])+'.png' # Чтобы они пропали перед кнопками
        hide expression 'otvet_'+str(zagadki_answers[1])+'.png'
        hide expression 'otvet_'+str(zagadki_answers[2])+'.png'
        hide expression 'otvet_'+str(zagadki_answers[3])+'.png'

    if right_num>=5 and cub_wis<5:
        $cub_wis=5
    elif right_num>=3 and cub_wis<3:
        $cub_wis=3
    elif right_num>=1 and cub_wis<1:
        $cub_wis=1
    
    if not zag:
        $ first_game+=1
        if first_game==1:
            $cub_bronz=1
        elif first_game==2:
            $cub_bronz=3
        elif first_game==3:
            $cub_bronz=5
        $ zag=True
        
    jump in_menu
    
#=========================================================================================ВОЗВРАЩЕНИЕ В МЕНЮ========ОБНУЛЕНИЕ ПЕРЕМЕНЫННЫХ=========
    
label in_menu:
    if cub_mat+cub_mem+cub_wis==18:
        pass
    elif cub_wis>4 and cub_mem>4 and cub_mat>4:
        $ cub_gold=5
    elif cub_wis>2 and cub_mem>2 and cub_mat>2:
        $ cub_gold=3
    elif cub_wis>0 and cub_mem>0  and cub_mat>0:
        $ cub_gold=1
    
    $ right_num=0
    $ circle_num=0
    $ zagadki_round=[]
    scene menu_down
    show good 
    with dissolve
    call screen good
    
    jump game_start
        
label in_menu_stop:
    $ right_num=0
    $ circle_num=0
    $ zagadki_round=[]
    jump game_start
    
label exit:
