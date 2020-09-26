# CSCI4120_Group22

Brian Manning - manningb96@students.ecu.edu
Isiah Turner - turnerisi99@students.ecu.edu

There should be no dependencies necessary other than this code was written using python 3.7.6.  

We ran the code initially with the Elbow configuration iterations from 1-10.  In this case, it chooses the wrong
K value of 3.  When running the best K value of 3, the visualizer and confusion matrix can be seen here:

## Kelbow interval 1-10
![Image of K3]
(https://github.com/brian0718/CSCI4120_Group22/tree/master/HW_elbow_kmeans/KElbow3.png)
![Image of ConfusionMatrix K3]
(https://github.com/brian0718/CSCI4120_Group22/tree/master/HW_elbow_kmeans/ConfusionMatrixK3.png)

## Accuracy Score = 75%

Then we changed the parameters of the visualizer to the interval K=(2-10).  In this case it chose the correct K=4.  The visualizer and confusion matrix can be seen here


![Image of K4]
(https://github.com/brian0718/CSCI4120_Group22/tree/master/HW_elbow_kmeans/KElbow4.png)
![Image of ConfusionMatrix K4]
(https://github.com/brian0718/CSCI4120_Group22/tree/master/HW_elbow_kmeans/ConfusionMatrixK4.png)

## Accuracy Score = 100%


The Code is currently configured to run the interval for KElbowVisualizer from 1-10.  

## Clearly the best K=4
