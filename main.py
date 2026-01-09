import streamlit as st
import os

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="Azure Wings – Aviation Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# SESSION STATE
# ============================================================================
if 'selected_module' not in st.session_state:
    st.session_state.selected_module = None

# ============================================================================
# CUSTOM CSS
# ============================================================================
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a1d2e 0%, #2d1b4e 100%);
    }
    
    .main {
        background-color: #1a1d2e;
        color: #ffffff;
    }
    
    h1, h2, h3, h4, p, label, span, div {
        color: white !important;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: white;
        border: none;
        padding: 12px;
        border-radius: 8px;
        margin: 5px 0;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4);
    }
    
    [data-testid="stSidebar"] {
        background-color: #1a1d2e;
    }
    
    .module-card {
        background: linear-gradient(135deg, #2d3250 0%, #3d4260 100%);
        padding: 30px;
        border-radius: 15px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .module-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(37, 99, 235, 0.3);
        border: 1px solid rgba(37, 99, 235, 0.5);
    }
    
    .feature-badge {
        background-color: rgba(37, 99, 235, 0.2);
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 12px;
        display: inline-block;
        margin: 5px 5px 5px 0;
        border: 1px solid rgba(37, 99, 235, 0.4);
    }
</style>
""", unsafe_allow_html=True)



# ============================================================================
# HEADER
# ============================================================================
st.markdown("""
<div style='text-align: center; padding: 40px 0 20px 0;'>
    <h1 style='font-size: 3.5rem; margin-bottom: 10px;'>🛫 Azure Wings</h1>
    <p style='font-size: 1.3rem; color: #94a3b8;'>Integrated Aviation Management Platform</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================================
# NAVIGATION INFO
# ============================================================================
st.markdown("""
<div style='background-color: rgba(37, 99, 235, 0.1); padding: 20px; border-radius: 10px; border-left: 4px solid #2563eb; margin: 30px 0;'>
    <h3 style='margin-top: 0;'>📍 Welcome to Azure Wings Platform</h3>
    <p style='color: #94a3b8; line-height: 1.8;'>
        This is your central hub for aviation operations management. Use the sidebar to navigate between modules
 for risk prediction, crew scheduling, and operational optimization.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# MODULE CARDS
# ============================================================================

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class='module-card'>
        <h2 style='color: #60a5fa; margin-top: 0;'>📊 Risk Predictions & AI Copilot</h2>
        <p style='color: #94a3b8; line-height: 1.8; margin: 20px 0;'>
            Advanced machine learning models for real-time aviation risk assessment and prediction across multiple domains.
        </p>
        <div style='margin: 20px 0;'>
            <span class='feature-badge'>Weather Delay Prediction</span>
            <span class='feature-badge'>Crew Sickness Analysis</span>
            <span class='feature-badge'>Equipment Failure Detection</span>
            <span class='feature-badge'>Emergency Landing Risk</span>
            <span class='feature-badge'>Operational Risk Index</span>
            <span class='feature-badge'>AI-Powered Copilot (Phi-3)</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("📊 Open **Risk Predictions & AI Copilot** from the sidebar")

        

with col2:
    st.markdown("""
    <div class='module-card'>
        <h2 style='color: #4ade80; margin-top: 0;'>📅 Crew Schedule Optimizer</h2>
        <p style='color: #94a3b8; line-height: 1.8; margin: 20px 0;'>
            Intelligent crew scheduling system powered by Google OR-Tools for optimal resource allocation and compliance.
        </p>
        <div style='margin: 20px 0;'>
            <span class='feature-badge'>OR-Tools Optimization</span>
            <span class='feature-badge'>Constraint Management</span>
            <span class='feature-badge'>Duty Hour Compliance</span>
            <span class='feature-badge'>Gantt Visualization</span>
            <span class='feature-badge'>Utilization Analytics</span>
            <span class='feature-badge'>Real-time Adjustments</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("📊 Open **Crew Schedule Optimizer** from the sidebar")

       

st.markdown("<br><br>", unsafe_allow_html=True)

# ============================================================================
# SYSTEM INFORMATION
# ============================================================================
st.markdown("---")

st.markdown("""
<div style='background-color: #2d3250; padding: 25px; border-radius: 12px; margin: 30px 0;'>
    <h3 style='margin-top: 0; color: #60a5fa;'>🔧 System Architecture</h3>
    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;'>
        <div>
            <h4 style='color: #94a3b8; font-size: 14px; margin-bottom: 10px;'>TECHNOLOGY STACK</h4>
            <p style='color: #cbd5e1; line-height: 1.8;'>
                • Python + Streamlit<br>
                • Scikit-learn ML Models<br>
                • Google OR-Tools CP-SAT<br>
                • Plotly Visualizations<br>
                • Phi-3 AI Copilot (Ollama)
            </p>
        </div>
        <div>
            <h4 style='color: #94a3b8; font-size: 14px; margin-bottom: 10px;'>DEPLOYMENT</h4>
            <p style='color: #cbd5e1; line-height: 1.8;'>
                • Multi-page Application<br>
                • Shared Session State<br>
                • Real-time Processing<br>
                • Persistent Data Storage<br>
                • Modular Architecture
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# QUICK START GUIDE
# ============================================================================
st.markdown("---")

with st.expander("📖 Quick Start Guide", expanded=False):
    st.markdown("""
    ### Getting Started with Azure Wings
    
    **Step 1: Launch a Module**
    - Click on "Launch Risk Predictions" or "Launch Schedule Optimizer" button
    - The module will automatically open in a new browser window
    - Keep this main page open to switch between modules
    
    **Step 2: Use the Module**
    - Each module opens independently with full functionality
    - You can run both modules simultaneously
    - Simply click the other launch button to open the second module
    
    **Step 3: Navigate Between Modules**
    - Return to this page to launch other modules
    - All modules can run at the same time
    - Each module maintains its own session state
    
    ---
    
    ### Module-Specific Instructions
    
    **Risk Predictions Module (screen2.py):**
    1. Select a prediction model from the radio buttons
    2. Fill in the required input parameters
    3. Click "Run Prediction" to get results
    4. Use the AI Copilot to ask questions about your predictions
    
    **Schedule Optimizer Module (screen3.py):**
    1. Adjust constraints in the sidebar (duty hours, rest time, max flights)
    2. Click "Generate Schedule" to run optimization
    3. View results in tabs: Gantt Chart, Crew Assignments, Flight Details, Utilization
    4. Use "Reset" to clear and start fresh
    
    ---
    
    ### Troubleshooting
    
    **If a module doesn't launch:**
    - Make sure screen2.py and screen3.py are in the same folder as main.py
    - Check that all required Python packages are installed
    - Verify that no other Streamlit apps are using the same port
    
    **Manual Launch (Alternative):**
    - Open a terminal in your project folder
    - Run: `streamlit run screen2.py` or `streamlit run screen3.py`
    """)

# ============================================================================
# CURRENT DIRECTORY INFO
# ============================================================================
st.markdown("---")
with st.expander("🗂️ System Information", expanded=False):
    st.markdown(f"**Current Directory:** `{os.getcwd()}`")
    st.markdown("**Available Python Files:**")
    python_files = [f for f in os.listdir('.') if f.endswith('.py')]
    for file in python_files:
        icon = "✅" if file in ["screen2.py", "screen3.py"] else "📄"
        st.markdown(f"- {icon} {file}")

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 20px 0;'>
    <p>Azure Wings Aviation Platform v2.0</p>
    <p style='font-size: 0.9rem;'>Powered by Machine Learning • OR-Tools • AI Copilot</p>
</div>
""", unsafe_allow_html=True)