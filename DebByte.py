import os
import sys
os.system("clear")
bun = """   

██████╗ ███████╗██████╗ ██████╗ ██╗   ██╗████████╗███████╗       
██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝       
██║  ██║█████╗  ██████╔╝██████╔╝ ╚████╔╝    ██║   █████╗         
██║  ██║██╔══╝  ██╔══██╗██╔══██╗  ╚██╔╝     ██║   ██╔══╝         
██████╔╝███████╗██████╔╝██████╔╝   ██║      ██║   ███████╗       
╚═════╝ ╚══════╝╚═════╝ ╚═════╝    ╚═╝      ╚═╝   ╚══════╝      

-by 0xSilver 

1) kali 
2) Parrot OS 
3) debain 
4) Flatpak + Flathub (BurpSuite, Cutter, Wireshark)
5) Visual Studio Code
6) Metasploit Framework from Rapid7


"""

# Check root permission
def is_root():
    return os.geteuid() == 0

if not is_root():
    print(" You must run this script as root.")
    sys.exit(1)

#-------------------------------
def ins_kali():
    os.system('echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" | tee /etc/apt/sources.list.d/kali.list > /dev/null')
    os.system('wget -q -O - https://archive.kali.org/archive-key.asc | gpg --dearmor | tee /etc/apt/trusted.gpg.d/kali.gpg > /dev/null')
    os.system('apt update')
    print("Done ...!")

def rem_kali (): 
    os.system('rm -f /etc/apt/sources.list.d/kali.list')
    os.system('rm -f /etc/apt/trusted.gpg.d/kali.gpg')
    os.system('apt update')
    print("Done ...!")

#-------------------------------
def ins_porrot():
    os.system('echo "deb http://deb.parrot.sh/parrot rolling main contrib non-free" > /etc/apt/sources.list.d/parrot.list')
    os.system('wget -qO - https://deb.parrot.sh/parrot/mirrors/parrot.gpg | gpg --dearmor > /etc/apt/trusted.gpg.d/parrot.gpg')
    os.system('apt update')
    print("Done ...!")

def rem_porrot():
    os.system('rm -f /etc/apt/sources.list.d/parrot.list')
    os.system('rm -f /etc/apt/trusted.gpg.d/parrot.gpg')
    os.system('apt update')
    print("Done ...!")

#-------------------------------
def ins_debian():
    os.system('echo "deb http://deb.debian.org/debian bookworm-backports main contrib non-free non-free-firmware" > /etc/apt/sources.list.d/backports.list')
    os.system('apt update')
    print("Done ...!")

def rem_debian():
    os.system('rm -f /etc/apt/sources.list.d/backports.list')
    os.system('apt update')
    print("Done ...!")

#-------------------------------
def ins_flatpak():
    os.system('apt install flatpak gnome-software-plugin-flatpak -y')
    os.system('flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo')
    print("Done ...!")

def rem_flatpak():
    os.system('flatpak remote-delete flathub')
    os.system('apt remove --purge flatpak gnome-software-plugin-flatpak -y')
    print("Done ...!")

#-------------------------------
def ins_vscode():
    os.system('wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg')
    os.system('echo "deb [arch=amd64] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list')
    os.system('apt update')
    os.system('apt install code -y')
    print("Done ...!")

def rem_vscode():
    os.system('rm -f /etc/apt/sources.list.d/vscode.list')
    os.system('rm -f /etc/apt/trusted.gpg.d/microsoft.gpg')
    os.system('apt update')
    os.system('apt remove --purge code -y')
    print("Done ...!")

#-------------------------------
def ins_metasploit():
    os.system('sudo apt-get install curl')
    os.system('curl https://raw.githubusercontent.com/rapid7/metasploit-framework/master/msfupdate | bash')
    print("Done ...!")

def rem_metasploit():
    os.system('apt remove --purge metasploit-framework -y')
    os.system('apt autoremove -y')
    print("Done ...!")

#-------------------------------
def main():
    print(bun)
    choice = input("Choose repo number to install/remove (e.g., 1): ").strip()
    action = input("Install (i) or Remove (r)? ").strip().lower()

    if action not in ["i", "r"]:
        print("Invalid action. Please enter 'i' for install or 'r' for remove.")
        sys.exit(1)

    if choice == "1":
        if action == "i":
            ins_kali()
        else:
            rem_kali()
    elif choice == "2":
        if action == "i":
            ins_porrot()
        else:
            rem_porrot()
    elif choice == "3":
        if action == "i":
            ins_debian()
        else:
            rem_debian()
    elif choice == "4":
        if action == "i":
            ins_flatpak()
        else:
            rem_flatpak()
    elif choice == "5":
        if action == "i":
            ins_vscode()
        else:
            rem_vscode()
    elif choice == "6":
        if action == "i":
            ins_metasploit()
        else:
            rem_metasploit()
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
