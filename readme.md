# AgriFlow: Comprehensive Agricultural Management Platform

AgriFlow is a **Streamlit-based web application** designed to streamline agricultural management. It provides role-based access control, allowing **Super Admins**, **Admins**, **Users (Buyers/Workers)**, and **Farmers** to manage their activities efficiently. The platform includes features like crop monitoring, marketplace integration, user management, and data analytics.

---

## Features

### **Super Admin**
- **Dashboard:** Overview of platform performance, total users, and revenue statistics.
- **User Management:** Add, edit, or remove admins and users.
- **Data Analytics:** Generate platform-wide reports (user engagement, crop yield, sales trends).
- **System Settings:** Manage platform configurations and permissions.

### **Admin**
- **Dashboard:** Admin-specific insights (local area data, user activity).
- **Farmer Management:** View, approve, or reject farmer profiles.
- **Crop Monitoring:** Monitor crop health and receive AI-powered predictions.
- **Market Management:** Manage buyer and seller connections.

### **User (Buyers/Workers)**
- **Marketplace:** Browse available crops/products, view market trends, and connect with farmers.
- **Profile Management:** Update personal details and track order history.
- **Support:** Access FAQs and raise support tickets.

### **Farmer**
- **Dashboard:** Overview of personal crop data, income summary, and expenses.
- **Crop Management:** Record crop planting, growth, and harvesting activities.
- **Marketplace Integration:** List crops for sale and manage transactions.
- **Alerts:** Receive weather updates, pest outbreak alerts, and disaster warnings.

---

## Demo Credentials

Use the following dummy credentials to test the platform:

| **Role**       | **Username**   | **Password** |
|----------------|----------------|--------------|
| Super Admin    | `superadmin`   | `super123`   |
| Admin          | `admin`        | `admin123`   |
| User           | `user`         | `user123`    |
| Farmer         | `farmer`       | `farmer123`  |

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Streamlit
- Pandas
- Plotly

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/agriflow.git
   cd agriflow
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Open your browser and navigate to `http://localhost:8501`.

---

## Customization

### Add Custom CSS
You can modify the custom CSS in the `inject_custom_css()` function in `app.py` to match your branding.

### Add More Features
- Integrate a database (e.g., SQLite, PostgreSQL) to store user and crop data.
- Add AI/ML models for crop health predictions and recommendations.
- Deploy the app using Streamlit Sharing, Heroku, or AWS.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or feedback, please contact:

- **Your Name**  
- **Email:** harsh.if56@tpoly.in 
- **GitHub:** [Harsh Tambade](https://github.com/HarshTambade)  

---

Enjoy using AgriFlow! 🌾