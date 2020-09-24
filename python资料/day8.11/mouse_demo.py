"""
    PyAutoGUI——做职场高手,让所有GUI自动化,击败无聊的办公室重复性操作
        GUI:图形用户界面(Graphical User Interface)
            例如 办公软件,音乐播放器,即时通讯工具...
        盘点工作中的机械化重复性操作：
            办公软件、邮件...
        作用：自动控制鼠标和键盘。
        文档：https://pyautogui.readthedocs.io/en/latest/install.html
        安装：
            1. 打开运行窗口 win + r
            2. 输入cmd，进入命令行。
            3. 输入pip install pyautogui
"""
import pyautogui

# 显示鼠标位置(运行在命令行模式)
# pyautogui.displayMousePosition()

# 　pyautogui.moveTo(ｘ轴，ｙ轴，持续时间）
pyautogui.moveTo(260,327,3) # 移动到酷狗
pyautogui.doubleClick() # 双击打开酷狗

# 等待3秒
pyautogui.sleep(5)
# pyautogui.moveTo(639,657,3) # (死的)移动到播放按钮
# pyautogui.click()# 单击播放按钮

# 自动识别播放按钮
# 1. 保存需要点击的按钮图片
# play_image = pyautogui.screenshot(region=(485,660, 50, 50))
# play_image.save("play.png")

# # 2. 根据图片定位
button_play_location = pyautogui.locateOnScreen('play.png')
# 3. 计算中心点
button_play_point = pyautogui.center(button_play_location)
pyautogui.moveTo(button_play_point.x,button_play_point.y,3) # 移动到播放按钮
pyautogui.click()# 单击播放按钮
