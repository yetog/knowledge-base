# AI Engineering Foundations (Week 0-1)

## Course Introduction & Setup

### What Makes This Course Different?

This course bridges the gap between "playing with AI models" and "building real AI applications that people actually use." You'll learn to think like a product engineer who specializes in AI, not just a data scientist who can train models.

#### Project-Based Learning

Instead of abstract tutorials, you'll build 6+ complete applications:

- **Week 1**: LLM Playground (like ChatGPT's interface)
- **Week 2**: Customer Support Chatbot (fine-tuned for your business)
- **Week 3**: Web Research Agent (like Perplexity AI)
- **Week 4**: Deep Research Assistant (multi-step reasoning)
- **Week 5**: Voice-Enabled Image Generator (multimodal AI)
- **Week 6**: Your Choice Capstone Project

#### Production-Ready Tech Stack

You'll use the same tools that power real AI companies:

- **Hugging Face**: The GitHub of AI models (100,000+ models)
- **IONOS**: Enterprise cloud infrastructure for deployment
- **ElevenLabs**: State-of-the-art voice AI
- **n8n**: Workflow automation (connect AI to everything else)

### Course Philosophy: Build to Learn

**Traditional Approach**: Theory → Practice → Maybe Build Something  
 **Our Approach**: Build → Understand Why It Works → Build Better

Each week follows this pattern:

1. **Quick Intro**: Just enough theory to get started
2. **Hands-On Building**: Immediate project work
3. **Deep Dive**: Understand the "why" behind what you built
4. **Enhancement**: Add advanced features
5. **Deployment**: Make it available to real users

### Success Metrics

By the end of this course, you should be able to:

- **Technical Skills**: Deploy any Hugging Face model as a production API
- **System Design**: Architect multi-service AI applications
- **Problem Solving**: Break down complex AI problems into solvable pieces
- **Portfolio**: Have 6+ GitHub repos showcasing different AI capabilities
- **Career Readiness**: Confidently discuss AI engineering in interviews

---

## Week 0: Foundation Project

### Deploy DistilBERT Sentiment API

Build and deploy your first production AI API using DistilBERT for sentiment analysis. This project teaches you the fundamentals of model deployment, API development, and cloud hosting.

#### What You'll Build

- **FastAPI application** with sentiment analysis endpoints
- **Docker configuration** for containerized deployment
- **Web interface** for interactive testing
- **Public deployment** on IONOS cloud infrastructure

#### Key Technologies

- **DistilBERT**: Lightweight BERT model for sentiment analysis
- **FastAPI**: Modern Python web framework for APIs
- **Docker**: Containerization for consistent deployment
- **Ubuntu 22.04**: Production server environment

#### API Endpoints

- `GET /`: Service information
- `GET /health`: Health check endpoint
- `POST /analyze`: Analyze single text sentiment
- `POST /analyze-batch`: Analyze multiple texts
- `GET /demo`: Web interface for testing

#### Example Response

```json
{
 "text": "I love this AI course!",
 "sentiment": "POSITIVE",
 "confidence": 0.999,
 "scores": {
 "POSITIVE": 0.999,
 "NEGATIVE": 0.001
 },
 "processing_time": 0.045
}
```

---

## Week 1: LLM Playground

### Understanding Transformer Architecture

Before building with LLMs, you need to understand how they work. Transformers revolutionized AI by allowing models to process all words simultaneously and learn relationships between any two words, regardless of distance.

#### The Transformer Revolution

**Before Transformers**: Sequential Processing

```python
# How old RNN/LSTM models processed text
text = "The cat sat on the mat"
hidden_state = initial_state

for word in text.split():
 hidden_state = process_word(word, hidden_state)
 # Model can only "remember" through hidden_state
 # Long sequences → vanishing gradients
 # Can't process in parallel
```

**After Transformers**: Parallel Attention

```python
# How transformers process text
text = "The cat sat on the mat"
tokens = tokenize(text) # All at once
attention_weights = compute_attention(tokens) # All pairs simultaneously
output = apply_attention(tokens, attention_weights) # Parallel processing
```

#### Core Components

##### 1. Self-Attention Mechanism

The heart of transformers - allows each word to "attend" to every other word:

```python
# Simplified attention calculation
def attention(query, key, value):
 """
 Query: What am I looking for?
 Key: What does each position contain?
 Value: What information should I extract?
 """
 scores = query @ key.T # Dot product for similarity
 weights = softmax(scores) # Convert to probabilities
 output = weights @ value # Weighted sum of values
 return output
```

##### 2. Multi-Head Attention

Instead of one attention mechanism, use multiple "heads" to capture different types of relationships:

- **Head 1**: Subject-verb relationships
- **Head 2**: Adjective-noun pairs
- **Head 3**: Long-distance dependencies
- **Head 4**: Syntactic structure

#### Three Transformer Architectures

##### Encoder-Only (BERT-style)

- **Purpose**: Understanding and analyzing text
- **Use Cases**: Classification, question answering, sentiment analysis
- **Popular Models**: BERT, DistilBERT, RoBERTa, DeBERTa

##### Decoder-Only (GPT-style)

- **Purpose**: Text generation and completion
- **Use Cases**: Text generation, conversation, code completion
- **Popular Models**: GPT-2, GPT-3, GPT-4, LLaMA, Falcon

##### Encoder-Decoder (T5-style)

- **Purpose**: Text-to-text transformation
- **Use Cases**: Translation, summarization, question answering
- **Popular Models**: T5, BART, mT5, UL2

### Interactive LLM Playground Project

Build a comprehensive interface for testing and comparing different language models with parameter controls and token visualization.

#### Features

- **Model Selection**: Switch between GPT-2, Falcon-7B, LLaMA-2
- **Parameter Controls**: Adjust temperature, max tokens, top-p, top-k
- **Token Visualization**: See how text gets tokenized
- **Probability Display**: View token-by-token probabilities
- **Save/Share**: Export interesting model outputs

#### Key Concepts

##### Tokenization

How models break text into processable units:

- **BPE**: Byte Pair Encoding
- **WordPiece**: Google's tokenization method
- **SentencePiece**: Language-agnostic tokenization

##### Generation Parameters

- **Temperature**: Controls randomness (0.0 = deterministic, 1.0 = creative)
- **Top-p**: Nucleus sampling - consider tokens that make up p% of probability mass
- **Top-k**: Consider only the k most likely next tokens
- **Max Length**: Maximum number of tokens to generate

### Architecture Comparison Example

```python
from transformers import pipeline

# Encoder model (BERT) - great for understanding
classifier = pipeline("sentiment-analysis")
result = classifier("I love transformers!")
print(f"Classification: {result}")

# Decoder model (GPT-2) - great for generation
generator = pipeline("text-generation", model="gpt2")
result = generator("Transformers are revolutionary because", max_length=50)
print(f"Generation: {result[0]['generated_text']}")

# Encoder-Decoder (T5) - great for transformation
summarizer = pipeline("summarization", model="t5-small")
long_text = """
Transformers are a type of neural network architecture that has become 
the foundation of modern natural language processing. They use attention 
mechanisms to process sequences of data, allowing them to understand 
context and relationships between words much better than previous approaches.
"""
result = summarizer(long_text, max_length=30)
print(f"Summary: {result[0]['summary_text']}")
```

---

## Key Learning Outcomes

After completing the foundations weeks, you will:

- **Understand** how transformer architectures work and why they're revolutionary
- **Deploy** your first production AI API with proper error handling and monitoring
- **Compare** different model architectures and choose the right one for specific tasks
- **Build** interactive interfaces for testing and exploring AI models
- **Master** the fundamentals of tokenization and text generation parameters

## Next Steps

With the foundations in place, you're ready to move on to:

- [Core Applications (Week 2-3)](core-applications.md) - Building chatbots and web research agents
- [Advanced Techniques (Week 4-5)](advanced-techniques.md) - Deep reasoning and multimodal AI
- [Capstone & Advanced (Week 6-7)](capstone-advanced.md) - Your independent project

---

## Resources

- [The Illustrated Transformer  (opens new window)](https://jalammar.github.io/illustrated-transformer/) – Visual explanation with diagrams
- [Attention Is All You Need  (opens new window)](https://arxiv.org/abs/1706.03762) – The original transformer paper
- [FastAPI Documentation  (opens new window)](https://fastapi.tiangolo.com/) – Comprehensive API framework guide
- [Hugging Face Course  (opens new window)](https://huggingface.co/course/chapter1/1) – Official introduction to NLP with Transformers
