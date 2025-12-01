import os
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
import streamlit as st

# Initialize the LLM for the Marketing Research Agent
llm = ChatGroq(
    groq_api_key="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",
    model_name="llama3-70b-8192",  # Replace with the actual Marketing Research model name
)

# Define the Marketing Research Agent with a specific goal
marketing_agent = Agent(
    role='Marketing Research Agent',
    goal='Provide in-depth insights and analysis on marketing trends, strategies, consumer behavior, and market research.',
    backstory=(
        "You are a Marketing Research Agent, skilled in gathering and analyzing information on market trends, "
        "consumer behavior, competitive landscape, and marketing strategies. Your role is to answer marketing-related questions "
        "with a detailed, data-driven approach, and strictly limit responses to marketing research only."
    ),
    verbose=True,
    llm=llm,
)

def process_question_with_agent(question):
    # Describe the task for the agent
    task_description = f"Research and provide a detailed answer to the marketing question: '{question}'"
    
    # Define the task for the agent to generate a response to the question
    research_task = Task(
        description=task_description,
        agent=marketing_agent,
        human_input=False,
        expected_output="Answer related to marketing research"  # Placeholder for expected output
    )

    # Instantiate the crew with the defined agent and task
    crew = Crew(
        agents=[marketing_agent],
        tasks=[research_task],
        verbose=2,
    )

    # Get the crew to work on the task and return the result
    result = crew.kickoff()
    
    return result

# Set the title of your app with Markdown
st.markdown("<h1 style='text-align: center;'>Marketing Research Chatbot</h1>", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask a marketing research question:"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get the response from the Marketing Research Agent
    with st.spinner("Processing..."):
        response = process_question_with_agent(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
