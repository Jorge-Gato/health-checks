#!/usr/bin/env python 3

import os
import sys

def check_reboot():
	"""Returns True if the computer has a pending reboot."""
	return os.path.exists("/run/reboot-required")

def main():
	if check_reboot():
		print("Pending Reboot.")
		sys.exit()

main()
