import pygame
import time
import random

def new_food(head):
    while True:
        # 循环，不断实例化food对象直到生成一个不与蛇头重合的食物
        new_food_instance = Food(random.randint(0, 45) * 20, random.randint(0, 28) * 20, (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255)))
        # 若new_food_instance和蛇头重合则不创建
        if new_food_instance.x != head.x and new_food_instance.y != head.y:
            break
    return new_food_instance
# 在窗体中绘制贪吃蛇
# 形参：一个是颜色另一个是实例化对象
def draw_element(surface, color, position, radius=10, is_food=False):
    pygame.draw.circle(surface, color, (position.x, position.y), radius)

def draw_snake(color, snake):
    draw_element(window, color, snake)

def draw_food(food):
    draw_element(window, food.color, food)
def show_end():
    while True:
        window.blit(init_background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_end()
        pygame.display.set_caption("贪吃蛇大冒险")
        font = pygame.font.SysFont("simHei", 40)
        fontsurf = font.render('游戏结束! 玩家1得分: {} 玩家2得分：{}'.format(score1, score2), True, black)
        window.blit(fontsurf, (150, 100))
        button("返回主菜单", 370, 300, 200, 40, blue, brightred, into_game)
        button("退出游戏", 370, 470, 200, 40, red, brightred, exit_end)
        pygame.display.update()
        clock.tick(20)
# 初始界面和游戏中途点击退出游戏时
def exit_end():
    pygame.quit()
    sys.exit()
def start_game_double():
    # 播放音乐
    pygame.mixer.music.play(-1)
    # 定义存分数的全局变量
    global score1
    global score2
    score1 = score2 = 0
    # 初始化存放玩家键盘输入运动方向的变量
    run_direction1 = "right"
    run_direction2 = "up"
    # 初始化贪吃蛇运动方向的变量
    run1 = run_direction1
    run2 = run_direction2
    # 实例化贪吃蛇和食物对象
    head1 = Snake(randint(0, 30) * 20, randint(0, 20) * 20)
    head2 = Snake(randint(0, 30) * 20, randint(0, 20) * 20)
    # 实例化蛇身长度为2个单位
    snake_body1 = [Snake(head1.x, head1.y + 20), Snake(head1.x, head1.y + 40)]
    snake_body2 = [Snake(head2.x, head2.y + 20), Snake(head2.x, head2.y + 40)]
    # 实例化食物列表，列表随着其中食物被吃掉应该不断缩短
    food_list = [Food(randint(0, 45) * 20, randint(0, 28) * 20, (randint(10, 255), randint(10, 255), randint(10, 255)))]
    for i in range(1,24):
        food_list.append(Food(randint(0, 45) * 20, randint(0, 28) * 20, (randint(10, 255), randint(10, 255), randint(10, 255))))
    # 实例化单个食物，方便循环内生成单个新食物
    food = Food(randint(0, 45) * 20, randint(0, 28) * 20, (randint(10, 255), randint(10, 255), randint(10, 255)))
    while True:
        window.blit(background, (0,0))
        # 监听玩家键盘输入的运动方向值，并根据输入转为up、down、right或left，方便程序中调用
        # pygame.event.get()返回一个列表，存放本次game执行中程序遇到的一连串事件（按时间顺序依次存放）
        for event in pygame.event.get():
            # pygame.QUIT事件是指用户点击窗口右上角的"×"
            if event.type == pygame.QUIT:
                # 显示结果界面
                show_end()
            # 若事件类型是按下键盘，分↑ ↓ ← →四种情况讨论
            elif event.type == pygame.KEYDOWN:
                # 若事件类型是按下键盘↑
                # key是键值，表示按下去的键值是什么
                if event.key == pygame.K_UP:
                    run_direction2 = "up"
                # 若事件类型是按下键盘↓
                if event.key == pygame.K_DOWN:
                    run_direction2 = "down"
                # 若事件类型是按下键盘←
                if event.key == pygame.K_LEFT:
                    run_direction2 = "left"
                # 若事件类型是按下键盘→
                if event.key == pygame.K_RIGHT:
                    run_direction2 = "right"
                # 若事件类型是按下键盘↑
                if event.key == ord('w'):
                    run_direction1 = "up"
                # 若事件类型是按下键盘↓
                if event.key == ord('s'):
                    run_direction1 = "down"
                # 若事件类型是按下键盘←
                if event.key == ord('a'):
                    run_direction1 = "left"
                # 若事件类型是按下键盘→
                if event.key == ord('d'):
                    run_direction1 = "right"
        # 绘制初始化的25个食物图像(24+1=25)
        # 随着该列表中的食物被吃掉，列表应该不断pop以清除已经被吃的事物
        for item in food_list:
            draw_food(item)
        # 绘制被贪吃蛇吃掉后新增的食物图像
        draw_food(food)
        # 绘制蛇头图像
        # 在绘制蛇头之前先检查是不是已经死亡，如果已死亡，则不绘制
        # ！！不能通过die_flag判断是否死亡因为每次循环一开头die_flag都初始化为False
        # 因此最好的方法是通过snake_body是否为空判断
        if len(snake_body1) != 0:
            draw_snake(black, head1)
        if len(snake_body2) != 0:
            draw_snake(black, head2)
        # 绘制蛇身图像
        for item in snake_body1:
            draw_snake(blue, item)
        for item in snake_body2:
            draw_snake(green, item)
        # 若蛇未死亡，则插入蛇头位置到蛇身列表中
        # 即：若蛇已死亡，则保持snake_body为空不变
        if len(snake_body1) != 0:
            snake_body1.insert(0, Snake(head1.x, head1.y))
        if len(snake_body2) != 0:
            snake_body2.insert(0, Snake(head2.x, head2.y))
        # 判断贪吃蛇原运动方向(run)与玩家键盘输入的运动方向(run_direction)是否违反正常运动情况
        if run1 == "up" and not run_direction1 == "down":
            run1 = run_direction1
        if run1 == "down" and not run_direction1 == "up":
            run1 = run_direction1
        if run1 == "left" and not run_direction1 == "right":
            run1 = run_direction1
        if run1 == "right" and not run_direction1 == "left":
            run1 = run_direction1
        if run2 == "up" and not run_direction2 == "down":
            run2 = run_direction2
        if run2 == "down" and not run_direction2 == "up":
            run2 = run_direction2
        if run2 == "left" and not run_direction2 == "right":
            run2 = run_direction2
        if run2 == "right" and not run_direction2 == "left":
            run2 = run_direction2
        # 根据玩家键入方向进行蛇头坐标的更新
        if run1 == "up":
            head1.y -= 20
        if run1 == "down":
            head1.y += 20
        if run1 == "left":
            head1.x -= 20
        if run1 == "right":
            head1.x += 20
        if run2 == "up":
            head2.y -= 20
        if run2 == "down":
            head2.y += 20
        if run2 == "left":
            head2.x -= 20
        if run2 == "right":
            head2.x += 20
        # 判断两条蛇是否死亡
        # 初始化四个死亡标志为False
        die_flag1 = die_flag2 = False
        # 此时snake_body1,2中均已包含蛇头
        # snake_body1,2第一个元素是蛇头，故不能从0号元素开始比较
        # 因为该蛇蛇头必然和自己重合
        # 这里snake_body1,2均从1号元素开始
        # 所以snake_body1[1:]+snake_body2[1:]是纯粹存储蛇身的列表
        for body in snake_body1[1:]+snake_body2[1:]:
            if head1.x == body.x and head1.y == body.y:
                die_flag1 = True
            if head2.x == body.x and head2.y == body.y:
                die_flag2 = True
        if die_flag1 == True or head1.x < 0 or head1.x > 960 or head1.y < 0 or head1.y > 600:
            # 注意：这边虽然蛇身列表清空，但head1对象仍存在
            # 故必须要在上面的绘制蛇头代码前面加上if先判断蛇是否死亡
            snake_body1.clear()
        if die_flag2 == True or head2.x < 0 or head2.x > 960 or head2.y < 0 or head2.y > 600:
            die_flag2 = True
            # 注意：这边虽然蛇身列表清空，但head1对象仍存在
            # 故必须要在上面的绘制蛇头代码前面加上if先判断蛇是否死亡
            snake_body2.clear()
        # 若两条蛇都死亡
        # 同样地，只能通过snake_body是否为空判断蛇是否死亡
        if len(snake_body1) == 0 and len(snake_body2) == 0:
            show_end()
        # 判断蛇头和食物坐标，若相等，则加分，并生成新的食物
        # 定义标志，表明是否找到和蛇头相等的食物
        global flag1
        global flag2
        flag1 = flag2 = 0
        # 如果蛇头和食物重合
        for item in food_list:
            # 在蛇1没死且蛇头1和某一食物坐标相等的条件下
            if len(snake_body1) != 0 and (head1.x == item.x and head1.y == item.y or head1.x == food.x and head1.y == food.y):
                flag1 = 1
                score1 += 1
                # 弹出被吃掉的这个食物
                food_list.pop(food_list.index(item))
                # 再产生一个食物
                food = new_food(head1)
                # 把新食物插入food_list，下一次循环中会更新绘制食物全体
                food_list.append(food)
                break
            # 在蛇2没死的且蛇头2和某一食物坐标相等的条件下
            elif len(snake_body2) != 0 and head2.x == item.x and head2.y == item.y or head2.x == food.x and head2.y == food.y:
                flag2 = 1
                score2 += 1
                # 弹出被吃掉的这个食物
                food_list.pop(food_list.index(item))
                # 再产生一个食物
                food = new_food(head2)
                # 把新食物插入food_list，下一次循环中会更新绘制食物全体
                food_list.append(food)
                break
        # 蛇1必须没死，否则pop会引发异常
        if len(snake_body1) != 0 and flag1 == 0:
            snake_body1.pop()
        # 蛇2必须没死，否则pop会引发异常
        if len(snake_body2) != 0 and flag2 == 0:
            snake_body2.pop ()
        font = pygame.font.SysFont("simHei", 25)
        mode_title1 = mode_title2 = font.render('正常模式', False, grey)
        socre_title1 = font.render('得分: %s' % score1, False, grey)
        socre_title2 = font.render('得分: %s' % score2, False, grey)
        window.blit(mode_title1, (50, 30))
        window.blit(socre_title1, (50, 65))
        window.blit(mode_title2, (800, 30))
        window.blit(socre_title2, (800, 65))
        # 更新蛇头蛇身和食物的数据
        pygame.display.update()
        # 通过帧率设置贪吃蛇速度
        clock.tick(8)
def start_kgame_double():
    # 播放音乐
    pygame.mixer.music.play(-1)
    # 定义存分数的全局变量
    global score1
    global score2
    score1 = score2 = 0
    # 初始化存放玩家键盘输入运动方向的变量
    run_direction1 = "right"
    run_direction2 = "up"
    # 初始化贪吃蛇运动方向的变量
    run1 = run_direction1
    run2 = run_direction2
    # 实例化贪吃蛇和食物对象
    head1 = Snake(randint(0, 30) * 20, randint(0, 20) * 20)
    head2 = Snake(randint(0, 30) * 20, randint(0, 20) * 20)
    # 实例化蛇身长度为2个单位
    snake_body1 = [Snake(head1.x, head1.y + 20), Snake(head1.x, head1.y + 40)]
    snake_body2 = [Snake(head2.x, head2.y + 20), Snake(head2.x, head2.y + 40)]
    # 实例化食物列表，列表随着其中食物被吃掉应该不断缩短
    food_list = [Food(randint(0, 45) * 20, randint(0, 28) * 20, (randint(10, 255), randint(10, 255), randint(10, 255)))]
    for i in range(1,24):
        food_list.append(Food(randint(0, 45) * 20, randint(0, 28) * 20, (randint(10, 255), randint(10, 255), randint(10, 255))))
    # 实例化单个食物，方便循环内生成单个新食物
    food = Food(randint(0, 45) * 20, randint(0, 28) * 20, (randint(10, 255), randint(10, 255), randint(10, 255)))
    while True:
        window.blit(background, (0,0))
        # 监听玩家键盘输入的运动方向值，并根据输入转为up、down、right或left，方便程序中调用
        # pygame.event.get()返回一个列表，存放本次game执行中程序遇到的一连串事件（按时间顺序依次存放）
        for event in pygame.event.get():
            # pygame.QUIT事件是指用户点击窗口右上角的"×"
            if event.type == pygame.QUIT:
                # 显示结果界面
                show_end()
            # 若事件类型是按下键盘，分↑ ↓ ← →四种情况讨论
            elif event.type == pygame.KEYDOWN:
                # 若事件类型是按下键盘↑
                # key是键值，表示按下去的键值是什么
                if event.key == pygame.K_UP:
                    run_direction2 = "up"
                # 若事件类型是按下键盘↓
                if event.key == pygame.K_DOWN:
                    run_direction2 = "down"
                # 若事件类型是按下键盘←
                if event.key == pygame.K_LEFT:
                    run_direction2 = "left"
                # 若事件类型是按下键盘→
                if event.key == pygame.K_RIGHT:
                    run_direction2 = "right"
                # 若事件类型是按下键盘↑
                if event.key == ord('w'):
                    run_direction1 = "up"
                # 若事件类型是按下键盘↓
                if event.key == ord('s'):
                    run_direction1 = "down"
                # 若事件类型是按下键盘←
                if event.key == ord('a'):
                    run_direction1 = "left"
                # 若事件类型是按下键盘→
                if event.key == ord('d'):
                    run_direction1 = "right"
        # 绘制初始化的25个食物图像(24+1=25)
        # 随着该列表中的食物被吃掉，列表应该不断pop以清除已经被吃的事物
        for item in food_list:
            draw_food(item)
        # 绘制被贪吃蛇吃掉后新增的食物图像
        draw_food(food)
        # 绘制蛇头图像
        # 在绘制蛇头之前先检查是不是已经死亡，如果已死亡，则不绘制
        if len(snake_body1) != 0:
            draw_snake(black, head1)
        if len(snake_body2) != 0:
            draw_snake(black, head2)
        # 绘制蛇身图像
        for item in snake_body1:
            draw_snake(blue, item)
        for item in snake_body2:
            draw_snake(green, item)
        # 插入蛇头位置到蛇身列表中
        if len(snake_body1) != 0:
            snake_body1.insert(0, Snake(head1.x, head1.y))
        if len(snake_body2) != 0:
            snake_body2.insert(0, Snake(head2.x, head2.y))
        # 判断贪吃蛇原运动方向(run)与玩家键盘输入的运动方向(run_direction)是否违反正常运动情况
        if run1 == "up" and not run_direction1 == "down":
            run1 = run_direction1
        if run1 == "down" and not run_direction1 == "up":
            run1 = run_direction1
        if run1 == "left" and not run_direction1 == "right":
            run1 = run_direction1
        if run1 == "right" and not run_direction1 == "left":
            run1 = run_direction1
        if run2 == "up" and not run_direction2 == "down":
            run2 = run_direction2
        if run2 == "down" and not run_direction2 == "up":
            run2 = run_direction2
        if run2 == "left" and not run_direction2 == "right":
            run2 = run_direction2
        if run2 == "right" and not run_direction2 == "left":
            run2 = run_direction2
        # 根据玩家键入方向进行蛇头坐标的更新
        if run1 == "up":
            head1.y -= 20
        if run1 == "down":
            head1.y += 20
        if run1 == "left":
            head1.x -= 20
        if run1 == "right":
            head1.x += 20
        if run2 == "up":
            head2.y -= 20
        if run2 == "down":
            head2.y += 20
        if run2 == "left":
            head2.x -= 20
        if run2 == "right":
            head2.x += 20
        # 实现穿墙
        # 蛇头穿出窗体共有8种情况
        if head1.x < 0:
            head1.x = 960
        if head1.x > 960:
            head1.x = 0
        if head1.y < 0:
            head1.y = 600
        if head1.y > 600:
            head1.y = 0
        if head2.x < 0:
            head2.x = 960
        if head2.x > 960:
            head2.x = 0
        if head2.y < 0:
            head2.y = 600
        if head2.y > 600:
            head2.y = 0
        # 定义死亡标志位
        die_flag1 = die_flag2 = False
        for body in snake_body1[1:]+snake_body2[1:]:
            if head1.x == body.x and head1.y == body.y:
                die_flag1 = True
            if head2.x == body.x and head2.y == body.y:
                die_flag2 = True
        if die_flag1 == True:
            snake_body1.clear()
        if die_flag2 == True:
            snake_body2.clear()
        # 若两条蛇都死亡
        if len(snake_body1) == 0 and len(snake_body2) == 0:
            show_end()
        # 判断蛇头和食物坐标，若相等，则加分，并生成新的食物
        # 定义标志，表明是否找到和蛇头相等的食物
        global flag1
        global flag2
        flag1 = flag2 = 0
        # 如果蛇头和食物重合
        for item in food_list:
            # 在蛇1没死且蛇头1和某一食物坐标相等的条件下
            if len(snake_body1) != 0 and (head1.x == item.x and head1.y == item.y or head1.x == food.x and head1.y == food.y):
                flag1 = 1
                score1 += 1
                # 弹出被吃掉的这个食物
                food_list.pop(food_list.index(item))
                # 再产生一个食物
                food = new_food(head1)
                # 把新食物插入food_list，下一次循环中会更新绘制食物全体
                food_list.append(food)
                break
            # 在蛇2没死的且蛇头2和某一食物坐标相等的条件下
            elif len(snake_body2) != 0 and head2.x == item.x and head2.y == item.y or head2.x == food.x and head2.y == food.y:
                flag2 = 1
                score2 += 1
                # 弹出被吃掉的这个食物
                food_list.pop(food_list.index(item))
                # 再产生一个食物
                food = new_food(head2)
                # 把新食物插入food_list，下一次循环中会更新绘制食物全体
                food_list.append(food)
                break
        # 蛇1必须没死，否则pop会引发异常
        if len(snake_body1) != 0 and flag1 == 0:
            snake_body1.pop()
        # 蛇2必须没死，否则pop会引发异常
        if len(snake_body2) != 0 and flag2 == 0:
            snake_body2.pop ()
        font = pygame.font.SysFont("simHei", 25)
        mode_title1 = mode_title2 = font.render('穿墙模式', False, grey)
        socre_title1 = font.render('得分: %s' % score1, False, grey)
        socre_title2 = font.render('得分: %s' % score2, False, grey)
        window.blit(mode_title1, (50, 30))
        window.blit(socre_title1, (50, 65))
        window.blit(mode_title2, (800, 30))
        window.blit(socre_title2, (800, 65))
        # 更新蛇头蛇身和食物的数据
        pygame.display.update()
        # 通过帧率设置贪吃蛇速度
        clock.tick(8)
1
def button(msg, x, y, w, h, ic, ac, action=None):
    # 获取鼠标位置
    mouse = pygame.mouse.get_pos()
    # 获取鼠标点击情况
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(window, ic, (x, y, w, h))
    # 设置按钮中的文字样式和居中对齐
    font = pygame.font.SysFont('simHei', 20)
    smallfont = font.render(msg, True, white)
    smallrect = smallfont.get_rect()
    smallrect.center = ((x + (w / 2)), (y + (h / 2)))
    window.blit(smallfont, smallrect)
def into_game():
    while True:
        window.blit(init_background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_end()
        # 设置字体
        font = pygame.font.SysFont("simHei", 50)
        # 初始界面显示文字
        fontsurf = font.render('欢迎来到贪吃蛇大冒险!', True, black)  # 文字
        fontrect = fontsurf.get_rect()
        fontrect.center = ((480), 200)
        window.blit(fontsurf, fontrect)
        button("正常模式", 370, 370, 200, 40, blue, brightred, start_game_double)
        button("可穿墙模式", 370, 420, 200, 40, violte, brightred, start_kgame_double)
        button("退出游戏", 370, 470, 200, 40, red, brightred, exit_end)
        pygame.display.update()
        clock.tick(20)