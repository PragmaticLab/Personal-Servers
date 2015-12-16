import os
import time
from splinter import Browser

class Printer:
	# def __init__(self, name="Brother_HL_L2300D_series"):
	def __init__(self, name="HLL2300D"):
		self.name = name

	def printer_print(self, directory="output.png", page_start=1, page_end=9999):
		sys_cmd = "lpr -P " + self.name + " -o sides=two-sided-long-edge -o page-ranges=" + str(page_start) + "-" + str(page_end) + " " + directory
		print sys_cmd
		os.system(sys_cmd)
		if page_end < 1000:
			time.sleep((page_end - page_start) * 2)
		else:
			time.sleep(10)
		print "done printing"

	def saveWebToFile(self, url, directory="output.png"):
		print "saving " + url + " to " + directory
		with Browser() as browser:
			browser.driver.set_window_size(1740, 800)
			browser.visit(url)
			time.sleep(4)
			ss = browser.screenshot()
			os.system("mv " + ss + " " + directory)
		print "done saving"

	def printUrl(self, url, directory="output.png", page_start=1, page_end=9999):
		self.saveWebToFile(url, directory)
		self.printer_print(directory, page_start, page_end)
