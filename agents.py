def user_behavior_agent(user_data):
    return {
        "laptop_model": user_data.get("laptop_model", "Generic Model"),
        "interest": user_data.get("interest", "productivity"),
    }

def recommendation_agent(user_profile, rag_chain, query):
    response = rag_chain.run({"query": query})
    return response

def feedback_agent(clicks):
    if clicks > 3:
        return "👍 Positive"
    else:
        return "👎 Needs Improvement"

def content_generation_agent(description, model="T5"):
    return f"<p>{description}</p>"