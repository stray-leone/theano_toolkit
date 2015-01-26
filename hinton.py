# coding=utf-8
import numpy as np
chars = [ " ","▁","▂","▃","▄","▅","▆","▇" ,"█" ]

class BarHack(str):
	def __str__(self):
		return self.internal
	def __len__(self):
		return 1

#bh = BarHack()

def plot(arr,max_arr=None):
    def visual(val,max_val):
            if abs(val) == max_val:
                    step = len(chars)-1
            else:
                    step = int(abs(float(val)/max_val)*len(chars))
            colourstart = ""
            colourend   = ""
            if val < 0: colourstart,colourend = '\033[90m','\033[0m'
            #bh.internal = colourstart + chars[step] + colourend
            return colourstart + chars[step] + colourend

    if max_arr == None: max_arr = arr
    max_val = max(abs(np.max(max_arr)),abs(np.min(max_arr)))
    print np.array2string(arr,
            formatter={'float_kind': lambda x: visual(x,max_val)},
            max_line_width = 5000
    )


if __name__ == "__main__":
	a = np.random.randn(10,10)
	print a
        plot(a)
	#print_arr(a)
