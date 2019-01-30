##packages: spc
library(readr)
library(kableExtra)
belgium <- read.csv("C:/Users/zafiirah/Desktop/AC level 3/FYP/public_cases.csv") 

#function to convert data about specific disease in sts class
#A surveillance time series {yit;t = 1, . . . , n, i = 1, . . . , m} is
#represented using objects of class sts (surveillance time series)
#The sts S4 class has the following form
# setClass( "sts", representation(epoch = "numeric",
#                                 freq = "numeric",
#                                 start = "numeric",
#                                 observed = "matrix",
#                                 state = "matrix",
#                                 alarm = "matrix",
#                                 upperbound = "matrix",
#                                 neighbourhood= "matrix",
#                                 populationFrac= "matrix",
#                                 map = "SpatialPolygonsDataFrame",
#                                 control = "list",
#                                 epochAsDate="logical",
#                                 multinomialTS="logical"))

belgium_sts <- function(disease, data){
  
  # filter the chosen disease
  disease_data <- dplyr::filter_(data, paste0("Subject == \"",disease,"\""))
  
  # aggregated cases by week to get the weekly number of cases
  observed <- dplyr::group_by(disease_data, DateMonday)
  observed <- dplyr::summarize(observed, n_cases = n())
  
  # create the sts object  min(lubridate::year(observed$DateMonday))
  disease_sts <- surveillance::sts(observed = observed$n_cases, # weekly number of cases
                                   ##observed A n × m matrix of counts representing yit
                                   start = c(2011, 01), # first week of the time series
                                   ##start A vector of length two containing the origin of the time
                                   ##series as c(year, week).
                                   frequency = 52, # weekly data
                                   ##freq A numeric specifying the period of the time series, i.e. 52 for
                                   ##weekly data, 12 for monthly data, etc.
                                   epochAsDate = FALSE,# we do have dates, not only index
                                   ##epochAsDate Boolean, if TRUE then the epoch vector is interpreted as a
                                   ##vector of class Date, i.e. dates in ISO 8601 date standard
                                   epoch = as.numeric(observed$DateMonday) # here are the dates 
  )
  
  disease_sts
}


library(surveillance)
######################################EARSC1--working############################################
#Function ears takes an sts and a control object as arguments
salmonella <- belgium_sts(disease = "SALM", data = belgium)
#plot(salmonella)
monitored_salmonellac1 <- earsC(salmonella,control = list(method = "C1",
                                                          alpha = 0.01,
                                                          baseline = 20))
plot(monitored_salmonellac1)
######################################EARSC2--working############################################
#Function ears takes an sts and a control object as arguments
salmonella <- belgium_sts(disease = "SALM", data = belgium)
#plot(salmonella)
monitored_salmonellac2 <- earsC(salmonella,control = list(method = "C2",
                                                          alpha = 0.01,
                                                          baseline = 20))
plot(monitored_salmonellac2)
######################################EARSC3--working############################################
#Function ears takes an sts and a control object as arguments
salmonella <- belgium_sts(disease = "SALM", data = belgium)
#plot(salmonella)
monitored_salmonellac3 <- earsC(salmonella,control = list(method = "C3",
                                                          alpha = 0.01,
                                                          baseline = 20))
plot(monitored_salmonellac3)
#############################FARRINGTON###############################################
#Function farrington takes an sts and a control object as arguments
#b Number of years to go back in time
#w Window size
#range Specifies the index of all timepoints in sts to monitor.
#alpha An approximate two-sided (1 − α)% prediction interval is calculated

control <- list(b = 25, w = 5, range = 64:417, alpha = 0.01)
monitored_salmonellafarrington <- farrington(salmonella, control = control)
plot(monitored_salmonellafarrington)

monitored_salmonella_df2 <- as.data.frame(monitored_salmonella2)
#knitr::kable(monitored_salmonella_df2)


#############################GLRNB--not working####################################################
#phase1 <- which((epoch(salmonella)) <= "2011-01-01")
#phase2 <- which((epoch(salmonella)) > "2011-01-01")
#control = list(range = phase2, c.ARL = 4, theta = log(2), ret = "cases",
#                  mu0 = list(S = 1, trend = TRUE, refit = FALSE))
#monitored_salmonella3 <- glrnb(salmonella, control = control)
#plot(monitored_salmonella3)


#############################CUSUM--not working####################################################
#kh <- find.kh(ARLa = 500, ARLr = 7)
#ha.cusum <- algo.cusum(aggregate(salmonella), control = list(k = kh$k,
#                      h = kh$h, m = "glm", trans = "rossi", range = 209:290))


###############################BAYES--not working#################################################
#ctrl <- list(range = 209:290, b = 2, w = 6, alpha = 0.005)
#hab62 <- algo.bayes(salmonella, control = ctrl)
