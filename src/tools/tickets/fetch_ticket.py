def fetch_ticket_node(state: GraphState) -> GraphState:
    print("Running fetch_ticket_node")
    # fetch_ticket needs a name or identifier
    ticket_info = fetch_ticket({"name": state.get("user_name")})
    return {"ticket_info": ticket_info}
  
