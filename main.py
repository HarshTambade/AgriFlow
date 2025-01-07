import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Custom CSS for modern UI
def inject_custom_css():
    st.markdown(
        """
        <style>
        /* Main title */
        h1 {
            color: #2E86C1;
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 20px;
        }

        /* Sidebar */
        .css-1d391kg {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Buttons */
        .stButton button {
            background-color: #28B463;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 1rem;
            border: none;
            transition: background-color 0.3s;
        }

        .stButton button:hover {
            background-color: #239B56;
        }

        /* Dataframes */
        .stDataFrame {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Expanders */
        .stExpander {
            background-color: #F4F6F6;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }

        /* Plotly charts */
        .plotly-graph-div {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Notifications */
        .stAlert {
            border-radius: 10px;
            padding: 15px;
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 30px;
            color: #7F8C8D;
            font-size: 0.9rem;
        }

        /* Purchase Cards */
        .card {
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color: #fff;
        }
        .card h3 {
            color: #2E86C1;
            margin-top: 0;
        }
        .card p {
            margin: 5px 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Page configuration
st.set_page_config(page_title="AgriFlow", page_icon="🌾", layout="wide")

# Inject custom CSS
inject_custom_css()

# Sample data for demonstration
def load_crop_data():
    return pd.DataFrame({
        "Crop": ["Wheat", "Rice", "Corn"],
        "Yield (tons)": [10, 15, 20],
        "Soil Health": ["Good", "Average", "Excellent"],
        "Region": ["North", "South", "East"],
        "Date": [datetime.now() - timedelta(days=2), datetime.now() - timedelta(days=1), datetime.now()],
    })

def load_market_data():
    return pd.DataFrame({
        "Product ID": [1, 2, 3],
        "Crop": ["Wheat", "Rice", "Corn"],
        "Price ($)": [200, 300, 250],
        "Quantity Available (tons)": [50, 30, 40],
        "Seller": ["Farmer A", "Farmer B", "Farmer C"],
    })

def load_user_data():
    return pd.DataFrame({
        "User ID": [1, 2, 3],
        "Name": ["John Doe", "Jane Smith", "Alice Johnson"],
        "Role": ["Admin", "Farmer", "User"],
        "Status": ["Active", "Pending", "Active"],
    })

# Dummy credentials for testing
DUMMY_CREDENTIALS = {
    "superadmin": {"password": "super123", "role": "Super Admin"},
    "admin": {"password": "admin123", "role": "Admin"},
    "user": {"password": "user123", "role": "User"},
    "farmer": {"password": "farmer123", "role": "Farmer"},
}

def authenticate_user(username, password):
    if username in DUMMY_CREDENTIALS and DUMMY_CREDENTIALS[username]["password"] == password:
        return DUMMY_CREDENTIALS[username]["role"]
    return None

# Initialize session state for profile, tickets, and market data
if "profile" not in st.session_state:
    st.session_state["profile"] = {
        "name": "",
        "email": "",
        "phone": "",
        "address": "",
    }

if "tickets" not in st.session_state:
    st.session_state["tickets"] = []

if "market_data" not in st.session_state:
    st.session_state["market_data"] = load_market_data()

if "alerts" not in st.session_state:
    st.session_state["alerts"] = []

# Main app
def main():
    st.title("AgriFlow: Comprehensive Agricultural Management Platform")
    st.sidebar.title("Login")

    # Login form
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        role = authenticate_user(username, password)
        if role:
            st.session_state["role"] = role
            st.session_state["username"] = username
            st.success(f"Logged in as {role}")
        else:
            st.error("Invalid credentials")

    # Redirect to role-specific dashboards
    if "role" in st.session_state:
        if st.session_state["role"] == "Super Admin":
            super_admin_dashboard()
        elif st.session_state["role"] == "Admin":
            admin_dashboard()
        elif st.session_state["role"] == "User":
            user_dashboard()
        elif st.session_state["role"] == "Farmer":
            farmer_dashboard()

    # Footer
    st.markdown('<div class="footer">© 2023 AgriFlow. All rights reserved.</div>', unsafe_allow_html=True)

# Super Admin Dashboard
def super_admin_dashboard():
    st.title("Super Admin Dashboard")

    # Sidebar navigation
    st.sidebar.header("Navigation")
    tab = st.sidebar.radio("Go to", ["Dashboard", "User Management", "Data Analytics", "System Settings", "Support"])

    if tab == "Dashboard":
        st.header("Platform Performance")
        st.write("Total Users: 1000")
        st.write("Revenue: $1,000,000")

        # Notifications
        st.subheader("System Notifications")
        st.write("1. New user registered: Farmer Z")
        st.write("2. Revenue increased by 10% this month.")

    elif tab == "User Management":
        st.header("User Management")
        user_data = load_user_data()
        st.write("User Data:")
        st.write(user_data)

        # Add/Edit User
        with st.expander("Add/Edit User"):
            user_id = st.number_input("User ID", min_value=1)
            name = st.text_input("Name")
            user_role = st.selectbox("Role", ["Admin", "Farmer", "User"])
            status = st.selectbox("Status", ["Active", "Pending"])
            if st.button("Save User"):
                st.success(f"User {name} saved successfully!")

    elif tab == "Data Analytics":
        st.header("Data Analytics")
        crop_data = load_crop_data()
        st.write("Crop Data:")
        st.write(crop_data)

        # Visualize crop yield
        fig = px.bar(crop_data, x="Crop", y="Yield (tons)", title="Crop Yield (tons)", color="Crop")
        st.plotly_chart(fig)

    elif tab == "System Settings":
        st.header("System Settings")
        st.write("Manage platform configurations and permissions.")

    elif tab == "Support":
        st.header("Support")
        st.write("Manage support tickets and user feedback.")

# Admin Dashboard
def admin_dashboard():
    st.title("Admin Dashboard")

    # Sidebar navigation
    st.sidebar.header("Navigation")
    tab = st.sidebar.radio("Go to", ["Dashboard", "Farmer Management", "Crop Monitoring", "Market Management", "Alerts"])

    if tab == "Dashboard":
        st.header("Admin Insights")
        st.write("Local Area Data:")
        st.write("User Activity: High")

    elif tab == "Farmer Management":
        st.header("Farmer Management")
        user_data = load_user_data()
        farmers = user_data[user_data["Role"] == "Farmer"]
        st.write("Registered Farmers:")
        st.write(farmers)

        # Approve/Reject Farmers
        with st.expander("Approve/Reject Farmers"):
            farmer_id = st.number_input("Farmer ID", min_value=1)
            action = st.selectbox("Action", ["Approve", "Reject"])
            if st.button("Submit"):
                st.success(f"Farmer {farmer_id} {action.lower()}ed.")

    elif tab == "Crop Monitoring":
        st.header("Crop Monitoring")
        crop_data = load_crop_data()

        # Filters
        st.subheader("Filters")
        region_filter = st.selectbox("Select Region", ["All"] + list(crop_data["Region"].unique()))
        crop_filter = st.selectbox("Select Crop", ["All"] + list(crop_data["Crop"].unique()))

        # Apply filters
        filtered_data = crop_data
        if region_filter != "All":
            filtered_data = filtered_data[filtered_data["Region"] == region_filter]
        if crop_filter != "All":
            filtered_data = filtered_data[filtered_data["Crop"] == crop_filter]

        st.write("Filtered Crop Data:")
        st.write(filtered_data)

        # Visualize crop yield
        fig1 = px.bar(filtered_data, x="Crop", y="Yield (tons)", title="Crop Yield (tons)", color="Crop")
        st.plotly_chart(fig1)

        # Visualize soil health
        fig2 = px.pie(filtered_data, names="Soil Health", title="Soil Health Distribution", color="Soil Health")
        st.plotly_chart(fig2)

    elif tab == "Market Management":
        st.header("Market Management")
        market_data = st.session_state["market_data"]

        # Add/Edit/Delete Products
        with st.expander("Add/Edit/Delete Products"):
            product_id = st.number_input("Product ID", min_value=1)
            crop = st.text_input("Crop")
            price = st.number_input("Price ($)", min_value=1)
            quantity = st.number_input("Quantity Available (tons)", min_value=1)
            seller = st.text_input("Seller")

            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("Add Product"):
                    new_product = {
                        "Product ID": product_id,
                        "Crop": crop,
                        "Price ($)": price,
                        "Quantity Available (tons)": quantity,
                        "Seller": seller,
                    }
                    st.session_state["market_data"] = st.session_state["market_data"].append(new_product, ignore_index=True)
                    st.success("Product added successfully!")
            with col2:
                if st.button("Update Product"):
                    st.session_state["market_data"].loc[st.session_state["market_data"]["Product ID"] == product_id, ["Crop", "Price ($)", "Quantity Available (tons)", "Seller"]] = [crop, price, quantity, seller]
                    st.success("Product updated successfully!")
            with col3:
                if st.button("Delete Product"):
                    st.session_state["market_data"] = st.session_state["market_data"][st.session_state["market_data"]["Product ID"] != product_id]
                    st.success("Product deleted successfully!")

        st.write("Marketplace Listings:")
        st.write(st.session_state["market_data"])

    elif tab == "Alerts":
        st.header("Alerts")

        # Send Alerts
        with st.expander("Send Alerts"):
            alert_message = st.text_area("Alert Message")
            if st.button("Send Alert"):
                st.session_state["alerts"].append({
                    "message": alert_message,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                })
                st.success("Alert sent successfully!")

        # View Alerts
        st.subheader("Recent Alerts")
        if st.session_state["alerts"]:
            for alert in st.session_state["alerts"]:
                st.write(f"**{alert['timestamp']}**: {alert['message']}")
        else:
            st.write("No alerts found.")

# User Dashboard
def user_dashboard():
    st.title("User Dashboard")

    # Sidebar navigation
    st.sidebar.header("Navigation")
    tab = st.sidebar.radio("Go to", ["Marketplace", "Profile Management", "Support"])

    if tab == "Marketplace":
        st.header("Marketplace")
        market_data = st.session_state["market_data"]

        # Display purchase cards
        for index, row in market_data.iterrows():
            with st.container():
                st.markdown(
                    f"""
                    <div class="card">
                        <h3>{row['Crop']}</h3>
                        <p><strong>Price:</strong> ${row['Price ($)']} per ton</p>
                        <p><strong>Seller:</strong> {row['Seller']}</p>
                        <p><strong>Quantity Available:</strong> {row['Quantity Available (tons)']} tons</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                # Buy button
                quantity = st.number_input(f"Quantity (tons) for {row['Crop']}", min_value=1, max_value=row['Quantity Available (tons)'], key=f"qty_{index}")
                if st.button(f"Buy {row['Crop']}", key=f"buy_{index}"):
                    st.success(f"You have purchased {quantity} tons of {row['Crop']} for ${quantity * row['Price ($)']}.")

    elif tab == "Profile Management":
        st.header("Profile Management")

        # Profile form
        with st.form("Profile Form"):
            st.write("Update your profile details:")
            name = st.text_input("Name", value=st.session_state["profile"]["name"])
            email = st.text_input("Email", value=st.session_state["profile"]["email"])
            phone = st.text_input("Phone", value=st.session_state["profile"]["phone"])
            address = st.text_input("Address", value=st.session_state["profile"]["address"])

            if st.form_submit_button("Save Profile"):
                st.session_state["profile"] = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "address": address,
                }
                st.success("Profile updated successfully!")

    elif tab == "Support":
        st.header("Support")

        # Support ticketing panel
        with st.expander("Raise a Support Ticket"):
            ticket_title = st.text_input("Title")
            ticket_description = st.text_area("Description")
            if st.button("Submit Ticket"):
                ticket_id = len(st.session_state["tickets"]) + 1
                st.session_state["tickets"].append({
                    "id": ticket_id,
                    "title": ticket_title,
                    "description": ticket_description,
                    "status": "Open",
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                })
                st.success(f"Ticket #{ticket_id} submitted successfully!")

        # View tickets
        st.subheader("Your Support Tickets")
        if st.session_state["tickets"]:
            for ticket in st.session_state["tickets"]:
                st.write(f"**Ticket #{ticket['id']}**: {ticket['title']}")
                st.write(f"**Status**: {ticket['status']}")
                st.write(f"**Date**: {ticket['date']}")
                st.write(f"**Description**: {ticket['description']}")
                st.write("---")
        else:
            st.write("No tickets found.")

# Farmer Dashboard
def farmer_dashboard():
    st.title("Farmer Dashboard")

    # Sidebar navigation
    st.sidebar.header("Navigation")
    tab = st.sidebar.radio("Go to", ["Dashboard", "Crop Management", "Marketplace", "Alerts", "Training"])

    if tab == "Dashboard":
        st.header("Crop Overview")
        crop_data = load_crop_data()
        st.write("Your Crop Data:")
        st.write(crop_data)

        # Visualize crop yield
        fig = px.bar(crop_data, x="Crop", y="Yield (tons)", title="Your Crop Yield (tons)", color="Crop")
        st.plotly_chart(fig)

    elif tab == "Crop Management":
        st.header("Crop Management")
        st.write("Record and monitor your crops here.")

    elif tab == "Marketplace":
        st.header("Marketplace")
        st.write("List your crops for sale and manage transactions.")

        # Sample form to list crops
        with st.form("List Crop"):
            crop_name = st.text_input("Crop Name")
            quantity = st.number_input("Quantity (tons)", min_value=1)
            price = st.number_input("Price ($)", min_value=1)
            if st.form_submit_button("List Crop"):
                st.success(f"Listed {quantity} tons of {crop_name} at ${price}/ton")

    elif tab == "Alerts":
        st.header("Alerts")
        st.write("Weather Updates: Sunny")
        st.write("Pest Outbreak Alerts: None")

    elif tab == "Training":
        st.header("Training and Support")
        st.write("Access tutorials on modern farming techniques.")
        st.write("Join farmer communities for shared knowledge.")

# Run the app
if __name__ == "__main__":
    main()