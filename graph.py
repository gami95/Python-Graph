import matplotlib.pyplot as py 

'''x=[1,2,3]
y=[1,4,9]
py.figure(1)
py.plot(x,y)

py.xlabel("x-axis")
py.ylabel("y-axis")

py.title("first graph")
py.show()
py.close()
'''
#language=["java","C","C++","Ruby","Python"]
'''lang={
	"java":"15",
	"C":"10",
	"C++":5,
	"Python":"25"
	}
ages=[2,3,10,8,63,15,20,25,62,9,3,3,3]
range=(0,100)
bins=10
py.figure(2)
py.hist(lang,bins,range,color="green",histtype="bar",rwidth=0.8)

py.xlabel("language")
py.ylabel("No_of_Employee")
py.title("HR data")
py.plot()
py.show()
py.close()
'''
Language_no=[1,2,3,4]
Language=["java","C","C++","Python"]

ar=[10,5,2,25]

py.bar(Language_no,ar,align='center')
py.xticks(Language_no,Language)
py.xlabel("Language")
py.ylabel("No_of_Employee")
py.plot()
py.show()
py.close()	
