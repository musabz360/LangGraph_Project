from typing import TypedDict, Annotated
from langgraph.graph import StateGraph




# Build the graph
builder = StateGraph(GraphState)

# Add nodes
builder.add_node("fetch_lead", fetch_lead_node)
builder.add_node("create_lead", create_lead_node)
builder.add_node("call_agent", call_agent)
builder.add_node("fetch_slots", fetch_slots_node)
builder.add_node("book_appointment", book_appointment_node)
builder.add_node("fetch_ticket", fetch_ticket_node)
builder.add_node("create_ticket", create_ticket_node)

# Set entry point: Start by fetching the lead
builder.set_entry_point("fetch_lead")

# Add conditional edges
builder.add_conditional_edges(
    "fetch_lead", # From node
    check_lead,   # Conditional function
    {
        "lead_exists": "call_agent", # If lead exists, go to agent
        "no_lead": "create_lead"     # If no lead, go to create lead
    }
)

# After creating a lead, go to the agent
builder.add_edge("create_lead", "call_agent")

# After calling the agent, route based on the task determined by the agent
builder.add_conditional_edges(
    "call_agent",
    route_agent_task,
    {
        "appointment_flow": "check_appointment_status", # If appointment task, check status (placeholder)
        "query_flow": "fetch_ticket",          # If query task, fetch ticket
        "unhandled": "call_agent" # Or handle unhandled tasks appropriately
    }
)

# Appointment flow:
# After checking appointment status (placeholder), fetch slots
builder.add_edge("check_appointment_status", "fetch_slots")

# After fetching slots, proceed to book the appointment (simplification)
builder.add_edge("fetch_slots", "book_appointment")

# Appointment flow ends after booking (simplification)
builder.set_finish_point("book_appointment")

# Ticket flow:
# After fetching ticket, check if it exists
builder.add_conditional_edges(
    "fetch_ticket",
    check_ticket_exists,
    {
        "ticket_exists": "__end__", # If ticket exists, end (or could go to a 'show_ticket_status' node)
        "no_ticket": "create_ticket"       # If no ticket, create ticket
    }
)

# Ticket flow ends after creating a ticket
builder.set_finish_point("create_ticket")

# Compile the graph
agent_prototype_graph = builder.compile()