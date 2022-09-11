#Covid-19 Tracker Backend

## Endpoints
### covid/casesPer100k
Method = GET
Returns a list number of covid cases (per 100k) sorted by date_updated for a county

URL Args:
    zip_code: 5-digit US Zip code 
    city, state (must be together)
    
Example URLs:
  /covid/casesPer100k?zip_code=12345
  /covid/casesPer100k?city=Los Angeles?state=California
    
Example JSON output:
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

###covid/communityLevel
Method = GET
Returns the most recent Covid-19 Community Level (low/medium/high) for a county.

URL Args:
    zip_code: 5-digit US Zip code 
    city, state (must be together)
    
Example URLs:
  /covid/communityLevel?zip_code=12345
  /covid/communityLevel?city=Los Angeles?state=California

Example JSON output:
{
    "county": "Los Angeles County",
    "community_level": "Low",
    "date_updated": "2022-09-08T00:00:00.000"
}

---

###covid/hesitancyRate
Method = GET
Returns the most recent percentage a county that has expressed hesitance about getting the COVID-19 vaccine.

URL Args:
    zip_code: 5-digit US Zip code 
    city, state (must be together)
    
Example URLs:
  /covid/communityLevel?zip_code=12345
  /covid/communityLevel?city=Los Angeles?state=California
  
Example JSON output:
{
    "county": "Los Angeles County, California",
    "estimated_hesitance": "0.0602"
}
  
###covid/
URL Args:
    zip_code: 5-digit US Zip code 
    city, state (must be together)
    
Example URLS:
   /covid/hospitalAdmissionsPer100k?zip_code=12345
  /covid/hospitalAdmissionsPer100k?city=Los Angeles?state=California

Example JSON output:
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
  
 
 


