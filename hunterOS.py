import time, os, shutil, sys

P = {}  # passwords
R="\033[0m"; RD="\033[31m"; GR="\033[32m"
def col(t,c): return c+t+R
def ex(p): return os.path.exists(p)

# Boot
print("=== HUNTER OS ===",GR)
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
        print(col("bad pass",RD)); exit()

# Owner
print("owner? (yes/no)")
while True:
    own=input("> ").lower()
    if own in ("yes","no"): break
    print("bad input")
owner=u if own=="yes" else input("real owner: ")

# Drive
t,us,fr=shutil.disk_usage("C:/")
print(f"C: {t//(1024**3)}GB total, {us//(1024**3)}GB used, {fr//(1024**3)}GB free")
print("welcome",owner)

CMDS=["calc","osedit","mkfolder","rmdir","view","rename","ls",
      "tasks","clear","shutdown","passwd","help","size","reboot"]
print("cmds:",", ".join(CMDS))

# Main loop
while True:
    a=input("hunterOS> ").lower()

    if a=="reboot":
        print("rebooting..."); time.sleep(1)
        os.execl(sys.executable, sys.executable, *sys.argv)

    elif a=="help":
        print("cmds:"); [print(" ",c) for c in CMDS]

    elif a=="passwd":
        if own!="yes": print(col("owner only",RD)); continue
        if input("old: ")!=P[u]:
            print(col("bad",RD)); continue
        nw=input("new: ")
        if nw!=input("confirm: "):
            print(col("no match",RD)); continue
        P[u]=nw; print(col("changed",GR))

    elif a=="mkfolder":
        d=input("folder: ")
        try: os.mkdir(d); print("made")
        except Exception as e: print("err",e)

    elif a=="rmdir":
        d=input("folder: ")
        try: os.rmdir(d); print("deleted")
        except Exception as e: print("err",e)

    elif a=="clear":
        os.system("cls" if os.name=="nt" else "clear")

    elif a=="view":
        f=input("file: ")
        print(open(f).read() if ex(f) else "no file")

    elif a in ("ls","list"):
        [print(" -",i) for i in os.listdir()]

    elif a=="tasks":
        if own!="yes": print("owner only"); continue
        print("tasks:"); [print(" -",t) for t in CMDS]

    elif a=="shutdown":
        print("bye"); break

    elif a in ("rename","renamedir"):
        o=input("old: "); n=input("new: ")
        if ex(o): os.rename(o,n); print("renamed")
        else: print("no file")

    elif a=="size":
        f=input("file: ")
        if os.path.isfile(f):
            s=os.path.getsize(f); print(f"{s} bytes")
        else: print("no file")

    elif a in ("osedit","oseditor"):
        m=input("make/del: ").lower()
        f=input("file: ")
        if m=="make":
            open(f,"w").write(input("content: "))
            print("made")
        elif m=="del":
            if ex(f): os.remove(f); print("deleted")
            else: print("no file")
        else: print("bad")

    elif a in ("calc","calculator"):
        a1=float(input("a: "))
        op=input("op: ")
        a2=float(input("b: "))
        try: print(eval(f"{a1}{op}{a2}"))
        except: print("bad op")

    else:
        print("invalid\n")
