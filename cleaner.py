import re
import subprocess
import os
import traceback

def refactor(file):
	#print "Refactoring: " + file
	s = open(file, 'r').read()

	reqs = re.findall("\[\s*([\'\"].+[\'\"])\s*\]", s, re.DOTALL)[0].split(",")
	#print reqs
	#print(len(reqs))

	varis = re.findall("function\s*\(([\da-zA-Z\"\'\,\s_\/\!\$\(\)\]\[]+)\)", s)[0].strip("'").split(",")
	#print(len(varis))

	codelines = []

	for i, r in enumerate(varis):
		codelines.append("        "+varis[i].strip() + " = require("+reqs[i].strip()+")")

	for j in range(i+1, len(reqs)):
		codelines.append("        require("+reqs[j].strip()+")")

	#codelines[4,5,6] should be made var
	c0 = list(codelines[0])
	c0[4:7] = list("var")
	codelines[0] = "".join(c0)
	codelines[-1] = codelines[-1]+";\n"

	replacer = "function (require) {" + "\n" + ",\n".join(codelines)

	match = re.findall(r"\[[\?\.\da-zA-Z\"\'\,\s_\/\!\$\(\)\]\[]+{", s, re.DOTALL)[0]
	code = s.replace(match, replacer)
	#print code
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
		  
	#refactor("file.js")

main()



# Section for substitution