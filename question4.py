import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def preprocess_dataframe(df):
    # Separate numerical and categorical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    # Define preprocessing for numerical columns (impute missing values, then scale)
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    # Define preprocessing for categorical columns (impute missing values, then one-hot encode)
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ])

    # Apply the preprocessing steps
    df_preprocessed = preprocessor.fit_transform(df)

    # Convert the preprocessed array back to a DataFrame
    df_preprocessed = pd.DataFrame(df_preprocessed, columns=numerical_cols.tolist() + 
                                                       preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_cols).tolist())

    return df_preprocessed

# Example usage
data = {
    'age': [25, 30, 35, None, 45],
    'salary': [50000, 60000, 70000, 80000, None],
    'department': ['sales', 'engineering', 'engineering', 'sales', None]
}
df = pd.DataFrame(data)

cleaned_df = preprocess_dataframe(df)
print(cleaned_df)
