#!/usr/bin/env python3
from colorama import Fore, Back, Style
import pyqrcode
import sys

print(Fore.GREEN + "This script will take a private Dropbox URL (https://dropbox.com/foo)",
      "and convert it to a sharable URL.\nIt will also create a QR code if you",
      "so wish.\n" + Style.RESET_ALL)

dropbox_priv = input(Fore.BLUE + "Please paste the dropbox URL:\n" +
                    Style.RESET_ALL)
if 'https://www.dropbox.com' not in dropbox_priv:
    print("Not a valid dropbox URL")
    sys.exit(1)

dropbox_shared = dropbox_priv.replace('https://www.dropbox.com','https://dl.dropboxusercontent.com')
print(Fore.GREEN + "\nSharable URL:\n" + dropbox_shared + Style.RESET_ALL)

filename = dropbox_shared.split('/')[-1].split('#')[0].split('?')[0].split('.')[0]

qr_confirm = input(Fore.RED + "\nWould you like to create a QR code? [Y/N]  " +
                   Style.RESET_ALL)

if "Y" in qr_confirm:
    pngname = filename + "-QR.png"
    print(Fore.GREEN + "Creating " + pngname + ".")
    url = pyqrcode.create(dropbox_shared)
    url.png(pngname, scale=3, module_color = [0, 0, 0, 128],background=[0xff,0xff,0xff])
    print(pngname + " created." + Style.RESET_ALL)
else:
    print(Fore.RED + "QR code not created. Script exiting...")
