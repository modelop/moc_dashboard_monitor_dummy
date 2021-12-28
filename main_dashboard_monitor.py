import modelop.monitors.volumetrics as volumetrics
import modelop.monitors.bias as bias
import modelop.monitors.stability as stability
import modelop.monitors.performance as performance
import modelop.monitors.drift as drift
import modelop.schema.infer as infer
import modelop.utils as utils

logger = utils.configure_logger()

MONITORING_PARAMETERS = {}


# modelop.init
def init(self, input_job_json):
    """A function to extract input schema from job JSON.
    Args:
        job_json (str): job JSON in a string format.
    """
    self.job_json = input_job_json


# modelop.metrics
def metrics(self, dataframe_1, dataframe_2, df_baseline, df_sample) -> dict:
    try:
        daily_inferences = execute_volumetrics_count(dataframe_1)
        print(" daily_inferences =%s", daily_inferences)
    except Exception:
        print("An exception happened while executing the daily_inferences monitor")
    """Heat map monitors"""
    try:
        input_volume = execute_volumetrics_count_comparison(dataframe_1, dataframe_2)
        print(" input_volume =%s", input_volume)
    except Exception:
        print("An exception happened while executing the input_volume monitor")
    try:
        #This one  depending on the input schema, might require scored DF
        output_integrity = execute_volumetrics_identifier_comparison(self.job_json,dataframe_1,dataframe_2)
        print(" output_integrity =%s", input_volume)
    except Exception:
        print("An exception happened while executing the output_integrity monitor")
    try:
        data_drift = execute_data_drift_comprehensive(self.job_json, df_baseline, df_sample)
        print(" data_drift =%s", input_volume)
    except Exception:
        print("An exception happened while executing the data_drift monitor")
    # concept_drfit = Pending to be defined
    try:
        #Maybe due to the input schema, the DF requires scored
        statistical_performance = execute_performance_classification(self.job_json, df_sample)
        print(" statistical_performance =%s", input_volume)
    except Exception:
        print("An exception happened while executing the statistical_performance monitor")

    try:
        stability_analysis = execute_stability_analysis(self.job_json, df_baseline, df_sample)
        print(" stability_analysis =%s", input_volume)
    except Exception:
        print("An exception happened while executing the stability_analysis monitor")

    try:
        ethical_fairness = execute_bias_comprehensive(self.job_json, dataframe_1)
        print(" ethical_fairness =%s", input_volume)
    except Exception:
        print("An exception happened while executing the ethical_fairness monitor")


"""
--- General aggregations and calculations
"""


def execute_volumetrics_count(df_1) -> dict:
    """
    Daily inferences
    """
    # Initialize Volumetric monitor with 1st input DataFrame
    volumetric_monitor = volumetrics.VolumetricMonitor(df_1)
    count_results = volumetric_monitor.count()
    result = {
        "volumetrics": {
            # Boolean top-level metric
            "record_count": count_results["values"]["record_count"],
            # Complete test results
            "volumetrics": [count_results]
        }
    }
    return result


"""
---- HEAT MAP monitors
"""


def execute_volumetrics_count_comparison(df_1, df_2) -> dict:
    """
    Input Volume monitor
    """
    # Initialize Volumetric monitor with 1st input DataFrame
    volumetric_monitor = volumetrics.VolumetricMonitor(df_1)
    count_comparison = volumetric_monitor.count_comparison(df_2)

    result = {
        # Boolean top-level metric
        "record_count_difference": count_comparison["values"][
            "record_count_difference"
        ],
        # Complete test results
        "volumetrics": [count_comparison]
    }
    return result


def execute_volumetrics_identifier_comparison(job_json, df_1, df_2):
    """
    Output integrity monitor
    """
    """
    Init(json_job)
    """
    # Extract input schema from job JSON
    input_schema_definition = infer.extract_input_schema(job_json)

    logger.info("Input schema definition: %s", input_schema_definition)

    # Get monitoring parameters from schema
    global MONITORING_PARAMETERS
    MONITORING_PARAMETERS = infer.set_monitoring_parameters(
        schema_json=input_schema_definition, check_schema=True
    )
    """
    --- end init
    """
    # Get identifier_columns from MONITORING_PARAMETERS
    identifier_columns = MONITORING_PARAMETERS["identifier_columns"]

    # Initialize Volumetric monitor with 1st input DataFrame
    volumetric_monitor = volumetrics.VolumetricMonitor(df_1)

    # Compare DataFrames on identifier_columns
    identifiers_comparison = volumetric_monitor.identifier_comparison(
        df_2, identifier_columns
    )

    result = {
        # Boolean top-level metric
        "identifiers_match": identifiers_comparison["values"]["identifiers_match"],
        # Complete test results
        "volumetrics": [identifiers_comparison],
    }

    return result


def execute_data_drift_comprehensive(job_json, df_baseline, df_sample) -> dict:
    """
          Data drift
    """
    """A function to extract input schema from job JSON.
    Args:
        job_json (str): job JSON in a string format.
    """

    # Extract input schema from job JSON
    input_schema_definition = infer.extract_input_schema(job_json)
    logger.info("Input schema definition: %s", input_schema_definition)

    # Get monitoring parameters from schema
    global MONITORING_PARAMETERS
    MONITORING_PARAMETERS = infer.set_monitoring_parameters(
        schema_json=input_schema_definition, check_schema=True
    )

    logger.info("numerical_columns: %s", MONITORING_PARAMETERS["numerical_columns"])
    logger.info("categorical_columns: %s", MONITORING_PARAMETERS["categorical_columns"])

    """
    --- end init
    """

    numerical_columns = MONITORING_PARAMETERS["numerical_columns"]
    categorical_columns = MONITORING_PARAMETERS["categorical_columns"]

    # Initialize DriftDetector
    drift_detector = drift.DriftDetector(
        df_baseline=df_baseline,
        df_sample=df_sample,
        numerical_columns=numerical_columns,
        categorical_columns=categorical_columns,
    )

    # Compute drift metrics
    # Epps-Singleton p-values
    es_drift_metrics = drift_detector.calculate_drift(pre_defined_test="Epps-Singleton")

    # Jensen-Shannon distance
    js_drift_metrics = drift_detector.calculate_drift(pre_defined_test="Jensen-Shannon")

    # Kullback-Leibler divergence
    logger.info("Kullback-Leibler: Setting num_buckets=5 for all numerical columns.")

    kl_drift_metrics = drift_detector.calculate_drift(
        pre_defined_test="Kullback-Leibler", num_buckets=5
    )
    # Kolmogorov-Smirnov p-values
    ks_drift_metrics = drift_detector.calculate_drift(
        pre_defined_test="Kolmogorov-Smirnov"
    )
    # Pandas summary
    summary_drift_metrics = drift_detector.calculate_drift(pre_defined_test="Summary")

    result = {
        # Top-level metrics
        str(feature + "_es_pvalue"): es_drift_metrics["values"][feature]
        for feature in es_drift_metrics["values"].keys()
    }

    result.update(
        {
            # Top-level metrics
            str(feature + "_js_distance"): js_drift_metrics["values"][feature]
            for feature in js_drift_metrics["values"].keys()
        }
    )
    result.update(
        {
            # Top-level metrics
            str(feature + "_kl_divergence"): kl_drift_metrics["values"][feature]
            for feature in kl_drift_metrics["values"].keys()
        }
    )
    result.update(
        {
            # Top-level metrics
            str(feature + "_ks_pvalue"): ks_drift_metrics["values"][feature]
            for feature in ks_drift_metrics["values"].keys()
        }
    )

    # Add Vanilla DriftDetector output
    result["data_drift"] = [
        es_drift_metrics,
        js_drift_metrics,
        kl_drift_metrics,
        ks_drift_metrics,
        summary_drift_metrics,
    ]
    return result


def execute_performance_classification(job_json, dataframe) -> dict:
    """
    Statistical Performance
    """
    """A function to extract input schema from job JSON.
    Args:
        job_json (str): job JSON in a string format.
    """

    # Extract input schema from job JSON
    input_schema_definition = infer.extract_input_schema(job_json)

    logger.info("Input schema definition: %s", input_schema_definition)

    # Get monitoring parameters from schema
    global MONITORING_PARAMETERS
    MONITORING_PARAMETERS = infer.set_monitoring_parameters(
        schema_json=input_schema_definition, check_schema=True
    )

    logger.info("label_column: %s", MONITORING_PARAMETERS["label_column"])
    logger.info("score_column: %s", MONITORING_PARAMETERS["score_column"])

    """
    --- end init
    """

    # Initialize ModelEvaluator
    model_evaluator = performance.ModelEvaluator(
        dataframe=dataframe,
        score_column=MONITORING_PARAMETERS["score_column"],
        label_column=MONITORING_PARAMETERS["label_column"],
    )

    # Compute classification metrics
    classification_metrics = model_evaluator.evaluate_performance(
        pre_defined_metrics="classification_metrics"
    )

    result = {
        # Top-level metrics
        "accuracy": classification_metrics["values"]["accuracy"],
        "precision": classification_metrics["values"]["precision"],
        "recall": classification_metrics["values"]["recall"],
        "auc": classification_metrics["values"]["auc"],
        "f1_score": classification_metrics["values"]["f1_score"],
        "confusion_matrix": classification_metrics["values"]["confusion_matrix"],
        # Vanilla ModelEvaluator output
        "performance": [classification_metrics],
    }
    return result


def execute_stability_analysis(job_json, df_baseline, df_sample):
    """
    Stability
    """
    """
    A function to extract input schema from job JSON.
    Args:
        job_json (str): job JSON in a string format.
    """

    # Extract input schema from job JSON
    input_schema_definition = infer.extract_input_schema(job_json)
    logger.info("Input schema definition: %s", input_schema_definition)

    # Get monitoring parameters from schema
    global MONITORING_PARAMETERS
    MONITORING_PARAMETERS = infer.set_monitoring_parameters(
        schema_json=input_schema_definition, check_schema=True
    )

    logger.info("predictors: %s", MONITORING_PARAMETERS["predictors"])
    logger.info("feature_dataclass: %s", MONITORING_PARAMETERS["feature_dataclass"])
    logger.info("special_values: %s", MONITORING_PARAMETERS["special_values"])
    logger.info("score_column: %s", MONITORING_PARAMETERS["score_column"])
    logger.info("label_column: %s", MONITORING_PARAMETERS["label_column"])
    logger.info("weight_column: %s", MONITORING_PARAMETERS["weight_column"])

    """
    --- end init
    """
    score_column = MONITORING_PARAMETERS["score_column"]
    predictors = MONITORING_PARAMETERS["predictors"]

    # Initialize StabilityMonitor
    stability_monitor = stability.StabilityMonitor(
        df_baseline=df_baseline,
        df_sample=df_sample,
        predictors=predictors,
        feature_dataclass=MONITORING_PARAMETERS["feature_dataclass"],
        special_values=MONITORING_PARAMETERS["special_values"],
        score_column=score_column,
        label_column=MONITORING_PARAMETERS["label_column"],
        weight_column=MONITORING_PARAMETERS["weight_column"],
    )

    # Set default n_groups for each predictor and score
    n_groups = {}
    for feature in MONITORING_PARAMETERS["numerical_columns"] + [
        MONITORING_PARAMETERS["score_column"]
    ]:
        # If a feature has more than 1 unique value, set n_groups to 2; else set to 1
        feature_has_distinct_values = int(
            (min(df_baseline[feature]) != max(df_baseline[feature]))
        )
        n_groups[feature] = 1 + feature_has_distinct_values

    # Compute stability metrics
    stability_metrics = stability_monitor.compute_stability_indices(
        n_groups=n_groups, group_cuts={}
    )

    result = {
        # Top-level metric
        str(score_column + "_PSI"): stability_metrics["values"][score_column][
            "stability_index"
        ]
    }

    result.update(
        # Top-level metrics
        {
            str(predictor + "_CSI"): stability_metrics["values"][predictor][
                "stability_index"
            ]
            for predictor in predictors
        }
    )
    # Add StabilityMonitor Vanilla output
    result["stability"] = [stability_metrics]
    return result


def execute_bias_comprehensive(job_json, dataframe) -> dict:
    """
    Ethical Fairness
    """
    """A function to extract input schema from job JSON.
     Args:
         job_json (str): job JSON in a string format.
     """

    # Extract input schema from job JSON
    input_schema_definition = infer.extract_input_schema(job_json)
    logger.info("Input schema definition: %s", input_schema_definition)

    # Get monitoring parameters from schema
    global MONITORING_PARAMETERS
    MONITORING_PARAMETERS = infer.set_monitoring_parameters(
        schema_json=input_schema_definition, check_schema=True
    )

    logger.info("label_column: %s", MONITORING_PARAMETERS["label_column"])
    logger.info("score_column: %s", MONITORING_PARAMETERS["score_column"])
    logger.info(
        "protected_classes: %s", str(MONITORING_PARAMETERS["protected_classes"])
    )

    """
    --- end init
    """
    if MONITORING_PARAMETERS["protected_classes"] == []:
        raise ValueError("Input Schema contains no Protected Classes!")

    result = {"bias": []}
    for protected_class in MONITORING_PARAMETERS["protected_classes"]:
        # Initialize BiasMonitor
        bias_monitor = bias.BiasMonitor(
            dataframe=dataframe,
            score_column=MONITORING_PARAMETERS["score_column"],
            label_column=MONITORING_PARAMETERS["label_column"],
            protected_class=protected_class,
            reference_group=None,
        )

        # Compute aequitas_bias (disparity) metrics
        bias_metrics = bias_monitor.compute_bias_metrics(
            pre_defined_test="aequitas_bias", thresholds={"min": 0.8, "max": 1.25}
        )
        # Add BiasMonitor Vanilla output
        result["bias"].append(bias_metrics)

        # Top-level metrics
        for group_dict in bias_metrics["values"]:
            result.update(
                {
                    str(
                        protected_class
                        + "_"
                        + group_dict["attribute_value"]
                        + "_statistical_parity"
                    ): group_dict["ppr_disparity"],
                    str(
                        protected_class
                        + "_"
                        + group_dict["attribute_value"]
                        + "_impact_parity"
                    ): group_dict["pprev_disparity"],
                }
            )

        # Compute aequitas_group (Group) metrics
        group_metrics = bias_monitor.compute_group_metrics(
            pre_defined_test="aequitas_group",
        )

        # Add BiasMonitor Vanilla output
        result["bias"].append(group_metrics)

    return result

