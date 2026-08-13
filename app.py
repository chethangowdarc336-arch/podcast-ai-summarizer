import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from gtts import gTTS
import tempfile
import re
from collections import Counter


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Podcast AI",
    page_icon="🎙️",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

/* Main title */
.hero-title {
    font-size: 45px;
    font-weight: 800;
    margin-bottom: 5px;
}

.hero-subtitle {
    font-size: 18px;
    opacity: 0.7;
    margin-bottom: 25px;
}

/* Cards */
.metric-card {
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(128,128,128,0.25);
    text-align: center;
}

.metric-number {
    font-size: 28px;
    font-weight: 700;
}

.metric-label {
    font-size: 14px;
    opacity: 0.65;
}

/* Section titles */
.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 12px;
}

/* Summary box */
.summary-box {
    padding: 22px;
    border-radius: 15px;
    border: 1px solid rgba(128,128,128,0.25);
    line-height: 1.7;
}

/* Topic badges */
.topic {
    display: inline-block;
    padding: 7px 13px;
    margin: 4px;
    border-radius: 20px;
    border: 1px solid rgba(128,128,128,0.3);
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="hero-title">🎙️ Podcast AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Transform long podcast conversations into concise, meaningful insights.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# MODEL
# =========================================================

MODEL_PATH = "./podcast_summarizer_final"

device = "cuda" if torch.cuda.is_available() else "cpu"


@st.cache_resource
def load_model():

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_PATH
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        MODEL_PATH
    )

    model.to(device)
    model.eval()

    return tokenizer, model


with st.spinner("Loading AI model..."):
    tokenizer, model = load_model()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("⚙️ Settings")

    summary_style = st.selectbox(
        "✨ Summary Style",
        [
            "Standard",
            "Short",
            "Detailed",
            "Key Takeaways"
        ]
    )

    summary_length = st.slider(
        "📏 Summary Length",
        min_value=50,
        max_value=180,
        value=100,
        step=10
    )

    st.divider()

    st.subheader("🤖 Model Information")

    st.write("Model: Fine-tuned BART")
    st.write(f"Device: {device.upper()}")
    st.write("Task: Abstractive Summarization")


# =========================================================
# INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">🎙️ Podcast Transcript</div>',
    unsafe_allow_html=True
)

text = st.text_area(
    "Paste your podcast transcript below",
    height=280,
    placeholder=(
        "Example:\n\n"
        "Today we discuss artificial intelligence, "
        "machine learning and how these technologies "
        "are transforming modern industries..."
    ),
    label_visibility="collapsed"
)


# =========================================================
# GENERATE BUTTON
# =========================================================

generate = st.button(
    "🚀 Generate AI Summary",
    type="primary",
    use_container_width=True
)


# =========================================================
# SUMMARY FUNCTION
# =========================================================

def generate_summary(text, max_length):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    with torch.no_grad():

        summary_ids = model.generate(
            inputs["input_ids"],
            num_beams=4,
            max_length=max_length,
            min_length=30,
            length_penalty=2.0,
            early_stopping=True,
            no_repeat_ngram_size=3
        )

    return tokenizer.decode(
        summary_ids[0],
        skip_special_tokens=True
    )


# =========================================================
# KEYWORD EXTRACTION
# =========================================================

def extract_topics(text):

    words = re.findall(
        r'\b[a-zA-Z]{5,}\b',
        text.lower()
    )

    stopwords = {
        "which", "there", "their", "about",
        "would", "could", "these", "those",
        "because", "where", "while",
        "today", "people", "really",
        "being", "using", "going",
        "after", "before", "through",
        "should", "other", "between"
    }

    words = [
        word for word in words
        if word not in stopwords
    ]

    counter = Counter(words)

    return [
        word.title()
        for word, count in counter.most_common(6)
    ]


# =========================================================
# RESULTS
# =========================================================

if generate:

    if not text.strip():

        st.warning(
            "⚠️ Please enter a podcast transcript first."
        )

    else:

        with st.spinner(
            "🤖 BART is analyzing the podcast..."
        ):

            summary = generate_summary(
                text,
                summary_length
            )

        st.success(
            "✅ Podcast summarized successfully!"
        )

        # -------------------------------------------------
        # ANALYTICS
        # -------------------------------------------------

        original_words = len(text.split())
        summary_words = len(summary.split())

        if original_words > 0:

            reduction = (
                1 - summary_words / original_words
            ) * 100

        else:

            reduction = 0


        reading_time = summary_words / 150


        st.markdown(
            '<div class="section-title">📊 Podcast Analytics</div>',
            unsafe_allow_html=True
        )


        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-number">
                        🎙️ {original_words}
                    </div>
                    <div class="metric-label">
                        Original Words
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col2:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-number">
                        📝 {summary_words}
                    </div>
                    <div class="metric-label">
                        Summary Words
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col3:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-number">
                        📉 {reduction:.1f}%
                    </div>
                    <div class="metric-label">
                        Compression
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col4:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-number">
                        ⏱️ {reading_time:.1f}
                    </div>
                    <div class="metric-label">
                        Reading Time (min)
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        st.divider()


        # -------------------------------------------------
        # TRANSCRIPT + SUMMARY
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '📖 Transcript &nbsp;&nbsp;→&nbsp;&nbsp; 📝 AI Summary'
            '</div>',
            unsafe_allow_html=True
        )


        left, right = st.columns(2)


        with left:

            st.subheader("🎙️ Original Transcript")

            st.text_area(
                "Transcript",
                text,
                height=350,
                disabled=True,
                label_visibility="collapsed"
            )


        with right:

            st.subheader("📝 Generated Summary")

            st.markdown(
                f"""
                <div class="summary-box">
                    {summary}
                </div>
                """,
                unsafe_allow_html=True
            )


        st.divider()


        # -------------------------------------------------
        # KEY TOPICS
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">🔑 Key Topics</div>',
            unsafe_allow_html=True
        )


        topics = extract_topics(text)


        topic_html = ""


        for topic in topics:

            topic_html += (
                f'<span class="topic">#{topic}</span>'
            )


        st.markdown(
            topic_html,
            unsafe_allow_html=True
        )


        st.divider()


        # -------------------------------------------------
        # KEY TAKEAWAYS
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">💡 Key Takeaways</div>',
            unsafe_allow_html=True
        )


        sentences = re.split(
            r'(?<=[.!?])\s+',
            summary
        )


        for i, sentence in enumerate(
            sentences[:5],
            1
        ):

            if sentence.strip():

                st.write(
                    f"**{i}.** {sentence.strip()}"
                )


        st.divider()


        # -------------------------------------------------
        # AUDIO SUMMARY
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">🔊 Audio Summary</div>',
            unsafe_allow_html=True
        )


        with st.spinner(
            "🎧 Creating audio summary..."
        ):

            tts = gTTS(
                text=summary,
                lang="en",
                slow=False
            )

            audio_file = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".mp3"
            )

            tts.save(
                audio_file.name
            )


        st.audio(
            audio_file.name,
            format="audio/mp3"
        )


        # Read audio for download

        with open(
            audio_file.name,
            "rb"
        ) as file:

            audio_bytes = file.read()


        # -------------------------------------------------
        # DOWNLOAD
        # -------------------------------------------------

        st.markdown(
            '<div class="section-title">📥 Export</div>',
            unsafe_allow_html=True
        )


        download1, download2 = st.columns(2)


        with download1:

            st.download_button(
                "📄 Download Text Summary",
                data=summary,
                file_name="podcast_summary.txt",
                mime="text/plain",
                use_container_width=True
            )


        with download2:

            st.download_button(
                "🎧 Download Audio Summary",
                data=audio_bytes,
                file_name="podcast_summary.mp3",
                mime="audio/mpeg",
                use_container_width=True
            )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🎙️ Podcast AI • Fine-tuned BART • "
    "Abstractive Text Summarization"
)