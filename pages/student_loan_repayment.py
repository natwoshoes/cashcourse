import streamlit as st

st.markdown("""
<style>       
        
.stMarkdown p {
    font-size: 20px;
}    

</style>
""", unsafe_allow_html=True)

st.title (" 🏦 Federal Student Loan Repayment")
st.subheader("Rundown")
st.write  ("A U.S. government program that provides financial assistance to students for college. It includes grants, loans, and work-study programs. Students apply by completing the FAFSA (Free Application for Federal Student Aid).")

st.subheader("Key Terms and Vocabulary")
with st.expander("Click Here To See!"):
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Repayment Plans**")
        st.write("options that allow borrowers to repay federal student loans over time, with varying terms, amounts, and durations based on income or loan type.")

        st.write("**Federal Loan Deferment**")
        st.write("temporarily postpones loan payments, often due to financial hardship, school enrollment, or military service, without accruing interest on subsidized loans.")
        
        st.write("**Federal Loan Forbearance**")
        st.write("temporarily pauses or reduces loan payments, usually due to financial difficulty, but interest continues to accrue on all loans.")


    with col2:
        st.write("**Federal Loan Forgiveness**")
        st.write("cancels all or part of a borrower's federal student loan balance after meeting specific criteria, like working in certain public service jobs.")
    
        st.write("**Federal Loan Discharge**")
        st.write("cancels a borrower's federal student loan due to specific circumstances, such as disability, school closure, or fraud.")  

# Create tabs for federal aid types
tabs = st.tabs(["Repayment Plans", "Loan Deferment and Forbearance", "Loan Forgiveness or Discharge"])
 
with tabs[0]:
    st.markdown("### Context")
    st.write("Federal student loan repayment plans offer flexibility to match borrowers' financial situations.")
    st.markdown("### Clarification")
    st.markdown("""
    1. **Standard Repayment Plan :**
        - *Payments : Fixed for 10 years.*
            - Pros: Fastest repayment, less interest.
            - Cons: Higher monthly payments.
    2. **Graduated Repayment Plan :**
        - *Payments : Start low, increase every 2 years, term is 10 years.*
            -Pros: Lower initial payments.
            - Cons: Higher total interest.
    3. **Extended Repayment Plan :**
        - Payments: Fixed or graduated for up to 25 years.
            - Eligibility: For balances of $30,000+.
            - Pros: Lower payments. 
            - Cons: Longer term, more interest.

    4. **Income-Driven Repayment (IDR) Plans :** 
        - Payments based on income and family size, with forgiveness after 20-25 years. 
            - IBR : 15 percent of income, 25-year forgiveness. 
            - PAYE : 10 percent of income, 20-year forgiveness. 
            - REPAYE : 10 percent of income, 20 years (undergrad) or 25 years (grad). 
            - ICR : 20 percent of income, 25-year forgiveness.
                - Pros : Lower payments, forgiveness. 
                - Cons : Longer repayment, more interest.
    5. **How to Apply :** 
        - Apply or change plans via StudentAid.gov or through your loan servicer. 
    """)

with tabs[1]:
    st.markdown("### Glimpse")
    st.write("Deferment and forbearance are temporary relief options for federal student loan borrowers who are unable to make payments.")
    st.markdown("### Guidance")
    st.markdown("""
    1. **Deferment :**
    - Eligibility : Available for situations like school enrollment, unemployment, or military service.
        - *Interest : Subsidized loans: The government pays interest.*
        - *Unsubsidized loans : Interest accrues and must be paid by the borrower.*
            - ***Duration :*** Varies (e.g., while in school or for up to 3 years for economic hardship). 
            - ***Pros :*** Government covers interest on subsidized loans. 
            - ***Cons :*** Interest accrues on unsubsidized loans, increasing the balance.
    2. **Forbearance :**
    - Eligibility : Available for reasons like financial hardship, medical issues, or job loss.
        - *Interest : Accrues on all loans, including subsidized loans, and is added to the balance if unpaid.*
        - *Duration : Up to 12 months, renewable.*
            - ***Pros :*** Easier to apply for and faster approval. 
            - ***Cons :*** Interest accrues on all loan types, raising the total balance.
    """)

with tabs[2]:
    st.markdown("### Intro")
    st.write("Federal Loan Forgiveness and Discharge offer relief for federal student loan borrowers under specific conditions.")
    st.markdown("### Explanation")
    st.markdown("""
    1. **Forgiveness Programs :**
        - Public Service Loan Forgiveness (PSLF) :
            - *For those working in qualifying public service jobs. Requires 120 qualifying payments under an IDR plan. Remaining loan balance is forgiven.*
        - Teacher Loan Forgiveness : 
            - *For teachers in low-income schools. Requires 5 years of service. Forgives up to $17,500.*
        - Income-Driven Repayment (IDR) Forgiveness : 
            - *For borrowers on IDR plans. After 20-25 years of payments, the remaining balance is forgiven.*
        - Military Service Forgiveness : 
            - *Available for military members. Forgiveness depends on the branch and service.*
        - How to Apply: 
            - *Submit required forms to your loan servicer or the Department of Education.*
    
    2. **Discharge Programs :**
        - Total and Permanent Disability : 
            - *For borrowers with total disability. Full loan cancellation after proof.*
        - School Closure : 
            - *If your school closes while you're enrolled. Full loan discharge.*
        - False Certification : 
            - *If the school falsely certified your eligibility. Full loan cancellation.*
        - Unpaid Refund : 
            - *If your school didn't return a required refund after withdrawal. Loan cancellation for that amount.*
        - Bankruptcy : 
            - *In rare cases, student loans can be discharged if you prove undue hardship in bankruptcy court.*
        - How to Apply: 
            - *Apply with documentation to your loan servicer or the Department of Education.*
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
    c1.page_link("pages/federal_student_aid.py", label="Federal Student Aid", icon="🏛️")