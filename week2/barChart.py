import matplotlib.pyplot as mpl 
x=[1,2,3,4,5]
y=[50,65,85,87,98]
text=["IBM","Amazon","Facebook","Microsoft","Google"]
colors=["red","orange","yellow","blue","green"]
mpl.xlim(0,6) 
mpl.ylim(0,100)
mpl.bar(x,y,tick_label=text,color=colors,linewidth=0.5) 
mpl.xlabel("Company")
mpl.ylabel("Percentage") 
mpl.title("Percentage Graph") 
mpl.show()