import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Crop production dashboard",layout="wide",initial_sidebar_state="expanded")
st.markdown("""
<style>
/* Entire Sidebar */
section[data-testid="stSidebar"]{
    background-color:#8B0000 !important;
    min-width:340px !important;
    max-width:340px !important;
    border-right:3px solid #C62828;
}

/* Sidebar inner background */
section[data-testid="stSidebar"] > div{
    background-color:#8B0000 !important;
}

/* Sidebar width */
section[data-testid="stSidebar"]{
    min-width:340px !important;
    max-width:340px !important;
}

/* Left align menu items */
.nav-link{
    justify-content:flex-start !important;
    text-align:left !important;
    display:flex !important;
    align-items:center !important;
    gap:10px !important;
}
[data-testid="stMetric"]{
    background: linear-gradient(135deg,#C62828,#8B0000) !important;
    border:2px solid #EF9A9A !important;
    border-radius:18px !important;
    padding:20px !important;
    box-shadow:0 6px 18px rgba(0,0,0,0.25);
}

[data-testid="stMetricLabel"]{
    color:white !important;
    font-weight:bold !important;
    font-size:16px !important;
}

[data-testid="stMetricValue"]{
    color:white !important;
    font-size:30px !important;
    font-weight:700 !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
section[data-testid="stSidebar"] label {
    color: white !important;
    font-size: 24px !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)
with st.sidebar:
    st.markdown(
    "<h2 style='color:white; font-size:30px; font-weight:bold;text-align:center;'>Agri-Vision Analysis Dashboard🌾</h2>",
    unsafe_allow_html=True
     )
    opt = option_menu(
        None,
        ["📜Overview",
         "📅Dataset",
         "🧹Data cleaning",
         "📊Data visualization",
         "🗺Hotspots",
         "💡Insights",
         "📩Export"],

         styles={

            # Menu Container
            "container": {
                "padding": "12px",
                "background-color": "#8B0000",
                "border-radius": "20px",
            },

            # Icons
            "icon": {
                "color": "white",
                "font-size": "20px",
            },

            # Menu Items
            "nav-link": {
                "color": "white",
                "font-size": "20px",
                "font-weight": "700",
                "text-align": "left",
                "margin": "8px 5px",
                "padding": "12px",
                "border-radius": "12px",
                "background-color": "#8B0000",
                "--hover-color": "#EF9A9A"
            },

            # Selected Menu
            "nav-link-selected": {
                "background-color": "#C62828",
                "color": "white",
                "font-weight": "700",
                "border-radius": "12px",
            },
        },

        key="sidebar_menu"
    )
    st.markdown("""
    <style>
    ul.nav.nav-pills li a{
    color:white !important;
    }

    ul.nav.nav-pills li a span{
    color:white !important;
    }
    </style>
    """, unsafe_allow_html=True)    
if opt=="📜Overview":
    st.title("Agri-Vision Analysis🌾")
    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go
    import streamlit as st
# Read dataset
    df = pd.read_csv("crop_production.csv")
    st.subheader("📍District Wise Overview")
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
       st.metric("Total records",len(df))
    with col2:
      st.metric("Total crops",df["Crop"].nunique())
    with col3:
      st.metric("Maximum Production","1.25B")
    with col4:
      st.metric("Total Columns",len(df.columns))  
    with col5:
      st.metric("Total Districts",df["District_Name"].nunique())
    df1=pd.read_csv("crop_yield.csv")
    st.subheader("🌍Region wise Overview")
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
      st.metric("Total Records",len(df1))
    with col2:
      st.metric("Total Crops",df1["Crop"].nunique())
    with col3:
      st.metric("Maximum Production",df1["Yield_tons_per_hectare"].max())
    with col4:
        st.metric("Total Columns",len(df1.columns))
    with col5:
      st.metric("Total Regions",df1["Region"].nunique())
    st.markdown("""
     <style>
     .card{
     background:#FFEBEE;
     border-radius:15px;
     padding:18px;
     text-align:center;
     box-shadow:0 0 8px
     rgba(239,83,80,0.35), 0 0 18px
     rgba(239,83,80,0.25), 0 0 30px
     rgba(239,83,80,0.15),
        
     border:2px solid #E8EAF6;
     height:280px;
     }
     .card h3{
     color:#2E7D32;
     }
     .card p{
     color:#555;
     font-size:17px;
     line-height:1.2;
     }
     </style>
     """, unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
         st.markdown("""
         <div class="card">
         <h3>🌾 Seasons</h3>
         <p>🌱 Kharif</p>
         <p>🌾 Rabi</p>
         <p>☀️ Summer</p>
         <p>🍂 Autumn</p>
         <p>📅 Whole Year</p>
         </div>
         """, unsafe_allow_html=True)
    with col2:
         st.markdown("""
         <div class="card">
         <h3>🌽 Crops</h3>
         <p>🌾 Rice</p>
         <p>🌿 Wheat</p>
         <p>🧵 Cotton</p>
         <p>🌱 Soyabean</p>
         <p>🌾 Barley</p>
         </div>
         """, unsafe_allow_html=True)
    with col3:
         st.markdown("""
         <div class="card">
         <h3>🪴 Soil Types</h3>
         <p>🏖️ Sandy</p>
         <p>🟤 Clay</p>
         <p>🌱 Loamy</p>
         <p>💧 Silt</p>
         <p>🌿 Peaty</p>
         </div>
         """, unsafe_allow_html=True)
    with col4:
         st.markdown("""
         <div class="card">
         <h3>🌦️ Weather</h3>
         <p>☀️ Sunny</p>
         <p>☁️ Cloudy</p>
         <p>🌧️ Rainy</p>
         </div>
         """, unsafe_allow_html=True)
# Top 5 districts by total production
    top5 = (
    df.groupby("District_Name", as_index=False)["Production"]
    .sum()
    .sort_values("Production", ascending=False)
    .head(5)
    .sort_values("Production"))
    fig = go.Figure()
    for _, row in top5.iterrows():
     fig.add_shape(
        type="line",
        x0=0,
        y0=row["District_Name"],
        x1=row["Production"],
        y1=row["District_Name"],
        line=dict(color="lightgray", width=4))
    # Lollipop heads
    fig.add_trace(
    go.Scatter(
        x=top5["Production"],
        y=top5["District_Name"],
        mode="markers+text",
        text=[f"{x:,.0f}" for x in top5["Production"]],
        textposition="middle right",
        marker=dict(
            size=24,
            color=top5["Production"],
            colorscale="Turbo",
            line=dict(color="white", width=2),
            showscale=True,
            colorbar=dict(title="Production")
        ),
        hovertemplate="<b>District:</b> %{y}<br><b>Production:</b> %{x:,.0f}<extra></extra>"
    )
    )
    fig.update_layout(
    title=dict(
       text="🏆 Top 5 Districts by Production",
        font=dict(size=26),
        x=0.0,xanchor="left"
    ),
    plot_bgcolor="#FFFDE7",
    paper_bgcolor="#FFF8E1",
    template="plotly_white",   # Change to "plotly_white" if needed
    height=550,
    hovermode="closest",
    font=dict(size=20),
    xaxis=dict(title="Production",title_font=dict(size=26),tickfont=dict(size=20),showgrid=True,gridcolor="gray"),
    yaxis=dict(title="District",title_font=dict(size=26),tickfont=dict(size=20),showgrid=False),
    margin=dict(l=20, r=20, t=60, b=20))
    st.plotly_chart(fig, use_container_width=True)
    import streamlit as st
    import pandas as pd
    import plotly.express as px
   # Read dataset
    df2 = pd.read_csv("crop_yield.csv")
# Convert Production to numeric
    df2["Yield_tons_per_hectare"] = pd.to_numeric(df2["Yield_tons_per_hectare"], errors="coerce")
# Sum production for each Region and Crop
    region_crop = (
     df2.groupby(["Region", "Crop"], as_index=False)["Yield_tons_per_hectare"]
     .sum()
    )
# Select the crop with highest production in each region
    top_crop = region_crop.loc[
     region_crop.groupby("Region")["Yield_tons_per_hectare"].idxmax()
   ]
# Sort
    top_crop = top_crop.sort_values(by="Yield_tons_per_hectare", ascending=False)
# Plot
    fig = px.bar(
    top_crop,
    x="Region",
    y="Yield_tons_per_hectare",
    color="Crop",
    text="Crop",
    title="Highest Producing Crop in Each Region",
    hover_data=["Crop", "Yield_tons_per_hectare"]
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(
    title_x=0.02,
    title_font_size=28,
    xaxis_title="Region",
    yaxis_title="Production",
    template="plotly_white",
    plot_bgcolor="#FFFDE7",
    paper_bgcolor="#FFF8E1",
    xaxis=dict(title_font=dict(size=23),
    tickfont=dict(size=18)),
    yaxis=dict(title_font=dict(size=23),
    tickfont=dict(size=18))
   )
    st.plotly_chart(fig, use_container_width=True)
    import streamlit as st
    st.markdown("""
    <style>
    div[data-testid="stHeading"] h3{
    font-size:32px !important;
    font-weight:800 !important;
    color:#000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.subheader("✨ Key Features")
    col1, col2 = st.columns(2)
    with col1:
     st.markdown("""
     <div style="background-color:#E8F5E9; padding:15px; border-radius:10px;">
        <h4>📊 Interactive Visualizations</h4>
        <p>Explore crop production trends using dynamic charts and graphs.</p>
     </div>
     """, unsafe_allow_html=True)

     st.markdown("<br>", unsafe_allow_html=True)

     st.markdown("""
     <div style="background-color:#E3F2FD; padding:15px; border-radius:10px;">
        <h4>🌾 Crop Analysis</h4>
        <p>Compare production and cultivated area across different crops.</p>
     </div>
     """, unsafe_allow_html=True)

     st.markdown("<br>", unsafe_allow_html=True)

     st.markdown("""
     <div style="background-color:#FFF9C4; padding:15px; border-radius:10px;">
        <h4>📅 Seasonal Insights</h4>
        <p>Analyze crop cultivation patterns across different seasons.</p>
     </div>
     """, unsafe_allow_html=True)
    with col2:
      st.markdown("""
     <div style="background-color:#F3E5F5; padding:15px; border-radius:10px;">
        <h4>🗺️ Regional Analysis</h4>
        <p>Study production trends across states and districts.</p>
     </div>
     """, unsafe_allow_html=True)

      st.markdown("<br>", unsafe_allow_html=True)

      st.markdown("""
      <div style="background-color:#FFF3E0; padding:15px; border-radius:10px;">
        <h4>📈 Trend Analysis</h4>
        <p>Track changes in crop production over multiple years.</p>
     </div>
     """, unsafe_allow_html=True)

      st.markdown("<br>", unsafe_allow_html=True)

      st.markdown("""
     <div style="background-color:#FCE4EC; padding:15px; border-radius:10px;">
        <h4>🎯 Decision Support</h4>
        <p>Generate insights to support farmers, researchers, and policymakers.</p>
     </div>
     """, unsafe_allow_html=True)    
    st.markdown("---")
    st.subheader("🛠️ Technologies Used")

    st.markdown("""
    <div style="background-color:#FAFAFA; padding:18px; border-radius:12px;">

    <span style="background:#D6EAF8; color:#154360; padding:8px 14px; border-radius:20px; margin:6px; display:inline-block;">
   Python
    </span>
   <span style="background:#D5F5E3; color:#145A32; padding:8px 14px; border-radius:20px; margin:6px; display:inline-block;">
    Pandas
   </span>

   <span style="background:#FCF3CF; color:#7D6608; padding:8px 14px; border-radius:20px; margin:6px; display:inline-block;">
   Matplotlib
   </span>
   <span style="background:#FDEDEC; color:#922B21; padding:8px 14px; border-radius:20px; margin:6px; display:inline-block;">
   Seaborn
   </span>
   <span style="background:#E8DAEF; color:#5B2C6F; padding:8px 14px; border-radius:20px; margin:6px; display:inline-block;">
   Plotly
   </span>
   <span style="background:#D4EFDF; color:#196F3D; padding:8px 14px; border-radius:20px; margin:6px; display:inline-block;">
   Streamlit
   </span>
   </div>
""", unsafe_allow_html=True)
elif opt=="📅Dataset":
    st.markdown("""
    <style>
    /* Horizontal Layout */
   div[role="radiogroup"]{
    display:flex;
    justify-content:center;
    gap:20px;
    margin-top:10px;
    margin-bottom:20px;
 }
   /* Select Dataset heading */
    label[data-testid="stWidgetLabel"] p{
    font-size:35px !important;font-weight:800 !important;color:#000000 !important;
    }
 /* Large Button Style */
 div[role="radiogroup"] label{
    background-color:#FFF5F5;
    border:2px solid #8B0000;
    border-radius:18px;
    padding:20px 35px !important;
    color:#8B0000 !important;
    transition:all 0.3s ease;
    cursor:pointer;min-width:300px;min-height:70px;text-align:center;justify-content:center !important;
 }
    div[role="radiogroup"] label div[data-testid="stMarkdownContainer"] p{
    font-size:23px !important;
    font-weight:800 !important;
    color:#8B0000 !important;
    margin:0 !important;
 /* Hover Effect */
    div[role="radiogroup"] label:hover{
    background:#8B0000 !important;
    color:white !important;
    transform:scale(1.05);
    box-shadow:0 6px 15px rgba(0,0,0,0.25);
 }

 </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>

 /* Tabs Container */
    .stTabs [data-baseweb="tab-list"]{
    gap:12px;
 }

 /* Normal Tabs */
   .stTabs [data-baseweb="tab"]{
    background:#A61B1B;
    color:white;
    font-size:24px;font-weight:800;padding:12px 28px;border-radius:10px 10px 0 0; transition:0.3s;
 }
 /* Increase tab text size */
 .stTabs [data-baseweb="tab"] div[data-testid="stMarkdownContainer"] p{
    font-size:24px !important;
    font-weight:800 !important;
  }

 /* Hover */
 .stTabs [data-baseweb="tab"]:hover{
    background:#7A0000;
    color:white;
 }

 /* Selected Tab */
 .stTabs [aria-selected="true"]{
    background:#5C0000 !important;
    color:white !important;
    border-bottom:4px solid #FFD700 !important;
    box-shadow:0 4px 10px rgba(0,0,0,0.3);
 }

 </style>
""", unsafe_allow_html=True) 

    button=st.radio("Select Dataset",["District-wise dataset","Region-Wise dataset"],index=None,key="dataset_radio")
    import pandas as pd
    if button== "District-wise dataset":
      df=pd.read_csv("crop_production.csv")
    else:
     df=pd.read_csv("crop_yield.csv")
    t1,t2,t3=st.tabs(["Dataset Summary","Dataset columns","Dataset value_counts"])
    with t1:
      from st_aggrid import AgGrid, GridOptionsBuilder
      st.markdown("""
      <h2 style='
     color:#000;
     font-size:34px;
     font-weight:800;'>
     📋 Dataset Preview
     </h2>
     """, unsafe_allow_html=True)# Slider
      st.markdown("""
     <style>

     /* Slider label */
     div[data-testid="stSlider"] label p{
     font-size:16px !important;   /* Change size as needed */
     font-weight:600 !important;color:#000000 !important;
     }
     </style>
     """, unsafe_allow_html=True)
      rows = st.slider(
        "🔍 Select number of rows",min_value=1,max_value=100,value=20,step=1
     )
     # Grid Options
      gb = GridOptionsBuilder.from_dataframe(df.head(rows))
      gb.configure_default_column(
        resizable=True,sortable=True,filter=True, minWidth=140
     )
      gridOptions = gb.build()
     # Table
      AgGrid(
        df.head(rows),
        gridOptions=gridOptions,fit_columns_on_grid_load=True,height=500, theme="balham",
        custom_css={
            ".ag-header": {
                "background-color": "#B71C1C !important",
                "color": "white !important","font-size": "18px","font-weight": "bold"
            },
            ".ag-header-cell": {
                "padding": "10px",
                "background-color": "#B71C1C !important","color": "white !important","border-right": "1px solid white"
            },
            ".ag-header-cell-label": {
                "color": "white !important","justify-content": "center",
                "font_weight":"bolc"
            },
            ".ag-cell": {
                "font-size": "15px",
                "text-align": "center","padding": "10px","border-bottom": "1px solid #EEEEEE"
            },
            ".ag-row:nth-child(even)": {
                "background-color": "#FFF5F5"
            },
            ".ag-root-wrapper": {
                "border": "1px solid #B71C1C","border-radius": "8px"
            }
        }
    )
    with t2:
      st.markdown("""
     <h2 style="
     color:#000;
     font-size:34px;
     font-weight:800;
     margin-bottom:10px;">
      📋 Columns Information
     </h2>
     """, unsafe_allow_html=True)
      column_info = pd.DataFrame({
        "Column No": range(len(df.columns)),
        "Column Name": df.columns,
        "Data Type": df.dtypes.astype(str).values,
        "Non-Null Values": df.notnull().sum().values,
        "Null Values": df.isnull().sum().values
     })
      from st_aggrid import AgGrid, GridOptionsBuilder
      gb = GridOptionsBuilder.from_dataframe(column_info)
      gb.configure_default_column(
        resizeable=True,
        sortable=True,filter=True,wraptext=False,autoHeight=False, minwidth=180
      )
      gridOptions = gb.build()
      AgGrid(
        column_info,
        gridOptions=gridOptions,
        fit_columns_on_grid_load=True,height=450,theme="balham",
        custom_css={
            ".ag-header": {
                "background-color": "#B71C1C !important",
                "color": "white !important","font-weight": "bold","font-size": "18px"
            },
            ".ag-header-cell": {
                "padding":"10px",
                "background-color": "#B71C1C !important","color": "white !important"
            },
            ".ag-header-cell-label": {
                "color": "white !important","justify-content": "center","font-weight": "bold"
            },
            ".ag-cell": {
                "text-align": "center",
                "font-size": "17px","line-height": "35px","border-right": "0.5px solid #eeeeee","border-bottom": "0.5px solid #eeeeee"
            },
            ".ag-row:nth-child(even)": {
                "background-color": "#FFF5F5"
            },
            ".ag-root-wrapper": {
                "border": "2px solid #B71C1C","border-radius": "8px"
            }
        }
    )
        # Create value counts table
      from st_aggrid import AgGrid, GridOptionsBuilder
    with t3:
     st.title("📊 Dataset Value Counts")
     # Select column
     column = st.selectbox("Select a column", df.columns)
    # Calculate value counts
     value_counts_df = (
        df[column]
        .value_counts()
        .reset_index()
     )
     value_counts_df.columns = [column, "Count"]
     # Configure AgGrid
     gb = GridOptionsBuilder.from_dataframe(value_counts_df)
     gb.configure_default_column(
        width=300,
        sortable=True,
        filter=True,
        resizable=True,
        cellstyle={
          "fontsize": "25px",
          "fontweight": "600"
        }
     )
     gridOptions = gb.build()
     # Display table
     AgGrid(
        value_counts_df,
        gridOptions=gridOptions,
        fit_columns_on_grid_load=True,height=400,theme="streamlit",
        custom_css={
        ".ag-header": {
            "background-color": "#B71C1C !important",
            "color": "white !important",
            "font-size": "18px","font-weight": "bold","border-bottom": "2px solid #8B0000"
        },
        ".ag-header-cell": {
            "background-color": "#B71C1C !important",
            "color": "white !important","border-right": "1px solid white"
        },
        ".ag-cell": {
            "background-color": "white",
            "color": "black",
            "border": "1px solid #E8B4B4","font size": "18px","font weight": "600"
        },
        ".ag-row": {
            "height": "40px ! important",
            "border-bottom": "1px solid #E8B4B4"
        },
        ".ag-root-wrapper": {
            "border": "2px solid #B71C1C",
            "border-radius": "8px"
        }
    }
)

elif opt=="🧹Data cleaning":
 st.title("🧹Data cleaning")
 import pandas as pd
 df=pd.read_csv("crop_production.csv")
#  st.subheader("🧹Data Cleaning")
# Original Report
 col1, col2, col3 = st.columns(3)
 with col1:
    st.metric("Original Rows", len(df))
 with col2:
    st.metric("Missing Values", df["Production"].isnull().sum())
 with col3:
    st.metric("Duplicate Rows", df.duplicated().sum())
 st.write("---")
 st.markdown("""
 <style>
 /* Radio widget heading */
 label[data-testid="stWidgetLabel"] p{
    font-size:28px !important;
    font-weight:bold !important;
    color:black !important;
 }

 /* Radio button label */
 label[data-testid="stWidgetLabel"] p{
    font-size:26px !important;
    font-weight:700 !important;
    color:black !important;
 }

 /* Radio option text */
 div[role="radiogroup"] label{
    font-size:22px !important;
    font-weight:600 !important;
 }
 /* Increase radio circle size */
 div[role="radiogroup"] input[type="radio"]{
    transform: scale(1.5);
 }

 </style>
 """, unsafe_allow_html=True)
# User Option
 option = st.radio("Select Missing Value Treatment",("Drop Missing Values","Fill with Mean","Fill with Median"))
# Run Button
 if st.button("🚀 Run Cleaning Pipeline"):
    clean_df = df.copy()
   # Missing Value Handling
    if option == "Drop Missing Values":
        clean_df = clean_df.dropna(subset=["Production"])
    elif option == "Fill with Mean":
        clean_df["Production"] = clean_df["Production"].fillna(clean_df["Production"].mean())
    elif option == "Fill with Median":
        clean_df["Production"] = clean_df["Production"].fillna(clean_df["Production"].median())
    # Remove Duplicates
    clean_df = clean_df.drop_duplicates()
    st.success("✅ Data Cleaning Completed Successfully!")
    st.subheader("📊 Cleaning Report")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Rows After Cleaning", len(clean_df))
    with c2:
        st.metric("Missing Values Left", clean_df["Production"].isnull().sum())
    with c3:
        st.metric("Duplicate Rows Left", clean_df.duplicated().sum())
    st.write("### Cleaned Dataset")
    display_df=clean_df.head(50)
    from st_aggrid import AgGrid, GridOptionsBuilder
    gb = GridOptionsBuilder.from_dataframe(display_df)
    gb.configure_default_column(
    sortable=True,filter=True,resizable=True
    )
    gridOptions = gb.build()
    AgGrid(
     display_df,
     gridOptions=gridOptions,fit_columns_on_grid_load=True,height=500,theme="streamlit",
     custom_css={
        ".ag-header": {
            "background-color": "#B71C1C !important",
            "color": "white !important","font-size": "17px","font-weight": "bold"
        },
        ".ag-header-cell": {
            "background-color": "#B71C1C !important","color": "white !important"
        },
        ".ag-cell": {
            "background-color": "white","color": "black","font-size": "15px","border": "1px solid #E8B4B4"
        },
        ".ag-root-wrapper": {
            "border": "2px solid #B71C1C","border-radius": "8px"
        }
    }
)
elif opt=="📊Data visualization":
   st.title("📊Data visualization")
   st.set_page_config(page_title="Agriculture Dashboard",layout="wide")
   st.markdown("""
 <style>

  /* Tabs container */
   .stTabs [data-baseweb="tab-list"]{
     gap: 12px;
     justify-content: left;
     background-color: #FFF8E1;
     padding: 10px;
     border-radius: 15px;
   }

   /* Individual tabs */
    .stTabs [data-baseweb="tab"]{
     height: 60px;
     padding: 0 30px;
     border-radius: 15px;
     background: #FFE082;
     color: #B71C1C !important;
     font-size: 30px;
     font-weight: 700;
     transition: all 0.3s ease;
     border: 2px solid #FFD54F;
    }

    /* Selected tab */
    .stTabs [aria-selected="true"]{
     background: linear-gradient(90deg,#B71C1C,#D32F2F) !important;
     color: white !important;
     border: none !important;
     box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    }

    /* Hover effect */
    .stTabs [data-baseweb="tab"]:hover{
     background:#FFCC80;
     transform: translateY(-2px);
   }

   </style>
    """, unsafe_allow_html=True)
   t1,t2,t3=st.tabs(["By production","By year","comparisons"])
   with t1:
     import pandas as pd
     import plotly.express as px
     df2=pd.read_csv("crop_yield.csv")
     scatter_df = df2.head(100)

     fig11 = px.scatter(
     scatter_df,
     x="Rainfall_mm",
     y="Yield_tons_per_hectare",
     color="Crop",
     size="Yield_tons_per_hectare",          # High production = bigger dot
     size_max=30,
     hover_data=[
        "Region",
        "Weather_Condition",
        "Yield_tons_per_hectare"
     ],
     title="Rainfall vs Production for Different Crops"
     )
     fig11.update_layout(width=700,height=700,
                         title_font_size=28,
                         title_x=0.01,
                         xaxis_title="Rainfall (mm)",
                         xaxis_title_font=dict(size=22, color="#000000"),
                         xaxis=dict(
                         tickfont=dict(size=18, color="#000000")
                        ),

    # Y-axis
                        yaxis_title="Yield (tons/hectare)",
                        yaxis_title_font=dict(size=22, color="#000000"),
                        yaxis=dict(
                        tickfont=dict(size=18, color="#000000")
                        )
                   )
            
     fig11.update_traces(marker=dict(opacity=0.7))
     st.plotly_chart(fig11, use_container_width=True)
     df2=pd.read_csv("crop_yield.csv")
     import pandas as pd
     import plotly.express as px
     import plotly.express as px
     import streamlit as st
     df2["Fertilizer_Used"] = df2["Fertilizer_Used"].map({True: "Yes", False: "No"})
     df2["Irrigation_Used"] = df2["Irrigation_Used"].map({True: "Yes", False: "No"})
     fig21= px.sunburst(
     df2,
     path=["Crop","Fertilizer_Used", "Irrigation_Used"],
     values="Yield_tons_per_hectare",
     title="Using the fertilizers and irrigation in differnt crops",
     color="Crop",
     hover_data=["Yield_tons_per_hectare"],
     color_discrete_sequence=[
        "#FFCDD2",
        "#EF9A9A",
        "#E57373",
        "#EF5350",
        "#E44336",
        "#E53935",
        "#D32F2F",
        "#C62828",
        "#8E0000"
     ]
     )
     fig21.update_layout(
        width=700,height=700,
        title_text="Using the fertilizers and Irrigation in different crops",
        title_font_size=28,
        title_x=0.01
     )
     st.plotly_chart(fig21, use_container_width=True)
     import streamlit as st
     import seaborn as sns
     import matplotlib.pyplot as plt
     import pandas as pd
     df2 = pd.read_csv("crop_yield.csv")
     fig15, ax = plt.subplots(figsize=(5,3))
     sns.violinplot(
     data=df2,
     x="Soil_Type",
     y="Yield_tons_per_hectare",
     inner="box",
     palette="coolwarm",
     ax=ax)
     ax.set_xlabel("Soil Type")
     ax.set_ylabel("Yield_tons_per_hectare")
     ax.set_title("Soil Type vs Yield")
     ax.grid(False)
     st.pyplot(fig15)
     import streamlit as st
     import seaborn as sns
     import matplotlib.pyplot as plt
     fig20, ax = plt.subplots(figsize=(5,3))
     sns.boxplot(
     data=df2,
     x="Weather_Condition",
     y="Days_to_Harvest",
     palette="Set1",
     ax=ax)
     sns.set_style("white")
     ax.set_xlabel("Weather Condition", fontsize=12)
     ax.set_ylabel("Harvesting Days", fontsize=12)
     ax.set_title("Harvesting Days vs Weather Condition", fontsize=20)
     ax.grid(True, linestyle="--", alpha=0.9)
     st.pyplot(fig20)
     import streamlit as st
     import seaborn as sns
     import matplotlib.pyplot as plt
     df=pd.read_csv("crop_production.csv")
     fig21, ax = plt.subplots(figsize=(5,3))
     sns.countplot(
     data=df.head(100),
     x="Season",
     hue="Crop",
     palette="rocket",
     ax=ax
     )
     ax.set_xlabel("Season", fontsize=12)
     ax.set_ylabel("Number of Counts", fontsize=12)
     ax.set_title("Season vs Crop", fontsize=15)
     ax.legend(title="Crop", loc="upper left", bbox_to_anchor=(1, 1))
     sns.set_style("darkgrid")
     st.pyplot(fig21)
     import streamlit as st
     import pandas as pd
     import matplotlib.pyplot as plt
     import seaborn as sns
     df2 = pd.read_csv("crop_yield.csv")
     fig, ax = plt.subplots(figsize=(7,3))
     sns.heatmap(
     df2[[
        "Rainfall_mm",
        "Temperature_Celsius",
        "Days_to_Harvest",
        "Yield_tons_per_hectare"
     ]].corr(),
     annot=True,
     linewidths=1,
     cmap="Reds",
     ax=ax
     )
     ax.set_title(
     "Correlation Matrix",
     fontsize=28,
     color="brown",
     loc="left"      # Left-align the title
     )
     sns.set_style("whitegrid")
     st.pyplot(fig)
   with t2:
     df = pd.read_csv("crop_production.csv")
     df2 = pd.read_csv("crop_yield.csv")
     first5_crops=df["Crop"].unique()[:5]
     year_df=(df[df["Crop"].isin(first5_crops)].groupby(["Crop_Year","Crop"],as_index=False)["Production"].sum())
     import plotly.express as px
     fig12 = px.line(year_df,x="Crop_Year",y="Production",color="Crop",markers=True,title="Crop Production by Year",hover_data=["Crop", "Production"],log_y=True)
     fig12.update_layout(title_font_size=28,title_x=0.01,width=700,height=500,
                        xaxis_title="Crop Year",xaxis_title_font=dict(size=22,color="black"),
                        xaxis=dict(tickfont=dict(size=18,color="black")),
                        yaxis_title="Production", yaxis_title_font=dict(size=22,color="black"),
                        yaxis=dict(tickfont=dict(size=18,color="black"))
                        )
     st.plotly_chart(fig12, use_container_width=True)
     import streamlit as st
     import seaborn as sns
     import matplotlib.pyplot as plt
     fig17, ax = plt.subplots(figsize=(10, 6))
     sns.boxplot(data=df.head(200),x="District_Name",y="Crop_Year",hue="Season",ax=ax)
     ax.set_xlabel("District_Name", fontsize=12)
     ax.set_ylabel("Crop_Year", fontsize=12)
     ax.set_title("District vs Crop Years with Respect to Season", fontsize=19)
     ax.legend(title="SEASON", loc="upper left", bbox_to_anchor=(1, 1))
     sns.set_style("darkgrid")
     sns.set_palette("Set2")
     st.pyplot(fig17)
     import plotly.express as px
     # Group data by Crop Year
     area_year_df = (df.groupby("Crop_Year", as_index=False)["Area"].sum())
     # Create Area Chart
     fig = px.area(
     area_year_df,
     x="Crop_Year",
     y="Area",
     title="🌾 Area Under Cultivation Over the Years",
     color_discrete_sequence=["#2E8B57"])  # Sea Green
     # Customize layout
     fig.update_layout(
     xaxis_title="Crop Year",
     yaxis_title="Cultivated Area",
     template="plotly_white",
     hovermode="x unified",
     title_x=0.01,
     title_font_size=28,
     xaxis_title_font=dict(size=22,color="black"),
     yaxis_title_font=dict(size=22,color="black"),
     xaxis=dict(tickfont=dict(size=18,color="black")),
     yaxis=dict(tickfont=dict(size=18,color="black")),
     font=dict(size=14))
     # Make boundary line thicker
     fig.update_traces(
     line=dict(color="#B71C1C",width=3),
     fillcolor="rgba(229,115,115,0.45)",
     hovertemplate="<b>Year:</b> %{x}<br><b>Area:</b> %{y:,.0f}<extra></extra>")
     st.plotly_chart(fig,use_container_width=True)
     import streamlit as st
     import plotly.express as px
     # Count unique crop types
     crop = (
     df.groupby(["Crop_Year", "Season"])["Crop"]
     .nunique()
     .reset_index(name="Crop"))
     # Stacked Bar Chart
     fig21 = px.bar(
     crop,
     x="Crop_Year",
     y="Crop",
     color="Season",
     barmode="stack",
     title="Crop Types Cultivated in Different Seasons Across Years",
     color_discrete_sequence=[
        "#FFCDD2",
        "#EF9A9A",
        "#E57373",
        "#EF5350",
        "#F44336",
        "#D32FDF"
        ]
     )
     fig21.update_layout(
     xaxis_title="Crop Year",
     yaxis_title="Number of Crop Types",
     template="plotly_white",
     title_x=0.01,
     title_font_size=28,
     xaxis_title_font=dict(size=22,color="black"),
     yaxis_title_font=dict(size=22,color="black"),
     xaxis=dict(tickfont=dict(size=18,color="black")),
     yaxis=dict(tickfont=dict(size=18,color="black")),
     legend_title="Season")
     st.plotly_chart(fig21, use_container_width=True)
     
   with t3:
     df = pd.read_csv("crop_production.csv")
     st.markdown("""
     <div style="
     background:#8B0000;
     border-radius:15px;
     padding:18px;
     text-align:center;
     margin-bottom:20px;
     ">
     <h2 style="
        color:white;
        margin:0;
        font-size:32px;
        font-weight:bold;
        text-transform:capitalize;">
        Rice Production Analysis 
     </h2>
     </div>
     """, unsafe_allow_html=True)
     col1, col2 = st.columns(2)
     with col1:
         import plotly.express as px
         import streamlit as st
# CSS (Page ke start me sirf ek baar likho)
        
# ---------------- Rice Production ----------------
         rice_df = df[df["Crop"] == "Rice"]
         district_data = (
           rice_df.groupby(["District_Name", "Season"])["Production"]
           .sum()
           .reset_index()
          )
         district_data = district_data.sort_values(
          by="Production",
         ascending=False
         ).head(10)
         fig4= px.bar(
         district_data,
         x="District_Name",
         y="Production",
         color="Season",
         color_discrete_sequence=[
         "#F44336",
         "#EF5350",
         "#E57373",
         "#EF9A9A",
         "#FFCDD2",
         "#FFEBEE"
         ],
         title="In District ",
         hover_data=["Season", "Production"]
         )
         fig4.update_layout(
         title_font_size=22,
         xaxis_title="District Name",
         yaxis_title="Production",
         xaxis_title_font=dict(size=22, color="black"),
         yaxis_title_font=dict(size=22, color="black"),
         xaxis=dict(
         tickfont=dict(size=16, color="black"),
         showline=True,
         linecolor="#8B0000",
         linewidth=2,
         mirror=True
         ), 
         yaxis=dict(
         tickfont=dict(size=16, color="black"),
         showline=True,
         linecolor="#8B0000",
         linewidth=2,
         mirror=True
         ),
         plot_bgcolor="white",
         paper_bgcolor="white",
         margin=dict(t=60, b=20, l=20, r=20)
         )
         fig4.update_xaxes(
         showgrid=True,
         gridcolor="#E8CACA"
         )
         fig4.update_yaxes(
         showgrid=True,
         gridcolor="#E8CACA"
         )
         st.plotly_chart(fig4, use_container_width=True,key="rice_district")
     import plotly.express as px
     df2 = pd.read_csv("crop_yield.csv")
     with col2:
         rice_df = df2[df2["Crop"] == "Rice"]         #rice production in region
         region_data = (
         rice_df.groupby(["Region", "Weather_Condition"])["Yield_tons_per_hectare"]
         .sum()
         .reset_index())
         fig32 = px.bar(
         region_data,
         x="Region",
         y="Yield_tons_per_hectare",
         title="Rice Yield Region Wise",
         color="Weather_Condition",
         color_discrete_sequence=[
         "#F44336",
         "#EF5350",
         "#E57373",
         "#EF9A9A",
         "#FFCDD2",
         "#FFEBEE"
          ],
         hover_data=["Weather_Condition", "Yield_tons_per_hectare"],
         log_y=True
         )
         fig32.update_layout(
         title_font_size=25,
         xaxis_title="Region",
         yaxis_title="Yield (tons/hectare)",
         xaxis_title_font=dict(size=22, color="black"),
         yaxis_title_font=dict(size=22, color="black"),
         xaxis=dict(
         tickfont=dict(size=16, color="black")
         ),
         yaxis=dict(
         tickfont=dict(size=16, color="black")
         ),
         plot_bgcolor="white",
         paper_bgcolor="white",
         margin=dict(l=20, r=20, b=20, t=60)
         )
            # Grid
         fig32.update_xaxes(showgrid=False)
         fig32.update_yaxes(
         showgrid=True,
         gridcolor="#F3D6D6",
             # Border only around graph area
         showline=True,
         linecolor="#8B0000",
         linewidth=2,
         mirror=True
         )
         st.plotly_chart(fig32, use_container_width=True,key="rice_region")
     st.markdown("""
     <div style="
     background:#8B0000;
     border-radius:15px;
     padding:18px;
     text-align:center;
     margin-bottom:20px;
     ">
     <h2 style="
        color:white;
        margin:0;
        font-size:32px;
        font-weight:bold;
        text-transform:capitalize;">
        Maize Production Analysis 
     </h2>
     </div>
     """, unsafe_allow_html=True)
     col3, col4 = st.columns(2)
     with col3:
         maize_df = df[df["Crop"] == "Maize"]
         maize_district = (
         maize_df.groupby(["District_Name","Season"], as_index=False)["Production"]
         .sum()
         .sort_values(by="Production", ascending=False)
         .head(10))
         fig4 = px.funnel(
         maize_district,
         y="District_Name",
         x="Production",
         hover_data=["Season"],
         color="District_Name",
         color_discrete_sequence=[
          "#D32F2F",
          "#E53935",
          "#EF5350",
          "#F0625D",
          "#E57373",
          "#EF9A9A",
          "#F4A6A6",
          "#F8B4B4",
          "#FBC4C4",
         ],
         title="In District")
         fig4.update_layout(height=450,margin=dict(l=20,r=20,t=60,b=20),title_font_size=22,
                            xaxis_title="Production",yaxis_title="District Name",
                            xaxis_title_font=dict(size=22, color="black"),
                            yaxis_title_font=dict(size=22, color="black"),
                            xaxis=dict(tickfont=dict(size=16, color="black")),
                            yaxis=dict(tickfont=dict(size=16, color="black"))
                           )
         st.plotly_chart(fig4, use_container_width=False)
     with col4:
         maize_df2 = df2[df2["Crop"] == "Maize"]
         maize_region = (
         maize_df2.groupby(["Region","Weather_Condition"], as_index=False)["Yield_tons_per_hectare"]
         .sum()
         .sort_values(by="Yield_tons_per_hectare", ascending=False).head(10))
         fig3 = px.funnel(
         maize_region,
         y="Region",
         x="Yield_tons_per_hectare",
         hover_data=["Weather_Condition"],
         color="Region",
         color_discrete_sequence=[
         "#FF6B6B",
         "#FF8080",
         "#FF9999",
         "#FFB3B3",
         "#FFCACA",
         "#FFDCDC",
         "#FFE5E5",
         "#FFF0F0",
         "#F8C8C8",
         "#F4A6A6"
         ],
         title="In Region")
         fig3.update_layout(title_font_size=22,xaxis_title="Yield_tons_per_hectare",
         yaxis_title="Region",
         xaxis_title_font=dict(size=22, color="black"),
         yaxis_title_font=dict(size=22, color="black"),
         xaxis=dict(tickfont=dict(size=16, color="black")),
         yaxis=dict(tickfont=dict(size=16, color="black")),
         margin=dict(t=60,b=20,l=20,r=20)
         )
         st.plotly_chart(fig3, use_container_width=False)
     st.markdown("""
     <div style="
     background:#8B0000;
     border-radius:15px;
     padding:18px;
     text-align:center;
     margin-bottom:20px;
     ">
     <h2 style="
        color:white;
        margin:0;
        font-size:32px;
        font-weight:bold;
        text-transform:capitalize;">
        Wheat Production Analysis 
     </h2>
     </div>
     """, unsafe_allow_html=True)
     col5,col6=st.columns(2)
     with col5:
         wheat_df = df[df["Crop"] == "Wheat"].head(100)     #wheat production in district
         fig6 = px.pie(
         wheat_df,
         names="District_Name",          
         values="Production",
         title=" In District",
         hole=0.3,
         color="District_Name",
         color_discrete_sequence=[
            "#D32F2F",
            "#EF3935",
            "#EF5350",
            "#F0625D",
            "#EF7373",
            "#EF9A9A",
            "#F4A6A6",
            "#F8B4B4",
            "#FBC4C4",
            "#FFCDD2"
         ]
         )
         fig6.update_layout(height=350,margin=dict(l=20,r=20,t=60,b=20))
         fig6.update_layout(title_font_size=22)
         st.plotly_chart(fig6) 
     with col6:
         wheat_df2 = df2[df2["Crop"] == "Wheat"]
         fig7 = px.pie(
         wheat_df2,
         names="Region",          
         values="Yield_tons_per_hectare",
         title="In Region",
         color="Region",
         hole=0.3,
         color_discrete_sequence=[
                 "#D32F2F",
                 "#E53935",
                 "#EF5350",
                 "#F0625D",
                 "#E57373",
                 "#EF9A9A",
                 "#F4A6A6",
                 "#F8B4B4",
                 "#FBC4C4",
                 "#FFCDD2"
              ]
             )
         fig7.update_layout(
         title_font_size=22)
         st.plotly_chart(fig7)  
     st.markdown("""
     <div style="
     background:#8B0000;
     border-radius:15px;
     padding:18px;
     text-align:center;
     margin-bottom:20px;
     ">
     <h2 style="
        color:white;
        margin:0;
        font-size:32px;
        font-weight:bold;
        text-transform:capitalize;">
        Soyabean Production Analysis
     </h2>
     </div>
     """, unsafe_allow_html=True)
     col7,col8=st.columns(2)
     with col7:
         df["Production"] = pd.to_numeric(df["Production"], errors="coerce")
# Remove missing values
         df = df.dropna(subset=["Production"])
# Filter Soyabean data (change to Soybean if that's the spelling in your dataset)
         soybean_df = df[df["Crop"] == "Soyabean"]
# Region-wise production
         soybean_region = (
         soybean_df.groupby("District_Name", as_index=False)["Production"]
         .sum()
         .sort_values(by="Production", ascending=False).head(5)
         )
         fig = px.bar(
         soybean_region,
         x="Production",
         y="District_Name",
         orientation="h",
         color="District_Name",
         color_discrete_sequence=[
            "#D32F2F",
            "#E53935",
            "#EF5350",
            "#F0625D",
            "#E57373"
         ],
         text_auto=True
         )
         fig.update_layout(
               title=dict(text="In District",font=dict(size=22)),
               xaxis_title="Production",
               yaxis_title="District_Name",xaxis_title_font=dict(size=22, color="black"),
               yaxis_title_font=dict(size=22, color="black"),xaxis=dict(tickfont=dict(size=16, color="black")),
               yaxis=dict(tickfont=dict(size=16, color="black")),
               height=500,
               margin=dict(t=60,b=20,l=20,r=20)
            )
         st.markdown("<div style='margin-top:40px;'></div>", unsafe_allow_html=True)
         st.plotly_chart(fig, use_container_width=True)
     with col8:
         soybean_df = df2[df2["Crop"] == "Soybean"]
# Region-wise soybean production
         soybean_region = (
         soybean_df.groupby("Region", as_index=False)["Yield_tons_per_hectare"]
         .sum()
         .sort_values(by="Yield_tons_per_hectare", ascending=False)
            )
# Horizontal bar chart
         fig = px.bar(
         soybean_region,
         x="Yield_tons_per_hectare",
         y="Region",
         orientation="h",
         color="Region",
         color_discrete_sequence=[
         "#D32F2F",
         "#A52A2A",
         "#C62828",
         "#CD5C5C",
         "#D32F2F",
         "#E53935",
         "#EF5350",
         "#F08080",
         "#FA8072"
         ],
         text="Yield_tons_per_hectare",
         title="🌱 Region-wise Soybean Production"
         )
         fig.update_traces(textposition="outside")
         fig.update_layout(
         title=dict(
         text="In Region ",
         x=0.01,
         xanchor="left",
         font=dict(size=22)
         ),
         xaxis_title="Production (Tonnes)",
         yaxis_title="Region",
         plot_bgcolor="white",
         xaxis_title_font=dict(size=22, color="black"),
         yaxis_title_font=dict(size=22, color="black"),
         xaxis=dict(tickfont=dict(size=16, color="black")),
         yaxis=dict(tickfont=dict(size=16, color="black")),
         margin=dict(t=60,b=20,l=20,r=20),
         paper_bgcolor="white",
         height=500
         )
         st.plotly_chart(fig, use_container_width=True)   
elif opt=="🗺Hotspots":
     st.set_page_config(layout="wide")
     import pandas as pd
     df = pd.read_csv("crop_production.csv")
     df2 = pd.read_csv("crop_yield.csv")
     import streamlit as st
     import pandas as pd
     import plotly.express as px
     import streamlit as st
     st.markdown("""
     <style>
     /* Sidebar heading */
     section[data-testid="stSidebar"] h2{
     color: white !important;
     font-size: 30px !important;
     font-weight: 800 !important;
     }
     /* Sidebar widget labels */
     section[data-testid="stSidebar"] label[data-testid="stWidgetLabel"] p{
     color: white !important;
     font-size: 22px !important;
     font-weight: 700 !important;
     }
     </style>
     """, unsafe_allow_html=True)
# ---------------- Title ----------------
     st.title("Hotspots through Map")
# ---------------- Read Dataset ----------------
     df = pd.read_csv("crop_production.csv")
     df["State_Name"] = df["State_Name"].str.strip()
# ---------------- Sidebar ----------------
     st.sidebar.header("Hotspot Filters")
# Crop Multiselect (Rice selected by default)
     crop_list= [
        "Bajra", 
        "Banana", 
        "Barley", 
        "Black pepper", 
        "Cashewnut", 
        "Dry chillies", 
        "Dry ginger", 
        "Garlic", 
        "Ginger", 
        "Jowar", 
        "Linseed",
        "Maize", 
        "Mango", 
        "Masoor", 
        "Moong(Green Gram)", 
        "Moth", 
        "Other Cereals & Millets", 
        "Potato", 
        "Ragi", 
        "Rice", 
        "Soyabean", 
        "Sugarcane", 
        "Sweet potato", 
        "Turmeric", 
        "Wheat", 
        "Urad", 
        "Cotton(lint)"
     ]
     selected_crops = st.sidebar.multiselect(
     "Select Crop(s)",
     options=crop_list,
     default=["Rice"]
     )
# Year Selectbox
     year_list = sorted(df["Crop_Year"].unique())
     selected_year = st.sidebar.selectbox(
     "Select Year",
     options=year_list,
     index=year_list.index(2010)   # Default year
     )
# ---------------- Filter Data ----------------
     state_data = (
     df[
        (df["Crop"].isin(selected_crops)) &
        (df["Crop_Year"] == selected_year)
     ]
     .groupby("State_Name", as_index=False)["Production"]
     .sum()
     )
     if state_data.empty:
          st.warning(
         f"""
         ⚠️ **No Data Available**

         The selected crop **{', '.join(selected_crops)}** was not cultivated in **{selected_year}**.

         👉 Please choose another crop or another year.
         """
         )
# ---------------- State Coordinates ----------------
     state_coords = pd.DataFrame({
      "State_Name": [
        "Andaman and Nicobar Islands",
        "Andhra Pradesh",
        "Arunachal Pradesh",
        "Assam",
        "Bihar",
        "Chandigarh",
        "Chhattisgarh",
        "Dadra and Nagar Haveli",
        "Goa",
        "Gujarat",
        "Haryana",
        "Himachal Pradesh",
        "Jharkhand",
        "Karnataka",
        "Kerala",
        "Madhya Pradesh",
        "Maharashtra",
        "Manipur",
        "Meghalaya",
        "Mizoram",
        "Nagaland",
        "Odisha",
        "Puducherry",
        "Punjab",
        "Rajasthan",
        "Sikkim",
        "Tamil Nadu",
        "Tripura",
        "Uttar Pradesh",
        "Uttarakhand",
        "West Bengal",
        "Telangana",
        "Jammu and Kashmir"
     ],
     "Latitude": [
        11.74, 15.91, 28.22, 
        26.20, 25.09, 30.73,
        21.28, 20.18, 15.30, 
        22.26, 29.06, 31.10,
        23.61, 15.32, 10.85,
        23.47, 19.75, 24.66,
        25.57, 23.16, 26.16, 
        20.95, 11.94, 31.15,
        27.02, 27.53, 11.13, 
        23.94, 26.85, 30.07,
        22.98, 17.12, 33.78
     ],
     "Longitude": [
        92.66, 79.74, 94.73, 
        92.93, 85.31, 76.78,
        81.86, 73.02, 74.12, 
        71.19, 76.09, 77.17,
        85.28, 75.71, 76.27, 
        77.95, 75.71, 93.91,
        91.88, 92.94, 94.56, 
        85.10, 79.81, 75.34,
        74.22, 88.51, 78.66, 
        91.99, 80.95, 79.02,
        87.85, 79.02, 76.58 
     ]
     })
# Merge coordinates
     state_data = state_data.merge(state_coords, on="State_Name", how="left")
# GeoJSON
     india_states_geojson = ("https://raw.githubusercontent.com/geohacker/india/master/state/india_state.geojson")
# ---------------- Choropleth Map ----------------
     fig = px.choropleth(
     state_data,
     geojson=india_states_geojson,
     locations="State_Name",
     featureidkey="properties.NAME_1",
     color="Production",
     color_continuous_scale="YlGnBu",
     title=f"Production of {', '.join(selected_crops)} Across Indian States ({selected_year})"
     )
# Bubble Markers
     fig.add_scattergeo(
     lat=state_data["Latitude"],
     lon=state_data["Longitude"],
     text=state_data["State_Name"],
     customdata=state_data["Production"],
     mode="markers",
     marker=dict(
        size=state_data["Production"] / state_data["Production"].max() * 40,
        color="red",
        opacity=0.8,
        line=dict(width=1, color="black")
    ),
    hovertemplate="<b>%{text}</b><br>Production: %{customdata:,.0f}<extra></extra>"
    )
# Layout
     fig.update_geos(
     fitbounds="locations",
     visible=False,
     projection_scale=6
     )
     fig.update_layout(
     height=800,
     title_font_size=28,
     margin=dict(l=0, r=0, t=60, b=0)
     )
# ---------------- Display ----------------
     st.plotly_chart(fig, use_container_width=True)
# ---------------- Crop Cultivation Area Map ----------------
     st.title("Crop Cultivation Area Across Indian States")
# Filter data using the SAME sidebar filters
     state_area = (
     df[
        (df["Crop"].isin(selected_crops)) &
        (df["Crop_Year"] == selected_year)
     ]
     .groupby("State_Name", as_index=False)["Area"]
     .sum()
     )
     state_area = state_area.merge(
     state_coords,
     on="State_Name",
     how="left"
     )
# Choropleth Map
     fig_area = px.choropleth(
     state_area,
     geojson=india_states_geojson,
     locations="State_Name",
     featureidkey="properties.NAME_1",
     color="Area",
     color_continuous_scale="Greens",
     title=f"Area Used for {', '.join(selected_crops)} Cultivation ({selected_year})",
     hover_name="State_Name",
     hover_data={
        "Area": ":,.0f"
     }
     )
     fig_area.add_scattergeo(
     lat=state_area["Latitude"],
     lon=state_area["Longitude"],
     text=state_area["State_Name"],
     customdata=state_area["Area"],
     mode="markers",
     marker=dict(
        size=(state_area["Area"] / state_area["Area"].max()) * 45 + 10,
        color=state_area["Area"],
        colorscale="Reds",
        showscale=False,
        opacity=0.9,
        line=dict(color="black", width=1)
     ),
     hovertemplate="<b>%{text}</b><br>Area: %{customdata:,.0f}<extra></extra>"  
     )
     fig_area.update_geos(
     fitbounds="locations",
     visible=False,
     projection_scale=6
     )
     fig_area.update_layout(
     height=800,
     margin=dict(l=0, r=0, t=60, b=0),
     title_font_size=28,
     coloraxis_colorbar=dict(title="Cultivated Area")
     )
     st.plotly_chart(fig_area, use_container_width=True)
     import streamlit as st
     import pandas as pd
     import plotly.express as px
     st.title("🌾 Season-wise Crop Production Across Indian States")
     df["Season"]=(df["Season"]
     .astype(str)
     .str.strip()
     .str.title()
     )

# ---------------- Season Selectbox ----------------
     season_options = [
     "Kharif",
     "Autumn",
     "Rabi",
     "Summer",
     "Winter"
     ]
     selected_season= st.selectbox(
     "🌦️ Select Season",
     options=season_options,
     key="season_production_map"
     )
 # ---------------- Filter Data ----------------
     filtered_df = df[
     (df["Crop"].isin(selected_crops)) &
     (df["Crop_Year"] == selected_year) &
     (df["Season"] == selected_season)
     ]
# ---------------- Group by State ----------------
     state_production = (
     filtered_df
     .groupby("State_Name", as_index=False)["Production"]
     .sum()
     )
# ---------------- State Coordinates ----------------
     state_coords = pd.DataFrame({
     "State_Name": [
             "Andaman and Nicobar Islands",
        "Andhra Pradesh",
        "Arunachal Pradesh",
        "Assam",
        "Bihar",
        "Chandigarh",
        "Chhattisgarh",
        "Dadra and Nagar Haveli",
        "Goa",
        "Gujarat",
        "Haryana",
        "Himachal Pradesh",
        "Jharkhand",
        "Karnataka",
        "Kerala",
        "Madhya Pradesh",
        "Maharashtra",
        "Manipur",
        "Meghalaya",
        "Mizoram",
        "Nagaland",
        "Odisha",
        "Puducherry",
        "Punjab",
        "Rajasthan",
        "Sikkim",
        "Tamil Nadu",
        "Tripura",
        "Uttar Pradesh",
        "Uttarakhand",
        "West Bengal",
        "Telangana",
        "Jammu and Kashmir"
     ],
     "Latitude": [
        11.74, 15.91, 28.22, 
        26.20, 25.09, 30.73,
        21.28, 20.18, 15.30, 
        22.26, 29.06, 31.10,
        23.61, 15.32, 10.85, 
        23.47, 19.75, 24.66,
        25.57, 23.16, 26.16, 
        20.95, 11.94, 31.15,
        27.02, 27.53, 11.13, 
        23.94, 26.85, 30.07,
        22.98, 17.12, 33.78
      ],
     "Longitude": [
        92.66, 79.74, 94.73, 
        92.93, 85.31, 76.78,
        81.86, 73.02, 74.12, 
        71.19, 76.09, 77.17,
        85.28, 75.71, 76.27, 
        77.95, 75.71, 93.91,
        91.88, 92.94, 94.56, 
        85.10, 79.81, 75.34,
        74.22, 88.51, 78.66, 
        91.99, 80.95, 79.02,
        87.85, 79.02, 76.58
     ]
     })
     state_production = state_production.merge(
     state_coords,
     on="State_Name",
     how="left"
     )
# ---------------- Choropleth Map ----------------
     fig22 = px.choropleth(
     state_production,
     geojson=india_states_geojson,
     locations="State_Name",
     featureidkey="properties.NAME_1",
     color="Production",
     color_continuous_scale="YlOrRd",
     title=f"{selected_season} Production of {', '.join(selected_crops)} ({selected_year})",
     hover_name="State_Name",
     hover_data={"Production": ":,.0f"}
     )
# ---------------- Production Bubble Markers ----------------
     fig22.add_scattergeo(
     lat=state_production["Latitude"],
     lon=state_production["Longitude"],
     text=state_production["State_Name"],
     customdata=state_production["Production"],
     mode="markers",
     marker=dict(
        size=(state_production["Production"] /
              state_production["Production"].max()) * 60,
        color="red",
        opacity=0.8,
        line=dict(width=1, color="black")
    ),
     hovertemplate="<b>%{text}</b><br>Production: %{customdata:,.0f}<extra></extra>"
     )
# ---------------- Layout ----------------
     fig22.update_geos(
     fitbounds="locations",
     visible=False,
     projection_scale=6
     )
     fig22.update_layout(
     height=850,
     margin=dict(l=0, r=0, t=60, b=0),
     title_font_size=28,
     coloraxis_colorbar=dict(title="Production")
     )
# ---------------- Display ----------------
     st.plotly_chart(fig22, use_container_width=True)
     import pandas as pd
     import plotly.express as px
     import streamlit as st

     st.title("🏆 Top High Production States in India")
# ---------------- Slider ----------------
     top_n = st.slider(
     "📍Select Number of Top States",
     min_value=4,
     max_value=10,
     value=5,
     step=1
     )
# ---------------- Group by State ----------------
     top_states = (
     df.groupby("State_Name", as_index=False)["Production"]
      .sum()
      .sort_values(by="Production", ascending=False)
      .head(top_n)
     )
# ---------------- State Coordinates ----------------
     state_coords = pd.DataFrame({
     "State_Name": [
        "Andaman and Nicobar Islands",
        "Andhra Pradesh",
        "Arunachal Pradesh",
        "Assam",
        "Bihar",
        "Chandigarh",
        "Chhattisgarh",
        "Dadra and Nagar Haveli",
        "Goa",
        "Gujarat",
        "Haryana",
        "Himachal Pradesh",
        "Jharkhand",
        "Karnataka",
        "Kerala",
        "Madhya Pradesh",
        "Maharashtra",
        "Manipur",
        "Meghalaya",
        "Mizoram",
        "Nagaland",
        "Odisha",
        "Puducherry",
        "Punjab",
        "Rajasthan",
        "Sikkim",
        "Tamil Nadu",
        "Tripura",
        "Uttar Pradesh",
        "Uttarakhand",
        "West Bengal",
        "Telangana",
        "Jammu and Kashmir"
     ],
     "Latitude": [
        11.74, 15.91, 28.22, 
        26.20, 25.09, 30.73,
        21.28, 20.18, 15.30, 
        22.26, 29.06, 31.10,
        23.61, 15.32, 10.85, 
        23.47, 19.75, 24.66,
        25.57, 23.16, 26.16, 
        20.95, 11.94, 31.15,
        27.02, 27.53, 11.13, 
        23.94, 26.85, 30.07,
        22.98, 17.12, 33.78
     ],
     "Longitude": [
        92.66, 79.74, 94.73, 
        92.93, 85.31, 76.78,
        81.86, 73.02, 74.12, 
        71.19, 76.09, 77.17,
        85.28, 75.71, 76.27, 
        77.95, 75.71, 93.91,
        91.88, 92.94, 94.56, 
        85.10, 79.81, 75.34,
        74.22, 88.51, 78.66, 
        91.99, 80.95, 79.02,
        87.85, 79.02, 76.58
     ]
     })
# ---------------- Merge Coordinates ----------------
     top_states = top_states.merge(
     state_coords,
     on="State_Name",
     how="left"
     )
# ---------------- India Choropleth ----------------
     fig = px.choropleth(
     top_states,
     geojson=india_states_geojson,
     locations="State_Name",
     featureidkey="properties.NAME_1",
     color="Production",
     color_continuous_scale="YlOrRd",
     title=f"🏆 Top {top_n} Highest Producing States in India"
     )
# ---------------- Bubble Markers ----------------
     fig.add_scattergeo(
     lat=top_states["Latitude"],
     lon=top_states["Longitude"],
      text=top_states["State_Name"],
     customdata=top_states["Production"],
     mode="markers",
     marker=dict(
        size=(top_states["Production"] /
              top_states["Production"].max()) * 45 + 10,

        color=top_states["Production"],
        colorscale="Reds",
        opacity=0.9,
        line=dict(color="black", width=1)
     ),
     hovertemplate=
     "<b>%{text}</b><br>" +
     "Production: %{customdata:,.0f}<extra></extra>"
     )
# ---------------- Layout ----------------
     fig.update_geos(
     fitbounds="locations",
     visible=False
     )
     fig.update_layout(
     height=800,
     margin=dict(l=0, r=0, t=60, b=0),
     title_font_size=28,
     title_x=0.02
     )
     st.plotly_chart(fig,use_container_width=True)
elif opt == "💡Insights":
    import streamlit as st

    # ---------- Heading ----------
    st.title("🌾 ANALYTICAL INSIGHTS")

    st.markdown("""
     <style>

     /* Generate Insights Button */
     div.stButton > button{
     width:100%;
     min-height:85px !important;
     background:linear-gradient(90deg,#B71C1C,#D32F2F,#EF5350) !important;
     color:white !important;
     border:none !important;
     border-radius:18px !important;
     box-shadow:0px 6px 15px rgba(183,28,28,0.35);
    }

 /* Button text */
    div.stButton > button *{
     font-size:25px !important;
     font-weight:900 !important;
     color:white !important;
    }
    </style>
    """, unsafe_allow_html=True)
    # ---------- Generate Button ----------
    generate = st.button("✨ Generate Insights", use_container_width=True)
    # ---------- Show Insights ----------
    if generate:
        st.subheader("🔍 Key Findings")
        insights = [
            "🌾 Soybean has the highest average yield among all crops in the dataset.",
            "📍 North region records the highest average crop yield.",
            "🌱 Chalky soil produces the highest average yield.",
            "☀️ Sunny weather conditions result in the highest crop yield.",
            "🌡️ Temperature has a weak positive relationship with crop yield (≈0.086).",
            "🌍 Kerala is the highest crop-producing state.",
            "🥈 Andhra Pradesh ranks second, followed by Tamil Nadu, Uttar Pradesh, and Assam.",
            "🥥 Coconut is the highest-produced crop overall.",
            "🌾 Sugarcane is the second most-produced crop.",
            "📈 2011 recorded the highest total crop production.",
            "🌱 Whole Year season contributes the maximum production.",
            "🌦️ Kharif has the highest seasonal production.",
            "❄️ Winter, ☀️ Summer, and 🍂 Autumn contribute comparatively lower production.",
            "🌾 Rice and Wheat are the major staple crops."
        ]
        colors = [
            "#FFEBEE",
            "#FFF3E0",
            "#FFFDE7",
            "#E8F5E9",
            "#E3F2FD",
            "#EDE7F6",
            "#FCE4EC"
        ]
        for i, item in enumerate(insights):
            color = colors[i % len(colors)]
            st.markdown(f"""
            <div style="
                background:{color};
                padding:18px;
                border-radius:15px;
                border-left:8px solid #B71C1C;
                margin-bottom:12px;
                font-size:19px;
                font-weight:600;
                color:#212121;
                box-shadow:0 3px 10px rgba(0,0,0,0.15);
            ">
                {item}
            </div>
            """, unsafe_allow_html=True)
else:
     import streamlit as st
     import pandas as pd

     st.title("📤 Export Dashboard")

     st.markdown("""
     ### Downloads analysis results and reports.

     Export filtered datasets, analytical insights, and dashboard reports
     for future reference.
     """)

    # Read datasets
     production_df = pd.read_csv("crop_production.csv")
     yield_df = pd.read_csv("crop_yield.csv")

     st.markdown("""
     <hr style="
     border: none;
     height: 6px;
     background: linear-gradient(to right, #8B0000, #B71C1C, #8B0000);
     border-radius: 20px;
     margin: 30px 0;
      ">
     """, unsafe_allow_html=True)

    # ---------------- Export Dataset ----------------
     st.subheader("📊 Export Dataset")

     st.download_button(
        label="⬇️ Download Crop Production CSV",
        data=production_df.to_csv(index=False),
        file_name="crop_production.csv",
        mime="text/csv"
     )

     st.download_button(
        label="⬇️ Download Crop Yield CSV",
        data=yield_df.to_csv(index=False),
        file_name="crop_yield.csv",
        mime="text/csv"
     )

     st.markdown("""
     <hr style="
     border: none;
     height: 6px;
     background: linear-gradient(to right, #8B0000, #B71C1C, #8B0000);
     border-radius: 20px;
     margin: 30px 0;
      ">
     """, unsafe_allow_html=True)

    # ---------------- Export Insights ----------------
     st.subheader("📝 Export Analytical Insights")

     insights = """
     🌾 Soybean has the highest average yield.
     📍 North region records the highest crop yield.
     🌱 Chalky soil is the most productive soil.
     ☀️ Sunny weather gives the highest yield.
     🌍 Kerala is the highest crop-producing state.
     🥈 Andhra Pradesh ranks second in production.
     🥥 Coconut is the highest-produced crop.
     🌾 Sugarcane is the second highest-produced crop.
     📈 2011 recorded the highest production.
     🌱 Whole Year season contributes maximum production.
     🌦️ Kharif is the highest seasonal producer.
     🌾 Rice and Wheat are the major staple crops.
     """
     st.markdown("""
     <style>

     /* Download Button */
     div.stDownloadButton > button {
     width: 100%;
     height: 55px;
     background: linear-gradient(90deg, #B71C1C, #D32F2F);
     color: white;
     font-size: 20px;
     font-weight: 700;
     border: none;
     border-radius: 12px;
     transition: 0.3s ease;
     box-shadow: 0px 4px 10px rgba(0,0,0,0.25);
     }

     /* Hover Effect */
     div.stDownloadButton > button:hover {
     background: linear-gradient(90deg, #8B0000, #B71C1C);
     transform: scale(1.02);
     color: white;
     }

     /* Click Effect */
     div.stDownloadButton > button:active {
     transform: scale(0.98);
     }

      </style>
      """, unsafe_allow_html=True)
     st.download_button(
        label="⬇️ Download Insights",
        data=insights,
        file_name="Analytical_Insights.txt",
        mime="text/plain"
     )

     st.markdown("""
     <hr style="
     border: none;
     height: 6px;
     background: linear-gradient(to right, #8B0000, #B71C1C, #8B0000);
     border-radius: 20px;
     margin: 30px 0;
      ">
     """, unsafe_allow_html=True)
      
     # ---------------- Dashboard Report ----------------
     st.subheader("📄 Dashboard Report")

     st.markdown("""
     <div style="
     background: linear-gradient(135deg,#FFF8E1,#FFECB3);
     border-left: 8px solid #B71C1C;
     padding:20px;
     border-radius:15px;
     box-shadow:0px 4px 12px rgba(0,0,0,0.2);
     font-size:18px;
     line-height:2;
     ">
     <h3 style="color:#B71C1C;">📊 AgriVision Dashboard Report</h3>

     ✅ Crop Production Analysis<br>
 
     ✅ Crop Yield Analysis<br>
 
     ✅ Hotspot Maps<br>

     ✅ Cultivation Area Analysis<br>

     ✅ Seasonal Production Analysis<br>

     ✅ Top Producing States<br>

     ✅ Correlation Analysis<br>

     ✅ Analytical Insights<br>

     <hr style="border:1px solid #B71C1C;">

     <b>Total Modules Covered:</b> 8<br>
     <b>Status:</b> ✔ Complete

     </div>
     """, unsafe_allow_html=True)

     st.markdown("""
     <style>
     div.stButton > button{
     width:100%;
     height:55px;
     font-size:22px;
     font-weight:bold;
     border-radius:12px;
     background:linear-gradient(90deg,#B71C1C,#D32F2F);
     color:white;
     border:none;
     }
     div.stButton > button:hover{
     background:linear-gradient(90deg,#8B0000,#B71C1C);
     color:white;
     }
     </style>
     """, unsafe_allow_html=True)

     if st.button("📥 Generate Dashboard Report"):
       st.success("✅ Dashboard Report Generated Successfully!")
       st.balloons()