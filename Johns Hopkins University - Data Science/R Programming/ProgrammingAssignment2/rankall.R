rankall <- function(outcome, num = "best") {
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
    data = data[which(data[columnName] != "Not Available"), ]
    result = split(data[columnName], data$State)
    r = as.data.frame(c())
    for(state in names(result)){
        statedata = data[which(data$State == state), ]
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
            name = NA
        } else {
            name = sortdata[which(sortdata$ranking == rank), ]$Hospital.Name
        }
        r = rbind(r, data.frame(hospital = name, state = state))
    }
    r
}
