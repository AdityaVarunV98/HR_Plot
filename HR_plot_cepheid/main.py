import matplotlib.pyplot as plt
import numpy as np


def BVal(row):
    ''' 
    Gets the B-V value from the row of data corresponding to a star

    Args:
        row (array_like): Sequence of data corresponding to the attributes of a star
    
    Returns:
        float: Returns the B-V value (Color Index), which is the last element of the row of data
    '''
    return row[-1]


def AbsMag(row):
    ''' 
    Gets the Absolute Magnitude value from the row of data corresponding to a star

    Args:
        row (array_like): Sequence of data corresponding to the attributes of a star
    
    Returns:
        float: Returns the Absolute Magnitude of a star, using the formula:
                        
                    M = Vmag + 5*log(Plx/100)
                    
            Where,
                    Vmag -> Johnson Magnitude (Apparent magnitude in the visual part of EM spectrum)
                    Plx  -> Parallax in milliarcsec  
    '''
    return row[1]+5*np.log10(row[4]/100)


# Loading the data of the stars (from whatsapp group), removing the rows with incomplete data
data = np.genfromtxt(r'HR_plot_cepheid\HR_data.txt', skip_header=1, invalid_raise=False, missing_values = "", filling_values=np.nan)

# Using the vectorize method of numpy to obtain the B-V and Absolute Magnitude values from each row, and storing in a numpy array
BValvec = np.vectorize(BVal, signature='(n)->()')
x_cor = BValvec(data)
AbsMagvec = np.vectorize(AbsMag, signature='(n)->()')
y_cor = AbsMagvec(data)

# Initializing fig, ax
fig, ax = plt.subplots(figsize=(8,10))

# Defining the plot limits
ax.set_xlim(-1, 3)
ax.set_ylim(10, -4)

# Defining the title, axes labels, and formatting them
ax.set_title('H-R Diagram')
ax.title.set_color('#8AB9B5')
ax.title.set_fontsize(30)
ax.set_xlabel('Color index (B-V)')
ax.xaxis.label.set_fontsize(20)
ax.xaxis.label.set_color('#8AB9B5')
ax.set_ylabel('Absolute magnitude')
ax.yaxis.label.set_fontsize(20)
ax.yaxis.label.set_color('#8AB9B5')

# Defining the background color
ax.set_facecolor('black')
fig.patch.set_facecolor('black')

# Defining the colors of the axes and parameter labels
ax.spines['bottom'].set_color('#C8C2AE')
ax.spines['left'].set_color('#C8C2AE')
ax.tick_params(axis='x', labelcolor='#C8C2AE')
ax.tick_params(axis='y', labelcolor='#C8C2AE')

# Plotting the points on the graph
ax.scatter(x_cor, y_cor, s=1.5, edgecolors='none', c='#34E4EA')

# Displaying the graph
plt.show()