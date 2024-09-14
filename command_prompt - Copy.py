import chatbot, random, time, all_the_chatbots, pyautogui
installin = ["installing pypykoko at users","installing "+str(random.randint(1,100))+" packages","adding all instances","adding current version","deleting file number "+str(random.randint(1,12))+" at once","downloading all data including gitfile29.json","installing at users/computer/files/programs/commands-storage/curdatasets all data sets are stored in this local file","installin version "+str(random.randint(0,99))+"."+str(random.randint(0,99))+"."+str(random.randint(0,99))+"","WARNING: installing in different directory that can create some problems, to fix this create a different directory with the name --command-ctrl-go with the ._install_ file extension","adding all data from gitlife-com.json","installing all xml statuses, will not work with .xml1-.xml999, use the extension .xml0.0-.xml0.99","installing u-r-old.txt with readme.txt","deleting all files in users including win32 and mor"]
errors = ["error number "+str(random.randint(111,999))+":","win error"+str(random.randint(111,9999)),"error: file is missing and/or deleted","could not install because you need to pay us the exact amount of $"+str(random.randint(1,100000)),"could not install because you need win32.5+","error: gpu is to slow","error: cpu is to slow"]
installed = [];error = False
print("Microsoft Windows = [Version 10.0.22631.3593](c) MicrosoFt CorpoRation. All rights reserved.")
talkto=random.randint(1,5)
while True:
    if random.randint(0,100)==0:
        pyautogui.write(all_the_chatbots.ask_707("you are the dumbest thing ever")+"you are the dumbest thing ever");pyautogui.keyDown("enter")
        if random.randint(0,1)==0:
            if random.randint(0,1)==0:
                pyautogui.moveTo(random.randint(-500,500), random.randint(-500,500)) 
            for i in range(random.randint(1,500)):
                pyautogui.click(duration=random.randint(.1,.75))
    prompt = input('C:/Users/users Laptop>').lower()
    if "install" in prompt and not "uninstall" in prompt:
        com = prompt.split("install")
        if not com[1] in installed:
            print("installing "+com[1])
            for i in range(random.randint(2,50)):
                time.sleep(random.randint(0,2))
                print(installin[random.randint(0,len(installin)-1)])
                if random.randint(1,50)==1:
                    print(errors[random.randint(0,len(errors)-1)])
                    error=True
                    break
            if(not error):
                print("succesfully install "+com[1])
                installed.append(com[1])
            print()
            error=False
        else:
            print(com[1]+ " already installed")
    elif "uninstall" in prompt:
        com = prompt.split("uninstall");ask=input("uninstall "+com[1]+"? ").lower()
        if "y" in ask:
            print("uninstalling "+com[1])
            time.sleep(random.randint(0,5))
            print("succesfully unistalled "+com[1])
    #elif :

    else:
        if talkto == 1:
            print(chatbot.Chat().say(prompt))
        elif talkto == 2:
            print(all_the_chatbots.ask_707(prompt))
        elif talkto == 3:
            print(all_the_chatbots.ask_alien_bot(prompt))
        elif talkto == 4:
            print(all_the_chatbots.ask_itachi(prompt))
        elif talkto == 5:
            print(all_the_chatbots.ask_virtual_teacher(prompt))