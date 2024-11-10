import streamlit as st

st.markdown("""
<style>       
        
.stMarkdown p {
    font-size: 20px;
}    

</style>
""", unsafe_allow_html=True)

st.title (" 🏛️ Federal Student Aid")
st.subheader("What is it?")
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
    st.markdown("### What is it?")
    st.write("The Federal Pell Grant is a need-based financial aid program for undergraduate students with financial need. It provides non-repayable funds to help cover college costs.")
    st.markdown("### Information")
    st.markdown("""
    1. **Eligibility :** 
        - Available to undergraduate students who have not earned a bachelor’s degree and demonstrate financial need via the FAFSA. Students must be enrolled in an eligible program. 
    2. **Award Amount :** 
        - For the 2023-2024 academic year, the maximum award is $7,395. The amount depends on financial need, cost of attendance, and enrollment status (full- or part-time). 
    3. **Application :** 
        - Complete the FAFSA to apply. Schools use the FAFSA to calculate eligibility and include the Pell Grant in the financial aid package. 
    4. **Lifetime Eligibility :** 
        - Students can receive Pell Grants for up to 12 semesters (or 6 years of full-time enrollment). 
    5. **Disbursement :** 
        - Funds are paid directly to the school for tuition and fees. Remaining funds are given to the student. 
    6. **No Repayment :** 
        - Unlike loans, Pell Grants do not need to be repaid. Tax-exempt: Pell Grants used for education-related expenses are not taxable.
    """)

with tabs[1]:
    st.markdown("### What is it?")
    st.write("The Federal Work-Study (FWS) Program provides part-time jobs for undergraduate and graduate students with financial need to help pay for education-related expenses. Jobs are available on-campus (e.g., library or lab assistant) or off-campus (e.g., nonprofit or government organizations), often related to the student's field of study.")
    st.markdown("### Information")
    st.markdown("""
    1. **Eligibility :** 
        - Requires financial need (determined by FAFSA), half-time enrollment, and satisfactory academic progress. 
    2. **Earnings :** 
        - Students earn at least minimum wage, working up to 20 hours/week during the school year (more during breaks). Earnings go directly to students. 
    3. **How to Apply :** 
        - Complete the FAFSA, then search for jobs through the school’s student employment office.
    4. **Benefits :** 
        - Provides job experience, helps reduce reliance on loans, and allows students to earn money without affecting future financial aid eligibility. 
    5. **Limitations :** 
        - Funding is limited, and not all eligible students will receive FWS jobs.
    """)

with tabs[2]:
    st.markdown("### What is it?")
    st.write("Outside Scholarships for College are financial awards from organizations, businesses, or foundations, not affiliated with the federal government or your school.")
    st.markdown("### Types of Scholarships")
    st.markdown("""
    1. **Merit-Based :** 
        - Based on academic performance.
    2. **Demographic-Based :** 
        - For specific groups (e.g., race, gender). Field of Study: For students in certain majors (e.g., STEM).
    3. **Community Service :** 
        - For students with volunteer work. Employer/Association-Based: From employers or professional organizations.
    4. **Essay/Creative :** 
        - Based on an essay or project submission.
    """)
    st.markdown("### Finding and Applying")
    st.markdown("""
    1. **How to Find Them :** 
        - Use scholarship search engines (Fastweb, Scholarships.com). Check with high school counselors and college financial aid offices. Look into employer-sponsored and community or religious group scholarships.
    2. **How to Apply :** 
        - Prepare materials: transcripts, letters of recommendation, essays, etc. Tailor essays to each scholarship’s focus. Submit applications on time.
    3. **Tips :** 
        - Avoid scams (never pay to apply). Apply to multiple scholarships. Stay organized and track deadlines.
    """)

with tabs[3]:
    st.markdown("### What is it?")
    st.write("The Federal Direct Subsidized Loan is a need-based loan for undergraduate students that helps pay for college costs. The government covers the interest while the student is in school, during the 6-month grace period after graduation, and during deferment.")
    st.markdown("### Information")
    st.markdown("""
    1. **Eligibility :** 
        - For undergraduate students with financial need (determined by FAFSA), enrolled at least half-time.
    2. **Loan Limits :** 
        - First-year: Up to 3500 dollars. Second-year: Up to 4500 dollars. Third-year and Beyond: Up to 5500 dollars. Lifetime limit: 23000 dollars for dependent students.
    3. **Interest Rate :** 
        - Fixed at 5.50% (for 2023-2024). 
    4. **Repayment :** 
        - Starts 6 months after graduation or dropping below half-time.
    5. **Benefits :** 
        - Lower cost due to government-paid interest while in school, fixed interest rates, and flexible repayment options.
    6. **Limitations :** 
        - Available only to undergraduates, with borrowing limits and eligibility for up to 150 percent of program length. 
    7. **How to Apply :** 
        - Complete the FAFSA to determine eligibility.
    """)

with tabs[4]:
    st.markdown("### What is it?")
    st.write("The Federal Direct Unsubsidized Loan is a federal student loan for undergraduate and graduate students, available regardless of financial need. Unlike subsidized loans, borrowers are responsible for paying the interest, which accrues from the moment the loan is disbursed, including while in school.")
    st.markdown("### Key Details")
    st.markdown("""
    1. **Eligibility :** 
        - Available to undergraduate and graduate students enrolled at least half-time.
    2. **Loan Limits :** 
        - Undergraduates: Up to 5500 for first-year students and 7500 for upperclassmen. Graduate students can recieve up to 20500 dollars per year.
    3. **Interest Rate :** 
        - 5.50 percent for undergraduates and 7.05 percent for graduate students (2023-2024).
    4. **Repayment :** 
        - Begins 6 months after graduation or dropping below half-time, with several repayment options available.
    5. **Benefits :** 
        - No financial need requirement. Fixed interest rates and flexible repayment plans. Drawbacks: Interest accrues while in school, increasing the loan’s total cost.
    6. **How to Apply :** 
        - Complete the FAFSA.
    """)

st.title (" 🏦 Federal Student Loan Repayment")
st.subheader("What is it?")
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
    st.markdown("### What is it?")
    st.write("Federal student loan repayment plans offer flexibility to match borrowers' financial situations.")
    st.markdown("### Information")
    st.markdown("""
    1. **Standard Repayment Plan :** 
        - Payments : Fixed for 10 years. Pros: Fastest repayment, less interest. Cons: Higher monthly payments.
    2. **Graduated Repayment Plan :** 
        - Payments : Start low, increase every 2 years, term is 10 years. Pros: Lower initial payments. Cons: Higher total interest.
    3. **Extended Repayment Plan :** 
        - Payments: Fixed or graduated for up to 25 years. Eligibility: For balances of $30,000+. Pros: Lower payments. Cons: Longer term, more interest.
    4. **Income-Driven Repayment (IDR) Plans :** 
        -  Plans: Payments based on income and family size, with forgiveness after 20-25 years. IBR: 15 percent of income, 25-year forgiveness. PAYE: 10 percent of income, 20-year forgiveness. REPAYE: 10 percent of income, 20 years (undergrad) or 25 years (grad). ICR: 20 percent of income, 25-year forgiveness. Pros: Lower payments, forgiveness. Cons: Longer repayment, more interest.
    5. **How to Apply :** 
        - Apply or change plans via StudentAid.gov or through your loan servicer. 
    """)

with tabs[1]:
    st.markdown("### What is it?")
    st.write("Deferment and forbearance are temporary relief options for federal student loan borrowers who are unable to make payments.")
    st.markdown("### Information")
    st.markdown("""
    1. **Deferment :**
    Eligibility : Available for situations like school enrollment, unemployment, or military service.
        - Interest : Subsidized loans: The government pays interest.
        - Unsubsidized loans : Interest accrues and must be paid by the borrower.
        - Duration : Varies (e.g., while in school or for up to 3 years for economic hardship). Pros: Government covers interest on subsidized loans. Cons: Interest accrues on unsubsidized loans, increasing the balance.
    2. **Forbearance :**
    Eligibility : Available for reasons like financial hardship, medical issues, or job loss.
        - Interest : Accrues on all loans, including subsidized loans, and is added to the balance if unpaid.
        - Duration : Up to 12 months, renewable. Pros: Easier to apply for and faster approval. Cons: Interest accrues on all loan types, raising the total balance.
    """)

with tabs[2]:
    st.markdown("### What is it?")
    st.write("Federal Loan Forgiveness and Discharge offer relief for federal student loan borrowers under specific conditions.")
    st.markdown("### Information")
    st.markdown("""
    1. **Forgiveness Programs :**
    Public Service Loan Forgiveness (PSLF) :
        - For those working in qualifying public service jobs. Requires 120 qualifying payments under an IDR plan. Remaining loan balance is forgiven. 
    Teacher Loan Forgiveness : 
        - For teachers in low-income schools. Requires 5 years of service. Forgives up to $17,500. 
    Income-Driven Repayment (IDR) Forgiveness : 
        - For borrowers on IDR plans. After 20-25 years of payments, the remaining balance is forgiven. 
    Military Service Forgiveness : 
        - Available for military members. Forgiveness depends on the branch and service.
    How to Apply: 
        - Submit required forms to your loan servicer or the Department of Education.
    2. **Discharge Programs :**
    Total and Permanent Disability : 
        - For borrowers with total disability. Full loan cancellation after proof. 
    School Closure : 
        - If your school closes while you're enrolled. Full loan discharge. 
    False Certification : 
        - If the school falsely certified your eligibility. Full loan cancellation. 
    Unpaid Refund : 
        - If your school didn't return a required refund after withdrawal. Loan cancellation for that amount. 
    Bankruptcy : 
        - In rare cases, student loans can be discharged if you prove undue hardship in bankruptcy court.
    How to Apply: 
    - Apply with documentation to your loan servicer or the Department of Education.
    """)