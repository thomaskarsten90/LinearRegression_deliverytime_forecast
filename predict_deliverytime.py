import pandas as pd
import kagglehub
from geopy.distance import geodesic
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Download and load dataset
data = kagglehub.dataset_download("sujalsuthar/amazon-delivery-dataset")
df = pd.read_csv(data + "/amazon_delivery.csv")

# Strip spaces from all string entries
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Drop rows with missing 'Weather' values
df.dropna(subset=['Weather'], inplace=True)

# Fill missing 'Agent_Rating' with mean value
df['Agent_Rating'] = df['Agent_Rating'].fillna(df['Agent_Rating'].mean())

# Create 'Traffic_Weather_Interaction' column
df['Traffic_Weather_Interaction'] = df['Traffic'] + '_' + df['Weather']

# Convert time columns to datetime
df['Order_Time'] = pd.to_datetime(df['Order_Time'], format='%H:%M:%S', errors='coerce')
df['Pickup_Time'] = pd.to_datetime(df['Pickup_Time'], format='%H:%M:%S', errors='coerce')

# Calculate time difference in minutes
df['Order_Pickup_Diff'] = (df['Pickup_Time'] - df['Order_Time']).dt.total_seconds() / 60

# Extract day of the week and month from 'Order_Date'
df['Order_DayOfWeek'] = pd.to_datetime(df['Order_Date']).dt.dayofweek
df['Order_Month'] = pd.to_datetime(df['Order_Date']).dt.month

# Define function to get period of the day
def get_period_of_day(hour):
    if 5 <= hour < 12:
        return 'Manhã'
    elif 12 <= hour < 18:
        return 'Tarde'
    else:
        return 'Noite'

# Apply function to get period of the day
df['Order_Period'] = df['Order_Time'].dt.hour.apply(get_period_of_day)

# Calculate distance using geopy
df['Distance'] = df.apply(lambda row: geodesic((row['Store_Latitude'], row['Store_Longitude']), 
                                               (row['Drop_Latitude'], row['Drop_Longitude'])).km, axis=1)

# Normalize delivery time
df['Normalized_Delivery_Time'] = df['Delivery_Time'] / (df['Order_Pickup_Diff'] + 1)

# Define function to get season
def get_season(month):
    if month in [12, 1, 2]:
        return 'inverno'
    elif month in [3, 4, 5]:
        return 'primavera'
    elif month in [6, 7, 8]:
        return 'verao'
    else:
        return 'outono'

# Apply function to get season
df['Order_Season'] = df['Order_Month'].apply(get_season)

# Calculate wait time in minutes
df['Wait_Time'] = (df['Pickup_Time'] - df['Order_Time']).dt.total_seconds() / 60

# Define numeric and categorical columns
numeric_columns = ['Agent_Age', 'Agent_Rating', 'Order_Pickup_Diff', 'Order_DayOfWeek', 'Order_Month', 'Distance', 'Normalized_Delivery_Time', 'Wait_Time']
categorical_columns = ['Weather', 'Traffic', 'Vehicle', 'Area', 'Category', 'Traffic_Weather_Interaction', 'Order_Period', 'Order_Season']

# Preprocessing
preprocessamento = df.copy()
present_numeric = [col for col in numeric_columns if col in preprocessamento.columns]
present_categorical = [col for col in categorical_columns if col in preprocessamento.columns]

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, present_numeric),
        ('cat', categorical_transformer, present_categorical)
    ]
)

X = preprocessamento[present_numeric + present_categorical]
y = df['Delivery_Time']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define and train model
def train_and_evaluate_model(model, X_train, y_train, X_test, y_test):
    pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', model)])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mae, r2, y_pred

models = {
    'Random Forest': RandomForestRegressor(
        max_depth=None, 
        max_features='sqrt', 
        min_samples_leaf=1, 
        min_samples_split=2, 
        n_estimators=200, 
        random_state=42
    )
}

results = {}
predictions = {}

for name, model in models.items():
    try:
        mae, r2, y_pred = train_and_evaluate_model(model, X_train, y_train, X_test, y_test)
        results[name] = {'Mean Absolute Error': mae, 'R2 Score': r2}
        predictions[name] = y_pred
    except Exception as e:
        results[name] = {'Error': str(e)}

results_df = pd.DataFrame.from_dict(results, orient='index').reset_index()
results_df.columns = ['Model'] + list(results_df.columns[1:])

if 'Mean Absolute Error' in results_df and 'R2 Score' in results_df:
    results_df_cleaned = (
        results_df[['Model', 'Mean Absolute Error', 'R2 Score']]
        .dropna()
        .sort_values(by='Mean Absolute Error')
    )
    print(results_df_cleaned)
else:
    print("Nenhuma métrica calculada. Verifique os erros nos modelos.")

rf_predictions = predictions['Random Forest']

y_test_reset = y_test.reset_index(drop=True)
X_test_reset = X_test.reset_index(drop=True)

y_pred_df = pd.DataFrame(rf_predictions, columns=['Delivery_Time_predicted'])

result_df = pd.concat([X_test_reset, y_test_reset, y_pred_df], axis=1)

result_df.to_excel('resultados_prediction.xlsx', index=False)