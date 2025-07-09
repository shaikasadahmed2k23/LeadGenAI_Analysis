"""
LEADGen AI - Streamlit UI
Professional lead generation tool with modern business interface.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import time  
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from leadGENAI import LeadGenAI

st.set_page_config(
    page_title="LEADGen AI - Intelligent Lead Generation",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .header-container {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    .header-title {
        color: white;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .header-subtitle {
        color: #e0e6ed;
        font-size: 1.2rem;
        text-align: center;
        font-weight: 300;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
    }
    .metric-title {
        color: #2c3e50;
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    .metric-value {
        color: #1e3c72;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
    }
    .metric-description {
        color: #7f8c8d;
        font-size: 0.85rem;
    }
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    .css-1d391kg {
        background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
    }
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    .success-message {
        background: linear-gradient(90deg, #56ab2f 0%, #a8e6cf 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        font-weight: 600;
    }
    .warning-message {
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        font-weight: 600;
    }
    .info-message {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        font-weight: 600;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background: white;
        border-radius: 8px 8px 0 0;
        color: #2c3e50;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def create_header():
    """Create the main header section."""
    st.markdown("""
    <div class="header-container">
        <div class="header-title">🚀 LEADGen AI</div>
        <div class="header-subtitle">Intelligent Lead Generation for Venture Capital Firms</div>
    </div>
    """, unsafe_allow_html=True)

def create_metric_card(title, value, description, color="#667eea"):
    """Create a styled metric card."""
    st.markdown(f"""
    <div class="metric-card" style="border-left-color: {color};">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-description">{description}</div>
    </div>
    """, unsafe_allow_html=True)

def create_investment_score_gauge(score):
    """Create an investment score gauge chart."""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Investment Score", 'font': {'size': 24}},
        delta = {'reference': 50},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 40], 'color': '#ff6b6b'},
                {'range': [40, 60], 'color': '#feca57'},
                {'range': [60, 80], 'color': '#48dbfb'},
                {'range': [80, 100], 'color': '#1dd1a1'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        font={'color': "#2c3e50"}
    )
    
    return fig

def create_growth_signals_chart(growth_signals):
    """Create a growth signals visualization."""
    if not growth_signals or growth_signals == "N/A":
        return None
    
    signals = growth_signals.split(', ')
    signal_counts = {}
    
    for signal in signals:
        signal_counts[signal] = signal_counts.get(signal, 0) + 1
    
    if not signal_counts:
        return None
    
    fig = px.bar(
        x=list(signal_counts.keys()),
        y=list(signal_counts.values()),
        title="Growth Signals Analysis",
        labels={'x': 'Growth Signal', 'y': 'Frequency'},
        color=list(signal_counts.values()),
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        font={'color': "#2c3e50"},
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    
    return fig

def create_funding_timeline(funding_rounds):
    """Create a funding timeline visualization."""
    if not funding_rounds:
        return None
    
    timeline_data = []
    for i, round_data in enumerate(funding_rounds):
        timeline_data.append({
            'Round': round_data.get('type', f'Round {i+1}'),
            'Amount': round_data.get('amount', 'N/A'),
            'Year': 2020 + i
        })
    
    fig = px.timeline(
        timeline_data,
        x_start='Year',
        y='Round',
        title='Funding Timeline',
        color='Amount',
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        font={'color': "#2c3e50"},
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    
    return fig

def display_company_profile(profile):
    """Display the company profile in a structured way."""
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Overview", "💰 Financial", "📈 Growth", "👥 Team & Contact", "📋 Raw Data"])
    
    with tab1:
        st.subheader("Company Overview")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            create_metric_card(
                "Founded Year",
                profile.get('founded_year', 'N/A'),
                "Company establishment year",
                "#667eea"
            )
        
        with col2:
            create_metric_card(
                "Company Age",
                f"{profile.get('company_age', 'N/A')} years",
                "Years since founding",
                "#764ba2"
            )
        
        with col3:
            create_metric_card(
                "Industry",
                profile.get('industry', 'N/A'),
                "Primary business sector",
                "#f093fb"
            )
        
        st.subheader("Investment Analysis")
        
        why_invest = profile.get('why_invest', '')
        score = 50
        
        if 'Investment score:' in why_invest:
            try:
                score_text = why_invest.split('Investment score:')[1].split('/')[0]
                score = int(score_text.strip())
            except:
                pass
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = create_investment_score_gauge(score)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### Investment Recommendation")
            st.markdown(f"**{profile.get('why_invest', 'N/A')}**")
            
            if score >= 80:
                st.markdown('<div class="success-message">🟢 Low Risk Investment</div>', unsafe_allow_html=True)
            elif score >= 60:
                st.markdown('<div class="info-message">🟡 Moderate Risk Investment</div>', unsafe_allow_html=True)
            elif score >= 40:
                st.markdown('<div class="warning-message">🟠 Moderate-High Risk Investment</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="warning-message">🔴 High Risk Investment</div>', unsafe_allow_html=True)
        
        st.subheader("Company Summary")
        st.info(profile.get('summary', 'No summary available'))
    
    with tab2:
        st.subheader("Financial Information")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            create_metric_card(
                "Revenue Estimate",
                profile.get('revenue_est', 'N/A'),
                "Annual revenue projection",
                "#56ab2f"
            )
        
        with col2:
            create_metric_card(
                "Total Funding",
                profile.get('total_funding_raised', 'N/A'),
                "Total capital raised",
                "#f093fb"
            )
        
        with col3:
            create_metric_card(
                "Valuation",
                profile.get('valuation', 'N/A'),
                "Company valuation",
                "#4facfe"
            )
        
        st.subheader("Funding Timeline")
        funding_fig = create_funding_timeline(profile.get('funding_rounds', []))
        if funding_fig:
            st.plotly_chart(funding_fig, use_container_width=True)
        else:
            st.info("No funding round data available")
    
    with tab3:
        st.subheader("Growth Analysis")
        
        growth_fig = create_growth_signals_chart(profile.get('growth_signals'))
        if growth_fig:
            st.plotly_chart(growth_fig, use_container_width=True)
        else:
            st.info("No growth signals data available")
        
        if profile.get('growth_signals') and profile['growth_signals'] != "N/A":
            signals = profile['growth_signals'].split(', ')
            st.subheader("Growth Signals Breakdown")
            
            for signal in signals:
                st.markdown(f"✅ **{signal.strip()}**")
    
    with tab4:
        st.subheader("Team & Contact Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Team Information")
            create_metric_card(
                "Team Size",
                profile.get('team_size', 'N/A'),
                "Number of employees",
                "#667eea"
            )
            
            st.markdown("### Location")
            st.info(profile.get('locations', 'N/A'))
        
        with col2:
            st.markdown("### Contact Information")
            
            emails = profile.get('contact_info', {}).get('emails', [])
            if emails:
                st.markdown("**📧 Email Addresses:**")
                for email in emails:
                    st.code(email)
            
            phones = profile.get('contact_info', {}).get('phones', [])
            if phones:
                st.markdown("**📞 Phone Numbers:**")
                for phone in phones:
                    st.code(phone)
            
            social_links = profile.get('social_links', {})
            if social_links:
                st.markdown("**🔗 Social Media:**")
                for platform, link in social_links.items():
                    st.markdown(f"**{platform.title()}:** {link}")
    
    with tab5:
        st.subheader("Raw Data")
        st.json(profile)

def main():
    """Main application function."""
    
    if 'lead_gen' not in st.session_state:
        st.session_state.lead_gen = LeadGenAI()
    
    create_header()
    
    st.sidebar.markdown("## 🎯 Analysis Options")
    
    analysis_type = st.sidebar.selectbox(
        "Analysis Type",
        ["Single Company", "Batch Analysis"],
        help="Choose between analyzing a single company or multiple companies"
    )
    
    if analysis_type == "Single Company":
        st.sidebar.markdown("### 📋 Company Information")
        
        company_name = st.sidebar.text_input(
            "Company Name",
            placeholder="e.g., Tesla, SpaceX, OpenAI",
            help="Enter the name of the company you want to analyze"
        )
        
        st.sidebar.markdown("### ⚙️ Analysis Settings")
        
        max_retries = st.sidebar.slider(
            "Max Retries",
            min_value=1,
            max_value=5,
            value=3,
            help="Maximum number of retry attempts for web requests"
        )
        
        delay_range = st.sidebar.slider(
            "Delay Range (seconds)",
            min_value=0.5,
            max_value=5.0,
            value=(1.0, 3.0),
            step=0.5,
            help="Range of delays between requests to avoid rate limiting"
        )
        
        st.session_state.lead_gen.max_retries = max_retries
        st.session_state.lead_gen.delay_range = delay_range
        
        st.sidebar.markdown("### 📤 Export Options")
        
        export_format = st.sidebar.selectbox(
            "Export Format",
            ["JSON", "Markdown", "Text"],
            help="Choose the format for exporting results"
        )
        
        if company_name:
            if st.button("🚀 Analyze Company", type="primary"):
                with st.spinner("🔍 Analyzing company data..."):
                    try:
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        for i in range(100):
                            time.sleep(0.01)
                            progress_bar.progress(i + 1)
                            if i < 30:
                                status_text.text("🔍 Searching for company information...")
                            elif i < 60:
                                status_text.text("📊 Extracting company data...")
                            elif i < 90:
                                status_text.text("📈 Analyzing investment potential...")
                            else:
                                status_text.text("✅ Analysis complete!")
                        
                        profile = st.session_state.lead_gen.extract_company_profile(company_name)
                        
                        st.session_state.current_profile = profile
                        
                        progress_bar.empty()
                        status_text.empty()
                        
                        st.success(f"✅ Analysis completed for {company_name}!")
                        
                    except Exception as e:
                        st.error(f"❌ Error during analysis: {str(e)}")
                        st.session_state.current_profile = None
            
            if 'current_profile' in st.session_state and st.session_state.current_profile:
                display_company_profile(st.session_state.current_profile)
                
                if st.button("📥 Export Results"):
                    if export_format == "JSON":
                        st.download_button(
                            label="Download JSON",
                            data=json.dumps(st.session_state.current_profile, indent=2),
                            file_name=f"{company_name}_analysis.json",
                            mime="application/json"
                        )
                    elif export_format == "Markdown":
                        report = st.session_state.lead_gen.generate_lead_report(company_name, "markdown")
                        st.download_button(
                            label="Download Markdown",
                            data=report,
                            file_name=f"{company_name}_analysis.md",
                            mime="text/markdown"
                        )
                    else:
                        report = st.session_state.lead_gen.generate_lead_report(company_name, "text")
                        st.download_button(
                            label="Download Text",
                            data=report,
                            file_name=f"{company_name}_analysis.txt",
                            mime="text/plain"
                        )
        
        else:
            st.markdown("""
            <div class="info-message">
                👋 Welcome to LEADGen AI! Enter a company name in the sidebar to start your analysis.
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <div class="metric-card">
                    <div class="metric-title">🔍 Comprehensive Analysis</div>
                    <div class="metric-value">Multi-Source</div>
                    <div class="metric-description">Data from Crunchbase, TechCrunch, LinkedIn, and more</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="metric-card">
                    <div class="metric-title">📊 Investment Scoring</div>
                    <div class="metric-value">AI-Powered</div>
                    <div class="metric-description">Intelligent investment recommendations and risk assessment</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                <div class="metric-card">
                    <div class="metric-title">📈 Growth Signals</div>
                    <div class="metric-value">Real-Time</div>
                    <div class="metric-description">Track hiring, funding, expansion, and growth indicators</div>
                </div>
                """, unsafe_allow_html=True)
    
    else:
        st.sidebar.markdown("### 📁 Batch Upload")
        
        uploaded_file = st.sidebar.file_uploader(
            "Upload Company List",
            type=['txt', 'csv'],
            help="Upload a file with company names (one per line)"
        )
        
        if uploaded_file is not None:
            if st.button("🚀 Analyze Batch", type="primary"):
                st.info("Batch analysis feature coming soon!")
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #7f8c8d; padding: 1rem;">
        <p>🚀 LEADGen AI - Powered by Advanced Web Scraping & AI Analysis</p>
        <p>© 2025 LEADGen AI. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 