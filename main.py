import streamlit as st
import pandas as pd
import plotly.express as px

# Custom CSS for better UI
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
            background-color: #F4F6F6;
            padding: 20px;
            border-radius: 10px;
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
    })

def load_market_data():
    return pd.DataFrame({
        "Crop": ["Wheat", "Rice", "Corn"],
        "Price ($)": [200, 300, 250],
        "Demand": ["High", "Medium", "Low"],
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

    # Platform Performance
    st.header("Platform Performance")
    st.write("Total Users: 1000")
    st.write("Revenue: $1,000,000")

    # User Management
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

    # Data Analytics
    st.header("Data Analytics")
    crop_data = load_crop_data()
    st.write("Crop Data:")
    st.write(crop_data)

    # Visualize crop yield
    fig = px.bar(crop_data, x="Crop", y="Yield (tons)", title="Crop Yield (tons)")
    st.plotly_chart(fig)

    # System Settings
    st.header("System Settings")
    st.write("Manage platform configurations and permissions.")

# Admin Dashboard
def admin_dashboard():
    st.title("Admin Dashboard")

    # Farmer Management
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

    # Crop Monitoring
    st.header("Crop Monitoring")
    crop_data = load_crop_data()
    st.write("Crop Health Data:")
    st.write(crop_data)

    # Visualize soil health
    fig = px.pie(crop_data, names="Crop", values="Yield (tons)", title="Crop Distribution")
    st.plotly_chart(fig)

    # Market Management
    st.header("Market Management")
    market_data = load_market_data()
    st.write("Marketplace Listings:")
    st.write(market_data)

# User Dashboard
def user_dashboard():
    st.title("User Dashboard")

    # Marketplace
    st.header("Marketplace")
    market_data = load_market_data()
    st.write("Available Crops:")
    st.write(market_data)

    # Visualize market demand
    fig = px.bar(market_data, x="Crop", y="Price ($)", color="Demand", title="Crop Prices and Demand")
    st.plotly_chart(fig)

    # Profile Management
    st.header("Profile Management")
    st.write("Update your personal details and track orders.")

# Farmer Dashboard
def farmer_dashboard():
    st.title("Farmer Dashboard")

    # Crop Management
    st.header("Crop Management")
    crop_data = load_crop_data()
    st.write("Your Crop Data:")
    st.write(crop_data)

    # Visualize crop yield
    fig = px.bar(crop_data, x="Crop", y="Yield (tons)", title="Your Crop Yield (tons)")
    st.plotly_chart(fig)

    # Marketplace Integration
    st.header("Marketplace")
    st.write("List your crops for sale and manage transactions.")

    # Sample form to list crops
    with st.form("List Crop"):
        crop_name = st.text_input("Crop Name")
        quantity = st.number_input("Quantity (tons)", min_value=1)
        price = st.number_input("Price ($)", min_value=1)
        if st.form_submit_button("List Crop"):
            st.success(f"Listed {quantity} tons of {crop_name} at ${price}/ton")

# Run the app
if __name__ == "__main__":
    main()