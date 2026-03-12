from planner_agent import planner_agent
from research_agent import research_agent
from writer_agent import writer_agent

print("Multi-Agent AI System")

while True:
    task = input("Enter a task (type exit to quit): ")

    if task.lower() == "exit":
        print("Goodbye!")
        break

    plan = planner_agent(task)
    research = research_agent(task)
    result = writer_agent(plan, research)

    print("AI System Output:")
    print(result)
