#1.This is Python 3.7 project.

#2.Please install/ define in IDE the requirements file.

#3.Following task definition each request will random integer in range of 0-9,

# if result will be 0 the request will include one corrupted file   

#4.BIyond.config - set the server to run over port 8081 , and limits the pool request to 4 parallel jobs

#5.the ETL process will executed under /files_upload and expect to get json with "filenames" attribute
    
#6.Request timeout per job define in the class init as ETL_REQUEST_TIMEOUT

#7.If file is uploaded twice it will be replaced with the newer version

#  (therefor we need to query for each new file before insert)

#8.In order to run tests folder 

#*run flak aap with <BIyond>.run.py

#*run pytets in IDE (Or terminal run with pytest command) for all "tests" folder or specific test 

#*tests parameters can defined with tests.test_params.py

#Regards

#Amir

