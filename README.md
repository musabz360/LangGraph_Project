# LangGraph Project with Tool Stubs

This repository contains a LangGraph project with modular structure and tool stubs for three main workflows:
1. Appointments
2. Leads
3. Tickets

## Project Structure

```
langgraph_project/
├── src/
│   ├── agents/       # Agent definitions
│   ├── graphs/       # LangGraph workflow definitions
│   ├── tools/        # Tool implementations for different domains
│   │   ├── appointments/
│   │   ├── leads/
│   │   └── tickets/
│   ├── utils/        # Shared utilities
|   ├── api/          # Fast Api
└── tests/            # Test files
```

## Tool Groups and Stubs

### Appointments
- `fetch_slots`: Retrieve available appointment slots
- `book_appointment`: Book an appointment

### Leads
- `fetch_lead`: Retrieve lead information
- `create_lead`: Create a new lead

### Tickets
- `fetch_ticket`: Retrieve ticket information
- `create_ticket`: Create a new support ticket

## Getting Started

1. Clone this repository
2. Install dependencies:
   ```
   pip install -e .
   ```
3. Run the example:
   ```
   python -m src.examples.run_example