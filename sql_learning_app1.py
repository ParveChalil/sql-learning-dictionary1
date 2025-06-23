{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "cc05005a-99d5-4b5c-a810-cac7830763ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "cfa60ea9-546f-4b7c-944d-af2029b2d91b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-23 17:15:37.297 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\ASUS\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-06-23 17:15:37.302 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Load the Excel dictionary\n",
    "df = pd.read_excel(\"SQL_Complete_Dictionary_A_to_Z.xlsx\")\n",
    "\n",
    "st.set_page_config(page_title=\"SQL Learning Dictionary\", layout=\"wide\")\n",
    "\n",
    "st.title(\"📘 SQL Learning Dictionary A–Z\")\n",
    "\n",
    "# Sidebar for filters\n",
    "st.sidebar.header(\"🔍 Filter Terms\")\n",
    "term_selected = st.sidebar.selectbox(\"Select SQL Term\", sorted(df['Term'].unique()))\n",
    "\n",
    "# Optional advanced filters\n",
    "command_filter = st.sidebar.multiselect(\"Filter by Category (e.g. DML, Function)\", df['Remark'].unique())\n",
    "\n",
    "# Filter data\n",
    "if command_filter:\n",
    "    filtered_df = df[df['Remark'].isin(command_filter) & (df['Term'] == term_selected)]\n",
    "else:\n",
    "    filtered_df = df[df['Term'] == term_selected]\n",
    "\n",
    "# Display selected term details\n",
    "for _, row in filtered_df.iterrows():\n",
    "    st.subheader(f\"📌 Term: `{row['Term']}`\")\n",
    "    st.markdown(f\"**Definition:** {row['Definition']}\")\n",
    "    st.markdown(f\"**Use Case:** {row['Use Case']}\")\n",
    "    st.markdown(f\"**Example:**\\n```sql\\n{row['Example']}```\")\n",
    "    st.markdown(f\"**Code:**\\n```sql\\n{row['Code']}```\")\n",
    "    st.info(f\"🔎 **Remark:** {row['Remark']}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e5c21976-7e94-45cf-acef-d391cfe2e585",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e8a84d9-151a-4a30-bfd7-3bfcdf7c2db1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba15509f-72b5-4639-af25-a0a79c9588f9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c709517-b569-4a1e-b097-5f0d31719e88",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f656f5bb-2bbb-4826-8056-72a58d0835ba",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
