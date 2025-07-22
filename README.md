# Project README

## Overview  
This project deploys a Django application and MongoDB on separate instances. It fetches and displays authentication tokens, network devices, and device interface information from Cisco DNA Center. The results of API calls are stored in MongoDB.

## Key Features  
- Obtain authentication token from Cisco DNA Center API  
- Retrieve and display network device information  
- Fetch interface details for each device  
- Log API call results (API type, device IP, timestamp, success/failure) into MongoDB  

## Tech Stack  
- Python 3.x  
- Django framework  
- MongoDB (using `djongo` driver)  
- Requests library (for Cisco DNA Center API calls)  

## Deployment Environment  
- Django app runs on a separate instance  
- MongoDB runs on a separate instance  

## Setup Summary  
1. Setup Django project and install dependencies  
2. Configure MongoDB connection in `settings.py`  
3. Run migrations to create MongoDB collections  
4. Add Cisco DNA Center connection info in `dnac_config.py`  
5. Launch Django app and verify API data retrieval  
