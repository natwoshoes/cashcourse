import streamlit as st
import google.generativeai as genai
import json

# Initialize Gemini
genai.configure(api_key="AIzaSyAB7IqPaUC3lNWFL5YfKpb2zlAVizz06ag")
model = genai.GenerativeModel("gemini-pro")

# Initialize session state
if 'flashcards' not in st.session_state:
    st.session_state.flashcards = []
if 'current_card_index' not in st.session_state:
    st.session_state.current_card_index = 0
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

# Custom CSS for the flipping card
st.markdown("""
<style>
.flip-card {
    background-color: transparent;
    width: 100%;
    height: 300px;
    perspective: 1000px;
    cursor: pointer;
    margin: 20px 0;
}

.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.8s;
    transform-style: preserve-3d;
}

.flip-card.flipped .flip-card-inner {
    transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.flip-card-front {
    background-color: #f8f9fa;
    color: #1f1f1f;
}

.flip-card-back {
    background-color: #e9ecef;
    color: #1f1f1f;
    transform: rotateY(180deg);
}

.card-content {
    padding: 20px;
    font-size: 1.2em;
}

.navigation-button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin: 5px;
}

.card-counter {
    font-size: 0.9em;
    color: #666;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

def generate_flashcards():
    """Generate financial literacy flashcards using Gemini"""
    prompt = """You are a financial literacy expert. Create exactly 5 flashcards about personal finance basics.
    For each flashcard, provide a question and its answer.
    Format your response as a valid JSON array of objects.
    Each object should have exactly two fields: "question" and "answer".
    Do not include any additional text, only the JSON array.
    Example format:
    [
        {
            "question": "What is compound interest?",
            "answer": "Interest earned on both the initial principal and previously accumulated interest."
        }
    ]"""
    
    try:
        response = model.generate_content(prompt)
        cleaned_text = response.text.strip()
        flashcards = json.loads(cleaned_text)
        
        if isinstance(flashcards, list) and len(flashcards) > 0:
            st.session_state.flashcards = flashcards
            st.session_state.current_card_index = 0
            st.session_state.show_answer = False
        else:
            st.error("Invalid flashcard format. Please try again.")
    except Exception as e:
        st.error(f"Error generating flashcards: {str(e)}")

def next_card():
    if st.session_state.current_card_index < len(st.session_state.flashcards) - 1:
        st.session_state.current_card_index += 1
    else:
        st.session_state.current_card_index = 0
    st.session_state.show_answer = False

def prev_card():
    if st.session_state.current_card_index > 0:
        st.session_state.current_card_index -= 1
    else:
        st.session_state.current_card_index = len(st.session_state.flashcards) - 1
    st.session_state.show_answer = False

# Main app
st.title("Financial Literacy Flashcards")
st.subheader("Click the card to flip it!")

# Generate new flashcards button
if st.button("Generate New Flashcards"):
    generate_flashcards()

# Display flashcard if available
if st.session_state.flashcards:
    current_card = st.session_state.flashcards[st.session_state.current_card_index]
    
    # Create the flipping card using HTML/CSS
    flip_class = "flipped" if st.session_state.show_answer else ""
    st.markdown(f"""
    <div class="flip-card {flip_class}" onclick="this.classList.toggle('flipped');">
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <div class="card-content">
                    <h3>Question</h3>
                    <p>{current_card["question"]}</p>
                </div>
            </div>
            <div class="flip-card-back">
                <div class="card-content">
                    <h3>Answer</h3>
                    <p>{current_card["answer"]}</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⬅️ Previous Card"):
            prev_card()
    with col2:
        if st.button("Flip Card"):
            st.session_state.show_answer = not st.session_state.show_answer
    with col3:
        if st.button("Next Card ➡️"):
            next_card()
    
    # Progress indicator
    st.progress((st.session_state.current_card_index + 1) / len(st.session_state.flashcards))
    st.markdown(f"""
    <div class="card-counter">
        Card {st.session_state.current_card_index + 1} of {len(st.session_state.flashcards)}
    </div>
    """, unsafe_allow_html=True)

else:
    st.write("Click 'Generate New Flashcards' to start learning!")