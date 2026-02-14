AI VIDEO GENERATION ASSISTANT – TECHNICAL DOCUMENTATION


1. PROJECT STRUCTURE AND HOW TO RUN
--------------------------------------------------------
This project includes the following files:
- main.py – key point of the application: takes user input, executes prompt generation, saves output
- agent.py – implements the core logic responsible for communicating with language model
- prompts.py - stores instructions defining the AI agent behavior and generation rules
- config.py – stores configuration values e.g. file paths
- aiagent_output.txt – sample output
- .env.example – template file providing the OpenAI API key


2. HOW TO RUN THE AGENT
--------------------------------------------------------
1.1 install python

1.2 open command line (cmd) and install dependencies
pip install openai pydantic python-dotenv
pip install rich fastapi uvicorn

1.3 create a .env file based on .env.example and add your api key
OPENAI_API_KEY=your_key_here

1.4 open config.py and set the output file path

1.5 run the application
python main.py

1.6 enter a short scene description, e.g. "A woman walking her dog."
The generated prompts will be saved to the location defined in config.py.


3. HOW THE AGENT WORKS
--------------------------------------------------------
The agent converts a short scene description (e.g. "A woman walking her dog.") into 10–15 structured cinematic prompts. Process overview:
2.1 the user enters a short scene description

2.2 the agent sends to the language model a system instruction defining the AI’s professional role the user’s description

2.3 the model generates a numbered sequence of detailed prompts

2.4 the output is saved to a file

The system prompt instructs the model to behave like a small creative film team including a director, cinematographer, screenwriter, art director and camera operator. This ensures structured and cinematic output.


4. HOW SCENE AND CHARACTER CONSISTENCY IS ENSURED
--------------------------------------------------------
Consistency is achieved through strict instructions and detailed prompting. The agent enforces:
- one character
- one place
- one time of day
- one visual style
- no outfit changes

The model is also instructed to maintain narrative progression and behave like:
- ai video planning agent
- film director
- cinematographer
- screenwriter
- storyboard artist
- art director
- camera operator

This ensures the output feels like a continuous cinematic scene rather than unrelated images.


5. DESIGN ASSUMPTIONS I MADE
--------------------------------------------------------
The solution was built with the following assumptions:
- generated prompts will be used for realistic image or video creation
- the scene represents a short continuous moment
- simplicity and clarity are prioritized over technical complexity
- the architecture is modular and easy to understand with a clear separation between input handling and prompt definition


6. FUTURE DEVELOPMENT AND SCALING
--------------------------------------------------------
The solution can be extended by:
- returning structured json instead of plain text
- adding multi-step planning such as character or environment profiles
- converting the script into a web application
- adding automated validation to check scene consistency
- introducing logging and configuration management for production use


7. SUMMARY
--------------------------------------------------------
This video generation assistant transforms a simple text description into a coherent cinematic sequence of detailed keyframe prompts. It demonstrates:
- practical integration with a language model api
- role-based prompt engineering
- controlled narrative and visual consistency
- clean modular software design

The solution is simple, scalable and ready for further development or integration.
