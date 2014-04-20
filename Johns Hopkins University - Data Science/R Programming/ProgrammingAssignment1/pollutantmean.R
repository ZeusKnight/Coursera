pollutantmean <- function(directory, pollutant, id = 1:332) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files
    
    ## 'pollutant' is a character vector of length 1 indicating
    ## the name of the pollutant for which we will calculate the
    ## mean; either "sulfate" or "nitrate".
    
    ## 'id' is an integer vector indicating the monitor ID numbers
    ## to be used
    
    ## Return the mean of the pollutant across all monitors list
    ## in the 'id' vector (ignoring NA values)
    total = 0
    row = 0
    for (i in id){
        file = paste(c(rep("0", 3 - nchar(i)), i, ".csv"), collapse = "")
        data = read.csv(paste(directory, "/", file, sep=""), header = TRUE, sep = ",", quote = "\"", dec = ".")
        total = total + sum(as.numeric(data[[pollutant]]), na.rm=TRUE)
        row = row + length(data[[pollutant]]) - sum(is.na(data["nitrate"]))
    }
    return (total / row)
}