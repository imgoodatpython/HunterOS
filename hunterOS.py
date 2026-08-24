import time, os, shutil, sys, math

P = {}  # passwords
R="\033[0m"; RD="\033[31m"; GR="\033[32m"
def col(t,c): return c+t+R
def ex(p): return os.path.exists(p)

# Boot
print("*===(HUNTER OS)===*",GR)
print("booting...")
for i in range(1,21):
    print(f"[{'#'*i + '-'*(20-i)}] {i*5}%"); time.sleep(0.03)
print("ready\n")

# Login
u=input("user: ")
if u not in P:
    P[u]=input("new pass: ")
else:
    if input("pass: ")!=P[u]:
        print(col("invaild",RD)); exit()

# Owner
print("owner? (yes/no)")
while True:
    own=input("> ").lower()
    if own in ("yes","no"): break
    print("invaild")
owner=u if own=="yes" else input("real owner: ")

# Drive
t,us,fr=shutil.disk_usage("C:/")
print(f"C: {t//(1024**3)}GB total, {us//(1024**3)}GB used, {fr//(1024**3)}GB free")
print("welcome",owner)

CMDS=["calc","osedit","mkfolder","rmdir","view","rename","ls",
      "tasks","clear","shutdown","passwd","help","size","reboot","version","whoami","time"]
DESC=[
    "calc: Simple calculator. Supports +, -, *, / using eval().",
    "OSedit: Create or delete files. make → create file, del → delete file.",
    "mkfolder: Create a new folder in the current directory.",
    "rmdir: Delete an empty folder.",
    "view: Display the contents of a text file.",
    "rename: Rename a file or folder.",
    "ls: List all files and folders in the current directory.",
    "tasks: Owner-only. Shows all available commands.",
    "clear: Clears the screen.",
    "shutdown: Exit HunterOS.",
    "passwd: Owner-only. Change your password. Requires old password + confirmation.",
    "help: Shows all commands.",
    "size: Shows the size of a file in bytes.",
    "reboot: Restarts HunterOS using os.execl.",
    "version: prints the codes version",
    "whoami: prints username password and ownership",
    "time: prints the current time once",
]
print("cmds:",", ".join(CMDS))

# Main loop
while True:
    a=input("hunterOS> ").lower()

    if a=="time":
        print(time.strftime("%Y/%m/%d %H:%M:%S"))
        continue

    elif a=="version":
        print("version 1.2 beta")

    elif a=="whoami":
        print(f"username:{u}, password:{P[u]}, owner Y/N:{own}")

    elif a=="reboot":
        print("rebooting..."); time.sleep(1)
        os.execl(sys.executable, sys.executable, *sys.argv)

    elif a=="help":
        print("cmds:"); [print(" ",d) for d in DESC]

    elif a=="passwd":
        if own!="yes": print(col("owner only",RD)); continue
        if input("old: ")!=P[u]:
            print(col("invaild",RD)); continue
        nw=input("new: ")
        if nw!=input("confirm: "):
            print(col("new and old dont match",RD)); continue
        P[u]=nw; print(col("changed",GR))

    elif a=="mkfolder":
        d=input("folder: ")
        try: os.mkdir(d); print("made")
        except Exception as e: print("error",e)

    elif a=="rmdir":
        d=input("folder: ")
        try: os.rmdir(d); print("deleted")
        except Exception as e: print("err",e)

    elif a=="clear":
        os.system("cls" if os.name=="nt" else "clear")

    elif a=="view":
        f=input("file: ")
        print(open(f).read() if ex(f) else "no file found")

    elif a in ("ls","list"):
        [print(" -",i) for i in os.listdir()]

    elif a=="tasks":
        if own!="yes": print("owner only"); continue
        print("tasks:"); [print(" -",t) for t in CMDS]

    elif a=="shutdown":
        print("shuting down"); break

    elif a in ("rename","renamedir"):
        o=input("old: "); n=input("new: ")
        if ex(o): os.rename(o,n); print("renamed")
        else: print("no file found")

    elif a=="size":
        f=input("file: ")
        if os.path.isfile(f):
            s=os.path.getsize(f); print(f"{s} bytes")
        else: print("no file found")

    elif a in ("osedit","oseditor"):
        m=input("make/del: ").lower()
        f=input("file: ")
        if m=="make":
            open(f,"w").write(input("content: "))
            print("made")
        elif m=="del":
            if ex(f): os.remove(f); print("deleted")
            else: print("no file found")
        else: print("error")

    elif a in ("calc","calculator"):
        a1=float(input("number1: "))
        op=input("symbol (+, -, *, /, //, %, **, sqrt): ").lower()
        if op == "sqrt":
            try:
                if a1 < 0:
                    raise ValueError
                print(math.sqrt(a1))
            except ValueError:
                print("invaild")
            continue
        a2=float(input("number2: "))
        if op not in ("+", "-", "*", "/", "**", "//", "%"):
            print("invaild")
            continue
        try:
            print(eval(f"{a1}{op}{a2}"))
        except (ArithmeticError, ValueError):
            print("invaild")

    else:
        print("invalid\n")
