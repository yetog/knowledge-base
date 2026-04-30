---
tags:
  - ai
  - course
  - learning
---

# Core Applications (Week 2-3)

## Overview

Weeks 2-3 focus on building practical AI applications that solve real business problems. You'll learn advanced fine-tuning techniques, agent frameworks, and workflow automation to create production-ready systems.

---

## Week 2: Customer Support Chatbot

### Fine-tuning Fundamentals

Learn the difference between pre-training, fine-tuning, and prompt engineering. Understanding when and how to fine-tune effectively separates hobbyists from professional AI engineers.

#### The Training Hierarchy

##### Pre-training (Foundation Learning)

```python
# Pre-training: Learning language from massive text corpora
# This happens once and costs millions of dollars

corpus = [
 "The internet contains billions of web pages...",
 "Machine learning is a subset of artificial intelligence...",
 "Customer service representatives help customers...",
 # ... billions more sentences
]

# Model learns:
# - Grammar and syntax
# - General knowledge 
# - Basic reasoning
# - Language patterns

# Result: A model that understands language but isn't specialized
```

##### Fine-tuning (Specialization)

```python
# Fine-tuning: Adapting to specific tasks with smaller datasets
# This is what we do as AI engineers

task_specific_data = [
 {"input": "I need help with my order", 
 "output": "I'd be happy to help you with your order. Can you provide your order number?"},
 {"input": "My product is defective", 
 "output": "I'm sorry to hear about the defective product. Let's get this resolved for you..."},
 # ... thousands more examples
]

# Model learns:
# - Task-specific patterns
# - Domain vocabulary
# - Appropriate tone and style
# - Specific behaviors
```

#### Parameter-Efficient Fine-tuning (PEFT)

Modern fine-tuning techniques that update only a small subset of model parameters, offering significant advantages:

```python
from peft import LoraConfig, get_peft_model

# Load base model
base_model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Configure LoRA (Low-Rank Adaptation)
lora_config = LoraConfig(
 r=16, # Rank of adaptation
 lora_alpha=32, # LoRA scaling parameter
 target_modules=["c_attn", "c_proj"], # Which layers to adapt
 lora_dropout=0.1, # Dropout for LoRA layers
)

# Apply LoRA to model
model = get_peft_model(base_model, lora_config)

# Output: trainable params: 294,912 || all params: 355,118,080 || trainable%: 0.08%
```

#### Benefits of PEFT

- **100x fewer trainable parameters** - Dramatically reduces compute requirements
- **Faster training and less memory** - Can train on smaller GPUs
- **Multiple adapters** - One base model, many specialized tasks
- **Prevents catastrophic forgetting** - Preserves original model capabilities

### Customer Support Chatbot Project

Build a production-ready customer support chatbot with fine-tuned conversation AI, context handling, and role-based responses.

#### Key Features

- **Fine-tuned responses** - Trained on specific FAQ dataset
- **Conversation context** - Maintains history across turns
- **Escalation handling** - Knows when to transfer to humans
- **Sentiment awareness** - Adjusts tone based on customer emotion
- **Multi-turn conversations** - Handles complex dialog flows

#### Data Preparation Workflow

```python
def prepare_conversation_data(data_path):
 """
 Prepare conversational data for fine-tuning
 Expected format: JSON with customer/agent turns
 """
 
 with open(data_path, 'r') as f:
 conversations = json.load(f)
 
 # Convert to training format
 training_data = []
 
 for conversation in conversations:
 # Build conversation history
 context = ""
 for turn in conversation['turns']:
 if turn['speaker'] == 'customer':
 context += f"Customer: {turn['text']}\n"
 else: # agent
 # Create training example
 input_text = context + "Agent:"
 output_text = turn['text']
 
 training_data.append({
 'input': input_text,
 'output': output_text,
 'conversation_id': conversation['id']
 })
 
 context += f"Agent: {turn['text']}\n"
 
 return training_data
```

#### Evaluation Metrics

- **Perplexity** - How well the model predicts responses
- **Response Quality** - Human evaluation of helpfulness
- **Conversation Success Rate** - Percentage of issues resolved
- **Escalation Rate** - When chatbot transfers to humans

---

## Week 3: Ask-the-Web Agent

### Agent Frameworks and Tool Orchestration

Build AI agents that can access external tools and APIs to gather information, similar to Perplexity AI or research assistants.

#### Agent Architecture Patterns

##### Planner-Worker Pattern

```python
class ResearchAgent:
 def __init__(self, llm, tools):
 self.llm = llm
 self.tools = tools
 self.memory = []
 
 def research(self, query):
 # 1. Plan the research approach
 plan = self.create_research_plan(query)
 
 # 2. Execute each step
 for step in plan:
 result = self.execute_step(step)
 self.memory.append(result)
 
 # 3. Synthesize findings
 report = self.synthesize_report(query, self.memory)
 return report
 
 def create_research_plan(self, query):
 prompt = f"""
 Break down this research query into specific steps:
 Query: {query}
 
 Available tools: web_search, summarize, fact_check
 
 Create a step-by-step plan:
 """
 
 response = self.llm.generate(prompt)
 return self.parse_plan(response)
```

#### Tool Integration with LangChain

```python
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.tools import DuckDuckGoSearchRun

# Define tools
search_tool = Tool(
 name="web_search",
 description="Search the web for current information",
 func=DuckDuckGoSearchRun().run
)

summarize_tool = Tool(
 name="summarize",
 description="Summarize long text content",
 func=summarization_pipeline
)

fact_check_tool = Tool(
 name="fact_check",
 description="Verify factual claims",
 func=fact_verification_function
)

tools = [search_tool, summarize_tool, fact_check_tool]
```

#### Web Search and Citation

```python
class WebSearchAgent:
 def search_with_citations(self, query):
 # Search multiple sources
 search_results = self.multi_source_search(query)
 
 # Extract and rank information
 ranked_info = self.rank_by_relevance(search_results, query)
 
 # Generate response with citations
 response = self.generate_cited_response(ranked_info, query)
 
 return response
 
 def generate_cited_response(self, sources, query):
 prompt = f"""
 Answer the query using the provided sources. Include citations [1], [2], etc.
 
 Query: {query}
 
 Sources:
 {self.format_sources(sources)}
 
 Provide a comprehensive answer with proper citations.
 """
 
 return self.llm.generate(prompt)
```

### n8n Workflow Automation

Integrate your AI agent with n8n to create automated workflows that connect to external services and databases.

#### Automated Research Pipeline

- **Trigger**: Email with research request
- **Agent**: Performs web research and analysis
- **Storage**: Saves results to Google Sheets
- **Notification**: Sends completion email with report

#### Workflow Configuration

```json
{
 "nodes": [
 {
 "name": "Email Trigger",
 "type": "Gmail Trigger",
 "parameters": {
 "filters": {
 "subject": "Research Request:"
 }
 }
 },
 {
 "name": "AI Research Agent",
 "type": "HTTP Request",
 "parameters": {
 "url": "https://your-vm.ionos.com/research",
 "method": "POST",
 "body": {
 "query": "{{ $json.body }}"
 }
 }
 },
 {
 "name": "Save to Sheets",
 "type": "Google Sheets",
 "parameters": {
 "operation": "append",
 "sheetId": "your-sheet-id",
 "values": [
 "{{ new Date().toISOString() }}",
 "{{ $json.query }}",
 "{{ $json.report }}"
 ]
 }
 }
 ]
}
```

### Ask-the-Web Agent Project

Build a Perplexity-style research agent with automated report generation and workflow integration.

#### Project Features

- **Multi-source search** - DuckDuckGo, Tavily API integration
- **Intelligent summarization** - Extract key information from web content
- **Citation tracking** - Maintain source attribution
- **Automated workflows** - n8n integration for reporting
- **Follow-up questions** - Handle iterative research

#### Example Interaction

```text
User: "What are the latest trends in renewable energy?"

Agent:
1. Searching for recent renewable energy developments...
2. Analyzing market reports and news articles...
3. Extracting key trends and statistics...
4. Generating comprehensive report with citations...

Report: Based on recent research, here are the key trends in renewable energy:

**Solar Power Growth**: Solar installations increased 25% in 2024, driven by 
decreasing costs and improved efficiency [1][2].

**Battery Storage Expansion**: Energy storage capacity doubled, making renewable 
energy more reliable [3][4].

**Green Hydrogen Development**: Major investments in hydrogen production for 
industrial applications [5][6].

Sources:
[1] International Energy Agency - Solar Report 2024
[2] Bloomberg New Energy Finance - Market Outlook
[3] Energy Storage Association - Annual Survey
[4] McKinsey Energy Insights - Battery Trends
[5] Hydrogen Council - Industry Report
[6] Clean Energy Wire - Market Analysis

Follow-up: Would you like me to dive deeper into any specific trend?
```

---

## Key Learning Outcomes

After completing weeks 2-3, you will:

- **Master fine-tuning** - Understand full fine-tuning vs PEFT techniques
- **Build conversational AI** - Create context-aware chatbots for business use
- **Architect agent systems** - Design multi-tool AI agents with proper orchestration
- **Integrate workflows** - Connect AI to external services using n8n automation
- **Handle citations** - Build trustworthy systems that provide source attribution
- **Deploy production systems** - Scale applications for real-world usage

## Technical Skills Developed

- **Parameter-Efficient Fine-tuning** - LoRA, adapters, and PEFT techniques
- **LangChain Framework** - Agent orchestration and tool integration
- **Web Search APIs** - DuckDuckGo, Tavily, and content extraction
- **Workflow Automation** - n8n configuration and API integration
- **Conversation Design** - Context handling and multi-turn dialog
- **Information Synthesis** - Combining multiple sources with proper attribution

## Next Steps

With core applications mastered, you're ready for:

- [Advanced Techniques (Week 4-5)](advanced-techniques.md) - Deep reasoning and multimodal AI
- [Capstone & Advanced (Week 6-7)](capstone-advanced.md) - Independent projects and advanced topics

---

## Resources

- [Hugging Face Fine-tuning Guide  (opens new window)](https://huggingface.co/docs/transformers/training) – Official fine-tuning documentation
- [LoRA Paper  (opens new window)](https://arxiv.org/abs/2106.09685) – Original LoRA research paper
- [LangChain Documentation  (opens new window)](https://docs.langchain.com/docs/) – Agent frameworks and tool integration
- [n8n Documentation  (opens new window)](https://docs.n8n.io/) – Workflow automation platform
