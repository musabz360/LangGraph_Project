


def create_lead_node(state: GraphState) -> GraphState:
    print("Running create_lead_node")
    user_name = state.get("user_name")
    # Assuming create_lead takes a name and maybe other initial data
    lead_info = create_lead({"name": user_name})
    return {"lead_info": lead_info}
