# 🎙️ Podcast AI Summarizer

An AI-powered application that generates concise summaries from podcast content using a fine-tuned BART model.

## 🚀 Live Demo

👉 [Try the Podcast AI Summarizer](https://podcast-ai-summarizer-rqzt6rnannenvtypnwntlc.streamlit.app/)

## 🤗 Model

[Hugging Face Model](https://huggingface.co/Chethangowdarc/podcast-bart-summarizer1)

## 💻 GitHub

[Source Code](https://github.com/chethangowdarc336-arch/podcast-ai-summarizer)

---------------------------------------------------------------------------------------------------------------------------------------------------
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
📂 
