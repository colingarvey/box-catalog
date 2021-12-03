#!/usr/bin/env python3
import sys

print("This script will take a private Dropbox URL (https://dropbox.com/foo)",
      "and convert it to a sharable URL.\nIt will also create a QR code if you",
      "so wish.\n")

dropbox_priv = input("Please paste the dropbox URL:\n")
if 'https://www.dropbox.com' not in dropbox_priv:
    print("Not a valid dropbox URL")
    sys.exit(1)

dropbox_shared = dropbox_priv.replace('https://www.dropbox.com','https://dl.dropboxusercontent.com')
print("\nSharable URL:\n" + dropbox_shared)

filename = dropbox_shared.split('/')[-1].split('#')[0].split('?')[0].split('.')[0]
