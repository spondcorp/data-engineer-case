import streamlit as st
import os
import pandas as pd
import glob


st.title("Spond Data Analytics")

output_dir_path = os.path.join("output")

daily_active_teams_data_path = os.path.join(output_dir_path, "daily_active_teams")

csv_files = glob.glob(os.path.join(daily_active_teams_data_path, "*.csv"))

df_list = [pd.read_csv(file) for file in csv_files]

combined_df = pd.concat(df_list, ignore_index=True)

st.dataframe(combined_df)

st.write("Daily Active Teams Data")
chart_data = combined_df.set_index("event_date")
st.bar_chart(chart_data, use_container_width=True)

# TODO: Enable pages to display different charts
# TODO: Error handling
