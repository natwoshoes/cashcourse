import streamlit as st
import random

st.title("Federal Student Aid")


def create_flashcards():
    # Define the flashcard content
    flashcards = [
        {"term": "Pell Grant", "definition": "A need-based financial aid for low-income undergraduate students that doesn't need to be repaid."},
        {"term": "Federal Work-Study Program", "definition": "provides part-time jobs for students with financial need, allowing them to earn money to help pay for college."},
        {"term": "Direct Subsidized Loans", "definition": "federal loans for undergraduate students with financial need, where the government pays the interest while the student is in school"},
        {"term": "Direct Unsubsidized Loans", "definition": "federal loans for students, available regardless of financial need, where the borrower is responsible for all interest, including while in school."},
        {"term": "Federal Loan Deferment", "definition": "options that allow borrowers to repay federal student loans over time, with varying terms, amounts, and durations based on income or loan type"},
        {"term": "Federal Loan Forbearance", "definition": " temporarily pauses or reduces loan payments, usually due to financial difficulty, but interest continues to accrue on all loans."},
        {"term": "Federal Loan Forgiveness", "definition": "cancels all or part of a borrower's federal student loan balance after meeting specific criteria, like working in certain public service jobs."},
        {"term": "Federal Loan Discharge ", "definition": "cancels a borrower's federal student loan due to specific circumstances, such as disability, school closure, or fraud."},
        {"term": "Outside Scholarships ", "definition": "financial awards for students from non-governmental sources, like private organizations, businesses, or foundations, to help pay for education."},

    ]
 # Initialize session state for flashcards if not exists
    if 'current_card_index' not in st.session_state:
        st.session_state.current_card_index = 0
    if 'show_definition' not in st.session_state:
        st.session_state.show_definition = False
    
    st.markdown("## 📚 Study Credit Terms with Flashcards")
    st.write("Test your knowledge by flipping through these flashcards!")
    
    st.markdown("""
        <style>
        .flashcard {
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            background-color: blue;
            margin: rem 0;
            text-align: center;
            min-height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Create columns for buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    # Navigation buttons
    with col1:
        if st.button("◀ Previous"):
            st.session_state.current_card_index = (st.session_state.current_card_index - 1) % len(flashcards)
            st.session_state.show_definition = False
            
    with col2:
        st.markdown(f"<h3 style='text-align: center;'>Card {st.session_state.current_card_index + 1} of {len(flashcards)}</h3>", unsafe_allow_html=True)
    
    with col3:
        if st.button("Next ▶"):
            st.session_state.current_card_index = (st.session_state.current_card_index + 1) % len(flashcards)
            st.session_state.show_definition = False
    
    # Current card
    current_card = flashcards[st.session_state.current_card_index]
    
    # Display card content
    if not st.session_state.show_definition:
        st.markdown(f'<div class="flashcard"><h2>{current_card["term"]}</h2></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="flashcard"><p>{current_card["definition"]}</p></div>', unsafe_allow_html=True)
    
    # Center the flip and shuffle buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Flip Card"):
            st.session_state.show_definition = not st.session_state.show_definition
        
        if st.button("🔀 Shuffle Cards"):
            st.session_state.current_card_index = random.randint(0, len(flashcards) - 1)
            st.session_state.show_definition = False
    st.set_page_config(page_title="Retirement Investment Guide", layout="wide")

    st.markdown("---")
    create_flashcards()

    #if __name__ == "__main__":
    