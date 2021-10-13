# employees
Simple aiohttp project
___
How to run the app  
first time: docker-compose -f docker-compose-start.yml up  
next times: docker-compose up  
run tests: docker-compose -f docker-compose-tests.yml up
___

GET /employees  
GET /employees?id={id}  
POST /employees  
PUT /employees?id={id}  
DELETE /employees?id={id}  

Fields:  
'employee_name',  
'e_mail',  
'phone_number',  
'inn',  
'position',  
'department',  
'passport',  
'passport_issued',  
'education',  
'address',  
'birth_date'

