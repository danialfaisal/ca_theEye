The Eye

A Django RestFul service designed to organize User activity data. Application deployed on heroku, use below credentials

https://ca-event-tracking.herokuapp.com/

**Superuser Credentials:**

username:  _superuser_

password:  _superuser_

**Requirements:**

An Event has a category, a name and a payload of data (the payload can change according to which event an Application is sending)

**A single "Events" model was created to minimize joining of tables and serialization. To avoid extracting key value pairs from dynamic JSON data, I just made the data attribute into a JSONfield. And since the analytics teams only needs to results from sessions, categories and timestamps. For each session, they'll be able to see the entire data field in the JSON format.**  


Different types of Events (identified by category + name) can have different validations for their payloads

**The Events class in models are indexed together with category and name. This enforces data integrity. The validations part is not done.**


Events in a Session should be sequential and ordered by the time they occurred

**The Events class in models is ordered by "timestamp"** 


Applications should be recognized as "trusted clients" to "The Eye"

**The inbuilt Django permission class "IsAuthenticatedOrReadOnly" is used which ensures that an authentication token is used to send API calls to the application. The JWT authentication settings are included in the settings.py file**  

Applications can send events for the same session

**The models and constraints take care of this.** 

"The Eye" will be receiving, in average, ~100 events/second, so consider not processing events in real time

**Not implemented. I tried using Memcached from Djangos cache framework but wasnt able to make it functional.**  

When Applications talk to "The Eye", make sure to not leave them hanging

**A status 200 is created when a CLinet API call is successful.** 

Your models should have proper constraints to avoid race conditions when multiple events are being processed at the same time

**Not implemented. I tried digging into Django cache framework and throttling but I couldn't figure it out.** 

An event that is sending an unexpected value in the payload

**The entire payload data is accumalated into one attribute**

An event that has an invalid timestamp (i.e.: future)

**Not implemented. We just need to add a function in the class to validate the timestamp attribute with the current time and raise an error. Didnt have the time to complete.** 

Your application is documented

**Included basic documentation**

Your application is dockerized

**Deployed it to Heroku instead**

A reusable client that talks to "The Eye"

**Application has an inbuilt client to Post API data. https://ca-event-tracking.herokuapp.com/api/event_list**