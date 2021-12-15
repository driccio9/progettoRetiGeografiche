import matplotlib.pyplot as plt

# line 1 points
x1 = ['2021-12-06','2021-12-07','2021-12-09']
y1 = [2, 4, 1]


# plotting the line 1 points
plt.plot(x1, y1, label="Sentimento 1")




# line 2 points
y2=[2,1,3]

# plotting the line 2 points
plt.plot(x1, y2, label="Sentimento 2")

# line 3 points
y3=[1,3,4]

# plotting the line 3 points
plt.plot(x1, y3, label="Sentimento 3")


# naming the x axis
plt.xlabel('Data')
# naming the y axis
plt.ylabel('Valutazione')
# giving a title to my graph
plt.title('Two lines on same graph!')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
