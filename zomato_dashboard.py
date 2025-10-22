import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(
    page_title="Zomato Restaurant Analysis Dashboard",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #FF6B6B;
        margin: 0.5rem 0;
    }
    .insight-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and preprocess the Zomato dataset"""
    df = pd.read_csv('Zomato-data-.csv')
    
    # Data cleaning - handle rate column
    def handle_rate(value):
        value = str(value).split('/')
        value = value[0]
        return float(value)
    
    df['rate'] = df['rate'].apply(handle_rate)
    
    return df

def main():
    # Header
    st.markdown('<h1 class="main-header">🍽️ Zomato Restaurant Analysis Dashboard</h1>', unsafe_allow_html=True)
    
    # Load data
    df = load_data()
    
    # Sidebar filters
    st.sidebar.header("🔍 Filters")
    
    # Restaurant type filter
    restaurant_types = df['listed_in(type)'].unique()
    selected_types = st.sidebar.multiselect(
        "Select Restaurant Types",
        restaurant_types,
        default=restaurant_types
    )
    
    # Online order filter
    online_order_filter = st.sidebar.selectbox(
        "Online Order",
        ["All", "Yes", "No"]
    )
    
    # Table booking filter
    table_booking_filter = st.sidebar.selectbox(
        "Table Booking",
        ["All", "Yes", "No"]
    )
    
    # Rating range filter
    min_rating, max_rating = st.sidebar.slider(
        "Rating Range",
        min_value=float(df['rate'].min()),
        max_value=float(df['rate'].max()),
        value=(float(df['rate'].min()), float(df['rate'].max())),
        step=0.1
    )
    
    # Cost range filter
    min_cost, max_cost = st.sidebar.slider(
        "Cost for Two People (₹)",
        min_value=int(df['approx_cost(for two people)'].min()),
        max_value=int(df['approx_cost(for two people)'].max()),
        value=(int(df['approx_cost(for two people)'].min()), int(df['approx_cost(for two people)'].max()))
    )
    
    # Apply filters
    filtered_df = df[
        (df['listed_in(type)'].isin(selected_types)) &
        (df['rate'] >= min_rating) &
        (df['rate'] <= max_rating) &
        (df['approx_cost(for two people)'] >= min_cost) &
        (df['approx_cost(for two people)'] <= max_cost)
    ]
    
    if online_order_filter != "All":
        filtered_df = filtered_df[filtered_df['online_order'] == online_order_filter]
    
    if table_booking_filter != "All":
        filtered_df = filtered_df[filtered_df['book_table'] == table_booking_filter]
    
    # Main content
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Restaurants", len(filtered_df))
    
    with col2:
        avg_rating = filtered_df['rate'].mean()
        st.metric("Average Rating", f"{avg_rating:.2f}")
    
    with col3:
        avg_cost = filtered_df['approx_cost(for two people)'].mean()
        st.metric("Avg Cost for Two", f"₹{avg_cost:.0f}")
    
    with col4:
        total_votes = filtered_df['votes'].sum()
        st.metric("Total Votes", f"{total_votes:,}")
    
    # Key Insights
    st.markdown("### 📊 Key Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Most popular restaurant type
        type_counts = filtered_df['listed_in(type)'].value_counts()
        most_popular_type = type_counts.index[0]
        st.markdown(f"""
        <div class="insight-box">
            <h4>🏆 Most Popular Restaurant Type</h4>
            <p><strong>{most_popular_type}</strong> with {type_counts.iloc[0]} restaurants</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Restaurant with highest votes
        if not filtered_df.empty:
            max_votes_idx = filtered_df['votes'].idxmax()
            top_restaurant = filtered_df.loc[max_votes_idx, 'name']
            top_votes = filtered_df.loc[max_votes_idx, 'votes']
            st.markdown(f"""
            <div class="insight-box">
                <h4>⭐ Most Voted Restaurant</h4>
                <p><strong>{top_restaurant}</strong> with {top_votes:,} votes</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Visualizations
    st.markdown("### 📈 Visualizations")
    
    # Create tabs for different analysis
    tab1, tab2, tab3, tab4 = st.tabs(["Restaurant Types", "Online Orders", "Ratings & Cost", "Detailed Analysis"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            # Restaurant type distribution
            fig1 = px.bar(
                x=filtered_df['listed_in(type)'].value_counts().index,
                y=filtered_df['listed_in(type)'].value_counts().values,
                title="Restaurant Types Distribution",
                labels={'x': 'Restaurant Type', 'y': 'Number of Restaurants'},
                color=filtered_df['listed_in(type)'].value_counts().values,
                color_continuous_scale='viridis'
            )
            fig1.update_layout(showlegend=False)
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            # Votes by restaurant type
            votes_by_type = filtered_df.groupby('listed_in(type)')['votes'].sum().reset_index()
            fig2 = px.line(
                votes_by_type,
                x='listed_in(type)',
                y='votes',
                title="Total Votes by Restaurant Type",
                markers=True
            )
            fig2.update_traces(line_color='#FF6B6B', marker_color='#FF6B6B')
            st.plotly_chart(fig2, use_container_width=True)
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            # Online order distribution
            online_counts = filtered_df['online_order'].value_counts()
            fig3 = px.pie(
                values=online_counts.values,
                names=online_counts.index,
                title="Online Order Availability",
                color_discrete_sequence=['#FF6B6B', '#4ECDC4']
            )
            st.plotly_chart(fig3, use_container_width=True)
        
        with col2:
            # Table booking distribution
            table_counts = filtered_df['book_table'].value_counts()
            fig4 = px.pie(
                values=table_counts.values,
                names=table_counts.index,
                title="Table Booking Availability",
                color_discrete_sequence=['#45B7D1', '#96CEB4']
            )
            st.plotly_chart(fig4, use_container_width=True)
    
    with tab3:
        col1, col2 = st.columns(2)
        
        with col1:
            # Rating distribution
            fig5 = px.histogram(
                filtered_df,
                x='rate',
                nbins=10,
                title="Rating Distribution",
                labels={'rate': 'Rating', 'count': 'Number of Restaurants'},
                color_discrete_sequence=['#FF6B6B']
            )
            st.plotly_chart(fig5, use_container_width=True)
        
        with col2:
            # Cost distribution
            fig6 = px.histogram(
                filtered_df,
                x='approx_cost(for two people)',
                nbins=15,
                title="Cost Distribution (for two people)",
                labels={'approx_cost(for two people)': 'Cost (₹)', 'count': 'Number of Restaurants'},
                color_discrete_sequence=['#4ECDC4']
            )
            st.plotly_chart(fig6, use_container_width=True)
    
    with tab4:
        col1, col2 = st.columns(2)
        
        with col1:
            # Rating vs Online Order
            fig7 = px.box(
                filtered_df,
                x='online_order',
                y='rate',
                title="Rating Distribution by Online Order Availability",
                color='online_order',
                color_discrete_sequence=['#FF6B6B', '#4ECDC4']
            )
            st.plotly_chart(fig7, use_container_width=True)
        
        with col2:
            # Cost vs Rating scatter plot
            fig8 = px.scatter(
                filtered_df,
                x='rate',
                y='approx_cost(for two people)',
                size='votes',
                color='listed_in(type)',
                title="Cost vs Rating (Size = Votes)",
                labels={'rate': 'Rating', 'approx_cost(for two people)': 'Cost (₹)'}
            )
            st.plotly_chart(fig8, use_container_width=True)
    
    # Restaurant Search and Details
    st.markdown("### 🔍 Restaurant Search")
    
    search_term = st.text_input("Search for a restaurant:", placeholder="Enter restaurant name...")
    
    if search_term:
        search_results = filtered_df[filtered_df['name'].str.contains(search_term, case=False, na=False)]
        
        if not search_results.empty:
            st.markdown(f"Found {len(search_results)} restaurant(s) matching '{search_term}'")
            
            for idx, row in search_results.iterrows():
                with st.expander(f"🍽️ {row['name']}"):
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Rating", f"{row['rate']}/5")
                        st.metric("Votes", f"{row['votes']:,}")
                    
                    with col2:
                        st.metric("Cost for Two", f"₹{row['approx_cost(for two people)']}")
                        st.metric("Type", row['listed_in(type)'])
                    
                    with col3:
                        online_status = "✅ Yes" if row['online_order'] == 'Yes' else "❌ No"
                        table_status = "✅ Yes" if row['book_table'] == 'Yes' else "❌ No"
                        st.write(f"**Online Order:** {online_status}")
                        st.write(f"**Table Booking:** {table_status}")
        else:
            st.warning(f"No restaurants found matching '{search_term}'")
    
    # Summary Statistics
    st.markdown("### 📋 Summary Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Numerical Summary")
        numeric_cols = ['rate', 'votes', 'approx_cost(for two people)']
        summary_stats = filtered_df[numeric_cols].describe()
        st.dataframe(summary_stats, use_container_width=True)
    
    with col2:
        st.markdown("#### Categorical Summary")
        categorical_summary = {
            'Restaurant Types': filtered_df['listed_in(type)'].value_counts().to_dict(),
            'Online Order': filtered_df['online_order'].value_counts().to_dict(),
            'Table Booking': filtered_df['book_table'].value_counts().to_dict()
        }
        
        for category, counts in categorical_summary.items():
            st.write(f"**{category}:**")
            for key, value in counts.items():
                st.write(f"  - {key}: {value}")
            st.write("")
    
    # Footer
    st.markdown("---")
    st.markdown("### 💡 Key Findings from Analysis")
    
    insights = [
        "🍽️ **Dining restaurants** dominate the dataset, being the most popular category",
        "📱 **Majority of restaurants** do not accept online orders",
        "⭐ **Most restaurants** receive ratings between 3.5 to 4.0",
        "🏆 **Empire Restaurant** has the highest number of votes",
        "📊 **Offline orders** tend to receive lower ratings compared to online orders",
        "💰 **Cost distribution** shows restaurants across various price ranges"
    ]
    
    for insight in insights:
        st.markdown(insight)

if __name__ == "__main__":
    main()
