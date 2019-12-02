#1.This is Python 3.7 project.
#2.Please install/ define in IDE the requirements file.
#3.Following to the task definition each request will random int 0-9,
#       if 0 will include one corrupted file   
#4.Biyond.config - set the server to run over port 8081 , and limits the pool request to 4 parallel jobs
#5.the ETL process will executed under /etl and expect to get json with "filenames" attribute    
#6.Request timeout per job define in the class init as ETL_REQUEST_TIMEOUT
#7.If file is uploaded twice it will be replaced with the newer version
#  (therefor we need to query for each new file before insert)
#Regards
#Amir

