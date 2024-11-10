import streamlit as st


st.markdown("""
<style>       
        
.stMarkdown p {
    font-size: 20px;
}    

</style>
""", unsafe_allow_html=True)

st.title (" 💳 Navigating Credit")
st.subheader("What is it?")
st.write  ("The idea of credit may be daunting at first, but it is essentially a tool— one that can give you access to more financial opportunities, but only if you manage it responsibly.")

st.subheader("Key Terms and Vocabulary")
with st.expander("Click Here To See!"):
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Credit**")
        st.write("An agreement where a debtor receives a sum of money or something else of value and agrees to repay the creditor of that money later, sometimes with interest.")

        st.write("**Creditor**")
        st.write("The lendor of the money.")
        
        st.write("**Debtor**")
        st.write("The borrower of the money.")


    with col2:
        st.write("**Interest**")
        st.write("An additional amount of money you pay or receive on top of the original sum. It's often expressed as percentages of the original sum.")
    
        st.write("**Credit Score**")
        st.write("A number from 300 to 800 that lenders use to determine if you are a reliable borrower.")

        st.write("**Repayments**")
        st.write("The payments you make to pay back money you've borrowed, including interest incurred.")

    
st.write("Credit, at its core, is the act of borrowing money from lenders (like a bank) to make purchases, with the promise that you will pay the lender back later. For example: If you buy a laptop for 1,000USD on a credit card, you're borrowing that 1,000USD from the credit card company. You'll pay it back in the future—either all at once or in smaller payments.")
    

# Create tabs for different investment types
tabs = st.tabs(["Credit Score", "Credit Cards", "Collection, Fees, and Debt"])
 
with tabs[0]:
    col1, col2 = st.columns(2)
    

    with col1:
        st.markdown("### What is it?")
        st.write("Everyone using credit is assigned a credit score: a type of financial report card. It tells lenders how trustworthy (also called creditworthiness) you are when it comes to paying back the money you owe (your debt). A FICO score, from the Fair Isaac Corporation, is the most commonly used credit model. Your score is ranked from 300-800. The higher your score, the better your credit is, and the more likely you are to be approved for loans or credit cards with lower interest rates.")
    with col2:
        st.image("Graphics/money.png")
    st.markdown("### What goes into a credit score?")
    st.write("Your credit score is affected by many factors:")
    st.markdown("""
        1. **Payment History**: This is the most important factor. It shows whether you pay your bills on time.
        2. **Amounts Owed**: This looks at how much debt you have compared to your total available credit. It's not just about how much debt you have, but also how much of your available credit you're using. If you're using a lot of your available credit (like maxing out a credit card), it can lower your score.
        3. **Length of Credit History**: The longer your history of using credit responsibly, the better, the more reliable you seem to lenders.
        4. **New Credit**: Opening several new credit accounts in a short period of time can lower your score. Each time you apply for credit, a "hard inquiry" is made, and too many inquiries can indicate to lenders that you're trying to borrow more than you can handle.
        5. **Types of Credit Used**: Having a mix of different types of credit can benefit your score, as it shows you can manage different types of debt responsibly.
        """)
    

with tabs[1]:
    col1,col2 = st.columns(2)

    with col1: 
     st.markdown("### What is it?")
     st.write("Most commonly, people utilize credit by opening a credit card. A credit card is like a loan that you can keep using up to a certain limit, as long as you make regular payments to pay it down. Imagine it like a revolving door—each time you pay back what you owe, your limit to how much you borrow goes back up. The more consistent you are with ")
     
    with col2:
        st.image("Graphics/credit.jpeg")

    st.write("Credit cards let you make purchases now and then pay later. However, if you don’t pay the full amount by the due date, you’ll have to pay interest, which can add up quickly. They are very convenient, but because of this, there is a large risk of falling into credit card debt, which can significantly lower your credit score as mentioned above.")
    st.write("To open a credit card, you must apply through a bank of your choice. Be selective when applying as each application may lower your credit score if you get denied!")
    st.markdown("### What kinds are there?")
    st.write("There are many different **types of credit cards** availables-- all with different benefits. These below are helpful starting points.")

    st.markdown("""
    1. **Student Credit Cards**
        - Specifically designed for people with little or no credit history, like college stdents. They often have lower credit limits and easier approval processes. These cards may offer rewards like cash back or points for purchases, such as dining or shopping. Using one responsibly (by paying on time) helps build your credit score and get you used to it. For example: The Discover it® Student Cash Back card offers 5% cashback on rotating categories and 1% on other purchases, plus cashback matching in your first year.
    2. **Secured Credit Cards**
        - Requires you to put down a deposit, which serves as your credit limit. It’s a good option if you’re new to credit or need to rebuild your score. The card functions like a regular credit card, and using it responsibly helps build your credit history. Many secured cards let you upgrade to an unsecured card over time. For example: The Capital One Secured Mastercard® lets you start with a deposit as low as $49 and offers a path to upgrade after responsible use
    3. **Travel Credit Cards**
        - For individuals who travel frequently for school, or work, they let you earn points or miles for purchases, which can be used to buy flights, hotel rooms, and other travel expenses. They typically require a bit more credit history, some entry-level travel cards have no annual fee and offer rewards on travel-related spending. For example: The Chase Sapphire Preferred® Card offers 2x points on travel and dining, while a more basic card like the Capital One QuicksilverOne offers 1.5% cashback on all purchases, which can be used for travel expenses   
    """)

with tabs[2]:
 col1, col2 = st.columns(2)
with col1:
        st.markdown("### What is it?")
        st.write("If you don’t manage your credit properly, it can lead to serious financial consequences, including accumulating high levels of debt. When you carry a balance on your credit card from month to month (meaning you don’t pay off the full amount), the credit card company charges interest on what you owe. This interest is often very high—sometimes 20% or more—making it easy to fall deeper into debt.")

with col2:
        st.image("Graphics/debt.png")
    
        
        st.write("On top of interest, there may be fees like late payment fees, over-the-limit fees, or annual fees that can add up quickly. If you don’t make at least the minimum payment on time, your credit score will drop, and it will be harder to get approved for loans or other credit in the future.")

with col1:
    st.image("Graphics/debt2.png")

with col2:
    st.write("If your credit card debt continues to grow and you still can’t make the payments, the credit card company may send your account to collections. This means they will hire a collection agency to try to get you to pay what you owe. Collection agencies can be persistent, calling you repeatedly and even reporting your unpaid debt to the credit bureaus, which can damage your credit for years. Poor credit can make it harder to rent an apartment, buy a car, or even get a job.")

st.write("To avoid all of this, it’s important to understand how credit cards work, use them responsibly, and always make at least the minimum payment to avoid falling into debt. If you do find yourself struggling, it’s better to reach out for help early—there are programs and professionals who can assist in managing or reducing debt!")

st.markdown(
    "<h2 style='text-align: center;'>Credit Card Decision Simulator 🎮💸 </h2>",
    unsafe_allow_html=True
)

with st.expander("1. Choose Your Credit Card Type", expanded=True):
    card_options = {
        "Low-Interest Card": {
            "interest_rate": 10,
            "annual_fee": 0,
            "credit_limit": 1000
        },
        "Rewards Card": {
            "interest_rate": 20,
            "annual_fee": 50,
            "credit_limit": 1500,
            "rewards_rate": 0.02  # Rewards 2% cash back on purchases
        },
        "Student Card": {
            "interest_rate": 25,
            "annual_fee": 0,
            "credit_limit": 500
        }
    }
    card_type = st.selectbox("Select a Credit Card Type", list(card_options.keys()))
    selected_card = card_options[card_type]
    
    # Display Card Details
    st.write(f"**Interest Rate:** {selected_card['interest_rate']}%")
    st.write(f"**Annual Fee:** ${selected_card['annual_fee']}")
    st.write(f"**Credit Limit:** ${selected_card['credit_limit']}")

# Initialize or reset balance and credit score
if "balance" not in st.session_state:
    st.session_state.balance = 0
if "credit_score" not in st.session_state:
    st.session_state.credit_score = 700

# --- Step 2: Make a Transaction ---
with st.expander("2. Make a Transaction", expanded=True):
    transaction_options = {
        "Pay for Books": 200,
        "Emergency Expense": 300,
        "Monthly Groceries": 100,
        "Pay Credit Card Balance": -st.session_state.balance
    }
    transaction = st.selectbox("Choose a Transaction", list(transaction_options.keys()))
    amount = transaction_options[transaction]
    
    if st.button("Submit Transaction"):
        # Calculate new balance
        if transaction == "Pay Credit Card Balance":
            payment = min(amount, st.session_state.balance)
            st.session_state.balance -= payment
            st.write(f"Paid off ${payment} of your credit card balance.")
        else:
            st.session_state.balance += amount
            st.write(f"Transaction completed: {transaction} - ${amount}")
        
        # Calculate rewards if applicable
        rewards = 0
        if "rewards_rate" in selected_card and amount > 0:
            rewards = amount * selected_card["rewards_rate"]
            st.write(f"Rewards Earned: ${rewards:.2f}")
        
        # Update credit score
        if st.session_state.balance > selected_card["credit_limit"]:
            st.session_state.credit_score -= 20
            st.write("You exceeded your credit limit! Your credit score has been penalized by 20 points.")
        elif st.session_state.balance > selected_card["credit_limit"] * 0.8:
            st.session_state.credit_score -= 10
            st.write("You're using more than 80% of your credit limit. Your credit score is reduced by 10 points.")
        elif transaction == "Pay Credit Card Balance":
            st.session_state.credit_score += 5
            st.write("Great! Paying down your balance has increased your credit score by 5 points.")
        
        # Display updated balance and credit score
        st.write(f"**New Balance:** ${st.session_state.balance}")
        st.write(f"**New Credit Score:** {st.session_state.credit_score}")

# --- Step 3: Summary ---
with st.expander("3. Summary :", expanded=True):
    st.write("Track your credit card balance, credit score, and see the effects of your decisions.")
    st.write(f"**Current Balance:** ${st.session_state.balance}")
    st.write(f"**Current Credit Score:** {st.session_state.credit_score}")


