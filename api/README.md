# Covid-19 Tracker Backend

## Endpoints
### covid/casesPer100k
Method = GET <br>
Returns a list number of covid cases (per 100k) sorted by date_updated for a county

URL Args: <br>
* zip_code: 5-digit US Zip code <br>
* city, state (must be together) <br>
    
Example URLs: <br>
* /covid/casesPer100k?zip_code=12345 <br>
* /covid/casesPer100k?city=Los Angeles?state=California <br>
    
Example JSON output:
```
[
    {
        "county": "Los Angeles County",
        "covid_cases_per_100k": "216.47",
        "date_updated": "2022-02-24T00:00:00.000"
    },
    {
        "county": "Los Angeles County",
        "covid_cases_per_100k": "111.43",
        "date_updated": "2022-03-03T00:00:00.000"
    },
    {
        "county": "Los Angeles County",
        "covid_cases_per_100k": "88.56",
        "date_updated": "2022-03-10T00:00:00.000"
    }
]
```

---

### covid/communityLevel
Method = GET <br>
Returns the most recent Covid-19 Community Level (low/medium/high) for a county.

URL Args:
* zip_code: 5-digit US Zip code <br>
* city, state (must be together) <br>

Example JSON output:
```
{
    "county": "Los Angeles County",
    "community_level": "Low",
    "date_updated": "2022-09-08T00:00:00.000"
}
```
---

### covid/hesitancyRate
Method = GET 
Returns the most recent percentage a county that has expressed hesitance about getting the COVID-19 vaccine.

URL Args:
* zip_code: 5-digit US Zip code <br>
* city, state (must be together) <br>
  
Example JSON output:
```
{
    "county": "Los Angeles County, California",
    "estimated_hesitance": "0.0602"
}
```

---

### covid/hospitalAdmissionsRatePer100k
URL Args:
* zip_code: 5-digit US Zip code <br>
* city, state (must be together) <br>
     
Example JSON output:
```
]
    {
        "county": "Los Angeles County, California",
        "hospital_admissions_per_100k": "9.6",
        "date_updated": "2022-08-25T00:00:00.000"
    },
    {
        "county": "Los Angeles County, California",
        "hospital_admissions_per_100k": "9.0",
        "date_updated": "2022-09-01T00:00:00.000"
    },
    {
        "county": "Los Angeles County, California",
        "hospital_admissions_per_100k": "7.8",
        "date_updated": "2022-09-08T00:00:00.000"
    }
]
```

---
 
 


