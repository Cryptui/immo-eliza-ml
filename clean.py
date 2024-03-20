import pandas as pd

def fill_missing_values(df, value=-1, replacements={'Missing': 'missing_info', 'MISSING': 'missing_info'}):
    """
    Fill missing values in a DataFrame.

    Parameters:
    - df: DataFrame to process.
    - value: Value to fill in for missing numeric data.
    - replacements: Dictionary mapping original missing value indicators to replacements.
    
    Returns:
    - DataFrame with missing values filled/replaced.
    """
    df_filled = df.fillna(value)
    for original, replacement in replacements.items():
        df_filled.replace(original, replacement, inplace=True)
    return df_filled

def calculate_bounds(data, feature):
    """
    Calculate lower and upper bounds for outlier detection.

    Parameters:
    - data: DataFrame containing the data.
    - feature: The name of the feature to calculate bounds for.

    Returns:
    - A tuple of (lower_bound, upper_bound).
    """
    Q1 = data[feature].quantile(0.25)
    Q3 = data[feature].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return lower_bound, upper_bound

def remove_outliers(df, features_to_check=['price', 'surface_land_sqm', 'total_area_sqm', 'nbr_bedrooms']):
    """
    Remove outliers from a DataFrame based on IQR for specified features.

    Parameters:
    - df: DataFrame from which to remove outliers.
    - features_to_check: List of features to check for outliers.

    Returns:
    - Tuple of (DataFrame with outliers removed, Dictionary of removed outliers count per feature).
    """
    df_clean = df.copy()
    removed_outliers = {}
    for feature in features_to_check:
        lower_bound, upper_bound = calculate_bounds(df_clean, feature)
        before_removal = len(df_clean)
        df_clean = df_clean[(df_clean[feature] >= lower_bound) & (df_clean[feature] <= upper_bound)]
        after_removal = len(df_clean)
        removed_outliers[feature] = before_removal - after_removal
    return df_clean, removed_outliers

def clean_data(input_df, features_to_check=['price', 'surface_land_sqm', 'total_area_sqm', 'nbr_bedrooms'], replacements={'Missing': 'missing_info', 'MISSING': 'missing_info'}):
    """
    Comprehensive cleaning of DataFrame.

    Parameters:
    - input_df: DataFrame to clean.
    - features_to_check: Features to check for outliers.
    - replacements: Missing value indicators and their replacements.

    Returns:
    - Cleaned DataFrame and dictionary of removed outliers count per feature.
    """
    df_filled = fill_missing_values(input_df, replacements=replacements)
    df_cleaned, removed_outliers = remove_outliers(df_filled, features_to_check)
    return df_cleaned, removed_outliers

if __name__ == "__main__":
    input_path = 'data/data_20240313_cleaned.csv'
    output_path = 'data/data_20240313_modified.csv'
    # Load the data into a DataFrame
    df_to_clean = pd.read_csv(input_path, decimal=',')
    # Clean the data
    cleaned_df, removed_outliers = clean_data(df_to_clean)
    # Save the modified DataFrame to a CSV file
    cleaned_df.to_csv(output_path, index=False)
    print(f"Modified data saved to: {output_path}")
    # Print the number of outliers removed and new range per variable
    for feature, count in removed_outliers.items():
        print(f"Outliers removed for {feature}: {count}")
        print(f"New range for {feature}: {cleaned_df[feature].min()} - {cleaned_df[feature].max()}")
