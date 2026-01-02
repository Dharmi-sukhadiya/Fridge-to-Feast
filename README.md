# 🥦 Fridge-to-Feast

**Turn your leftovers into gourmet meals instantly using AI Vision.**

## 💡 Inspiration
We've all been there: staring at an open fridge full of random ingredients, having zero idea what to cook, and ending up ordering expensive takeout. **Fridge-to-Feast** solves this by using AI to "see" your ingredients and generate recipes instantly.

## 🚀 Key Features
*   **📸 AI Vision:** Snap a photo of your fridge, and the AI identifies every ingredient.
*   **👨‍🍳 Personalized Recipes:** Gets recipes based *only* on what you have.
*   **🔥 Gordon Ramsay Mode:** A unique "Roast & Toast" feature where the AI roasts your sad fridge contents before helping you cook. (Judges love this!)
*   **⚡ Blazing Fast:** Powered by Google Gemini 1.5 Flash for instant results.

## 🛠️ Tech Stack
*   **Language:** Python
*   **Frontend:** Streamlit
*   **AI Model:** Google Gemini 1.5 Flash (via Google Gen AI SDK)
*   **Computer Vision:** PIL (Python Imaging Library)

## 💻 How to Run This Project locally

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Dharmi-sukhadiya/Fridge-to-Feast.git
    cd Fridge-to-Feast
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your API Key**
    *   Get a free API Key from [Google AI Studio](https://aistudio.google.com/).
    *   Create a new file named `.env` in the main folder.
    *   Add your key inside:
        ```
        GOOGLE_API_KEY=your_actual_api_key_here
        ```

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```

## 🏆 Hackathon Goal
Built to reduce food waste and make cooking fun and accessible for everyone.

*Made with ❤️ and Python.*
