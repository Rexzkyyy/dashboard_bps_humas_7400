# =============================================================================
# DASHBOARD PUSAT KENDALI KEHUMASAN — BPS SULTRA
# styles.py v3.0 — Unified Nexus Slate Design System
# =============================================================================

BPS_ORANGE = "#F26522"
BPS_BLUE = "#8CCEFF"
SURFACE_DARK = "#0D0D15"
SURFACE_CARD = "rgba(31, 31, 39, 0.6)"

def get_all_styles() -> str:
    """Returns all CSS combined for the application."""
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

    /* ── Global Setup ─────────────────────────────────────────── */
    html, body, [class*="css"], .stApp {{
        font-family: 'Inter', sans-serif !important;
        background: {SURFACE_DARK} !important;
        background-attachment: fixed !important;
        color: #e4e1ed !important;
    }}
    
    .stApp {{
        background-image: 
            radial-gradient(at 0% 0%, rgba(242, 101, 34, 0.12) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(140, 206, 255, 0.08) 0px, transparent 50%) !important;
    }}

    h1, h2, h3, .sb-logo-title, .chart-header, .gcard-label {{
        font-family: 'Manrope', sans-serif !important;
    }}

    /* ── Hide Streamlit Elements ──────────────────────────────── */
    #MainMenu, footer {{ visibility: hidden !important; }}
    header[data-testid="stHeader"] {{ background: transparent !important; }}
    [data-testid="stAppDeploy"], .stDeployButton {{ display: none !important; }}
    [data-testid="stDecoration"] {{ display: none !important; }}

    /* ── Sidebar Redesign (Command Center Style) ───────────────── */
    [data-testid="stSidebar"] {{
        background: rgba(19, 19, 27, 0.7) !important;
        backdrop-filter: blur(40px) !important;
        -webkit-backdrop-filter: blur(40px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
        box-shadow: 15px 0 60px rgba(0,0,0,0.5) !important;
    }}
    
    [data-testid="stSidebar"] div.stButton > button {{
        width: 100% !important;
        background: transparent !important;
        border: 1px solid rgba(255,255,255,0.03) !important;
        color: #888aaa !important;
        text-align: left !important;
        padding: 14px 20px !important;
        font-weight: 500 !important;
        border-radius: 14px !important;
        transition: all 0.3s ease !important;
        margin-bottom: 8px !important;
    }}
    
    [data-testid="stSidebar"] div.stButton > button:hover {{
        background: rgba(242, 101, 34, 0.1) !important;
        color: #F26522 !important;
        border-color: rgba(242, 101, 34, 0.3) !important;
        transform: translateX(6px);
    }}
    
    [data-testid="stSidebar"] div.stButton > button[kind="primary"] {{
        background: linear-gradient(90deg, rgba(242, 101, 34, 0.2), transparent) !important;
        border-left: 5px solid #F26522 !important;
        color: #F26522 !important;
        font-weight: 800 !important;
        border-radius: 0 14px 14px 0 !important;
    }}

    /* ── Premium Metric Cards (Nexus Slate) ────────────────────── */
    .gcard-wrap {{
        background: {SURFACE_CARD} !important;
        backdrop-filter: blur(32px) !important;
        -webkit-backdrop-filter: blur(32px) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 28px !important;
        padding: 2.2rem 2.5rem;
        margin-bottom: 1.5rem;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 30px 70px rgba(0,0,0,0.4) !important;
    }}
    
    .gcard-wrap:hover {{
        transform: translateY(-12px) scale(1.02);
        background: rgba(41, 41, 52, 0.8) !important;
        border-color: rgba(242, 101, 34, 0.4) !important;
        box-shadow: 0 40px 90px rgba(242, 101, 34, 0.15) !important;
    }}

    .gcard-label {{
        font-size: 0.75rem;
        color: #F26522;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    
    .gcard-value {{
        font-size: 3rem;
        font-weight: 800;
        color: #FFFFFF;
        line-height: 1;
        margin-bottom: 0.8rem;
        letter-spacing: -0.02em;
    }}
    
    .gcard-sub {{
        font-size: 0.85rem;
        color: #888aaa;
        font-weight: 400;
    }}

    /* ── Page Header Redesign ─────────────────────────────────── */
    .pg-header {{
        background: rgba(19, 19, 27, 0.5) !important;
        backdrop-filter: blur(28px) !important;
        border-left: 8px solid #F26522;
        padding: 2.5rem 3.5rem;
        margin: 2rem 0 4rem 0 !important;
        border-radius: 32px;
        box-shadow: 0 35px 80px rgba(0,0,0,0.4);
        border: 1px solid rgba(255,255,255,0.07);
    }}
    
    .pg-header h1 {{
        font-size: 3.2rem !important;
        font-weight: 800 !important;
        color: #FFFFFF !important;
        margin: 0 !important;
        letter-spacing: -0.03em;
    }}
    
    .header-tag {{
        font-size: 0.8rem;
        color: #F26522;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.25em;
        margin-bottom: 1rem;
        display: block;
    }}

    /* ── Chart Container ────────────────────────────────────────── */
    [data-testid="stVerticalBlock"]:has(> .chart-header) {{
        background: rgba(31, 31, 39, 0.5) !important;
        backdrop-filter: blur(32px) !important;
        padding: 40px !important;
        border-radius: 32px !important;
        box-shadow: 0 40px 90px rgba(0,0,0,0.4) !important;
        border: 1px solid rgba(255,255,255,0.06) !important;
        margin-bottom: 3rem !important;
    }}
    
    .chart-header {{
        font-size: 1.5rem;
        color: #FFFFFF;
        font-weight: 800;
        margin-bottom: 2.5rem;
        display: block;
        padding-left: 20px;
        border-left: 6px solid #F26522;
    }}

    /* ── Custom Scrollbar ──────────────────────────────────────── */
    ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
    ::-webkit-scrollbar-track {{ background: #0D0D15; }}
    ::-webkit-scrollbar-thumb {{ background: rgba(242,101,34,0.3); border-radius: 10px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #F26522; }}

    /* ── Modern Table ───────────────────────────────────────────── */
    .modern-table {{
        width: 100%;
        border-collapse: collapse;
        color: #e4e1ed;
        font-size: 1rem;
    }}
    .modern-table th {{
        background: rgba(255,255,255,0.03);
        padding: 20px 15px;
        text-align: left;
        border-bottom: 3px solid #F26522;
        color: #888aaa;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.15em;
    }}
    .modern-table td {{
        padding: 22px 15px;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }}
    .modern-table tr:hover {{
        background: rgba(242, 101, 34, 0.05) !important;
    }}
    
    .badge-source {{
        background: rgba(242, 101, 34, 0.15);
        color: #F26522;
        padding: 4px 12px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 700;
        border: 1px solid rgba(242, 101, 34, 0.3);
    }}
    
    /* ── Mobile Responsiveness (Nexus Slate Mobile Fix) ────────── */
    @media (max-width: 768px) {{
        .pg-header {{
            padding: 1.5rem !important;
            margin: 1rem 0 2rem 0 !important;
            border-radius: 16px;
        }}
        .pg-header h1 {{
            font-size: 1.8rem !important;
            letter-spacing: -0.01em;
        }}
        .header-tag {{
            font-size: 0.65rem;
            letter-spacing: 0.15em;
        }}
        
        .gcard-wrap {{
            padding: 1.5rem !important;
            border-radius: 20px !important;
            margin-bottom: 1rem !important;
        }}
        .gcard-value {{
            font-size: 2.1rem !important;
        }}
        
        .chart-header {{
            font-size: 1.1rem !important;
            margin-bottom: 1.5rem !important;
        }}
        
        /* Table Responsive */
        .table-wrap {{
            overflow-x: auto !important;
            -webkit-overflow-scrolling: touch;
            margin-bottom: 2rem;
        }}
        .modern-table {{
            font-size: 0.85rem !important;
        }}
        .modern-table th, .modern-table td {{
            padding: 12px 10px !important;
            white-space: nowrap !important;
        }}
    }}
    
    .sb-footer {{
        padding: 2rem 1.5rem;
        font-size: 0.75rem;
        color: #555577;
        text-align: center;
        border-top: 1px solid rgba(255,255,255,0.05);
        margin-top: 2rem;
    }}
    </style>
    """

def get_main_css(): return get_all_styles()
def get_sidebar_css(): return ""
def get_metric_card_css(): return ""
def get_page_header_css(): return ""
