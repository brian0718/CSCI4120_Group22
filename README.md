# CSCI4120_Group22

Brian Manning - manningb96@students.ecu.edu
Isiah Turner - turnerisi99@students.ecu.edu

There should not be any requirements other than to open the jupyter notebook and run it.  The iris.data file is included in the repo.  
If you want to run the plot numerous times, you need to clear the kernel or the graph will start shifting to the right.  
I didn't spend a lot of effort trying to fix that since technically I could have just turned in a .py file that runs the whole thing in one shot.

K seemed to stablaize around 10.  When averaging only 5 runs it seemed instable and sometimes the optimal K would vary.  
We tested many higher subruns at 100, 150, 200 and 250 and K seemed to stabalize around 10 at 96%-97% accuracy (sometimes 9 and 11).  
However there did not seem to be much variation between differnt values of K, until K was chosen much higher than 20.  
Around 30 you see a noticable drop in accuracy. We believe that is because at 30 you start having too 
much influence from other classifications in the dataset.
