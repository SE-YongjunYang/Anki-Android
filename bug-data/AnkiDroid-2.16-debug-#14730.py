# bug reproduction script for bug #4451of ankidroid
import sys
import time

import uiautomator2 as u2

# avd_serial: emulator-5554

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)



    d.app_start("com.ichi2.anki.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.ichi2.anki.debug":
            break
        time.sleep(2)
    wait()

    # 点击蓝色圆形“+”
    out = d(resourceId="com.ichi2.anki.debug:id/fab_main").click()
    if not out:
        print("Success: click add")
    wait()

    # 点击弹出的add灰色方框
    out = d(resourceId="com.ichi2.anki.debug:id/add_note_label").click()
    if not out:
        print("Success: 点击弹出的add灰色方框")
    wait()


    # 点击“链接”图标
    out = d(resourceId="com.ichi2.anki.debug:id/id_media_button", description="Attach multimedia content to the Front field").click()
    if not out:
        print("Success: 点击“链接”图标")
    wait()


    # 点击弹出的“Record audio"
    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
    if not out:
        print("Success: 点击弹出的'Record audio'")
    wait()


    # 点击开始录制
    out = d(resourceId="com.ichi2.anki.debug:id/action_start_recording").click()
    if not out:
        print("Success: 点击开始录制")
    wait()


    # 点击完成录制，绿色“√”圆形图标
    out = d(resourceId="com.ichi2.anki.debug:id/action_save_recording").click()
    if not out:
        print("Success: 点击完成录制，绿色“√”圆形图标")
    wait()

    # 点击中间的播放按钮
    out = d(resourceId="com.ichi2.anki.debug:id/action_play_recording").click()
    if not out:
        print("Success: 点击中间的播放按钮")
    wait()



    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)