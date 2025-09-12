# Goal: Set up your development environment and authenticate to the Google AI service.

## Step 1: Installing the SDK

First, you need to install the `google-generativeai` library, which is the official Software Development Kit (SDK) for Python. The best practice is to do this inside a "virtual environment" to avoid conflicts with other Python projects.

### **1a. Create a Project Folder and Virtual Environment**

Open your terminal or command prompt and run these commands:

```bash
# Create a new folder for your project and move into it
mkdir gemini-project
cd gemini-project

# Create a virtual environment (e.g., named "venv")
# On macOS/Linux
python3 -m venv venv

# On Windows
python -m venv venv
```

### **1b. Activate the Virtual Environment**

You must activate the environment before installing anything.

```bash
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

Your terminal prompt should now change to show `(venv)` at the beginning, indicating the environment is active.

### **1c. Install the SDK**

Now, use `pip` (Python's package installer) to install the library.

```bash
pip install google-generativeai
```

That's it\! The SDK is now installed in your isolated project environment.

## Step 2: Getting an API Key from Google AI Studio

To use the model, your code needs to authenticate with an API key. This is a secret credential that proves you have permission to make requests.

### **2a. Go to Google AI Studio**

Open your web browser and navigate to **[https://aistudio.google.com/](https://aistudio.google.com/)**. You will need to sign in with your Google account.

**2b. Generate the API Key**

1.  Once you are in Google AI Studio, look for a button or menu item on the left that says **"Get API key"**. Click on it.
2.  You will be taken to a page where you can manage your API keys. Click the button that says **"Create API key in new project"**.
3.  A new API key will be generated for you. It will be a long string of random characters.

### **2c. Copy and Secure Your Key**

  * **Copy the key immediately.**
  * **IMPORTANT:** Treat this API key like a password. Do not share it publicly or commit it to a public code repository like GitHub. Store it in a secure location, like a password manager.

## Step 3: Configuring the API Key in Python

Now we will write Python code to use the key you just created. There are two main ways to do this: a simple way for testing, and a more secure way for real projects.

### **Method A: The Simple Way (for quick tests)**

This method involves putting your key directly into the code. It's fine for a quick test, but **not recommended for real applications**.

1.  Create a new Python file, e.g., `test_gemini.py`.
2.  Write the following code, pasting your API key where indicated.

<!-- end list -->

```python
import google.generativeai as genai

# WARNING: Do not do this in production code.
# This is for quick testing only.
genai.configure(api_key="PASTE_YOUR_API_KEY_HERE")

# Now you can use the model
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Explain the importance of API keys in one sentence.")

print(response.text)
```

### **Method B: The Secure & Recommended Way (Using Environment Variables)**

This method keeps your secret API key out of your source code. The code reads the key from your computer's "environment".

#### **3a. Set the Environment Variable**

First, you need to tell your terminal session what the key is. Close your Python script for now and go back to your terminal (make sure your virtual environment is still active).

```bash
# On macOS/Linux
export GOOGLE_API_KEY="PASTE_YOUR_API_KEY_HERE"

# On Windows (Command Prompt)
set GOOGLE_API_KEY="PASTE_YOUR_API_KEY_HERE"

# On Windows (PowerShell)
$env:GOOGLE_API_KEY="PASTE_YOUR_API_KEY_HERE"
```

**Note:** This environment variable only lasts for your current terminal session. If you close the terminal, you'll need to set it again.

#### **3b. Write the Python Code**

Now, create or modify your Python file (`test_gemini.py`) to read the key from the environment.

```python
import os
import google.generativeai as genai

# The secure way to configure the API key.
# The SDK will automatically look for the GOOGLE_API_KEY environment variable.
# Or you can explicitly load it like this:
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Check if the API key was found
if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set. Please set the environment variable.")

# Now you can use the model
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Explain the importance of API keys in one sentence.")

print("--- Gemini Response ---")
print(response.text)
print("-----------------------")
```

## ✅ Final Check

Run your Python script from the terminal where you set the environment variable:

```bash
python test_gemini.py
```

If everything is set up correctly, you will see a response from the Gemini model printed to your console, like this:

```
--- Gemini Response ---
API keys are essential for authenticating and authorizing application access to a service, ensuring secure and controlled usage.
-----------------------
```

**Congratulations\!** You have successfully installed the SDK, obtained an API key, and authenticated from your Python environment. You are now ready to start building with the Google AI SDK.