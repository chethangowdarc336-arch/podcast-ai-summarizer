# podcast-ai-summarizer
=======
# 🎙️ Podcast AI — Intelligent Podcast Summarizer

An AI-powered podcast summarization application that converts long podcast transcripts into concise and meaningful summaries using a fine-tuned **BART (Bidirectional and Auto-Regressive Transformers)** model.

The application is built using **Streamlit** and provides text summaries, audio summaries, podcast analytics, key topics, key takeaways, and downloadable outputs.

---

## 📌 Project Overview

Podcasts and long-form audio content can contain a large amount of information, making it difficult for users to quickly identify the most important points.

This project provides an AI-based solution that automatically summarizes podcast transcripts.

The system uses a fine-tuned **BART sequence-to-sequence model** trained on the **CNN/DailyMail dataset** for abstractive text summarization.

### Main Pipeline

```text
Podcast Transcript
        ↓
Text Preprocessing
        ↓
Fine-Tuned BART Model
        ↓
Abstractive Summary
        ↓
 ┌───────────────┐
 │               │
 ↓               ↓
Text Summary   gTTS
                 ↓
            Audio Summary


✨ Features

🎙️ Podcast Transcript Input

Users can paste a podcast transcript directly into the Streamlit application.

🤖 AI-Powered Summarization

A fine-tuned BART Transformer model generates an abstractive summary from the provided transcript.

✨ Summary Styles

Users can select different summary styles:

Standard
Short
Detailed
Key Takeaways
📏 Summary Length Control

A slider allows users to control the desired summary length.

📊 Podcast Analytics

The application displays:

Original word count
Summary word count
Compression percentage
Estimated reading time

Example:

Original Words     Summary Words     Compression
     1250               180              85.6%
📖 Transcript and Summary Comparison

The original transcript and generated summary are displayed side-by-side for easy comparison.

🔑 Key Topics

The application identifies frequently occurring meaningful terms from the transcript and displays them as topic tags.

Example:

#ArtificialIntelligence
#MachineLearning
#Technology
#Education
💡 Key Takeaways

Important points from the generated summary are displayed as numbered takeaways.

🔊 Audio Summary

The generated text summary is converted into speech using gTTS.

Users can listen to the audio directly inside the application.

📥 Download Results

Users can download:

📄 Text summary as .txt
🎧 Audio summary as .mp3
🧠 Machine Learning Model

The core model used in this project is BART.

BART is a Transformer-based sequence-to-sequence architecture that is well suited for abstractive text summarization.

The model was fine-tuned using the CNN/DailyMail dataset.

Model Workflow
CNN/DailyMail Dataset
          ↓
       Article
          ↓
      Tokenization
          ↓
     BART Model
          ↓
       Training
          ↓
   Fine-Tuned BART
          ↓
Podcast Transcript
          ↓
   Generated Summary
📚 Dataset

The project uses the CNN/DailyMail dataset for training the summarization model.

Each dataset sample contains:

article
highlights

Where:

article → input text
highlights → target summary

The model learns to generate the highlights from the corresponding article.

The trained model is then used to summarize podcast transcripts.

🛠️ Technologies Used
Technology	Purpose
Python	Main programming language
PyTorch	Deep learning framework
Hugging Face Transformers	BART model and tokenization
Hugging Face Datasets	Dataset loading and processing
Streamlit	Web application and UI
gTTS	Text-to-speech conversion
SentencePiece	Tokenization support
CNN/DailyMail	Training dataset
🏗️ System Architecture
                  ┌──────────────────────┐
                  │       User           │
                  └──────────┬───────────┘
                             │
                             ↓
                  ┌──────────────────────┐
                  │ Streamlit Interface  │
                  └──────────┬───────────┘
                             │
                             ↓
                  ┌──────────────────────┐
                  │ Podcast Transcript   │
                  └──────────┬───────────┘
                             │
                             ↓
                  ┌──────────────────────┐
                  │   Tokenization       │
                  └──────────┬───────────┘
                             │
                             ↓
                  ┌──────────────────────┐
                  │ Fine-Tuned BART      │
                  │ Summarization Model  │
                  └──────────┬───────────┘
                             │
                             ↓
                  ┌──────────────────────┐
                  │  Text Summary        │
                  └──────────┬───────────┘
                             │
                  ┌──────────┴───────────┐
                  ↓                      ↓
        ┌─────────────────┐    ┌─────────────────┐
        │ Analytics       │    │      gTTS       │
        │ Topics          │    │ Text-to-Speech  │
        │ Takeaways       │    └────────┬────────┘
        └─────────────────┘             │
                                        ↓
                              ┌─────────────────┐
                              │  Audio Summary  │
                              │      .mp3       │
                              └─────────────────┘
📂 Project Structure
podcast_summarizer/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── podcast_summarizer_final/
    │
    ├── config.json
    ├── generation_config.json
    ├── model.safetensors
    ├── tokenizer_config.json
    ├── tokenizer.json
    └── ...
⚙️ Installation
1. Clone the Repository
git clone <YOUR_GITHUB_REPOSITORY_URL>

Move into the project directory:

cd podcast_summarizer
2. Install Dependencies
pip install -r requirements.txt

Alternatively:

pip install streamlit torch transformers sentencepiece gtts
📋 Requirements

The requirements.txt file should contain:

streamlit
torch
transformers
sentencepiece
gtts
▶️ Running the Application

Start the Streamlit application using:

streamlit run app.py

The application will be available at:

http://localhost:8501
🖥️ Application Workflow
Step 1 — Enter Transcript

Paste the podcast transcript into the text input area.

Step 2 — Select Summary Settings

Choose:

Summary style
Summary length
Step 3 — Generate Summary

Click:

🚀 Generate AI Summary
Step 4 — BART Processing

The fine-tuned BART model processes the transcript and generates an abstractive summary.

Step 5 — View Results

The application displays:

📝 AI Summary
📊 Podcast Analytics
🔑 Key Topics
💡 Key Takeaways
Step 6 — Generate Audio

The generated summary is converted into speech using gTTS.

Step 7 — Download

Users can download:

📄 podcast_summary.txt
🎧 podcast_summary.mp3
📊 Example Output
Original Transcript
Today we discuss artificial intelligence and machine learning.
These technologies are transforming many industries including
healthcare, finance and education. Machine learning systems can
analyze large amounts of data and identify patterns that help
organizations make better decisions...
Generated Summary
Artificial intelligence and machine learning are transforming
industries such as healthcare, finance and education by analyzing
large datasets and identifying useful patterns.
Analytics
Original Words: 1250
Summary Words: 180
Compression: 85.6%
Reading Time: 1.2 minutes
🔊 Audio Summary

The generated summary is converted into an MP3 file using gTTS.

The user can:

▶ Play Audio

        ↓

🎧 Download Audio Summary

Output:

podcast_summary.mp3
🎯 Project Objectives

The main objectives of the project are:

Develop an AI-powered podcast summarization system.
Fine-tune a BART Transformer model for abstractive summarization.
Generate concise summaries from long-form text.
Build an interactive Streamlit web application.
Provide summary analytics.
Extract important topics from podcast transcripts.
Present key takeaways from generated summaries.
Convert generated summaries into audio.
Allow users to download text and audio summaries.
📈 Advantages
Saves time when consuming long podcasts.
Provides concise and meaningful summaries.
Uses Transformer-based deep learning.
Provides both text and audio outputs.
Easy-to-use Streamlit interface.
Provides useful summary analytics.
Allows users to download generated results.
⚠️ Current Limitations
The current application accepts podcast transcripts rather than directly processing audio files.
BART has a maximum input token limit, so extremely long transcripts need to be processed in chunks.
Key topic extraction currently uses frequency-based text processing.
gTTS requires an internet connection to generate speech.
The BART model was fine-tuned using CNN/DailyMail news articles rather than a podcast-specific dataset.
🚀 Future Enhancements

The current system can be extended into a complete audio-to-summary pipeline.

Future Architecture
Podcast MP3 / WAV
       ↓
     Whisper
       ↓
Speech-to-Text
       ↓
Transcript
       ↓
Fine-Tuned BART
       ↓
Text Summary
       ↓
      gTTS
       ↓
Audio Summary

Future improvements include:

🎵 Direct MP3/WAV podcast upload
🎙️ Automatic speech recognition using Whisper
⏱️ Timestamp-based summaries
📌 Automatic podcast chapter generation
🌍 Multilingual summarization
🔍 Semantic search across podcast content
👥 Speaker identification
📊 Advanced podcast analytics
☁️ Cloud deployment
📱 Mobile application
🧠 Podcast-specific model fine-tuning
🔬 Machine Learning Methodology

The summarization process follows these major stages:

1. Dataset Collection

The CNN/DailyMail dataset is loaded using the Hugging Face Datasets library.

2. Preprocessing

Articles and corresponding highlights are prepared for model training.

3. Tokenization

The text is converted into token IDs using the BART tokenizer.

4. Model Fine-Tuning

The BART sequence-to-sequence model is trained to generate summaries from input articles.

5. Evaluation

Generated summaries can be evaluated using ROUGE metrics.

The commonly used metrics are:

ROUGE-1
ROUGE-2
ROUGE-L
6. Inference

The trained model receives a podcast transcript and generates a concise summary.

7. Text-to-Speech

The generated summary is converted into speech using gTTS.

🧪 Evaluation

The summarization model can be evaluated using ROUGE metrics.

ROUGE-1

Measures unigram overlap between the generated summary and reference summary.

ROUGE-2

Measures bigram overlap.

ROUGE-L

Measures the longest common subsequence between the generated and reference summaries.

These metrics help evaluate how closely the generated summary matches the reference summary.

💻 Hardware

The model can be trained using a GPU-enabled environment such as Google Colab.

For inference, the Streamlit application can run using:

CPU

or, if available:

CUDA GPU

The application automatically detects the available device.

🔐 Model Files

The trained model is stored in:

podcast_summarizer_final/

Important files include:

config.json
model.safetensors
generation_config.json
tokenizer_config.json
tokenizer.json

If the model files are too large for GitHub, they can be hosted separately and downloaded before running the application.

🧑‍💻 How the Application Works Internally

The Streamlit application loads the trained model:

tokenizer = AutoTokenizer.from_pretrained(
    "./podcast_summarizer_final"
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    "./podcast_summarizer_final"
)

The transcript is tokenized:

inputs = tokenizer(
    text,
    return_tensors="pt",
    max_length=512,
    truncation=True
)

The BART model generates the summary:

summary_ids = model.generate(
    inputs["input_ids"],
    num_beams=4,
    max_length=128
)

The generated tokens are converted back into text:

summary = tokenizer.decode(
    summary_ids[0],
    skip_special_tokens=True
)

The summary is then converted into audio:

tts = gTTS(
    text=summary,
    lang="en"
)

tts.save("podcast_summary.mp3")
🎓 Project Domain
Artificial Intelligence
        ↓
Natural Language Processing
        ↓
Transformer Models
        ↓
Abstractive Text Summarization
        ↓
Text-to-Speech
        ↓
Streamlit Application
⭐ Key Highlights
🤖 Fine-Tuned BART Model
📚 CNN/DailyMail Dataset
📝 Abstractive Summarization
📊 Podcast Analytics
🔑 Key Topic Extraction
💡 Key Takeaways
🔊 Audio Summary
📥 TXT & MP3 Download
🖥️ Streamlit Web Interface
🏁 Conclusion

Podcast AI provides an intelligent solution for simplifying long-form podcast content.

The system combines a fine-tuned BART Transformer model with a Streamlit interface to generate concise summaries from podcast transcripts. The application further improves accessibility by converting the generated summaries into audio using gTTS.

The project demonstrates the practical application of Natural Language Processing, Transformer-based deep learning, abstractive summarization, and text-to-speech technology in a user-friendly AI application.

👨‍💻 Project

Project Name: Podcast AI — Intelligent Podcast Summarizer

Domain: Artificial Intelligence / Natural Language Processing

Core Model: Fine-Tuned BART

Dataset: CNN/DailyMail

Frontend: Streamlit

Programming Language: Python

Deep Learning Framework: PyTorch

Text-to-Speech: gTTS

Task: Abstractive Podcast Summarization
