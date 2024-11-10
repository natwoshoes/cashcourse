import streamlit as st
import pandas as pd
import random


def create_flashcards():
    # Define the flashcard content
    flashcards = [
        {"term": "Roth IRA", "definition": "A retirement account where you invest after-tax money and withdrawals in retirement are tax-free."},
        {"term": "Brokerage Account", "definition": "An investment account that lets you buy and sell various investments like stocks and bonds."},
        {"term": "Index Funds", "definition": "Investment funds that track a market index, offering broad market exposure with lower fees."},
        {"term": "Stocks", "definition": "Shares of ownership in a company that can be bought and sold."},
        {"term": "Retirement", "definition": "The period when you stop working and live off accumulated savings and investments."},
        {"term": "Compound Interest", "definition": "When your investment earnings generate their own earnings over time."},
        {"term": "Risk Tolerance", "definition": "How much investment risk you're comfortable taking with your money."},
        {"term": "Expense Ratio", "definition": "The annual fee that funds charge investors, expressed as a percentage."}
    ]
    
    # Initialize session state for flashcards if not exists
    if 'current_card_index' not in st.session_state:
        st.session_state.current_card_index = 0
    if 'show_definition' not in st.session_state:
        st.session_state.show_definition = False
    
    st.markdown("## 📚 Study Investment Terms with Flashcards")
    st.write("Test your knowledge by flipping through these flashcards!")
    
    # Style the flashcard container
    st.markdown("""
        <style>
        .flashcard {
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
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

def main():
    # Header
    st.title("💰 Retirement Investment Guide")
    st.markdown("Investing for retirement means putting money into accounts or investments now, while you're young, to help ensure you have enough money to live on when you're older and no longer working. The idea is that the earlier you start, the more time your money has to grow. You can invest in things like stocks, bonds, or special retirement accounts (like a Roth IRA or 401(k)), and over time, your investments can earn interest or increase in value. The goal is to have a bigger nest egg by the time you retire, so you don't have to rely on just Social Security or your savings. Starting to invest early can make a big difference in how much you'll have when you're older!")

    # Terms to Know in an expander
    with st.expander("📚 Click here to learn important investment terms"):
        # Create three columns for better organization
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Roth IRA**")
            st.markdown("A retirement account where you invest after-tax money and withdrawals in retirement are tax-free.")
            
            st.markdown("**Brokerage Account**")
            st.markdown("An investment account that lets you buy and sell various investments like stocks and bonds.")
            
            st.markdown("**Index Funds**")
            st.markdown("Investment funds that track a market index, offering broad market exposure with lower fees.")
            
        with col2:
            st.markdown("**Stocks**")
            st.markdown("Shares of ownership in a company that can be bought and sold.")
            
            st.markdown("**Retirement**")
            st.markdown("The period when you stop working and live off accumulated savings and investments.")
            
            st.markdown("**Compound Interest**")
            st.markdown("When your investment earnings generate their own earnings over time.")
            
        with col3:
            st.markdown("**Risk Tolerance**")
            st.markdown("How much investment risk you're comfortable taking with your money.")
            
            st.markdown("**Expense Ratio**")
            st.markdown("The annual fee that funds charge investors, expressed as a percentage.")

    # Investment Options header (outside expander)
    st.header("Investment Options")
    
    # Create tabs for different investment types
    tabs = st.tabs(["Roth IRAs", "Brokerage Accounts", "Index Funds", "Stocks"])
    
    with tabs[0]:
        st.subheader("Roth IRAs")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### What is it?")
            st.write("A Roth IRA is a special type of retirement account. It’s like a savings account for your future, but with extra benefits. The money you put in grows tax-free, and when you take it out later in life (after age 59½), you don’t pay taxes on it. The best part is that you can take out the money you put in at any time without penalty. It’s a great way to save for the long term and keep more of your earnings.")
        with col2:
            st.markdown("### Tips")
            st.write("- Start as early as possible to maximize compound interest")
            st.write("- You can contribute up to the annual limit if you have earned income")
            
        # Add an example compound interest calculator
        st.markdown("### 📊 Compound Interest Calculator")
        initial = st.number_input("Initial Investment ($)", min_value=0, value=1000)
        monthly = st.number_input("Monthly Contribution ($)", min_value=0, value=100)
        years = st.number_input("Investment Period (Years)", min_value=1, max_value=50, value=30)
        rate = st.slider("Expected Annual Return (%)", min_value=1, max_value=12, value=7)
        
        # Calculate future value
        rate_decimal = rate / 100
        periods = years * 12
        future_value = initial * (1 + rate_decimal) ** years
        future_value += monthly * (((1 + rate_decimal/12) ** periods - 1) / (rate_decimal/12))
        
        st.markdown(f"### Estimated Future Value: ${future_value:,.2f}")

        st.markdown(f"#### Think you have it down it pact? Try studying terms using the flashcards!")

    
    with tabs[1]:
        st.subheader("Brokerage Accounts")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### What are they?")
            st.write("A brokerage account is an account that lets you buy and sell stocks, bonds, and other investments. Think of it like a wallet for your investments. To buy and sell stocks, you need to open a brokerage account with a company that helps you make those transactions, like a bank or an online platform. Some accounts charge fees, while others may not, but the goal is to provide you a place to manage your investments.")
        with col2:
            st.markdown("### Tips")
            st.write("- Choose low-fee brokers")
            st.write("- Diversify your investments to manage risk")
            
        # Add comparison table of popular brokers
        st.markdown("### Popular Online Brokers Comparison")

        broker_data = {
            'Broker': ['Fidelity', 'Charles Schwab', 'Vanguard', 'E*TRADE'],
            'Stock Trade Fee': ['$0', '$0', '$0', '$0'],
            'Minimum Investment': ['$0', '$0', '$0', '$0'],
            'Mutual Fund Fees': ['$0-$49.95', '$0-$49.95', '$0-$50', '$0-$49.99']
        }
        st.table(pd.DataFrame(broker_data))
    
    with tabs[2]:
        st.subheader("Index Funds")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### What are they?")
            st.write("**Index funds** are a type of investment that follow a market index, which is basically a list of top-performing companies. They're a simple and affordable way to invest your money. Instead of putting your money into just one company, index funds let you invest in a bunch of different companies all at once. This helps reduce risk and gives you more variety in your investments. It's like the saying, 'Don’t put all your eggs in one basket!'—if one company doesn't do well, you're still protected because you're invested in many others.")
        with col2:
            st.markdown("### Tips")
            st.write("- Great for beginners")
            st.write("- Provide broad market exposure with lower fees than many managed funds")
            
        # Add popular index funds comparison
        st.markdown("### Popular Index Funds")
        index_data = {
            'Fund Name': ['S&P 500 Index Fund', 'Total Stock Market Index Fund', 'International Stock Index Fund'],
            'Type': ['Large-Cap US Stocks', 'Full US Market', 'International Stocks'],
            'Typical Expense Ratio': ['0.03% - 0.15%', '0.03% - 0.15%', '0.05% - 0.20%']
        }
        st.table(pd.DataFrame(index_data))
    
    with tabs[3]:
        st.subheader("Stocks")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### What are they?")
            st.write("Stocks are like tiny pieces of ownership in a company. When you buy a stock, you own a small part of that company. If the company does well and makes money, the value of your stock can go up, which means you can sell it for a profit. But if the company struggles, the value can go down, and you could lose money. Buying stocks is one way to invest in a company and potentially make money over time.")
        with col2:
            st.markdown("### Tips")
            st.write("- Research before buying")
            st.write("- Avoid investing money you may need soon, as stocks can be unpredictable")
        
        # Add risk assessment tool
        st.markdown("### 📊 Risk Assessment Tool")
        st.write("Answer these questions to gauge if individual stock investing is right for you:")
        
        risk_score = 0
        emergency_fund = st.radio("Do you have an emergency fund of 3-6 months of expenses?", ["Yes", "No"])
        risk_score += 1 if emergency_fund == "Yes" else 0
        
        debt = st.radio("Are you free of high-interest debt?", ["Yes", "No"])
        risk_score += 1 if debt == "Yes" else 0
        
        timeline = st.radio("Is your investment timeline longer than 5 years?", ["Yes", "No"])
        risk_score += 1 if timeline == "Yes" else 0
        
        knowledge = st.radio("Do you understand basic financial statements and stock analysis?", ["Yes", "No"])
        risk_score += 1 if knowledge == "Yes" else 0
        
        st.markdown(f"### Your Stock Investment Readiness Score: {risk_score}/4")
        if risk_score <= 2:
            st.warning("Consider starting with index funds before investing in individual stocks.")
        else:
            st.success("You appear to be well-positioned for stock investing. Remember to start small and diversify!")
    st.markdown("---")
    create_flashcards()
    # Footer with disclaimer
    st.markdown("---")
    st.caption("Disclaimer: This information is for educational purposes only and should not be considered financial advice. Always consult with a qualified financial advisor for personalized recommendations.")
    

if __name__ == "__main__":
    main()


