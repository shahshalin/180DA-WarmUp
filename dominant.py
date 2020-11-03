"""
The way that I changed this code up to make it my own and to fit the requirements of the project spec was by modifying the original code to function in a loop (as seen in the while(1) block of code) and making it so that the user sees their video constantly (and a rectangle in the middle corresponding to where the object they want to see the histogram for should be located) until they press the "t" button on their keyboard at which time the histogram will pop up and that histogram can be interacted with as a plt object.

Most of the inspiration and code for the two defined functions come from https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097. 
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

cap = cv2.VideoCapture(0)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
blue = (255, 0, 0) 

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar


h_lower = int(h/4)
h_upper = int(3*h/4)
w_lower = int(w/4) 
w_upper = int(3*w/4)
while(1): 
    _, frame = cap.read()
    mod_frame = frame[h_lower:h_upper,w_lower:w_upper]
    frame = cv2.rectangle(frame,(w_lower,h_upper),(w_upper,h_lower), blue, 2)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) == ord('t'):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = frame.reshape((frame.shape[0] * frame.shape[1],3)) #represent as row*column,channel number
        # print(frame.shape)
        clt = KMeans(n_clusters=3) #cluster number
        clt.fit(frame)

        hist = find_histogram(clt)
        bar = plot_colors2(hist, clt.cluster_centers_)
        plt.axis("off")
        plt.imshow(bar)
        plt.waitforbuttonpress()
        plt.show()
