from sklearn.externals import joblib

# Save Model
joblib.dump(model, 'bitcoin_price_model.pkl')

# Upload Model to Oracle Cloud (simplified for illustration)
def deploy_model_to_oracle(model_file):
    # Placeholder for cloud upload logic
    pass
