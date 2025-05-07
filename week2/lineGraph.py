import matplotlib.pyplot as mpl 
x1=[1,4,6,8]
y1=[2,5,8,9]
mpl.plot(x1,y1,label="line A",color="r") 
x2=[3,6,8,10]
y2=[2,4,8,9]
mpl.plot(x2,y2,label="line B",color="g")
mpl.xlim(0,12)
mpl.ylim(0,12)
mpl.xlabel("X-axis") 
mpl.ylabel("Y-axis") 
mpl.title("Graph")
mpl.legend()
mpl.show() 