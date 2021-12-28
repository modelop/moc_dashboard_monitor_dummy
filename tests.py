import main_dashboard_monitor as dashboard
import pandas as pd
import modelop.schema.infer as infer

if __name__ == "__main__":
    # Reading sample data in order to test first monitor
    data_frame_1 = pd.read_json('./sampleData/df_sample.json', lines=True)
    data_frame_2 = pd.read_json('./sampleData/df_baseline.json', lines=True)

    df_sample = pd.read_json('./sampleData/df_sample.json', lines=True)
    df_baseline = pd.read_json('./sampleData/df_baseline.json', lines=True)
    df_sample_scored = pd.read_json('./sampleData/df_sample_scored.json', lines=True)
    df_baseline_scored = pd.read_json('./sampleData/df_baseline_scored.json', lines=True)
    # Updated job, because input schema was all in UPPER CAPS
    jobAsString = open('./sampleData/jsonJobWithInputSchema_germanCredit_updated.json', 'r').read()
    json_job_dict = {"rawJson": jobAsString}
    input_schema = infer.extract_input_schema(json_job_dict)

    volumetrics_count_result = dashboard.execute_volumetrics_count(data_frame_1)
    print(f'Volumetrics count result {volumetrics_count_result}')

    input_volume = dashboard.execute_volumetrics_count_comparison(data_frame_1, data_frame_2)
    print(f'Volumetrics count comparison result {input_volume}')

    output_integrity = dashboard.execute_volumetrics_identifier_comparison(json_job_dict, df_sample_scored,
                                                                           df_baseline_scored)
    print(f'Volumetrics identifier comparison result {output_integrity}')

    data_drift = dashboard.execute_data_drift_comprehensive(json_job_dict, df_baseline_scored,
                                                            df_sample_scored)
    print(f'Data drift comprehensive result {data_drift}')

    statistical_performance = dashboard.execute_performance_classification(json_job_dict, df_sample_scored)
    print(f'Performance classification result {statistical_performance}')

    #I think requires scored, due to the input_schema
    stability_analysis = dashboard.execute_stability_analysis(json_job_dict, df_baseline_scored, df_sample_scored)
    print(f'Stability Analysis result {stability_analysis}')

    ethical_fairness = dashboard.execute_bias_comprehensive(json_job_dict,df_sample_scored)
    print(f'Bias comprehensive result {stability_analysis}')