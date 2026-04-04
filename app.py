import streamlit as st
import hashlib
import json
from datetime import datetime

# Page config
st.set_page_config(
    page_title="EduVerify India",
    page_icon="🎓",
    layout="wide"
)

# Title & Header
st.title("🎓 EduVerify India")
st.subheader("Blockchain-Based Academic Credential Verification")
st.markdown("---")

# Sidebar
st.sidebar.header("📋 Menu")
option = st.sidebar.radio("Navigate", ["Home", "Verify Certificate", "Issue Certificate (Demo)", "About"])

# Mock blockchain (in-memory for demo)
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

# Home Page
if option == "Home":
    st.header("🚀 Welcome to EduVerify India")
    st.markdown("""
    ### Problem Solved
    - **40% of Indian resumes** contain fake degrees
    - Traditional verification takes **2–4 weeks**
    - Employers lose **crores** in bad hires
    
    ### Our Solution
    ✅ Instant verification in **seconds**  
    ✅ Tamper-proof blockchain records  
    ✅ Student-owned digital credentials  
    ✅ QR code scanning (no app needed)
    
    ### How It Works
    1. **University** issues degree → logs hash on blockchain
    2. **Student** receives digital certificate with QR code
    3. **Employer** scans QR → verifies instantly on-chain
    4. **Verifier** confirms authenticity without contacting university
    """)
    
    st.info("💰 **Token System**: EduCoin (EDU) rewards students for sharing verified credentials!")
    
    # Visual flow
    st.markdown("### 🔗 Blockchain Flow")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Block 1", "University", "Issues Degree")
    with col2:
        st.metric("Block 2", "Student", "Receives QR")
    with col3:
        st.metric("Block 3", "Employer", "Scans QR")
    with col4:
        st.metric("Block 4", "Verifier", "Confirms")

# Verify Certificate Page
elif option == "Verify Certificate":
    st.header("🔍 Verify a Degree Certificate")
    
    cert_hash = st.text_input("Enter Certificate Hash or Scan QR Code", placeholder="e.g., a3f5b8c9d2e1...")
    
    if st.button("Verify Now"):
        if cert_hash:
            # Mock verification (in real app, query blockchain)
            mock_record = {
                "student_name": "Rahul Sharma",
                "degree": "B.Tech in Computer Science",
                "university": "IIT Delhi",
                "graduation_year": 2024,
                "cgpa": "9.2/10.0",
                "issue_date": "2024-06-15",
                "status": "✅ VERIFIED",
                "blockchain_hash": cert_hash
            }
            
            st.success("Certificate Verified Successfully!")
            st.json(mock_record)
            
            st.markdown("""
            **Verification Details:**
            - Issued by: IIT Delhi (Authorized Institution)
            - Logged on: Polygon Blockchain
            - Immutable: Yes
            - Tamper-proof: Yes
            """)
        else:
            st.warning("Please enter a certificate hash.")

# Issue Certificate (Demo)
elif option == "Issue Certificate (Demo)":
    st.header("📜 Issue a Digital Certificate (University Demo)")
    
    col1, col2 = st.columns(2)
    with col1:
        student_name = st.text_input("Student Name")
        degree = st.text_input("Degree/Course")
        university = st.text_input("University Name")
    with col2:
        graduation_year = st.number_input("Graduation Year", min_value=2020, max_value=2030)
        cgpa = st.text_input("CGPA")
        issue_date = st.date_input("Issue Date", datetime.now())
    
    if st.button("Issue Certificate"):
        if student_name and degree and university:
            # Create certificate data
            cert_data = {
                "student_name": student_name,
                "degree": degree,
                "university": university,
                "graduation_year": graduation_year,
                "cgpa": cgpa,
                "issue_date": str(issue_date),
                "timestamp": datetime.now().isoformat()
            }
            
            # Generate blockchain hash
            cert_hash = hashlib.sha256(json.dumps(cert_data, sort_keys=True).encode()).hexdigest()
            
            # Store in mock blockchain
            block = {
                "block_number": len(st.session_state.blockchain) + 1,
                "timestamp": datetime.now().isoformat(),
                "data": cert_data,
                "hash": cert_hash,
                "previous_hash": st.session_state.blockchain[-1]["hash"] if st.session_state.blockchain else "0"
            }
            st.session_state.blockchain.append(block)
            
            st.success(f"✅ Certificate Issued Successfully!")
            st.markdown(f"**Certificate Hash:** `{cert_hash}`")
            st.json(cert_data)
            
            st.info("📱 Student can now download QR code and share with employers!")
        else:
            st.warning("Please fill all required fields.")

# About Page
elif option == "About":
    st.header("📖 About EduVerify India")
    
    st.markdown("""
    ### Mission
    To eliminate fake degrees and restore trust in India's education and hiring systems through blockchain technology.
    
    ### Key Benefits
    - ⚡ **Instant Verification**: Seconds instead of weeks
    - 🔒 **Tamper-Proof**: Immutable blockchain records
    - 🎯 **Student Ownership**: Learners control their credentials
    - 💰 **Cost Savings**: Reduces admin burden for universities
    
    ### Token System: EduCoin (EDU)
    - Students earn EDU for sharing verified credentials
    - Employers pay EDU for bulk verification
    - Universities earn EDU for each certificate issued
    
    ### Compliance & Risks Managed
    - ✅ Follows UGC digital credential standards
    - ✅ DPDP Act 2023 compliant (encrypted data)
    - ✅ 2FA for wallet security
    - ✅ Backup systems for 99.9% uptime
    
    ### Team
    Built by: **Bhumi Sachdeva**  
    Experiment 8: Blockchain Startup Design Project
    """)
    
    st.markdown("---")
    st.caption("© 2026 EduVerify India | Blockchain for Education")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | Experiment 8: Blockchain Startup Design")
