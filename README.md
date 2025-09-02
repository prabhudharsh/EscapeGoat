<div align="center">
<br />
<img src="landing-logo.png" alt="escapeGoat Logo" width="80">
<h1 align="center">escapeGoat</h1>
<p align="center">
<strong>Your Strategic Communications Assistant.</strong>
<br />
AI-powered alibis for navigating the com plexities of modern social and professional challenges.
</p>
<br />
</div>

Concept
In a world that demands constant availability, navigating expectations can be challenging. escapeGoat is a sophisticated web application that leverages the power of generative AI to serve as a discreet and powerful ally. It helps users craft, analyze, and manage plausible explanations for complex situations where the stakes are high and clarity is critical. It moves beyond a simple generator to become a complete toolkit for strategic communication, featuring a sleek, minimalist interface designed to facilitate clear thinking under pressure.

<br>

Core Features
Excuse Studio: The core of the application where users generate tailored alibis. Go beyond simple inputs by selecting from categories like Late for Work or Missed Deadline and choosing a specific style—Professional for formal environments, Casual for low-stakes social settings, or Bulletproof for scenarios requiring an airtight explanation that preemptively considers edge cases.

Delivery Toolkit: An excuse is only as good as its delivery. This feature allows you to instantly rewrite any alibi with a new tone (Sincere, Urgent, Humorous) or, more importantly, stress-test it. The integrated "Skeptic" AI provides a list of challenging follow-up questions, allowing you to anticipate scrutiny and build unshakeable confidence in your story.

Alibi Vault: A secure, private library to save, categorize, and manage your most effective excuses. Over time, this becomes a personalized playbook, helping you recognize patterns and understand which communication strategies are most effective within your specific social and professional circles.

Scenario Simulator: (Coming Soon) A conversational AI training ground to practice delivering your alibi. This feature will act as a "dojo" for your communication skills, pitting you against a variety of AI-powered personalities to ensure you're prepared for any real-world conversation.

<br>

Tech Stack
Component

Technology

Backend

<img src="https://www.google.com/search?q=https://i.imgur.com/j2aM2sP.png" alt="Flask" width="16" /> Flask

AI Engine

<img src="https://www.google.com/search?q=https://i.imgur.com/k28V7fJ.png" alt="Gemini" width="16" /> Google Gemini API (1.5 Flash)

Frontend

<img src="https://www.google.com/search?q=https://i.imgur.com/YhPyw5b.png" alt="JS" width="16" /> HTML • CSS • Vanilla JavaScript

Deployment

Python 3.x

<br>

Getting Started
Follow these steps to get a local copy of the application up and running on your machine.

Prerequisites
Python 3.8+

A Google Gemini API Key obtained from Google AI Studio.

Installation
Clone the repository:

git clone [https://github.com/your-username/escapeGoat.git](https://github.com/your-username/escapeGoat.git)
cd escapeGoat

Create and activate a virtual environment:

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

Install the required packages from requirements.txt:

pip install -r requirements.txt

Configure your environment:

Create a file named .env in the root of the project.

Add your Google Gemini API key to this file:

GENAI_API_KEY=YOUR_API_KEY_HERE

Run the application:

python app.py

The application will be available at http://127.0.0.1:5000.

<div align="center">
<p>Built for the modern professional landscape. Navigate life's conversations with confidence.</p>
</div>
