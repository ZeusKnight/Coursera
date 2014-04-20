complete <- function(directory, id = 1:332) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files
    
    ## 'id' is an integer vector indicating the monitor ID numbers
    ## to be used
    
    ## Return a data frame of the form:
    ## id nobs
    ## 1  117
    ## 2  1041
    ## ...
    ## where 'id' is the monitor ID number and 'nobs' is the
    ## number of complete cases
    a = 0
    table = c()
    for (i in id){
        file = paste(c(rep("0", 3 - nchar(i)), i, ".csv"), collapse = "")
        data = read.csv(paste(directory, "/", file, sep=""), header = TRUE, sep = ",", quote = "\"", dec = ".")
        a = a + 1
        table = rbind(table, c(i, sum(!(is.na(data["nitrate"]) | is.na(data["sulfate"])))))
    }
    colnames(table) <- c("id", "nobs")
    table = as.data.frame(table)
    table
}