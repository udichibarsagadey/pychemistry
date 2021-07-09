import matplotlib.pyplot as plt

days = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [33.3,36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
plt.plot(days, temperature , color = "Aqua" , marker = "o", linestyle = "dashdot",linewidth =  3, markersize = 9 )
plt.title('Temperature')
plt.xlabel('days')
plt.ylabel('temperature')
plt.show()


