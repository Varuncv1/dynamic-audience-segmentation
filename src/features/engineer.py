def extract_features(session_dict):
    return {
        "total_items": session_dict["total_items"],
        "total_value": session_dict["total_value"],
        "num_products": session_dict["num_products"],
        "session_duration": session_dict["session_duration_mins"],
        "hour_of_day": session_dict["hour_of_day"],
        # any extras you added in the notebook
    }
