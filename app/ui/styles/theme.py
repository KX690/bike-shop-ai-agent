"""
theme.py

Responsabilidad:
    Definir y aplicar el sistema de estilos global de la aplicación Streamlit.
"""

import streamlit as st


def apply_custom_theme() -> None:
    """Aplica el tema visual global de la aplicación."""

    st.markdown(
        """
        <style>

        /* =====================================================
           BASE LAYOUT
        ===================================================== */

        .main {
            padding: 2rem;
        }

        /* =====================================================
           TYPOGRAPHY
        ===================================================== */

        .main-title {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(
                135deg,
                #ff6b35 0%,
                #f7931e 35%,
                #ffb347 100%
            );
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }

        .subtitle {
            font-size: 1.2rem;
            color: #2f2f33;
            font-weight: 500;
            margin-bottom: 1.5rem;
        }

        /* =====================================================
           CHAT MESSAGES
        ===================================================== */

        .user-message {
            background: linear-gradient(
                135deg,
                #ff6b35 0%,
                #d9480f 100%
            );
            color: white !important;
            padding: 1rem 1.5rem;
            border-radius: 18px 18px 4px 18px;
            margin: 0.5rem 0;
            max-width: 80%;
            margin-left: auto;
            box-shadow: 0 4px 12px rgba(217, 72, 15, 0.2);
            border: none;
        }

        .assistant-message {
            background: #fff4ec;
            color: #2f2f33;
            padding: 1rem 1.5rem;
            border-radius: 18px 18px 18px 4px;
            margin: 0.5rem 0;
            max-width: 80%;
            border-left: 4px solid #2ecc71;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }

        /* =====================================================
           INPUT
        ===================================================== */

        .stTextInput > div > div > input {
            border-radius: 25px !important;
            border: 2px solid #ffd9b3;
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
            transition: all 0.3s ease;
            background-color: white;
        }

        .stTextInput > div > div > input:focus {
            border-color: #ff6b35 !important;
            box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.2);
        }

        /* =====================================================
           LOADING
        ===================================================== */

        .stSpinner > div {
            border-color: #ff6b35 transparent transparent transparent !important;
        }

        /* =====================================================
           CARDS / STATISTICS
        ===================================================== */

        .stat-card {
            background: linear-gradient(
                135deg,
                #fff4ec 0%,
                #ffe8d6 100%
            );
            padding: 1rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            text-align: center;
            margin: 0.5rem 0;
            border: 1px solid #ffd9b3;
        }

        .stat-card div {
            color: #2f2f33;
        }

        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #d9480f;
        }

        /* =====================================================
           BUTTONS
        ===================================================== */

        .stButton > button {
            border-radius: 20px !important;
            transition: all 0.3s ease !important;
        }

        .stButton > button:hover {
            transform: scale(0.98);
        }

        /* =====================================================
           INFO BOX
        ===================================================== */

        .info-box {
            background: linear-gradient(
                135deg,
                #ffe8d6 0%,
                #d4edda 100%
            );
            padding: 1rem 1.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            border-left: 4px solid #2ecc71;
        }

        .info-box p {
            margin: 0;
            color: #2f2f33;
        }

        /* =====================================================
           SIDEBAR
        ===================================================== */

        .sidebar-section {
            background: #fff4ec;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            border: 1px solid #ffd9b3;
        }

        .sidebar-section h2 {
            color: #d9480f !important;
            margin-bottom: 0.3rem;
        }

        .sidebar-section h3,
        .sidebar-section .sidebar-title {
            color: #d9480f !important;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .sidebar-section p {
            color: #2f2f33 !important;
            margin: 0.5rem 0;
        }

        .sidebar-section strong {
            color: #d9480f !important;
        }

        .sidebar-section ul {
            color: #2f2f33 !important;
            padding-left: 1.5rem;
            margin: 0.5rem 0;
        }

        .sidebar-section ul li {
            color: #2f2f33 !important;
            margin-bottom: 0.3rem;
        }

        .sidebar-section span {
            color: #2f2f33 !important;
        }

        .sidebar-section .text-secondary {
            color: #b56a45 !important;
            font-size: 0.8rem;
        }

        .sidebar-section .text-muted {
            color: #7f8c8d !important;
            font-size: 0.85rem;
        }

        /* =====================================================
           FOOTER
        ===================================================== */

        .footer {
            text-align: center;
            color: #b56a45;
            padding: 2rem 0 1rem 0;
            border-top: 2px solid #ffe8d6;
            margin-top: 2rem;
            font-size: 0.9rem;
        }

        .footer strong {
            color: #d9480f !important;
        }

        .footer span {
            color: #b56a45 !important;
        }

        /* =====================================================
           STATUS BADGES
        ===================================================== */

        .status-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        .status-online {
            background: #d4edda;
            color: #155724;
        }

        .status-offline {
            background: #f8d7da;
            color: #721c24;
        }

        /* =====================================================
           METRICS
        ===================================================== */

        .metric-value {
            color: #d9480f;
            font-size: 1.5rem;
            font-weight: bold;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
