
```markdown
# Chat with your Docs RAG Application

This project creates a completely Local "Chat with your Docs" retrieval augmented generation (RAG) application using Cohere's ⌘ R, served locally using Ollama. It also utilizes the Qdrant vector database (self-hosted) and Fastembed for embedding generation.

![Flow Diagram](https://raw.githubusercontent.com/horizonbymuneeb/Local-RAG-app-using-Cohere-s--R-and-Ollama/main/resources/flow.png)

## Key Features

- High precision on RAG and tool use tasks.
- Low latency and high throughput.
- Long 128k-token context length.
- Strong multilingual capabilities across 10 key languages.

## For Local PC and For Lightingai.com

## Installation

To set up the project, follow these steps:

1. Clone the repository.
2. Install the required dependencies.
3. Set up Cohere's ⌘ R locally using Ollama.
4. Configure the Qdrant vector database (self-hosted).(autoset in lightingai)
5. Use Fastembed for embedding generation.

To run Ollama, execute the following command:
```bash
ollama serve
```

After Ollama is running, execute the following command to start the Streamlit app:
```bash
streamlit run app.py
```

## Usage

To run the project, follow these steps:

1. Install Ollama by following the instructions on their [website](https://ollama.com/).
2. Install the Cohere model for Ollama. You can find the model installation instructions on Cohere's website.
3. Run Ollama by executing the following command:
```bash
ollama serve
   ```
4. After Ollama is running, execute the following command to start the Streamlit app:
```bash
pip install -r requirements.txt
```

```bash
streamlit run app.py
```
5. Open your web browser and navigate to the Streamlit app URL to interact with the "Chat with your Docs" application.

## Dependencies

- Cohere's ⌘ R
- Ollama
- Qdrant vector database
- Fastembed

## Contributing Guidelines

We welcome contributions to the project! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

## Code Standards

Please follow the coding standards and guidelines used in the project.

## Issues

If you encounter any issues or bugs, please report them [here](https://github.com/horizonbymuneeb/Local-RAG-app-using-Cohere-s--R-and-Ollama/issues).

## License

This project is licensed under the [MIT License](LICENSE).

```

This README provides a detailed overview of the project, including its features, installation instructions, usage guidelines, and contribution details.