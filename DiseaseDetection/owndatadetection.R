diseases <- readr::read_csv("C:/Users/zafiirah/Desktop/AC level 3/FYP/allData.csv")
print(knitr::kable(head(belgium)))

diseases_sts <- function(disease, data){
  
  # filter the chosen disease
  disease_data <- dplyr::filter_(data, paste0("Subject == \"",disease,"\""))
  
  # aggregated cases by week to get the weekly number of cases
  observed <- dplyr::group_by(disease_data, DateMonday)
  observed <- dplyr::summarize(observed, n_cases = n())
  
  # create the sts object
  specific_disease_sts <- surveillance::sts(observed = observed$n_cases, # weekly number of cases
                                   start = c(min(lubridate::year(observed$DateMonday)), 01), # first week of the time series
                                   frequency = 52, # weekly data
                                   epochAsDate = TRUE, # we do have dates, not only index
                                   epoch = as.numeric(observed$DateMonday) # here are the dates
  )
  
  specific_disease_sts
}

library(surveillance)
influenza <- diseases_sts(disease = "influenza", data = diseases)
plot(influenza)
print(epoch(salmonella))

######################################EARSC1--working############################################
monitored_salmonella_C1 <- earsC(influenza,
                                  control = list(
                                                 method = "C1",
                                                 alpha = 0.001,
                                                 baseline = 3))
plot(monitored_salmonella_C1)
######################################EARSC2--working############################################

monitored_salmonella_C2 <- earsC(influenza,
                              control = list(
                                method = "C2",
                                alpha = 0.001,
                                baseline = 3))
plot(monitored_salmonella_C2)

######################################EARSC3--working############################################
monitored_salmonella_C3 <- earsC(influenza,
                               control = list(
                                 method = "C3",
                                 alpha = 0.05,
                                 baseline = 3))
plot(monitored_salmonella_C3)
######################################FARRINGTON-- not working########################################
#Function farrington takes an sts and a control object as arguments
#b Number of years to go back in time
#w Window size
#range Specifies the index of all timepoints in sts to monitor.
#alpha An approximate two-sided (1 − α)% prediction interval is calculated

control <- list(b = 2, w = 5, range = 2:19, alpha = 0.01)
monitored_salmonellafarrington <- farrington(influenza, control = control)
plot(monitored_salmonellafarrington)

#monitored_salmonella_df2 <- as.data.frame(monitored_salmonella2)
#knitr::kable(monitored_salmonella_df2)
