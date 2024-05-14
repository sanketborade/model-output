{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7e91cbb9-c83d-48ee-9c70-49a8ebb50579",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overwriting deploy.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile deploy.py\n",
    "\n",
    "import streamlit as st\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "# Define the accuracy data\n",
    "data = {\n",
    "    'Model': ['DBSCAN', 'HDBSCAN', 'KMeans', 'Local Outlier Factor', 'One-Class SVM', 'Isolation Forest'],\n",
    "    'Accuracy': [0.8303926940639269, 0.7082009132420092, 0.074337899543379, 0.16960730593607307, 0.21968949771689497, 1.0]\n",
    "}\n",
    "\n",
    "# Create a DataFrame from the data\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# Display the DataFrame using Streamlit\n",
    "st.title('Model Accuracy Comparison')\n",
    "st.dataframe(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04cb7d84-386c-4047-a8ed-79dc95d93ac4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
