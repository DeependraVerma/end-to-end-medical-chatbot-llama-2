# Medical Chatbot

## Overview
Medical Chatbot is an innovative project leveraging advanced NLP models and vector database technologies to provide insightful medical information. Utilizing the Llama-2 model and Pinecone as a vector DB, this chatbot aims to transform the way medical knowledge is accessed and delivered.

## Features
- **Llama-2 Model Integration**: Uses the powerful Llama-2-7B-Chat-GGML model for accurate and context-aware responses.
- **Pinecone Vector Database**: Efficient storage and retrieval of sentence embeddings for quick response times.
- **Flask Web Application**: User-friendly web interface built with Flask, HTML, and CSS.
- **Modular Backend Structure**: Utilizes `template.py` for clean and maintainable code structure.
- **Comprehensive Data Source**: Employs The Gale Encyclopedia of Medicine as a primary knowledge source.

## Installation
To set up the Medical Chatbot, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/DeependraVerma/end-to-end-medical-chatbot-llama-2.git
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To start the Medical Chatbot application, run the Flask app:

```
flask run
```

Navigate to the provided local URL in your web browser to interact with the chatbot.

## Model Download
Download the Llama-2 model using the following link:
[Download Llama-2 Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin)

## Dependencies
- ctransformers==0.2.5
- sentence-transformers==2.2.2
- pinecone-client
- langchain==0.0.225
- flask
- pypdf
- python-dotenv
- -e .

## Contributing
Contributions to the Medical Chatbot are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute.

## Contact
- **Developer**: Deependra Verma
- **Email**: deependra.verma00@gmail.com
- **Portfolio**: [Deependra's Data Science Portfolio](https://deependradatascience-productportfolio.netlify.app/)
- **Kaggle Profile**: [Deependra Verma on Kaggle](https://www.kaggle.com/deependraverma13)

## License
This project is licensed under the [MIT License](LICENSE.md).

---
**Note**: This project is not a substitute for professional medical advice, diagnosis, or treatment.
```