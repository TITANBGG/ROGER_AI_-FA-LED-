---
license: apache-2.0
language:
  - code
programming_language:
  - Java
  - JavaScript
  - Python
---
# Dataset summary
This repository is dedicated to prompts used to perform in-context learning with [starcoder](https://huggingface.co/bigcode/starcoder). As a matter of fact, the model is an 
autoregressive language model that is trained on both code and natural language text. It can be turned into an AI-powered technical assistant by prepending conversations to 
its 8192-tokens context window.

# Format
The prompt is a .txt file which contains multiple conversations between a human and the assistant. Here is the format 

```
-----
Human: <instruction>
Assistant: <answer>

-----

Human: <instruction>
Assistant: <answer>
Human: <instruction>
Assistant: <answer>
.
.
.
-----
```

# Use cases
We want the technical assistant to cover a diverse set of use cases
- **Code-to-text**:
  - `What is the purpose of the following code?<code>`
  - `What is the bug in the following code?<code>`
- **Text-to-code**:
  - `Write/Design/Implement a function to <task>`
- **Code-to-code**:
  - `Translate this <code> from <programming language> to <programming language>.`
- **Text-to-text**:
  - `What is <technical concept>`
- **General-purpose Q&A**
  - `What are you?`
  - `What is your purpose?`

 # Scope of the work
 As a model designed for coding tasks, the user should not expect the model to output relevant answers when prompted with a general-purpose question. When it comes to coding 
 requests, the output of the model should be post-processed before testing them.