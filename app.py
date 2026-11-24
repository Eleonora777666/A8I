import datetime
import random
import streamlit as st

st.set_page_config(
    page_title="A8I — Autonomous AI Agency Command Center",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {
            "id": 1,
            "client": "Target Partner #1",
            "agent": "Outbound Marketplace Strategist",
            "offer": "Automated workflow and content generation subscription",
            "status": "Sent",
            "response": "Awaiting response",
            "date": str(datetime.date.today()),
        }
    ]

if "logs" not in st.session_state:
    st.session_state.logs = [
        f"[{datetime.datetime.now().strftime('%H:%M:%S')}] A8I System initialized. Exactly 8 AI agents online."
    ]

TEAM = {
    "Project Manager (Chief of Staff)": "Main coordinator: distributes tasks, manages internal state",
    "Listing Copywriter": "Specialist in SEO product descriptions and text generation",
    "Market Research Analyst": "Market researcher: scanning targets and gathering data",
    "Competitive Price Strategist": "Price analyst: monitoring competitors and margins",
    "Review & Support Triage Specialist": "Customer service specialist: feedback and ticket handling",
    "Campaign & Promo Builder (Graphic Designer)": "Creative agent: visual assets, mockups, and promos",
    "Catalog & Inventory Auditor": "Technical auditor: internal catalog and stock check",
    "Outbound Marketplace Strategist": "Sales manager: sending proposals and custom plans",
}

st.sidebar.title("🔐 A8I Boss Authorization")
boss_pass = st.sidebar.text_input("Enter Boss Password", type="password")

if boss_pass != "admin123" and boss_pass != "":
    st.sidebar.error("Invalid password!")

st.title("🚀 A8I — Autonomous AI Agency Command Center")
st.markdown("**Strictly 8 Autonomous Employees** | 100% Free | Local Memory Only")

st.sidebar.markdown("---")
st.sidebar.subheader("👥 Team Composition (8 Agents)")
selected_role = st.sidebar.selectbox("Select employee to inspect:", list(TEAM.keys()))
st.sidebar.info(f"**Role:** {TEAM[selected_role]}")

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview & Tasks",
    "🎯 Outbound & Proposals",
    "💬 PM Direct Chat",
    "📋 System Logs",
])

with tab1:
    st.header("Agency Control Panel")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Employees", "8")
    col2.metric("Active Tasks", len(st.session_state.tasks))
    col3.metric("Budget / Subscriptions", "0.00 (Free)")

    st.markdown("### Assign New Task")
    with st.form("task_form"):
        client_name = st.text_input("Target Client / Partner Name", "Partner Entity A")
        task_desc = st.text_area("Task description for the agency", "Run market analysis and prepare outbound proposal")
        assigned_agent = st.selectbox("Assign Agent", list(TEAM.keys()))
        submitted = st.form_submit_button("Submit Task")

        if submitted:
            new_task = {
                "id": len(st.session_state.tasks) + 1,
                "client": client_name,
                "agent": assigned_agent,
                "offer": task_desc,
                "status": "In Progress",
                "response": "Pending",
                "date": str(datetime.date.today()),
            }
            st.session_state.tasks.append(new_task)
            st.session_state.logs.append(
                f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Task #{new_task['id']} assigned to {assigned_agent}"
            )
            st.success(f"Task successfully delegated to: {assigned_agent}!")

with tab2:
    st.header("Outbound & Proposals Module")
    st.markdown("Displaying all sent proposals and engagement statuses.")

    if st.button("📦 Generate & Send New Proposal"):
        rand_id = random.randint(10, 99)
        sim_client = f"Partner #{rand_id}"
        sim_offer = "Automated outreach bundle (Standard Plan)"
        st.session_state.tasks.append({
            "id": len(st.session_state.tasks) + 1,
            "client": sim_client,
            "agent": "Outbound Marketplace Strategist",
            "offer": sim_offer,
            "status": "Sent",
            "response": "No response yet",
            "date": str(datetime.date.today()),
        })
        st.session_state.logs.append(
            f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Outbound Strategist sent proposal to {sim_client}"
        )
        st.rerun()

    if st.session_state.tasks:
        for t in st.session_state.tasks:
            with st.expander(f"Proposal #{t['id']} | Client: {t['client']} | Status: {t['status']}"):
                st.write(f"**Responsible Agent:** {t['agent']}")
                st.write(f"**Offer Details:** {t['offer']}")
                st.write(f"**Client Reaction:** {t['response']}")
                st.write(f"**Date:** {t['date']}")

                if st.button(f"Simulate response from {t['client']}", key=f"ans_{t['id']}"):
                    t["response"] = "Client replied: 'Looks great, let's proceed with integration!'"
                    t["status"] = "Negotiation"
                    st.session_state.logs.append(
                        f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Incoming response received from {t['client']}!"
                    )
                    st.rerun()
    else:
        st.info("No proposals sent yet.")

with tab3:
    st.header("Direct Chat with Project Manager (Chief of Staff)")
    st.markdown("Consult with the chief coordinator regarding system performance.")

    user_query = st.text_input("Message for PM", "Provide a full operational summary of A8I.")
    if st.button("Send Query to PM"):
        pm_reply = (
            f"PM Report: All 8 agents are fully operational. "
            f"Total managed records: {len(st.session_state.tasks)}. Operating entirely in local memory with zero external costs."
        )
        st.info(pm_reply)
        st.session_state.logs.append(
            f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Boss requested summary from PM."
        )

with tab4:
    st.header("Internal System Logs (Local Memory)")
    st.markdown("Real-time execution log of agent operations.")
    for log_entry in reversed(st.session_state.logs):
        st.text(log_entry)