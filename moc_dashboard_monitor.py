import modelop.utils as utils

logger = utils.configure_logger()

# modelop.init
def init():
    pass


# modelop.metrics
def metrics(df_1):
    result = {
        "value_one": "1",
        "second_value": "second_value"
    }
    yield result