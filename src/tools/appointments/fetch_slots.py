def fetch_slots_node(state: GraphState) -> GraphState:
    print("Running fetch_slots_node")
    # fetch_slots might not need input based on its definition, but let's pass lead_info just in case
    appointment_info = fetch_slots(state.get("lead_info", {}))
    return {"appointment_info": appointment_info}
