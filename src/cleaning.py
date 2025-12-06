import pandas as pd


class DataCleaner:

    def __init__(self, housing_data_file_path: str, unemployment_data_file_path: str):
        raw_data_housing = pd.read_csv(housing_data_file_path)
        raw_data_unemployment = pd.read_csv(unemployment_data_file_path, skiprows=2).dropna()
        self.clean_unemployment_data = self.unemployment_full_clean(raw_data_unemployment)
        self.clean_housing_data = self.housing_full_clean(raw_data_housing)
        
    
    @staticmethod
    def rename_unemployment_columns(unemployment_dataset: pd.DataFrame) -> pd.DataFrame: 
        """
        Changes the names of the columns on the unemployment dataset.
        
        :param unemployment_dataset: The unemployment dataset from the Bureau of Labor Statistics found in the README.md.
        :type unemployment_dataset: pd.DataFrame
        :return:
        :rtype: DataFrame
        """
        columns_to_rename = {
        "Area FIPS Code" : "FIPS_Code",
        "ST FIPS Code" : "State_FIPS_Code",
        "Civilian Labor Force" : "Civilian_Labor_Force",
        "Unemployment Rate" : "Unemployment_Rate",
        "LAUS Code" : "LAUS_Code"
        }
        return unemployment_dataset.rename(columns=columns_to_rename)

   
    @staticmethod
    def drop_n_values_for_unemployment_df(unemployment_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Drops rows with '(n)' value in the unemployment dataset.
        
        :param unemployment_dataset: The unemployment dataset from the Bureau of Labor Statistics found in the README.md.
        :type unemployment_dataset: pd.DataFrame
        :return:
        :rtype: DataFrame
        """
        df_to_clean = unemployment_dataset.copy()
        column_names = df_to_clean.columns
        for column in column_names:
            if df_to_clean[column].dtype == 'object':
                mask = df_to_clean[column].str.contains(r'\(n\)', na=False)
                df_to_clean = df_to_clean[~mask]
            else:
                pass
        return df_to_clean

    # changes all object columns to int64 type
    @staticmethod
    def unemployment_object_columns_to_int64(unemployment_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Typecasts appropriate columns in the unemployment dataset to int64 in the unemployment dataset.
        
        :param unemployment_dataset: The unemployment dataset from the Bureau of Labor Statistics found in the README.md.
        :type unemployment_dataset: pd.DataFrame
        :return:
        :rtype: DataFrame
        """
        
        df_to_clean = unemployment_dataset.copy()
        object_columns = ['Employment', 'Unemployment', "Unemployment_Rate", "Civilian_Labor_Force"]
        for column in object_columns:
            df_to_clean[column] = (df_to_clean[column]
                               .astype(str)
                               .str.replace(",", "")
                               .str.replace(".", "")
                               .astype(int))
        return df_to_clean
    
    @staticmethod
    def unemployment_float_cols_to_int64(unemployment_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Typecasts appropriate float columns to int64 in the unemployment dataset.
        
        :param unemployment_dataset: The unemployment dataset from the Bureau of Labor Statistics found in the README.md.
        :type unemployment_dataset: pd.DataFrame
        :return: 
        :rtype: DataFrame
        """
        data_to_clean = unemployment_dataset.copy()
        float_columns = ['State_FIPS_Code', 'FIPS_Code', 'Year', 'Month']
        for column in float_columns:
            data_to_clean[column] = data_to_clean[column].astype(int)
        return data_to_clean
    
    @staticmethod
    def rename_housing_value_columns(housing_value_dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Renames columns in the housing value dataset.
        
        :param housing_value_dataset: The housing value index dataset from the Federal Housing Finance Agency found in the README.md.
        :type housing_value_dataset: pd.DataFrame
        :return:
        :rtype: DataFrame
        """
        columns_to_rename = {
        "index_nsa" : "Not_Seasonally_Adjusted_Index",
        "index_sa" : "Seasonally_Adjusted_Index",
        "yr" : "Year",
        "qtr" : "Quarter",
        "metro_name" : "Metro_Name",
        "cbsa" : "CBSA"
        }
        return housing_value_dataset.rename(columns=columns_to_rename)

        
    def unemployment_full_clean(self, raw_unemployment_data: pd.DataFrame):
        """
        Serves as the wrapper function that cleans the unemployment dataset.
        
        :param self:
        :param raw_unemployment_data: The unemployment dataset from the Bureau of Labor Statistics found in the README.md.
        :type raw_unemployment_data: pd.DataFrame
        """
        renamed_columns = self.rename_unemployment_columns(raw_unemployment_data)
        no_nas = self.drop_n_values_for_unemployment_df(renamed_columns)
        object_now_int_columns = self.unemployment_object_columns_to_int64(no_nas)
        float_now_int_columns = self.unemployment_float_cols_to_int64(object_now_int_columns)
        return float_now_int_columns
    
    def housing_full_clean(self, housing_dataframe: pd.DataFrame) -> pd.DataFrame:
        renamed_housing_columns = self.rename_housing_value_columns(housing_dataframe)
        return renamed_housing_columns