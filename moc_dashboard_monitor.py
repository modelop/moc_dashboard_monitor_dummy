import modelop.utils as utils
from datetime import timedelta, datetime
import random

logger = utils.configure_logger()

notificationTypes = ["MODEL_NOTIFICATION", "MODEL_TEST_NOTIFICATION", "ENGINE_NOTIFICATION", "PROCESS_NOTIFICATION"
    , "MODEL_REVIEW_NOTIFICATION", "MODEL_DOCUMENT_REVIEW_NOTIFICATION", "JOB_NOTIFICATION"]
severitiesTypes = ["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"]
isOpenType = [True, False]


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
                {"createdDate": iteratedDate, "incidentType": getRandomIncidentType(),
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


# modelop.metrics
def metrics(df_1):
    actualROIAllTime = random.randint(30, 100)
    numberOfOpenPriorityIssues = random.randint(5, 20)
    incidentsTimelineYTD = getIncidentsTimeLineYTD()

    result = {
        "createdDate": datetime.now().strftime('%m/%d/%Y %H:%M:%S'),
        "actualROIAllTime": actualROIAllTime,
        "actualROIThisYear": actualROIAllTime + 3,
        "allVolumetricMonitorRecordCount": random.randint(1, 50),
        "numberOfOpenPriorityIssues": numberOfOpenPriorityIssues,
        "numberOfOpenPriorityIssuesMTD": numberOfOpenPriorityIssues - 1,
        "heatMap": {
            "inputVolume": {"testResult": "GREEN", "passed": True},
            "outputIntegrity": {"testResult": "GREEN", "passed": True},
            "dataDrift": {"testResult": "YELLOW", "passed": True},
            "conceptDrift": {"testResult": "GREEN", "passed": True},
            "statisticalPerformance": {"testResult": "GREEN", "passed": True},
            "stabilitity": {"testResult": "GREEN", "passed": True},
            "ethicalFairness": {"testResult": "GREEN", "passed": True}
        },
        "dailyInferencesLast30Days": getInferences(),
        "notificationsTimelineYTD": incidentsTimelineYTD,
        "notificationsGroupedByTypeYTD": getNotificationsByGroup(incidentsTimelineYTD)
    }
    yield result


if __name__ == "__main__":
    output = metrics(1)
    print(next(output))
