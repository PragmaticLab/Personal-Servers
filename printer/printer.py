import os
import time
import pdfkit

class Printer:
	# def __init__(self, name="Brother_HL_L2300D_series"):
	def __init__(self, name="HLL2300D"):
		self.name = name

	def printer_print(self, directory="output.pdf", page_start=1, page_end=9999):
		sys_cmd = "lpr -P " + self.name + " -o sides=two-sided-long-edge -o page-ranges=" + str(page_start) + "-" + str(page_end) + " " + directory
		print sys_cmd
		os.system(sys_cmd)
		if page_end < 1000:
			time.sleep((page_end - page_start) * 2)
		else:
			time.sleep(10)
		print "done printing"

	def saveWebToFile(self, url, directory="output.pdf"):
		print "saving " + url + " to " + directory
		if "." in url[-4:-1]:
			os.system("wget " + url + " -O " + directory)
			time.sleep(4)
		else:
			pdfkit.from_url(url, directory)
		print "done saving"

	def printUrl(self, url, directory, page_start=1, page_end=9999):
		self.saveWebToFile(url, directory)
		self.printer_print(directory, page_start, page_end)
