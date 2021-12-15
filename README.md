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
  "createdDate": "12/15/2021 01:44:35",
  "actualROIAllTime": 75,
  "actualROIThisYear": 78,
  "allVolumetricMonitorRecordCount": 45,
  "numberOfOpenPriorityIssues": 14,
  "numberOfOpenPriorityIssuesMTD": 13,
  "heatMap": {
    "inputVolume": {
      "testResult": "GREEN",
      "passed": "true"
    },
    "outputIntegrity": {
      "testResult": "GREEN",
      "passed": "true"
    },
    "dataDrift": {
      "testResult": "YELLOW",
      "passed": "true"
    },
    "conceptDrift": {
      "testResult": "GREEN",
      "passed": "true"
    },
    "statisticalPerformance": {
      "testResult": "GREEN",
      "passed": "true"
    },
    "stability": {
      "testResult": "GREEN",
      "passed": "true"
    },
    "ethicalFairness": {
      "testResult": "GREEN",
      "passed": "true"
    }
  },
  "dailyInferencesLast30Days": [
    {
      "date": "12/14/2021",
      "count": 8
    },
    {
      "date": "12/13/2021",
      "count": 23
    },
    {
      "date": "12/12/2021",
      "count": 5
    },
    {
      "date": "12/11/2021",
      "count": 19
    },
    {
      "date": "12/10/2021",
      "count": 11
    },
    {
      "date": "12/09/2021",
      "count": 8
    },
    {
      "date": "12/08/2021",
      "count": 1
    },
    {
      "date": "12/07/2021",
      "count": 2
    },
    {
      "date": "12/06/2021",
      "count": 8
    },
    {
      "date": "12/05/2021",
      "count": 13
    },
    {
      "date": "12/04/2021",
      "count": 15
    },
    {
      "date": "12/03/2021",
      "count": 2
    },
    {
      "date": "12/02/2021",
      "count": 8
    },
    {
      "date": "12/01/2021",
      "count": 8
    },
    {
      "date": "11/30/2021",
      "count": 10
    },
    {
      "date": "11/29/2021",
      "count": 23
    },
    {
      "date": "11/28/2021",
      "count": 15
    },
    {
      "date": "11/27/2021",
      "count": 11
    },
    {
      "date": "11/26/2021",
      "count": 6
    },
    {
      "date": "11/25/2021",
      "count": 15
    },
    {
      "date": "11/24/2021",
      "count": 6
    },
    {
      "date": "11/23/2021",
      "count": 22
    },
    {
      "date": "11/22/2021",
      "count": 10
    },
    {
      "date": "11/21/2021",
      "count": 14
    },
    {
      "date": "11/20/2021",
      "count": 11
    },
    {
      "date": "11/19/2021",
      "count": 22
    },
    {
      "date": "11/18/2021",
      "count": 8
    },
    {
      "date": "11/17/2021",
      "count": 7
    },
    {
      "date": "11/16/2021",
      "count": 18
    }
  ],
  "notificationsTimelineYTD": [
    {
      "createdDate": "12/15/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "12/12/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "12/11/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": true
    },
    {
      "createdDate": "12/09/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    },
    {
      "createdDate": "12/08/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "12/07/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "12/06/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "12/05/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": false
    },
    {
      "createdDate": "12/03/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "11/29/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": false
    },
    {
      "createdDate": "11/28/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "11/27/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "11/24/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "11/20/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": false
    },
    {
      "createdDate": "11/16/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    },
    {
      "createdDate": "11/15/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "11/13/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": false
    },
    {
      "createdDate": "11/12/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "11/11/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "11/10/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    },
    {
      "createdDate": "11/06/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "11/03/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "11/02/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    },
    {
      "createdDate": "11/01/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "10/31/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "10/29/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "10/28/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "10/25/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "WARN",
      "isOpen": true
    },
    {
      "createdDate": "10/24/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "10/23/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "10/21/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    },
    {
      "createdDate": "10/19/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "10/13/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "10/12/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": true
    },
    {
      "createdDate": "10/11/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "10/10/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "10/09/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "10/07/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "10/05/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "10/01/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "09/30/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "09/29/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "WARN",
      "isOpen": true
    },
    {
      "createdDate": "09/28/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "09/27/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "WARN",
      "isOpen": true
    },
    {
      "createdDate": "09/26/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": false
    },
    {
      "createdDate": "09/23/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": false
    },
    {
      "createdDate": "09/21/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "09/20/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "09/16/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "09/15/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "09/10/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "09/09/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "09/08/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "09/06/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "09/05/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "09/04/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    },
    {
      "createdDate": "09/03/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    },
    {
      "createdDate": "09/02/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "08/31/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "08/27/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "08/23/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "08/21/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "08/10/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    },
    {
      "createdDate": "08/08/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "08/07/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "08/05/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": false
    },
    {
      "createdDate": "08/03/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "07/29/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "WARN",
      "isOpen": true
    },
    {
      "createdDate": "07/26/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "07/25/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": true
    },
    {
      "createdDate": "07/21/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": true
    },
    {
      "createdDate": "07/19/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "07/18/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "07/16/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "07/10/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "07/09/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "WARN",
      "isOpen": true
    },
    {
      "createdDate": "07/07/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "WARN",
      "isOpen": true
    },
    {
      "createdDate": "07/05/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "07/04/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": true
    },
    {
      "createdDate": "07/03/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    },
    {
      "createdDate": "07/02/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": false
    },
    {
      "createdDate": "07/01/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": true
    },
    {
      "createdDate": "06/29/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "06/28/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "06/26/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "06/25/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "06/23/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "WARN",
      "isOpen": true
    },
    {
      "createdDate": "06/21/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "06/20/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "WARN",
      "isOpen": true
    },
    {
      "createdDate": "06/17/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "06/13/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "06/12/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "06/09/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": false
    },
    {
      "createdDate": "06/06/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "06/02/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": false
    },
    {
      "createdDate": "05/30/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "05/29/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "05/28/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "05/27/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "05/25/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "05/24/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "05/23/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "05/22/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    },
    {
      "createdDate": "05/21/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": false
    },
    {
      "createdDate": "05/20/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "05/19/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "05/18/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "05/17/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "05/15/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "05/14/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "05/13/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "WARN",
      "isOpen": true
    },
    {
      "createdDate": "05/12/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "05/10/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "05/09/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "05/08/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "05/05/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "04/29/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": false
    },
    {
      "createdDate": "04/28/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "04/27/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "04/26/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "04/25/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "04/23/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": false
    },
    {
      "createdDate": "04/22/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "WARN",
      "isOpen": true
    },
    {
      "createdDate": "04/20/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "04/19/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": true
    },
    {
      "createdDate": "04/15/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "04/13/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "04/12/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "04/11/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": true
    },
    {
      "createdDate": "04/10/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "04/09/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "04/08/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "04/04/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "04/01/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "03/29/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "03/26/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "03/24/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "03/23/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "03/22/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    },
    {
      "createdDate": "03/21/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "03/17/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": false
    },
    {
      "createdDate": "03/15/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    },
    {
      "createdDate": "03/14/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "03/11/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "03/09/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "03/06/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "03/05/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "03/04/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    },
    {
      "createdDate": "03/03/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "03/02/2021",
      "incidentType": "MODEL_DOCUMENT_REVIEW_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": true
    },
    {
      "createdDate": "03/01/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": false
    },
    {
      "createdDate": "02/27/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "02/26/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": false
    },
    {
      "createdDate": "02/24/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "02/23/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "02/18/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": false
    },
    {
      "createdDate": "02/13/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "02/12/2021",
      "incidentType": "MODEL_NOTIFICATION",
      "severity": "INFO",
      "isOpen": false
    },
    {
      "createdDate": "02/11/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": true
    },
    {
      "createdDate": "02/09/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": false
    },
    {
      "createdDate": "02/08/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "02/07/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": false
    },
    {
      "createdDate": "02/06/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "WARN",
      "isOpen": true
    },
    {
      "createdDate": "02/04/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "INFO",
      "isOpen": true
    },
    {
      "createdDate": "02/03/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "02/01/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "WARN",
      "isOpen": false
    },
    {
      "createdDate": "01/30/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": true
    },
    {
      "createdDate": "01/27/2021",
      "incidentType": "PROCESS_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "01/25/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "01/24/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": false
    },
    {
      "createdDate": "01/20/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": false
    },
    {
      "createdDate": "01/18/2021",
      "incidentType": "JOB_NOTIFICATION",
      "severity": "ERROR",
      "isOpen": true
    },
    {
      "createdDate": "01/17/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "WARN",
      "isOpen": true
    },
    {
      "createdDate": "01/10/2021",
      "incidentType": "MODEL_TEST_NOTIFICATION",
      "severity": "TRACE",
      "isOpen": false
    },
    {
      "createdDate": "01/08/2021",
      "incidentType": "ENGINE_NOTIFICATION",
      "severity": "DEBUG",
      "isOpen": false
    },
    {
      "createdDate": "01/03/2021",
      "incidentType": "MODEL_REVIEW_NOTIFICATION",
      "severity": "FATAL",
      "isOpen": false
    }
  ],
  "notificationsGroupedByTypeYTD": {
    "PROCESS_NOTIFICATION": 32,
    "MODEL_TEST_NOTIFICATION": 24,
    "MODEL_NOTIFICATION": 18,
    "ENGINE_NOTIFICATION": 32,
    "MODEL_DOCUMENT_REVIEW_NOTIFICATION": 24,
    "JOB_NOTIFICATION": 21,
    "MODEL_REVIEW_NOTIFICATION": 25
  }
}
```
