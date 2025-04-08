# Restaurant_Bot
URL: https://huggingface.co/spaces/Nsain25/Restaurant_Bot

1. Project Overview
The goal of this project was to create a simple yet functional AI-powered restaurant chatbot.
Initially, we aimed to implement a more complex NLP-based solution using Hugging Face Transformers, but due to limitations of space build environments and resource constraints on Hugging Face Spaces, we opted for a rule-based chatbot using Python and Gradio. This pivot ensured smoother performance, ease of deployment, and minimal dependency requirements.
•	Provide an interactive and personalized chatbot for restaurant services.
•	Enable users to place orders and receive confirmations.
•	Collect essential information like name and address.
•	Maintain conversational flow using a rule-based approach.
•	Deploy publicly with an accessible URL.

3. Technologies Used
- Python 3
- Gradio (for UI)
- Hugging Face Spaces (for hosting)
- difflib (for future fuzzy matching)
3. Change in Plan: Explanation
The original plan was to use a large language model from Hugging Face's Transformers library to handle natural language queries. However, Hugging Face Spaces (free tier) often faces memory limitations and does not support running heavy ML models without significant setup. To ensure a smooth and accessible experience, we decided to build a rule-based chatbot that offers prompt-based responses, mimicking NLP-style interaction.

Issues Faced with ngrok and share=True
While testing the chatbot in a local setup with share=True:
•	No build logs appeared on Hugging Face Spaces.
•	No public URL was generated even after setting share=True
•	Errors like: “ To create a public link, set share=True in launch() “ continued to show up, despite already setting it.
•	Hugging Face's Space environment doesn’t need share=True, as it already exposes your app with a persistent public URL.

Realization & Pivot
•	After multiple attempts and rechecking the logs, we realized:
•	Hugging Face Spaces doesn't require or support share=True in the same way local environments do.
•	Spaces builds its own public link, independent of ngrok.
•	So we removed share=True to avoid misleading logs and fully shifted to Hugging Face Spaces for deployment.

Debugging Journey Summary
1.	No Logs Displayed:
→ Build logs remained empty when trying to deploy with share=True.
2.	No Public URL:
→ We expected a link from launch(share=True), which didn’t work in the Hugging Face environment.
3.	Restarted Space:
→ Still didn’t trigger build logs or expose a link.
4.	Checked App.py:
→ Code was valid, interface setup was correct.
5.	Final Fix:
→ Simply removed share=True and reloaded the Space. Hugging Face then generated a working public URL in the top-right corner of the interface.

4. Application Logic & Features
The chatbot provides:
- A friendly greeting and name recognition
- Options to view menu, get restaurant info (timing, location, contact)
- Menu ordering with context preservation
- Address collection and order confirmation
- Emoji-enhanced replies for better user experience
- Fully functional web interface using Gradio
- Remembers orders via user_order list.
- Response matching is done using keyword checks

5. Code Explanation (app.py)
- `responses`: A dictionary storing various response options
- `chatbot_response()`: Main function to handle and route user inputs
- Global variables: Used to store user name, order items, and address
- Gradio Interface: Defines input and output types and binds the chatbot function
- `iface.launch(share=True)`: Launches the app with public link (automatically handled by Hugging Face Spaces)

6. Deployment on Hugging Face Spaces
Steps followed:
1. Created a new Space on Hugging Face
2. Selected 'Gradio' as SDK
3. Uploaded `app.py` and `requirements.txt`
4. Committed changes and deployed
5. Hugging Face generated the public link automatically

Limitations
-	Rule-based: No NLP or intent classification.
-	No session persistence.
-	Not integrated with a real order management system or database.

7. Future Enhancements
- Integrate NLP models for better intent detection
- Add voice support and multilingual capability
- Connect with real-time backend for order processing
- Enable authentication and user accounts
- Add payment gateway integration
- Add LLM (like GPT-3.5) or intent classification for better understanding.
- Better web interface.

8. Conclusion
The AI-powered restaurant chatbot is a practical solution tailored for Hugging Face's resource limits. The use of Gradio allowed quick prototyping with an interactive frontend. With future upgrades, this project can be expanded into a fully intelligent restaurant assistant.
