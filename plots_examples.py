
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import random

plt.style.use('ggplot')
plt.rcParams.update({'font.size': 16})


#####################################################################
#################           BASIC PLOTS 

#A np.array() of the stuff to plot
#This example just makes a random list to use as data points
lst_data_points_to_plot = random.sample(range(10, 900), 55) #pick 55 random numbers that fall between 10 and 899
print(lst_data_points_to_plot) #the points you are going to plot


size_of_x_axis = len(lst_data_points_to_plot) #same as total_flips
x_axis_arr = lst_data_points_to_plot #np.zeros(size_of_x_axis)
plot_pixel_height = 12  #how tall the plot is on the screen
plot_pixel_width = 5 #how wide the plot is on the screen
y_axis_min = (min(lst_data_points_to_plot) - .1) #make a little buffer space on the bottom of the y axis
y_axis_max = (max(lst_data_points_to_plot) + .1) #make a little buffer space on the top of the y axis
def plot_pfair_prob(size_of_x_axis, lst_data_points_to_plot):
    fig, ax = plt.subplots(figsize=(plot_pixel_height,plot_pixel_width))
    len_of_x_axis = np.arange(1, size_of_x_axis + 1) #makes sure x axis values are not smooshed
    ax.plot(len_of_x_axis, lst_data_points_to_plot) 
    ax.set_ylim([y_axis_min, y_axis_max]) #sets the range of the y axis
    ax.set_title('Basic Plot')
    ax.set_ylabel('Y Axis Label')
    ax.set_xlabel('X_Axis_Label');
    plt.show()
plot_pfair_prob(size_of_x_axis, lst_data_points_to_plot)




#####################################################################
#################           PLOT WITH LOTS OF PLOTTED LINES



 
#this graph plots the pdf of the binomial distribution
#

fig, ax = plt.subplots(figsize=(10,5))
x = np.linspace(0,1,1000)
for (a,b,s) in [(2,2,"p-"), (1,1,"o-"), (15,1,"b"), 
                (50,20,"r--"), (100,200,"g--")]:
        ax.plot(x,
                stats.beta(a,b).pdf(x),
                s,
                label="({0},{1})".format(a,b))
ax.legend(title=r"($\alpha,\beta$)", loc="upper left")
ax.set_xlabel("p")
ax.set_ylabel("pdf");