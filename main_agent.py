from rag_module import load_docs, create_vectorstore, get_rag_chain
from agents import user_behavior_agent, recommendation_agent, feedback_agent, content_generation_agent

def run_system(user_query, user_data, knowledge_path):
    docs = load_docs(knowledge_path)
    vectorstore = create_vectorstore(docs)
    rag_chain = get_rag_chain(vectorstore)

    user_profile = user_behavior_agent(user_data)
    recommendation = recommendation_agent(user_profile, rag_chain, user_query)
    feedback = feedback_agent(clicks=5)
    html_description = content_generation_agent(recommendation)

    return {
        "recommendation": recommendation,
        "feedback": feedback,
        "html": html_description
    }