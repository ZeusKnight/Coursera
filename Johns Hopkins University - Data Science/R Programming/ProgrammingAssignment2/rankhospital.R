rankhospital <- function(state, outcome, num = "best") {
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
    statedata = data[which(data$State == state & data[columnName] != "Not Available"), ]
    sortdata = statedata[order(as.numeric(statedata[[columnName]]), statedata$Hospital.Name, na.last = NA), ]
    sortdata = cbind(sortdata, ranking = 1 : nrow(sortdata))
    if(num == "best"){
        rank = 1
    } else if(num == "worst"){
        rank = nrow(sortdata)
    } else {
        rank = as.numeric(num)
    }
    
    if(rank > nrow(sortdata)){
        result = NA
    } else {
        result = sortdata[which(sortdata$ranking == rank), ]$Hospital.Name
    }
    ## Return hospital name in that state with the given rank
    ## 30-day death rate
    result
}