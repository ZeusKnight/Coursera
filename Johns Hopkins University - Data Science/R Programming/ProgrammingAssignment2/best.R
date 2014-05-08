best <- function(state, outcome) {
    ## Check that state and outcome are valid
    if(!outcome %in% c("heart attack", "heart failure", "pneumonia")){
        stop("invalid outcome")
    } else {
        if(outcome == "heart attack"){
            columnName = "Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack"
        }
        if(outcome == "heart failure"){
            columnName = "Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure"
        }
        if(outcome == "pneumonia"){
            columnName = "Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia"
        }
    }
    ## Read outcome data
    data <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
    if(!state %in% data$State){
        stop("invalid state")
    }
    ## Return hospital name in that state with lowest 30-day death
    min = sapply(split(as.numeric(data[[columnName]]), data$State), min, na.rm = TRUE)[[state]]
    result <- data[which(data$State == state & data[columnName] == min),]$Hospital.Name
    ## rate
    result
}
