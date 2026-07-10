import streamlit as st
from streamlit_option_menu import option_menu
with st.sidebar:
    opt=option_menu("Menu Bar",["📜Overview","📅Dataset","📁Upload & Preview","🧹Data cleaning","📊Data visualization","🗺Hotspots","💡Insights","📩Export"],icons=["Bar chart"],key="sidebar_menu")
if opt=="📜Overview":
   st.title("Agri-Vision Analysis🌾")
   import pandas as pd
   df=pd.read_csv("crop_production.csv")
   st.subheader("📍 District Wise Overview")
   col1, col2, col3, col4, col5 = st.columns(5)
   with col1:
    st.metric("Total Records", len(df))
   with col2:
    st.metric("Total Crops", df["Crop"].nunique())
   with col3:
    st.metric("Maximum Production","1.25B")
   with col4:
    st.metric("Total Columns", len(df.columns))
   with col5:
    st.metric("Total Districts", df["District_Name"].nunique())
   st.subheader("🌍 Region Wise Overview")
   df1=pd.read_csv("crop_yield.csv")
   col1, col2, col3, col4, col5 = st.columns(5)
   with col1:
    st.metric("Total Records", len(df1))
   with col2:
    st.metric("Total Crops",df1["Crop"].nunique())
   with col3:
    st.metric("Maximum Production",df1["Yield_tons_per_hectare"].max())
   with col4:
    st.metric("Total Columns", len(df1.columns))
   with col5:
    st.metric("Total Regions",df1["Region"].nunique())
    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go
    import streamlit as st
   
 # Read dataset
   df = pd.read_csv("crop_production.csv")
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
    title="🏆 Top 5 Districts by Production",
    plot_bgcolor="#FFFDE7",
    paper_bgcolor="#FFF8E1",
    template="plotly_white",   # Change to "plotly_white" if needed
    xaxis_title="Production",
    yaxis_title="District",
    height=550,
    hovermode="closest",
    font=dict(size=14),
    xaxis=dict(showgrid=True, gridcolor="gray"),
    yaxis=dict(showgrid=False),
    margin=dict(l=20, r=20, t=60, b=20))
   st.plotly_chart(fig, use_container_width=True)
   import streamlit as st
   import pandas as pd
   import plotly.express as px
   # Read dataset
   df = pd.read_csv("crop_yield.csv")
   # Top 5 crops with highest average yield
   top5 = (
     df.groupby("Crop", as_index=False)["Yield_tons_per_hectare"]
     .mean()
     .sort_values("Yield_tons_per_hectare", ascending=False)
     .head(5)
   )
   # Create vertical bar chart
   fig = px.bar(
     top5,
     x="Crop",
     y="Yield_tons_per_hectare",
     color="Yield_tons_per_hectare",
     color_continuous_scale="Turbo",
     text="Yield_tons_per_hectare",
     title="🌾 Top 5 Crops with Highest Yield (tons/hectare)")
  # Customize chart
   fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside",
    marker_line_color="black",
    marker_line_width=1.5
    )

   fig.update_layout(
     template="plotly_white",

     # Colorful graph background
     plot_bgcolor="#FFFDE7",      # Inside graph
     paper_bgcolor="#FFF8E1",     # Outside graph
     title={
        "text":"🌾 Top 5 Crops with Highest Yield (tons/hectare)",
        "x":0.5,
        "font":dict(size=22)
    },

    xaxis_title="Crop",
    yaxis_title="Yield (tons/hectare)",

    height=550,

    xaxis=dict(showgrid=False,tickangle=-20 ),
    yaxis=dict(showgrid=True, gridcolor="white"),

    font=dict(size=14),
    coloraxis_showscale=False
)
   st.plotly_chart(fig, use_container_width=True)
   import streamlit as st
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
elif opt=="📅Dataset":
  button=st.radio("Select Datset",["District-wise dataset","Region-Wise dataset"],index=None,key="dataset_radio")
  import pandas as pd
  if button== "District-wise dataset":
      df=pd.read_csv("crop_production.csv")
  else:
     df=pd.read_csv("crop_yield.csv")
  t1,t2,t3=st.tabs(["Dataset Summary","dataset columns","dataset value_counts"])
  with t1:
    st.title("Data-set")
    st.write(df.columns)
  with t2:
    st.title("Columns")
    st.write(df.head(10))
  with t3:
    st.title("Information")
    st.write(df.value_counts())
elif opt=="📁Upload & Preview":
 st.title("Dataset Analysis Dashboard")
 file = st.file_uploader("Upload CSV File", type=["csv"])
 if file is not None:
    import pandas as pd
    df = pd.read_csv(file)
 st.title("Dataset Summary")
 rows = df.shape[0]
 cols = df.shape[1]
 missing = df.isnull().sum().sum()
 duplicates = df.duplicated().sum()
 c1, c2, c3, c4 = st.columns(4)
 c1.metric("Rows", rows)
 c2.metric("Columns", cols)
 c3.metric("Missing Values", missing)
 c4.metric("Duplicates", duplicates)
 rows_show = st.slider(
    "Rows to Preview",
    min_value=5,
    max_value=100,
    value=10)
 t1, t2, t3 = st.tabs(["Preview", "Columns Info", "Null values"])
 with t1:
    st.dataframe(df.head(rows_show))
 with t2:
    st.write(df.columns)
 with t3:
    column = st.selectbox("Select Column", df.columns)
    st.write(df[column].isnull().sum())
#for data cleaning 
elif opt=="🧹Data cleaning":
 import pandas as pd
 df=pd.read_csv("crop_production.csv")
 st.subheader("🧹Data Cleaning")
# Original Report
 col1, col2, col3 = st.columns(3)
 with col1:
    st.metric("Original Rows", len(df))
 with col2:
    st.metric("Missing Values", df["Production"].isnull().sum())
 with col3:
    st.metric("Duplicate Rows", df.duplicated().sum())
 st.write("---")
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
    st.dataframe(clean_df.head())
elif opt=="📊Data visualization":
   st.set_page_config(page_title="Agriculture Dashboard",layout="wide")
   t1,t2,t3,t4=st.tabs(["By production","By year","correlation","comparisons"])
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
     title="Rainfall vs Production for Different Crops")
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
     color_discrete_sequence=px.colors.qualitative.Set2)
     fig21.update_layout(width=700,height=700)
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
     palette="viridis",
     ax=ax)
     ax.set_xlabel("Season", fontsize=12)
     ax.set_ylabel("Number of Counts", fontsize=12)
     ax.set_title("Season vs Crop", fontsize=15)
     ax.legend(title="Crop", loc="upper left", bbox_to_anchor=(1, 1))
     sns.set_style("darkgrid")
     st.pyplot(fig21)
     
    
 
   with t2:
     df = pd.read_csv("crop_production.csv")
     df2 = pd.read_csv("crop_yield.csv")
     year_df=(df.head(5).groupby(["Crop_Year","Crop"],as_index=False)["Production"].sum().head(5))
     df=pd.read_csv("crop_production.csv")
     import plotly.express as px
     year_df = (
     df.groupby(["Crop_Year", "Crop"], as_index=False)["Production"]
     .sum())
     fig12 = px.line(year_df,x="Crop_Year",y="Production",color="Crop",markers=True,title="Crop Production by Year",hover_data=["Crop", "Production"],log_y=True)
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
     title_x=0.5,
     font=dict(size=14))

     # Make boundary line thicker
     fig.update_traces(
     line=dict(width=3),
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
     color_discrete_sequence=px.colors.qualitative.Set1)

     fig21.update_layout(
     xaxis_title="Crop Year",
     yaxis_title="Number of Crop Types",
     template="plotly_white",
     title_x=0.5,
     legend_title="Season")

     st.plotly_chart(fig21, use_container_width=True)
   with t3:
     import plotly.express as px
     corr_df = df2[
    ["Rainfall_mm", "Temperature_Celsius", "Yield_tons_per_hectare", "Days_to_Harvest"]]

     # Correlation matrix
     corr_matrix = corr_df.corr()

     # Heatmap
     fig13 = px.imshow(
     corr_matrix,
     text_auto=".2f",                # Correlation values show karega
     color_continuous_scale="Viridis",  # Attractive Red-Yellow-Green colors
     title="Correlation Heatmap",
     aspect="auto")
     fig13.update_layout(title_x=0.5,width=700,height=600,font=dict(size=14))
     st.plotly_chart(fig13, use_container_width=True)

   with t4:
     df = pd.read_csv("crop_production.csv")
     df2 = pd.read_csv("crop_yield.csv")
     col1, col2 = st.columns(2)
     with col1:
         rice_df = df[df["Crop"] == "Rice"]       #rice prodcution in district
         district_data = (
         rice_df.groupby(["District_Name", "Season"])["Production"]
         .sum()
         .reset_index())
         district_data=district_data.sort_values(
         by="Production",
         ascending=False
         ).head(10)
         fig4 = px.bar(
         district_data,
         x="District_Name",
         y="Production",
         color="Season",
         color_discrete_sequence=px.colors.qualitative.Set2,
         title="Rice Production District Wise",
         hover_data=["Season", "Production"])
         st.plotly_chart(fig4)
         import plotly.express as px
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
         color_discrete_sequence=px.colors.qualitative.Set2,
         title="Top 10 Districts by Maize Production")
         fig4.update_layout(height=450,margin=dict(l=20,r=20,t=40,b=20))
         st.plotly_chart(fig4, use_container_width=False)
         import plotly.express as px
         wheat_df = df[df["Crop"] == "Wheat"].head(100)     #wheat production in district
         fig6 = px.pie(
         wheat_df,
         names="District_Name",          
         values="Production",
         title="District-wise Wheat Production",
         color="District_Name",
         color_discrete_sequence=px.colors.qualitative.Set2)
         fig6.update_layout(height=350,margin=dict(l=10,r=10,t=40,b=10))
         st.plotly_chart(fig6) 
         with col2:
             rice_df = df2[df2["Crop"] == "Rice"]         #rice production in region
             region_data = (
             rice_df.groupby(["Region", "Weather_Condition"])["Yield_tons_per_hectare"]
             .sum()
             .reset_index())
             fig3 = px.bar(
             region_data,                             
             x="Region",
             y="Yield_tons_per_hectare",
             title="Rice Yield Region Wise",
             color="Weather_Condition",
             color_discrete_sequence=px.colors.qualitative.Set2,
             hover_data=["Weather_Condition", "Yield_tons_per_hectare"],
             log_y=True)
             st.plotly_chart(fig3)
             import plotly.express as px
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
              color_discrete_sequence=px.colors.qualitative.Set2,
             title="Region by Maize Production")
             st.plotly_chart(fig3, use_container_width=False)
             df2 = pd.read_csv("crop_yield.csv")    #wheat  production in region
             wheat_df2 = df2[df2["Crop"] == "Wheat"]
             fig7 = px.pie(
             wheat_df2,
             names="Region",          
             values="Yield_tons_per_hectare",
             title="Region-wise Wheat Production",
             color="Region",
              color_discrete_sequence=px.colors.qualitative.Set2)
             st.plotly_chart(fig7)  
elif opt=="🗺Hotspots":
     st.set_page_config(layout="wide")
     import pandas as pd
     df = pd.read_csv("crop_production.csv")
     df2 = pd.read_csv("crop_yield.csv")
     import streamlit as st
     import pandas as pd
     import plotly.express as px
     import streamlit as st
# ---------------- Title ----------------
     st.title("Hotspots through Map")
# ---------------- Read Dataset ----------------
     df = pd.read_csv("crop_production.csv")
     df["State_Name"] = df["State_Name"].str.strip()
# ---------------- Sidebar ----------------
     st.sidebar.header("Hotspot Filters")
# Crop Multiselect (Rice selected by default)
     crop_list = sorted(df["Crop"].dropna().unique())
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
# ---------------- State Coordinates ----------------
     state_coords = pd.DataFrame({
     "State_Name": [
        "Punjab",
        "Haryana",
        "Uttar Pradesh",
        "West Bengal",
        "Andhra Pradesh",
        "Tamil Nadu"
     ],
     "Latitude": [
        31.15,
        29.06,
        26.85,
        22.98,
        15.91,
        11.13
     ],
     "Longitude": [
        75.34,
        76.09,
        80.95,
        87.85,
        79.74,
        78.66
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
     coloraxis_colorbar=dict(title="Cultivated Area")
    )
     st.plotly_chart(fig_area, use_container_width=True)
     import streamlit as st
     import pandas as pd
     import plotly.express as px
     st.title("🌾 Season-wise Crop Production Across Indian States")
     df["Season"]=df["Season"].str.strip()
# ---------------- Season Selectbox ----------------
     season_options = [
     "Kharif",
     "Whole Year",
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
    ],
     "Latitude": [
        11.74,
        15.91,
        28.22,
        26.20,
        25.09,
        30.73,
        21.28,
        20.18,
        15.30,
        22.26,
        29.06,
        31.10,
        23.61,
        15.32,
        10.85,
        23.47,
        19.75,
        24.66,
        25.57,
        23.16,
    ],
     "Longitude": [
        92.66,
        79.74,
        94.73,
        92.93,
        85.31,
        76.78,
        81.86,
        73.02,
        74.12,
        71.19,
        76.09,
        77.17,
        85.28,
        75.71,
        76.27,
        77.95,
        75.71,
        93.91,
        91.88,
        92.94,
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
        "Uttarakhand"
    ],

    "Latitude": [
        11.74, 15.91, 28.22, 26.20, 25.09, 30.73,
        21.28, 20.18, 15.30, 22.26, 29.06, 31.10,
        23.61, 15.32, 10.85, 23.47, 19.75, 24.66,
        25.57, 23.16, 26.16, 20.95, 11.94, 31.15,
        27.02, 27.53, 11.13, 23.94, 26.85, 30.07
    ],

    "Longitude": [
        92.66, 79.74, 94.73, 92.93, 85.31, 76.78,
        81.86, 73.02, 74.12, 71.19, 76.09, 77.17,
        85.28, 75.71, 76.27, 77.95, 75.71, 93.91,
        91.88, 92.94, 94.56, 85.10, 79.81, 75.34,
        74.22, 88.51, 78.66, 91.99, 80.95, 79.02
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
     title_x=0.02
     )

# ---------------- Display ----------------
     st.plotly_chart(fig, use_container_width=True)
elif opt=="💡Insights":
    import streamlit as st
# ---------- Heading ----------
    st.markdown(
     '<div class="Insights-title">📊 ANALYTICAL INSIGHTS</div>',
     unsafe_allow_html=True
     )

# ---------- Big Generate Insights Button ----------
    generate = st.button("✨ Generate Insights", use_container_width=True)

# ---------- Display Insights Only After Button Click ----------
    if generate:
     st.subheader("🔍 Key Findings")
     Insights = [
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
     for item in Insights:
         st.info(item)
else:
     import streamlit as st
     import pandas as pd

     st.title("📤 Export Dashboard")

     st.markdown("""
     ### Download your analysis results and reports.

     Export filtered datasets, analytical insights, and dashboard reports
     for future reference.
     """)

    # Read datasets
     production_df = pd.read_csv("crop_production.csv")
     yield_df = pd.read_csv("crop_yield.csv")

     st.divider()

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

     st.divider()

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

     st.download_button(
        label="⬇️ Download Insights",
        data=insights,
        file_name="Analytical_Insights.txt",
        mime="text/plain"
     )

     st.divider()

    # ---------------- Dashboard Report ----------------
     st.subheader("📄 Dashboard Report")

     st.info("""
     ✔ Crop Production Analysis

     ✔ Crop Yield Analysis

     ✔ Hotspot Maps

     ✔ Cultivation Area Analysis

     ✔ Seasonal Production Analysis

     ✔ Top Producing States

     ✔ Correlation Analysis

     ✔ Analytical Insights
     """)

     if st.button("📥 Generate Report"):
        st.success("✅ Dashboard Report Generated Successfully!")
        st.balloons()