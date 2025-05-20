def book_appointment_node(state: GraphState) -> GraphState:
    print("Running book_appointment_node")
    # book_appointment needs time and name, assuming state will have this
    # This is a simplification; a real agent would get time from user input
    appointment_info = book_appointment({"name": state.get("user_name"), "time": "user_specified_time"})
    return {"appointment_info": appointment_info}
