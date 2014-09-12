import re
import subprocess
import os
import traceback

def refactor(file):
	s = open(file, 'r').read()

	reqs = re.findall("\[\s*([\'\"][\.\da-zA-Z\"\'\,\s_\/\!\$\(\)\]\[]+[\'\"])\s*\]", s, re.DOTALL)[0].split(",")
	
	varis = re.findall("function\s*\(([\da-zA-Z\"\'\,\s_\/\!\$\(\)\]\[]+)\)", s)[0].strip("'").split(",")
	
	codelines = []
	
	for i, r in enumerate(varis):
		codelines.append("        "+varis[i].strip() + " = require("+reqs[i].strip()+")")

	c0 = list(codelines[0])
	c0[4:7] = list("var")
	codelines[0] = "".join(c0)
	codelines[-1] = codelines[-1]+";\n"
	replacer = "function (require) {" + "\n" + ",\n".join(codelines)

	for j in range(i+1, len(reqs)):
		replacer += "    require("+reqs[j].strip()+");\n"
	
	match = re.findall(r"\[[\?\.\da-zA-Z\"\'\,\s_\/\!\$\(\)\]\[]+{", s, re.DOTALL)[0]
	code = s.replace(match, replacer)
	
	open(file, 'w').write(code)

def main():
	
	os.chdir(os.path.expanduser("~/workspace/rebelmouse/static/js"))
	
	files = subprocess.check_output("grep -lrF 'define([' ./|grep -v \"plugins\"|grep -v \"libs\"|grep -v \"utils\"", shell=True).split("\n")
	
	del files[-1]
	
	#files = ["./file.js"]
	
	for i, file in enumerate(files):
		try:
			refactor(file)
			#print("%d files, out of %d" % (i,len(files)))
		
		except Exception,e:
			#traceback.print_exc()
			print "Error in: "+file

main()



# Section for substitution