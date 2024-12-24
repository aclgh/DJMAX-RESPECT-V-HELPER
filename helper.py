import keyboard

right_key = ['j', 'k']
right_target = 'l'
left_key = ['d', 'f']
left_target = 's'
# 定义触发事件：按下两个键时模拟按下另一个键
key_pressed = {right_target: False, left_target: False}


def on_key_event(event):
    # 监听并处理按键事件
    if keyboard.is_pressed(right_key[0]) and keyboard.is_pressed(right_key[1]):
        if not key_pressed[right_target]:  # 如果目标键 right_target 没有按下
            keyboard.press(right_target)
            key_pressed[right_target] = True
            print(f"模拟按下 {right_target}")
    else:
        if key_pressed[right_target]:  # 如果目标键 right_target 已经按下，释放它
            keyboard.release(right_target)
            key_pressed[right_target] = False

    if keyboard.is_pressed('d') and keyboard.is_pressed('f'):
        if not key_pressed[left_target]:  # 如果目标键 left_target 没有按下
            keyboard.press(left_target)
            key_pressed[left_target] = True
            print(f"模拟按下 {left_target}")
    else:
        if key_pressed[left_target]:  # 如果目标键 left_target 已经按下，释放它
            keyboard.release(left_target)
            key_pressed[left_target] = False


# 设置监听
keyboard.hook(on_key_event)

# 启动监听并保持程序运行
keyboard.wait(']')  # 按下 ']' 键退出程序
