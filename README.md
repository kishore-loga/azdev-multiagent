# GitAgent

This repository contains implementations of single and multi-agent systems using Microsoft Azure AI Agent and Autogen frameworks.

## File Structure

```
┣ 📂MultiAgent
 ┃ ┣ 📂backend_dir
 ┃ ┃ ┗ 📜test-main.py
 ┃ ┣ 📂blog
 ┃ ┣ 📜multiAgentAutogen.ipynb
 ┃ ┗ 📜multiAgentAzAgent.ipynb
┣ 📂SingleAgent
 ┃ ┣ 📂blog
 ┃ ┗ 📜AzAiAgent.ipynb
┣ 📜.env
┣ 📜.gitignore
┗ 📜requirements.txt
```

## Description

### Single Agent

The `SingleAgent` directory contains an implementation of a single agent using the Microsoft Azure AI Agent service.

- `AzAiAgent.ipynb`: Jupyter notebook demonstrating the use of Microsoft Azure AI Agent.

### Multi Agent

The `MultiAgent` directory contains implementations of multi-agent systems.

- `multiAgentAzAgent.ipynb`: Jupyter notebook demonstrating the use of Autogen and Microsoft AI Agent service.
- `multiAgentAutogen.ipynb`: Jupyter notebook demonstrating the use of the Autogen framework with 5 agents.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/kishore-loga/azdev-multiagent.git
    ```
2. Navigate to the project directory:
    ```bash
    cd azdev-multiagent
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Open the Jupyter notebooks in the `SingleAgent` and `MultiAgent` directories to explore the implementations.

## References
Major inspirations were taken from the below two github repos.
https://github.com/kinfey/MultiAIAgent/tree/main
https://microsoft.github.io/autogen/0.2/docs/Examples/

## License

This project is licensed under the MIT License.
