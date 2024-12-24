import keyboard

# 定义触发事件：按下两个键时模拟按下另一个键
key_pressed = {'l': False, 's': False}


def on_key_event(event):
    # 监听并处理按键事件
    if keyboard.is_pressed('j') and keyboard.is_pressed('k'):
        if not key_pressed['l']:  # 如果目标键 'l' 没有按下
            keyboard.press('l')
            key_pressed['l'] = True
            print("模拟按下 'l'")
    else:
        if key_pressed['l']:  # 如果目标键 'l' 已经按下，释放它
            keyboard.release('l')
            key_pressed['l'] = False

    if keyboard.is_pressed('d') and keyboard.is_pressed('f'):
        if not key_pressed['s']:  # 如果目标键 's' 没有按下
            keyboard.press('s')
            key_pressed['s'] = True
            print("模拟按下 's'")
    else:
        if key_pressed['s']:  # 如果目标键 's' 已经按下，释放它
            keyboard.release('s')
            key_pressed['s'] = False


# 设置监听
keyboard.hook(on_key_event)

# 启动监听并保持程序运行
keyboard.wait(']')  # 按下 ']' 键退出程序
