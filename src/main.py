#######################################################################################################
#  ____   _____   ______________  _______   _        ___   _     _ ___  _____   ____     ___________ #
# |  __ \|  __ \ / |__   _/  __ \|__   _/  | \      / _ \ | \   | | _ \/  __ \ |  __|   /  __|_   _/ #
# | |  \ \ |  \ |  / \| | | |  \ \  | |    |  \    / / \ \|  \  | |/ \ \ /  \_\| |\    /  | \  | |   #
# | |__/ / |__/ | |   | | | |_  |_| | |    | \ \  / /___\ \ \ \ | |   | |  ____| |_\  / / |_ \ | |   #
# |  ___/|  _  /| |   | | |  _|  _  | |    | |\ \/ /______ \ \ \| |___| | |___ |  _|\/ /|  _| \| |   #
# | |    | | \ \| |_  | | | |   | | | |    | | \/ / | |   \ \ \ \ |___  |    | | | \__/ | |  \ \ |   #
# | |    | |  \ | \ \_/ / | |__/ /  | |    | | / /  | |   |\ \ \  |   | |___/ /| |__    | |__ \  |   #
# |_|    |_|   \_\_\___/  \_____/   |_|    |_|/_/   |_|   |_\_\ \_|   |_|____/ |____|   |____| \_|   #
#                                                                                                    #
#######################################################################################################
# Author: DAAV, LLC (https://github.com/daavofficial)
# Language: Python 3.10
# License: GPLv3
## Project-Management
# Easy to use graphical application for managing projects
##########################################################
# Project Lead: Anonoei (https://github.com/Anonoei)

import argparse
import datetime

import interface
import config.config as config

def main():
    parser = argparse.ArgumentParser(add_help=True, description="Easy to use graphical application for managing projects")
    parser.add_argument("-UI", help="specify user interface to use", choices=['CUI', 'GUI'])
    parser.add_argument("-t", "--testing", help="use testing paths", action="store_true")
    print("  ____   _____   ______________  _______   _        ___   _     _ ___  _____   ____     ___________ ")
    print(" |  __ \|  __ \ / |__   _/  __ \|__   _/  | \      / _ \ | \   | | _ \/  __ \ |  __|   /  __|_   _/ ")
    print(" | |  \ \ |  \ |  / \| | | |  \ \  | |    |  \    / / \ \|  \  | |/ \ \ /  \_\| |\    /  | \  | |   ")
    print(" | |__/ / |__/ | |   | | | |_  |_| | |    | \ \  / /___\ \ \ \ | |   | |  ____| |_\  / / |_ \ | |   ")
    print(" |  ___/|  _  /| |   | | |  _|  _  | |    | |\ \/ /______ \ \ \| |___| | |___ |  _|\/ /|  _| \| |   ")
    print(" | |    | | \ \| |_  | | | |   | | | |    | | \/ / | |   \ \ \ \ |___  |    | | | \__/ | |  \ \ |   ")
    print(" | |    | |  \ | \ \_/ / | |__/ /  | |    | | / /  | |   |\ \ \  |   | |___/ /| |__    | |__ \  |   ")
    print(" |_|    |_|   \_\_\___/  \_____/   |_|    |_|/_/   |_|   |_\_\ \_|   |_|____/ |____|   |____| \_|   ")
    print(f" {config.VERSION}, made by 'DAAV, LLC' developers.\n")
    args = parser.parse_args()
    if args.testing:
        print("Using testing paths")
        config.PATH_ROOT = config.TESTING_PATH_ROOT

    if args.UI == "CUI":
        LaunchCUI(args)
    elif args.UI == "GUI":
        LaunchGUI(args)
    else:
        LaunchMenu(args)
    exit()

def LaunchCUI(args):
    args.UI = interface.Type.CUI
    LaunchUI(args)

def LaunchGUI(args):
    args.UI = interface.Type.GUI
    LaunchUI(args)

def LaunchUI(args):
    ui = interface.UI(args)
    ui.Start()

def LaunchMenu(args):
    print("\tNote: UI is still developmental")
    print("\tPlease specify which interface you want to use:")
    print("\t    1) CUI       2) GUI")
    UsrInput = ""
    while True:
        UsrInput = input("\tSelect an option > ")
        try:
            UsrInput = int(UsrInput)
            if UsrInput == 1:
                LaunchCUI(args)
                break
            elif UsrInput == 2:
                LaunchGUI(args)
                break
            else:
                print(" ERR: Invalid option")
                continue
        except ValueError:
            UsrInput = UsrInput.lower()
            if "exit" in UsrInput:
                print("Goodbye!")
                exit()
            elif "reload" in UsrInput:
                print("Reloading...")
                exit(-1)
            elif 'cui' in UsrInput:
                LaunchCUI(args)
                break
            elif 'gui' in UsrInput:
                LaunchGUI(args)
                break
            elif 'help' in UsrInput:
                print("\tCommands:")
                print("\t  help\n\t\tshow this menu")
                print("\t  1 | cui\n\t\tlaunch cui")
                print("\t  2 | gui\n\t\tlaunch gui")
                print("\t  reload\n\t\treload Project-Management")
            else:
                print(" ERR: Invalid option, type 'help' to view commands")
                continue
        except KeyboardInterrupt:
            print("Goodbye!")
            exit()


def old_code():
    config.PATH_CURRENT_PROJECT = config.PATH_ROOT + "/Name"

    ctb = Contribution()
    ctb.SetName("Initial commit")
    ctb.SetDate(datetime.datetime.now().date())
    ctb.SetNumber("001")
    ctb.SetDescription("Initial commit")
    ctb.SetLead("Anonoei")
    ctb.SetVersionChange(Version("0.0.1"))
    ctb.UpdateProgress(10.0, datetime.datetime.now().date())

    ctb.Push("Anonoei", 1.5, datetime.datetime.now().date(), "Updated README")

    print(repr(ctb))
    print("-----------------------------------")

    ctb.Export(config.PATH_CURRENT_PROJECT + "/Contributions")

    ctb = Contribution()
    ctb.Import(config.PATH_CURRENT_PROJECT + "/Contributions", "001. Initial commit")
    print(repr(ctb))

if __name__ == '__main__':
    main()
