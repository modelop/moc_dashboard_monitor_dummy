import modelop.utils as utils
from datetime import timedelta, datetime
import random

logger = utils.configure_logger()

notificationTypes = ["MODEL_NOTIFICATION", "MODEL_TEST_NOTIFICATION", "ENGINE_NOTIFICATION", "PROCESS_NOTIFICATION"
    , "MODEL_REVIEW_NOTIFICATION", "MODEL_DOCUMENT_REVIEW_NOTIFICATION", "JOB_NOTIFICATION"]
severitiesTypes = ["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"]
isOpenType = ["true", "false"]

## Defining Green multiple times to force a best looking Dashboard
heatMapColors = ["Gray", "Green", "Green", "Green", "Green", "Green", "Green", "Green", "Yellow", "Green", "Green",
                 "Green", "Green", "Green", "Green", "Red"]


# modelop.init
def init():
    pass


def getInferences():
    array = []
    for x in range(1, 30):
        updated_date = (datetime.now() + timedelta(days=-x)).strftime('%m/%d/%Y')
        array.append({"date": updated_date, "count": random.randint(0, 25)})
    return array


def getIncidentsTimeLineYTD():
    incidentsTimeLineYTD = []
    today = datetime.now()
    # Getting current date of year
    dayOfYear = int(format(today, '%j'))
    datesYTD = [today - timedelta(days=x) for x in range(dayOfYear)]
    for iteratedDate in datesYTD:
        if random.randint(1, 10) % 2 == 0:
            incidentsTimeLineYTD.append(
                {"createdDate": iteratedDate.strftime('%m/%d/%Y'), "incidentType": getRandomIncidentType(),
                 "severity": getRandomSeverityType(),
                 "isOpen": getRandomIsOpenType()})

    return incidentsTimeLineYTD


def getRandomIncidentType():
    return notificationTypes[random.randint(0, len(notificationTypes) - 1)]


def getRandomSeverityType():
    return severitiesTypes[random.randint(0, len(severitiesTypes) - 1)]


def getRandomIsOpenType():
    return isOpenType[random.randint(0, len(isOpenType) - 1)]


def getNotificationsByGroup(notificationsArray):
    notificationsByGroupDict = {}
    for notification in notificationsArray:
        if notificationsByGroupDict.get(notification['incidentType']) is not None:
            notificationsByGroupDict[notification['incidentType']] = notificationsByGroupDict.get(
                notification['incidentType']) + 1
        else:
            notificationsByGroupDict[notification['incidentType']] = 1
    return notificationsByGroupDict


def generateHeatMapValues(metricName=""):
    color = heatMapColors[random.randint(0, len(heatMapColors) - 1)]
    return {"testResult": color, "description": metricName}


# modelop.metrics
def metrics(df_1):
    actualROIAllTime = random.randint(30, 100)
    numberOfOpenPriorityIssues = random.randint(5, 20)
    incidentsTimelineYTD = getIncidentsTimeLineYTD()
    dailyInferencesLast30Days = getInferences()
    notificationsByGroup = getNotificationsByGroup(incidentsTimelineYTD)
    yield {
        "createdDate": datetime.now().strftime('%m/%d/%Y %H:%M:%S'),
        "actualROIAllTime": actualROIAllTime,
        "actualROIThisYear": actualROIAllTime + 3,
        "allVolumetricMonitorRecordCount": random.randint(1, 50),
        "numberOfOpenPriorityIssues": numberOfOpenPriorityIssues,
        "numberOfOpenPriorityIssuesMTD": numberOfOpenPriorityIssues - 1,
        "heatMap": {
            # "Input Volume": generateHeatMapValues(
            #     "This ModelOp Center monitor detects discrepancies between two assets based on their record counts & identifiers."),
            # "Output Integrity": generateHeatMapValues(
            #     "This ModelOp Center monitor detects discrepancies between two assets based on their record identifiers."),
            # "Data Drift": generateHeatMapValues(
            #     "This ModelOp Center monitor runs and compares Kolmogorov-Smirnov, Epps-Singleton, Jensen-Shannon, Kullback-Leibler, and Pandas summary on input data."),
            # "Concept Drift": generateHeatMapValues(
            #     "This ModelOp Center monitor runs and compares Kolmogorov-Smirnov, Epps-Singleton, Jensen-Shannon, Kullback-Leibler, and Pandas summary on output data."),
            # "Statistical Performance": generateHeatMapValues(
            #     "This ModelOp Center monitor computes classification metrics such as AUC, Accuracy, Precision, Recall, and F1_score."),
            # "Stability": generateHeatMapValues(
            #     "This ModelOp Center monitor computes stability metrics, including Population Stability Index (PSI) and Characteristic Stability Indices (CSI), and their breakdown by buckets."),
            # "Ethical Fairness": generateHeatMapValues(
            #     "This ModelOp Center monitor computes disparity metrics (with respect to reference groups) and group metrics on protected classes, such as race or gender."),
            "Data Inputs Health": generateHeatMapValues("All pipelines that provide data input to the Usuals"),
            "DeepBrew Health": generateHeatMapValues("DeepBrew model"),
            "Ecosystem Health": generateHeatMapValues("Ecosystem health"),
            "Response SLA": generateHeatMapValues(""),
            "Business KPI SLA": generateHeatMapValues("Engagement, conversion and revenue KPIs"),
            "Economic Projection": generateHeatMapValues("Projected annual NIR")
        },
        "dailyInferencesLast30Days": dailyInferencesLast30Days,
        "notificationsTimelineYTD": incidentsTimelineYTD,
        "notificationsGroupedByTypeYTD": notificationsByGroup
    }

# if __name__ == "__main__":
#     output = metrics(1)
#     print('Result')
#     print(next(output))
