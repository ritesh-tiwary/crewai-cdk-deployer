import subprocess
from crewai.tools import tool
from crewai import Agent, Task, Crew

# --- Agent Definitions ---
planner = Agent(
    role="Planner",
    goal="Understand infrastructure requests and break them into CDK tasks",
    backstory="Cloud architect expert in AWS planning best practices.",
    verbose=True,
    allow_delegation=True
)

cdk_writer = Agent(
    role="CDK Engineer",
    goal="Generate AWS CDK code based on infrastructure plan",
    backstory="Writes Python CDK code securely and efficiently.",
    verbose=True
)

@tool
def deploy_with_approval():
    """Deploy AWS infrastructure using CDK after asking the user for approval."""
    print("\n🛡️  Approval required to deploy to AWS via CDK.")
    choice = input("Approve deployment? (yes/no): ")
    if choice.strip().lower() == "yes":
        print("\n🚀 Running CDK synth and deploy...\n")
        subprocess.run(["cdk", "synth"], check=True)
        subprocess.run(["cdk", "deploy", "--require-approval", "never"], check=True)
        return "✅ Deployment complete."
    else:
        return "❌ Deployment aborted by user."

cdk_executor = Agent(
    role="CDK Deployer",
    goal="Deploy CDK code to AWS after explicit approval",
    backstory="Deploys only when approved. Uses CDK CLI.",
    tools=[deploy_with_approval],  # ✅ Now it's a valid BaseTool
    verbose=True
)

# --- Task Definitions ---
plan_task = Task(
    description="Plan infrastructure for a public FastAPI app in ECS using Fargate and RDS Postgres.",
    expected_output="A step-by-step infrastructure plan listing all AWS resources to provision.",
    agent=planner
)

cdk_task = Task(
    description="Write Python AWS CDK code for VPC, ECS (Fargate), and RDS setup.",
    expected_output="A complete Python CDK code snippet stored in infra_stack.py that implements the planned infrastructure.",
    agent=cdk_writer
)

deploy_task = Task(
    description="Run 'cdk synth' and 'cdk deploy' after approval.",
    expected_output="Output logs confirming successful CDK synthesis and deployment, or user-declined deployment.",
    agent=cdk_executor
)

# --- Crew Execution ---
crew = Crew(
    agents=[planner, cdk_writer, cdk_executor],
    tasks=[plan_task, cdk_task, deploy_task],
    verbose=True
)

if __name__ == "__main__":
    print("\n🔧 Bootstrapping CrewAI AWS CDK Deployer")
    crew.kickoff()