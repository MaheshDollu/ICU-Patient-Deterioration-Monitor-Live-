import pandas as pd
import numpy as np
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

# Dummy generated data for demonstration
np.random.seed(42)
N = 1000
data = pd.DataFrame({
    "heart_rate": np.random.randint(50, 150, N),
    "spo2": np.random.randint(85, 100, N),
    "resp_rate": np.random.randint(10, 35, N),
    "temperature": np.round(np.random.uniform(36.0, 40.0, N), 1),
    "deterioration": np.random.binomial(1, 0.15, N)  # 15% positive class
})

X = data[["heart_rate", "spo2", "resp_rate", "temperature"]]
y = data["deterioration"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "model_serving/xgb_model.joblib")

# Evaluate
pred_probs = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, pred_probs)
print(f"Validation AUC: {auc:.3f}")
