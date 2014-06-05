X_train = read.table("getdata-projectfiles-UCI HAR Dataset/UCI HAR Dataset/train/X_train.txt", colClasses = c("numeric"))
X_test = read.table("getdata-projectfiles-UCI HAR Dataset/UCI HAR Dataset/test/X_test.txt", colClasses = c("numeric"))

subject_train = read.table("getdata-projectfiles-UCI HAR Dataset/UCI HAR Dataset/train/subject_train.txt", colClasses = c("numeric"))
subject_test = read.table("getdata-projectfiles-UCI HAR Dataset/UCI HAR Dataset/test/subject_test.txt", colClasses = c("numeric"))
colnames(subject_train) <- "subject"
colnames(subject_test) <- "subject"

activity_train = read.table("getdata-projectfiles-UCI HAR Dataset/UCI HAR Dataset/train/y_train.txt", colClasses = c("numeric"))
activity_test = read.table("getdata-projectfiles-UCI HAR Dataset/UCI HAR Dataset/test/y_test.txt", colClasses = c("numeric"))
colnames(activity_train) <- "activity"
colnames(activity_test) <- "activity"

X_data = rbind(X_train, X_test)
subject_data = rbind(subject_train, subject_test)
activity_data = rbind(activity_train, activity_test)
criteria = cbind(subject_data, activity_data)

rownames(criteria) = seq(1, nrow(criteria))
rownames(X_data) = seq(1, nrow(X_data))

mean_table = data.frame(matrix(0, length(unique(criteria$subject)), length(unique(criteria$activity))))
sd_table = data.frame(matrix(0, length(unique(criteria$subject)), length(unique(criteria$activity))))
for(i in unique(criteria$subject)){
    for(j in unique(criteria$activity)){
        row = rownames(criteria[criteria$subject == i & criteria$activity == j, ])
        subject_activity_data = X_data[as.numeric(row), ]
        mean_table[i, j] = mean(sapply(subject_activity_data, as.numeric))
        sd_table[i, j] = sd(sapply(subject_activity_data, as.numeric))
    }
}

activity_list = read.table("getdata-projectfiles-UCI HAR Dataset/UCI HAR Dataset/activity_labels.txt")
colnames(mean_table) = tolower(as.character(activity_list[, 2]))
colnames(sd_table) = tolower(as.character(activity_list[, 2]))

complete_data = cbind(subject_data, activity_data, X_data)

for(i in 1 : nrow(activity_list)){
    complete_data$activity[complete_data$activity == i] = tolower(as.character(activity_list[i, 2]))
}