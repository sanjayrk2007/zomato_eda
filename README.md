# 🍽️ Zomato Restaurant Analysis Dashboard

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-5.15+-purple.svg)](https://plotly.com)

An interactive data analysis dashboard for Zomato restaurant data, featuring comprehensive EDA (Exploratory Data Analysis) and an interactive Streamlit web application for restaurant insights and analytics.

## 📊 Project Overview

This project analyzes Zomato restaurant data to uncover patterns, trends, and insights about restaurant preferences, ratings, pricing, and customer behavior. The analysis is presented through both a detailed Jupyter notebook and an interactive web dashboard.

### 🎯 Key Objectives
- Analyze restaurant distribution across different categories
- Understand customer preferences and rating patterns
- Explore the relationship between pricing and ratings
- Investigate online ordering trends and their impact on ratings
- Provide interactive tools for data exploration and restaurant discovery

## 🚀 Features

### 📈 Interactive Dashboard
- **Real-time Filtering**: Filter restaurants by type, rating, cost, and availability
- **Dynamic Visualizations**: Interactive charts that update based on user selections
- **Restaurant Search**: Find specific restaurants with detailed information
- **Key Insights**: Automatically generated insights and statistics
- **Responsive Design**: Works seamlessly on desktop and mobile devices

### 📊 Analysis Components
- **Restaurant Type Analysis**: Distribution and popularity of different categories
- **Rating Analysis**: Rating patterns and distribution across restaurants
- **Cost Analysis**: Pricing trends and cost-to-rating relationships
- **Online Ordering Impact**: Comparison of online vs offline order ratings
- **Customer Engagement**: Vote analysis and popular restaurant identification

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib & Seaborn**: Static visualizations
- **Plotly**: Interactive visualizations
- **Jupyter Notebook**: EDA and analysis documentation

## 📁 Project Structure

```
zomato-analysis-dashboard/
├── 📊 Zomato_EDA.ipynb          # Comprehensive EDA notebook
├── 🌐 zomato_dashboard.py       # Interactive Streamlit dashboard
├── 📄 Zomato-data-.csv          # Restaurant dataset
├── 📋 requirements.txt          # Python dependencies
├── 📖 README.md                 # Project documentation
├── 🚫 .gitignore               # Git ignore file

```

## 🎯 Key Findings

Based on the comprehensive analysis of 148 restaurants:

### 🏆 Restaurant Categories
- **Dining restaurants** dominate the dataset, being the most popular category
- **Cafes** and **Buffet** restaurants also have significant presence
- Dining restaurants receive the highest total votes from customers

### ⭐ Rating Patterns
- Most restaurants receive ratings between **3.5 to 4.0**
- **Empire Restaurant** has the highest number of votes (most popular)
- Average rating across all restaurants is approximately **3.8/5**

### 📱 Online Ordering Trends
- **Majority of restaurants** do not accept online orders
- **Offline orders tend to receive lower ratings** compared to online orders
- Online ordering availability varies significantly across restaurant types

### 💰 Pricing Insights
- Cost for two people ranges from **₹300 to ₹800**
- No strong correlation between higher prices and better ratings
- Price distribution shows restaurants across various budget ranges

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/zomato-analysis-dashboard.git
   cd zomato-analysis-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**
   ```bash
   streamlit run zomato_dashboard.py
   ```

4. **Open your browser**
   - Navigate to `http://localhost:8501`
   - Start exploring the interactive dashboard!

### Alternative: Jupyter Notebook
```bash
jupyter notebook Zomato_EDA.ipynb
```

## 📊 Dashboard Features

### 🔍 Interactive Filters
- **Restaurant Type**: Multi-select filter for different categories
- **Rating Range**: Slider to filter by rating (3.0 - 5.0)
- **Cost Range**: Slider to filter by cost for two people
- **Online Ordering**: Filter by online order availability
- **Table Booking**: Filter by table booking availability

### 📈 Visualization Tabs
1. **Restaurant Types**: Distribution charts and vote analysis
2. **Online Orders**: Pie charts for availability analysis
3. **Ratings & Cost**: Histograms and distribution analysis
4. **Detailed Analysis**: Box plots and scatter plots for correlations

### 🔎 Search Functionality
- Search restaurants by name
- View detailed restaurant information
- Expandable cards with metrics and features

## 📈 Data Insights

### Statistical Summary
- **Total Restaurants**: 148
- **Average Rating**: 3.8/5
- **Average Cost for Two**: ₹600
- **Total Votes**: 45,000+
- **Restaurant Types**: 4 main categories

### Business Insights
- **Customer Preference**: Dining restaurants are most preferred
- **Digital Adoption**: Limited online ordering adoption
- **Quality Perception**: Ratings are generally positive (3.5-4.0 range)
- **Market Opportunity**: Potential for improving online ordering services

## 🎨 Screenshots

*[Add screenshots of your dashboard here]*

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 🙏 Acknowledgments

- Zomato for providing the dataset
- Streamlit team for the amazing web framework
- Plotly for interactive visualization capabilities
- The open-source community for various Python libraries

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Plotly Documentation](https://plotly.com/python/)
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)

## 🔮 Future Enhancements

- [ ] Add geographic analysis if location data is available
- [ ] Implement restaurant recommendation system
- [ ] Add more advanced statistical analysis
- [ ] Create restaurant comparison tool
- [ ] Add export functionality for filtered data
- [ ] Implement user authentication and saved preferences
- [ ] Add more interactive visualizations
- [ ] Create mobile app version

---

⭐ **Star this repository if you found it helpful!**

📧 **Feel free to reach out for any questions or suggestions!**

