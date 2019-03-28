#import subprocess
#subprocess.call("C:/Users/zafiirah/PycharmProjects/Rprogramming/detection_disease.R", shell=True)
import rpy2.robjects as robjects
r_source = robjects.r['source']
r_source("C:/Users/zafiirah/PycharmProjects/Rprogramming/disease_detection.R")
print ('r script finished running')
