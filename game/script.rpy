# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
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
    scene menu_down with dissolve
    "бу"
    
label lamps:
    "бубу"
    
label zagadki:
    "бубубу"
