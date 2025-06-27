# CrewAI CDK Deployer

This project uses a \*\*multi-agent AI system powered by \*\*[**CrewAI**](https://github.com/joaomdmoura/crewAI) to automatically plan, generate, and deploy AWS infrastructure using the **AWS CDK (Cloud Development Kit)** with approval workflows.

---

## 🤖 Agents

### 1. PlannerAgent

* Interprets natural language infra goals.
* Plans infrastructure components (VPC, ECS, RDS, etc).

### 2. CDKWriterAgent

* Generates CDK code in Python.
* Writes to `cdk/stacks/infra_stack.py`.

### 3. CDKExecutorAgent

* Asks for deployment approval.
* Runs `cdk synth` and `cdk deploy` after approval.

---

## 🧱 Tech Stack

| Component       | Tool                                     |
| --------------- | ---------------------------------------- |
| Agent Framework | CrewAI                                   |
| LLM             | Claude-compatible (via Anthropic API)    |
| IaC Tool        | AWS CDK (Python)                         |
| Approval Logic  | CLI prompt (can extend to Slack/Webhook) |

---

## 🚀 Quickstart

### 1. Clone and Install

```bash
git clone https://github.com/ritesh-tiwary/crewai-cdk-deployer.git
cd crewai-cdk-deployer
pip install -r requirements.txt
```

### 2. Set up AWS CDK

```bash
cd cdk
cdk init app --language python
pip install -r requirements.txt
```

### 3. Run the AI Agent System

```bash
cd ..
python main.py
```

You'll be prompted to approve the deployment before it runs `cdk deploy`.

---

## ✅ Example Prompt

> "Create an ECS Fargate service with a public-facing FastAPI app and an RDS Postgres instance."

The system will:

* Plan the infra.
* Generate CDK Python code.
* Request deployment approval.

---

## 🔐 Approval Workflow

The deployment agent will pause and request explicit user input:

```
🛡️  Approval required to deploy to AWS via CDK.
Approve deployment? (yes/no):
```

✅ Planned support for Slack or webhook-based approvals.

---

## 📌 To Do

* Claude API integration (via `anthropic` SDK)
* Slack approval hook
* GitHub Actions CI/CD integration

---

## 📄 License

MIT License

---

## 🤝 Contributing

Feel free to fork this repo, suggest improvements, or open issues. AI-driven DevOps automation is the future—help shape it!
