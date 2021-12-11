# MOC DASHBOARD MONITOR
This ModelOp Center monitor returns the calculations for the main MOC Dashboard.

## Input Assets

| Type          | Number | Description                                           |
| ------------- | ------ | ----------------------------------------------------- |
| Baseline Data | **0**  | |
| Sample Data   | **1**  | Dataset to count |

## Assumptions & Requirements

## Execution
1. `metrics` function runs the content for the MOC Dashboard.
2. Test result is returned under the list of `volumetrics` tests.

## Monitor Output

```JSON
{
"createdDate":'11/29/2021 00:30:00',
"actualROIAllTime":100,
"actualROIThisYear":70,
"allVolumetricMonitorRecordCount":0.0,
"numberOfOpenPriorityIssues":0,
"numberOfOpenPriorityIssuesMTD":0,
"numberOfOpenComplianceIssues":23,
"numberOfOpenComplianceIssuesMTD":10,
"heatMap":{
            "inputVolume":{"testResult":"GREEN","passed":true},
            "outputIntegrity":{"testResult":"GREEN","passed":true},
            "dataDrift":{"testResult":"YELLOW","passed":true},
            "conceptDrift":{"testResult":"GREEN","passed":true},
            "statisticalPerformance":{"testResult":"GREEN","passed":true},
            "stabilitity":{"testResult":"GREEN","passed":true},
            "ethicalFairness":{"testResult":"GREEN","passed":true}
            },
"dailyInferencesLast30Days":[
            {"date":'11/01/2021',"count":50},
            {"date":'11/02/2021',"count":19},
                        (...)
            {"date":'11/29/2021',"count":21},
            {"date":'11/30/2021',"count":123}
          ],
"notificationsTimelineYTD":[
            {"createdDate":'11/01/2021',"incidentType":"Input Data Issues","priority":"high","state":"Open","notificationID":"22989b9b-36bf-4134-8815-e1c84b672483" },
            {"createdDate":'11/02/2021',"incidentType":"Runtime Issues","priority":"high","state":"Open","notificationID":"f5c3ab1a-3f45-4e7d-8ef5-4647e06747c0" }, 
                                                            (...)
            {"createdDate":'11/30/2021',"incidentType":"Model Performance Issues","priority":"high","state":"Open","notificationID":"0fcbb5dd-8667-405c-ac8f-52f72ca24454" }
          ],
"notificationsGroupedByTypeYTD":[
            {"incidentType":"Input Data Issues", "count":25},
            {"incidentType":"Runtime Issues", "count":50},
            {"incidentType":"Model Performance Issues", "count":25}
          ]
}
```