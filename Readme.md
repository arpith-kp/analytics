# Analytics project

This is sample project to show how to do analytics on Ad Campaigns

# Tech Stack

  - Python
  - Druid
  - Imply
  - Django

# Setup
   - We need to setup [Druid] which is used for analytics, once Druid/Imply to setup, install requirements specified in `requirements.txt` in an virtualenv.
  - Once setup is complete, start Imply `bin/supervise -c conf/supervise/quickstart.conf`. You need to be in imply-2.2.3 folder
  - Start REST server `python manage.py runserver`. You need to be in Celtra(src code) folder.

# Usage
   - You can use [Pivot] to do visual analysis on the data.
   - You can also use Rest API to get similar data.
#### Rest API's
**Metrics**
---
**URL**

  - <_api/v1/metrics/campaign/(campaign_id)_>

* **Method:**
  
  <_GET_>

*  **URL Params**

   <_campaign_id_> 

   **Required:**
 
   `campaign_id=[integer]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``` json [{"event": {"adId": "AdID","impressions": IMPRESSION,"interactions": INTERACTIONS,"swipes": SWIPES}, timestamp": "TIMESTAMP","version": "v1"}]```
 
* **Error Response:**

  * **Code:** 500 <br />
    **Content:** `{ error : "Internal server Error" }`

* **Sample Call:**

  <_http GET http://localhost:8000/api/v1/metrics/campaign/105._> 

**URL**

 - <_api/v1/api/v1/metrics/last_week_>

* **Method:**
  
  <_GET_>

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``` json [
    {
        "event": {
            "adId": "AdId",
            "impressions": IMPRESSIONS,
            "user": USER
        },
        "timestamp": "TIMESTAMP",
        "version": "v1"
    }]```
 
* **Error Response:**

  * **Code:** 500 <br />
    **Content:** `{ error : "Internal server Error" }`

* **Sample Call:**

  <_http GET http://localhost:8000/api/v1/metrics/last_week_> 


[Druid]: <https://docs.imply.io/on-premise/quickstart>
[Pivot]: <http://104.197.203.180:9095/>
   