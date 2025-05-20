



def fetch_lead_node(state: GraphState) -> GraphState:
    print("Running fetch_lead_node")
    user_name = state.get("user_name")
    lead_info = fetch_lead({"name": user_name})
    return {"lead_info": lead_info}
