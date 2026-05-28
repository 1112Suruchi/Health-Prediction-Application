# Health prediction logic

def predict_health(glucose, haemoglobin, cholesterol):

    if glucose > 140:
        return "Possible Diabetes Risk"

    elif haemoglobin < 12:
        return "Possible Anemia"

    elif cholesterol > 240:
        return "Possible Heart Disease Risk"

    else:
        return "Healthy"