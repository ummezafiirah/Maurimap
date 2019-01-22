# Title     : TODO
# Objective : TODO
# Created by: zafiirah
# Created on: 1/17/2019
#print(.libPaths())
library(readr)
library(kableExtra)
belgium <- read.csv("C:/Users/zafiirah/Desktop/AC level 3/FYP/public_cases.csv")
#print(belgium)
knitr::kable(head(belgium))
#print(knitr::kable(head(belgium)))
#########################################################################################################
belgium_sts <- function(disease, data){

  # filter the chosen disease
  disease_data <- dplyr::filter_(data, paste0("Subject == \"",disease,"\""))

  # aggregated cases by week to get the weekly number of cases
  observed <- dplyr::group_by(disease_data, DateMonday)
  observed <- dplyr::summarize(observed, n_cases = n())

  # create the sts object
  disease_sts <- surveillance::sts(observed = observed$n_cases, # weekly number of cases
                                   start = c(min(lubridate::year(observed$DateMonday)), 01), # first week of the time series
                                   frequency = 52, # weekly data
                                   epochAsDate = TRUE, # we do have dates, not only index
                                   epoch = as.numeric(observed$DateMonday) # here are the dates
  )

  disease_sts
}
#########################################################################################################
library(surveillance)
library("ggplot2")
png("mygraphic.png")
#salmonella <- belgium_sts(disease = "SALM", data = belgium)
salmonella <- belgium_sts(disease = "V_RSV", data = belgium)
#V_RSV
plot(salmonella)
dev.off()
