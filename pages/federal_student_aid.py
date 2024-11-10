import streamlit as st

st.markdown("""
<style>       
        
.stMarkdown p {
    font-size: 20px;
}    

</style>
""", unsafe_allow_html=True)

st.title (" 🏛️ Federal Student Aid")
st.subheader("Overview")
st.write  ("A U.S. government program that provides financial assistance to students for college. It includes grants, loans, and work-study programs. Students apply by completing the FAFSA (Free Application for Federal Student Aid).")

st.subheader("Key Terms and Vocabulary")
with st.expander("Click Here To See!"):
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Pell Grant**")
        st.write("A need-based financial aid for low-income undergraduate students that doesn't need to be repaid.")

        st.write("**Federal Work-Study Program**")
        st.write("Provides part-time jobs for students with financial need, allowing them to earn money to help pay for college.")
        
        st.write("**Direct Subsidized Loans**")
        st.write("federal loans for undergraduate students with financial need, where the government pays the interest while the student is in school.")


    with col2:
        st.write("**Direct Unsubsidized Loans**")
        st.write("federal loans for students, available regardless of financial need, where the borrower is responsible for all interest, including while in school.")
    
        st.write("**Outside Scholarships**")
        st.write("Financial awards for students from non-governmental sources, like private organizations, businesses, or foundations, to help pay for education.") 

# Create tabs for federal aid types
tabs = st.tabs(["Pell Grant", "Work Study", "Outside Scholarships", "Direct Subsidized Loans", "Direct Subsidized Loans"])
with tabs[0]:
    st.markdown("### Abstract")
    st.write("The Federal Pell Grant is a need-based financial aid program for undergraduate students with financial need. It provides non-repayable funds to help cover college costs.")
    st.markdown("### Information")
    st.markdown("""
    - **Eligibility :** 
        - *Available to undergraduate students who have not earned a bachelor’s degree and demonstrate financial need via the FAFSA. Students must be enrolled in an eligible program.*
    - **Award Amount :** 
        - *For the 2023-2024 academic year, the maximum award is $7,395. The amount depends on financial need, cost of attendance, and enrollment status (full- or part-time).*
    - **Lifetime Eligibility :** 
        - *Students can receive Pell Grants for up to 12 semesters (or 6 years of full-time enrollment).*
    - **Disbursement :** 
        - *Funds are paid directly to the school for tuition and fees. Remaining funds are given to the student.*
    - **No Repayment :** 
        - *Unlike loans, Pell Grants do not need to be repaid. 
    - **Tax-exempt :** 
        - *Pell Grants used for education-related expenses are not taxable.*
    - **Application :** 
        - *Complete the FAFSA to apply. Schools use the FAFSA to calculate eligibility and include the Pell Grant in the financial aid package.*
    """)

with tabs[1]:
    st.markdown("### Brief")
    st.write("The Federal Work-Study (FWS) Program provides part-time jobs for undergraduate and graduate students with financial need to help pay for education-related expenses. Jobs are available on-campus (e.g., library or lab assistant) or off-campus (e.g., nonprofit or government organizations), often related to the student's field of study.")
    col1, col2 = st.columns(2)

    with col1 :
        st.image("Graphics/guy_with_money_next_to_grad.png", width=325)
        st.markdown("### Details")
        st.markdown("""
        - **Eligibility :** 
            - *Requires financial need (determined by FAFSA), half-time enrollment, and satisfactory academic progress.*
        """)
    
    with col2:
        st.markdown("""
        - **Earnings :** 
            - *Students earn at least minimum wage, working up to 20 hours/week during the school year (more during breaks). Earnings go directly to students.*
        - **Benefits :** 
            - *Provides job experience, helps reduce reliance on loans, and allows students to earn money without affecting future financial aid eligibility.*
        - **Limitations :** 
            - *Funding is limited, and not all eligible students will receive FWS jobs.*
        - **How to Apply :** 
            - *Complete the FAFSA, then search for jobs through the school’s student employment office.*
        """)
         

with tabs[2]:
    st.markdown("### Summary")
    st.write("Outside Scholarships for College are financial awards from organizations, businesses, or foundations, not affiliated with the federal government or your school.")
    st.markdown("### Types of Scholarships")
    st.markdown("""
    - **Merit-Based :** 
        - *Based on academic performance.*
    - **Demographic-Based :** 
        - *For specific groups (e.g., race, gender). Field of Study: For students in certain majors (e.g., STEM).*
    - **Community Service :** 
        - *For students with volunteer work. Employer/Association-Based: From employers or professional organizations.*
    - **Essay/Creative :** 
        - *Based on an essay or project submission*
    """)
    st.markdown("### Finding and Applying")
    st.markdown("""
    1. **How to Find Them :** 
        - *Use scholarship search engines (Fastweb, Scholarships.com). Check with high school counselors and college financial aid offices. Look into employer-sponsored and community or religious group scholarships.*
    2. **How to Apply :** 
        - *Prepare materials: transcripts, letters of recommendation, essays, etc. Tailor essays to each scholarship’s focus. Submit applications on time.*
    3. **Tips :** 
        - *Avoid scams (never pay to apply). Apply to multiple scholarships. Stay organized and track deadlines.*
    """)
    
    with tabs[3]:
     st.markdown("### Description")
     st.write("The Federal Direct Subsidized Loan is a need-based loan for undergraduate students that helps pay for college costs. The government covers the interest while the student is in school, during the 6-month grace period after graduation, and during deferment.")
     col1, col2 = st.columns(2)

     with col1 :
        st.markdown("### Facts")
        st.markdown("""
        - **Eligibility :** 
            - *For undergraduate students with financial need (determined by FAFSA), enrolled at least half-time.*
        - **Loan Limits :** 
            - *First-year: Up to 3500 dollars. Second-year: Up to 4500 dollars. Third-year and Beyond: Up to 5500 dollars.*
                - ***Lifetime limit: 23000 dollars for dependent students.***
        - **Interest Rate :** 
            - *Fixed at 5.50% (for 2023-2024).*
        - **Benefits :** 
            - *Lower cost due to government-paid interest while in school, fixed interest rates, and flexible repayment options.*
    """)

    with col2:
         st.image("Graphics/american_flag_behind_bank.png", width=325)
         st.markdown("""
        - **Repayment :** 
            - *Starts 6 months after graduation or dropping below half-time.*
        - **Limitations :** 
            - *Available only to undergraduates, with borrowing limits and eligibility for up to 150 percent of program length.*
        - **How to Apply :** 
            - *Complete the FAFSA to determine eligibility.*
        """)

with tabs[4]:
    st.markdown("### Highlight")
    st.write("The Federal Direct Unsubsidized Loan is a federal student loan for undergraduate and graduate students, available regardless of financial need. Unlike subsidized loans, borrowers are responsible for paying the interest, which accrues from the moment the loan is disbursed, including while in school.")
    st.markdown("### Key Details")
    st.markdown("""
    - **Eligibility :** 
        - *Available to undergraduate and graduate students enrolled at least half-time.*
    - **Loan Limits :** 
        - *Undergraduates: Up to 5500 for first-year students and 7500 for upperclassmen. Graduate students can recieve up to 20500 dollars per year.*
    - **Interest Rate :** 
        - *5.50 percent for undergraduates and 7.05 percent for graduate students (2023-2024).*
    - **Benefits :** 
        - *No financial need requirement. Fixed interest rates and flexible repayment plans.*
    - **Repayment :** 
        - *Begins 6 months after graduation or dropping below half-time, with several repayment options available.*
    - **Drawbacks :** 
        - *Interest accrues while in school, increasing the loan’s total cost.*
    - **How to Apply :** 
        - *Complete the FAFSA.*
    """)

# inject CSS directly with markdown
st.markdown("""
<style>    
            
.stPageLink {
    border-style: solid;
    border-radius: 5px;
    padding: 1em;
    max-width: 100%;
}
                 
.stPageLink p {
    font-size: 17px;
    text-align: center;  
}
       
.stPageLink:hover {
    background-color: #89C7FA;
    color: black;
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

</style>
""", unsafe_allow_html=True)

c1 = st.container()
with c1:
    c1.page_link("pages/student_loan_repayment.py", label="Federal Student Loan Repayment", icon="🏦")