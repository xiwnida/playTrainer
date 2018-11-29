init python:
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
        
init:
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# Переменные
    $ cub_bronz=0
    $ cub_mat=0
    $ cub_mem=0
    $ cub_wis=0
    $ cub_gold=0
    $ num1=0 # Первое число для математики
    $ num2=0 # Второе число для математики
    $ operate=0 # Сложение или вычитание
    $ answer='' # Хранит в себе ответ пользователя
    $ right_answer='' # Хранит в себе правильный ответ
    $ circle_num=0 # Считает количество прохождений цикла
    $ right_num=0 # Считает количество правильных ответов
    $ first_game=False # Определяет, играл ли пользователь хотя бы в одну игру (для бронзового кубка)

# Экраны
screen text1:
    imagebutton:
        idle "text1_idle"
        hover "text1_hover"
        focus_mask True
        action Jump("text2")
        
screen text2:
    imagebutton:
        idle "text2_idle"
        hover "text2_hover"
        focus_mask True
        action Jump("text3")

screen text3:
    imagebutton:
        idle "text3_idle"
        hover "text3_hover"
        focus_mask True
        action Jump("game_start")
        
screen matema_text:
    imagebutton:
        idle "text1_idle"
        hover "text1_hover"
        focus_mask True
        action Jump("matema2")
        
        
screen main_menu_screen:
    imagebutton:
        idle "but1_idle"
        hover "but1_hover"
        focus_mask True
        action Jump("matem")
        
    imagebutton:
        idle "but2_idle"
        hover "but2_hover"
        focus_mask True
        action Jump("lamps")
        
    imagebutton:
        idle "but3_idle"
        hover "but3_hover"
        focus_mask True
        action Jump("zagadki")
    
    if cub_gold>0:
        imagebutton:
            idle "cub_gold"
            hover "cub_gold_hover"
            focus_mask True
            action Jump("start_game2")    
    
    if cub_bronz>0:
        imagebutton:
            idle "cub_bronz"
            hover "cub_bronz_hover"
            focus_mask True
            action Jump("start_game2")
    
    if cub_mat>0:
        imagebutton:
            idle "cub_mat"
            hover "cub_mat_hover"
            focus_mask True
            action Jump("start_game2")
        
    if cub_mem>0:
        imagebutton:
            idle "cub_mem"
            hover "cub_mem_hover"
            focus_mask True
            action Jump("start_game2")
        
    if cub_wis>0:       
        imagebutton:
            idle "cub_wis"
            hover "cub_wis_hover"
            focus_mask True
            action Jump("start_game2")
            
            
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
    scene menu_cubs   # Сначала меню с кнопками, если вдруг нужно получить кубок

    if cub_bronz==2:   # Показать все изображения кубков, если они уже были получены ранее
        show cub_bronz
    if cub_mat==2:
        show cub_mat
    if cub_mem==2:
        show cub_mem
    if cub_wis==2:
        show cub_wis
    if cub_gold==2:
        show cub_gold
    with dissolve
     
    if cub_bronz==1:        # Добавить кубки с эффектом появления, если они были получены только что
        show cub_bronz with zoomin
        $ cub_bronz=2
    if cub_mat==1:
        show cub_mat with zoomin
        $ cub_mat=2
    if cub_mem==1:
        show cub_mem with zoomin
        $ cub_mem=2
    if cub_wis==1:
        show cub_wis with zoomin
        $ cub_wis=2
    if cub_gold==1:
        show cub_gold with zoomin
        $ cub_gold=2
    
label start_game2:   # Метка для перехода, если игрок нажимает на кубки
    scene menu_main
    call screen main_menu_screen  # Вызов основного экрана, который отвечает за навигацию по меню

    
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
                show expression "right_"+str(right_num)+'.png'
                show right with dissolve
                $renpy.pause(1)
                hide right with dissolve
            else:
                show wrong with dissolve
                $renpy.pause(1)
                hide wrong with dissolve
            $ answer=''
            $ circle_num+=1
    if right_answer>=3 and cub_mat==0:
        $cub_mat=1
    if first_game==False:
        $cub_bronz=1
        $ first_game=True
    $ circle_num=0
    jump game_start
label lamps:
    "бубу"
    
label zagadki:
    "бубубу"
