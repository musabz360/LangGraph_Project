
def create_ticket_node(state: GraphState) -> GraphState:
    print("Running create_ticket_node")
    # create_ticket needs details about the query
    # This is a simplification; a real agent would get query details from user input
    ticket_info = create_ticket({"name": state.get("user_name"), "issue": "user_query_details"})
    return {"ticket_info": ticket_info}
