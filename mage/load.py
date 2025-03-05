#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(dataframe_list, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    #passage_df, weather_df, date_df, sensor_df
    tables = ['fact_table','dim_customer','dim_product','dim_order']
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    
    for index, df in enumerate(dataframe_list):
        table_id = f'de-test-project-444415.supply_chain.{tables[index]}'
        
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            df,
            table_id,
            if_exists='replace',  # Specify resolution policy if table name already exists
        )

