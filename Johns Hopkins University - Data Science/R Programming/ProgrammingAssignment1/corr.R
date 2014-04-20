corr <- function(directory, threshold = 0) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files
    
    ## 'threshold' is a numeric vector of length 1 indicating the
    ## number of completely observed observations (on all
    ## variables) required to compute the correlation between
    ## nitrate and sulfate; the default is 0
    
   ## Return a numeric vector of correlations
    vec = c()
    for (i in 1:332){
        file = paste(c(rep("0", 3 - nchar(i)), i, ".csv"), collapse = "")
        data = read.csv(paste(directory, "/", file, sep=""), header = TRUE, sep = ",", quote = "\"", dec = ".")
        if(sum(!(is.na(data["nitrate"]) | is.na(data["sulfate"]))) > threshold){
            logic = (is.na(data["nitrate"]) | is.na(data["sulfate"]))
            x = c(data[["nitrate"]])
            x = x[!logic]
            y = c(data[["sulfate"]])
            y = y[!logic]
            vec = c(vec, cor(x, y))
        }
    }
    vec
}