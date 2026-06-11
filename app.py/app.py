{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "749ed876-82b7-49c4-98c3-e04892994a9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-06-08 08:07:34.831 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:36.695 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\HP\\AppData\\Roaming\\Python\\Python313\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-06-08 08:07:36.698 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:36.700 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:36.702 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:36.703 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:36.704 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:36.705 No runtime found, using MemoryCacheStorageManager\n",
      "2026-06-08 08:07:36.707 No runtime found, using MemoryCacheStorageManager\n",
      "2026-06-08 08:07:36.708 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:36.709 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:36.710 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:36.711 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:37.214 Thread 'Thread-3': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:37.221 Thread 'Thread-3': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:37.223 Thread 'Thread-3': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:40.387 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:40.389 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-06-08 08:07:40.391 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "ename": "KeyError",
     "evalue": "'label'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\anaconda4\\Lib\\site-packages\\pandas\\core\\indexes\\base.py:3812\u001b[39m, in \u001b[36mIndex.get_loc\u001b[39m\u001b[34m(self, key)\u001b[39m\n\u001b[32m   3811\u001b[39m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[32m-> \u001b[39m\u001b[32m3812\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_engine\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget_loc\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcasted_key\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   3813\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err:\n",
      "\u001b[36mFile \u001b[39m\u001b[32mpandas/_libs/index.pyx:167\u001b[39m, in \u001b[36mpandas._libs.index.IndexEngine.get_loc\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mpandas/_libs/index.pyx:196\u001b[39m, in \u001b[36mpandas._libs.index.IndexEngine.get_loc\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mpandas/_libs/hashtable_class_helper.pxi:7088\u001b[39m, in \u001b[36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mpandas/_libs/hashtable_class_helper.pxi:7096\u001b[39m, in \u001b[36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[39m\u001b[34m()\u001b[39m\n",
      "\u001b[31mKeyError\u001b[39m: 'label'",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[31mKeyError\u001b[39m                                  Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 28\u001b[39m\n\u001b[32m     24\u001b[39m \u001b[38;5;66;03m# ---------------------------\u001b[39;00m\n\u001b[32m     25\u001b[39m \u001b[38;5;66;03m# Train model\u001b[39;00m\n\u001b[32m     26\u001b[39m \u001b[38;5;66;03m# ---------------------------\u001b[39;00m\n\u001b[32m     27\u001b[39m X = df[\u001b[33m\"\u001b[39m\u001b[33mtext\u001b[39m\u001b[33m\"\u001b[39m]\n\u001b[32m---> \u001b[39m\u001b[32m28\u001b[39m y = \u001b[43mdf\u001b[49m\u001b[43m[\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mlabel\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m]\u001b[49m\n\u001b[32m     30\u001b[39m X_train, X_test, y_train, y_test = train_test_split(\n\u001b[32m     31\u001b[39m     X, y, test_size=\u001b[32m0.2\u001b[39m, random_state=\u001b[32m42\u001b[39m\n\u001b[32m     32\u001b[39m )\n\u001b[32m     34\u001b[39m vectorizer = TfidfVectorizer(stop_words=\u001b[33m\"\u001b[39m\u001b[33menglish\u001b[39m\u001b[33m\"\u001b[39m, max_df=\u001b[32m0.7\u001b[39m)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\anaconda4\\Lib\\site-packages\\pandas\\core\\frame.py:4113\u001b[39m, in \u001b[36mDataFrame.__getitem__\u001b[39m\u001b[34m(self, key)\u001b[39m\n\u001b[32m   4111\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m.columns.nlevels > \u001b[32m1\u001b[39m:\n\u001b[32m   4112\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m._getitem_multilevel(key)\n\u001b[32m-> \u001b[39m\u001b[32m4113\u001b[39m indexer = \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mcolumns\u001b[49m\u001b[43m.\u001b[49m\u001b[43mget_loc\u001b[49m\u001b[43m(\u001b[49m\u001b[43mkey\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   4114\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m is_integer(indexer):\n\u001b[32m   4115\u001b[39m     indexer = [indexer]\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\anaconda4\\Lib\\site-packages\\pandas\\core\\indexes\\base.py:3819\u001b[39m, in \u001b[36mIndex.get_loc\u001b[39m\u001b[34m(self, key)\u001b[39m\n\u001b[32m   3814\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(casted_key, \u001b[38;5;28mslice\u001b[39m) \u001b[38;5;129;01mor\u001b[39;00m (\n\u001b[32m   3815\u001b[39m         \u001b[38;5;28misinstance\u001b[39m(casted_key, abc.Iterable)\n\u001b[32m   3816\u001b[39m         \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28many\u001b[39m(\u001b[38;5;28misinstance\u001b[39m(x, \u001b[38;5;28mslice\u001b[39m) \u001b[38;5;28;01mfor\u001b[39;00m x \u001b[38;5;129;01min\u001b[39;00m casted_key)\n\u001b[32m   3817\u001b[39m     ):\n\u001b[32m   3818\u001b[39m         \u001b[38;5;28;01mraise\u001b[39;00m InvalidIndexError(key)\n\u001b[32m-> \u001b[39m\u001b[32m3819\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m(key) \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01merr\u001b[39;00m\n\u001b[32m   3820\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m:\n\u001b[32m   3821\u001b[39m     \u001b[38;5;66;03m# If we have a listlike key, _check_indexing_error will raise\u001b[39;00m\n\u001b[32m   3822\u001b[39m     \u001b[38;5;66;03m#  InvalidIndexError. Otherwise we fall through and re-raise\u001b[39;00m\n\u001b[32m   3823\u001b[39m     \u001b[38;5;66;03m#  the TypeError.\u001b[39;00m\n\u001b[32m   3824\u001b[39m     \u001b[38;5;28mself\u001b[39m._check_indexing_error(key)\n",
      "\u001b[31mKeyError\u001b[39m: 'label'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "# ---------------------------\n",
    "# Title\n",
    "# ---------------------------\n",
    "st.title(\"📰 Fake News Detection App\")\n",
    "st.write(\"Enter a news article and check whether it's REAL or FAKE.\")\n",
    "\n",
    "# ---------------------------\n",
    "# Load dataset\n",
    "# ---------------------------\n",
    "@st.cache_data\n",
    "def load_data():\n",
    "    df = pd.read_csv(\"News.csv\")\n",
    "    df = df.fillna(\"\")\n",
    "    return df\n",
    "\n",
    "df = load_data()\n",
    "\n",
    "# ---------------------------\n",
    "# Train model\n",
    "# ---------------------------\n",
    "X = df[\"text\"]\n",
    "y = df[\"label\"]\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X, y, test_size=0.2, random_state=42\n",
    ")\n",
    "\n",
    "vectorizer = TfidfVectorizer(stop_words=\"english\", max_df=0.7)\n",
    "X_train_tfidf = vectorizer.fit_transform(X_train)\n",
    "\n",
    "model = LogisticRegression()\n",
    "model.fit(X_train_tfidf, y_train)\n",
    "\n",
    "# ---------------------------\n",
    "# User input\n",
    "# ---------------------------\n",
    "user_input = st.text_area(\"✍️ Enter News Text Here:\")\n",
    "\n",
    "if st.button(\"Check News\"):\n",
    "    if user_input.strip() == \"\":\n",
    "        st.warning(\"Please enter some text.\")\n",
    "    else:\n",
    "        input_vector = vectorizer.transform([user_input])\n",
    "        prediction = model.predict(input_vector)\n",
    "\n",
    "        if prediction[0] == 1:\n",
    "            st.success(\"✅ REAL NEWS\")\n",
    "        else:\n",
    "            st.error(\"🚨 FAKE NEWS\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8a0334d-9511-4be7-a2cd-b9bb661362e1",
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
