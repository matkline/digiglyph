from __future__ import print_function #Import advanced print functionality from Python 3

#Color Dictionary- palette based upon https://en.wikipedia.org/wiki/Help:Distinguishable_colors

#Input
file_to_open = raw_input("Enter input file name:")
output_file = raw_input("Enter output file name:")

file = open(file_to_open,"r") #Open input file with read permissions
export = open(str(output_file), "w") #Open output file with write permissions

original = file.read()

original = original.lower() #Convert input to lowercase

# Define Color Dictionary
cd = {      
	"a" : [240, 163, 255],
	"b" : [0, 117, 220],
	"c" : [153, 63, 0],
	"d" : [76,0,92],
	"e" : [255,255, 255],
	"f" : [0, 92, 49],
	"g" : [43,206,72],
	"h" : [255, 204, 153],
	"i" : [128,128,128],
	"j" : [148,255,181],
	"k" : [143,124,0],
	"l" : [157,204,0],
	"m" : [194, 0, 136],
	"n" : [0,51,128],
	"o" : [255,164,5],
	"p" : [255,168,187],
	"q" : [66,102,0],
	"r" : [255,0,16],
	"s" : [94,241,242],
	"t" : [0,153,143],
	"u" : [224,255,102],
	"v" : [116,10,255],
	"w" : [153,0,0],
	"x" : [255,255,128],
	"y" : [255,255,0],
	"z" : [255,80,5]
	}

errorcolor = "0 0 0" #All characters not in the dictionary output to Black Pixels (RGB (0,0,0))

def trans(x):
	for i in x:
		try:
			print(*cd[i], sep=' ', end = ' ', file=export)
		 #If the character isn't found in the dictionary, a black pixel is printed
		except KeyError:
			print(errorcolor, file=export)
			

# PPM File Specificationb
fileformat = "P3"
colorrange = 255
columns = 1


#Output
print(fileformat, file=export) #PPM File Specification
if len(original) <= 96: #This is equivalent to 32 pixels (3 rgb values * 32)
	print(len(original), end= ' ', file=export),
	print(columns, file=export)
	print(colorrange, file=export)

else:
	print("Error")
	

trans(original)
