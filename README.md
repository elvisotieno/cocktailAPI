# cocktailAPI
# cocktailAPI
This is a REST API (Cocktails API) with all the CRUD functionalities where: 
- User can register and login 
- User can add/update/delete a cocktail 
- User can view all cocktails in the system 
- User can view the cocktails they added 
- User can fetch 5 random drinks/cocktails from the Api 
- User can view the details of one cocktail 
- User can fetch 5 random latest drinks/cocktails from Api  
Endpoint to that shows 10 latest cocktails in the system in real time without the need to keep fetching. This is built using Celery, Redis and Django chanels 
-Celery provides workers. A worker is a function that executes our tasks(the function used to fetch 10 latest cocktails from the database). 
- Redis serves as a broker, whose main function is to store our tasks in a queue data structure
-After redis put the task in a queue, it starts to pass these tasks to our workers periodicaly
-after worker is done executing it stores the result in a Result Bakend(still a queue enabled by Rabit), this is made possible through the use of websockets
-and then we can rebroadcast our cocktails to the user asynchronously...
