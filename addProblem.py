import sys
import os

def hello(a,b):
    print("hello and that's your sum:", a + b)

def createFile(filename):
	f = open(filename,"w+")
	f.close()

def createDir(dir):
	if not os.path.exists(dir):
		os.makedirs(dir)

def createProblem(args, verbose = False):
	args = [s.lower() for s in args]
	args = [s.title() for s in args]
	dirname = args[0]+'.'+'_'.join(args[1:])
	
	if verbose:
		print('creating directory: ' + dirname)
	createDir(dirname)
	solutionFileName = dirname + '/solution.py'
	if verbose:
		print('creating file: ' + solutionFileName)
	createFile(solutionFileName)

if __name__ == "__main__":
	allArgs = sys.argv[1:]
	createProblem(allArgs, verbose = True)