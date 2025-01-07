import tkinter as tk
from tkinter import scrolledtext
from huggingface_hub import InferenceClient

client = InferenceClient(api_key="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")  # key

def send_message():
    user_input = prompt_input.get("1.0", tk.END).strip()
    if not user_input:
        response_display.insert(tk.END, "Please enter a prompt.\n")
        return

    # apicall
    messages = [{"role": "user", "content": user_input}]
    
    try:
        # send to hfmod
        completion = client.chat.completions.create(
            model="Qwen/Qwen2.5-72B-Instruct",  # model base
            messages=messages,
            max_tokens=500
        )
        # output display
        response = completion.choices[0].message["content"]
        response_display.insert(tk.END, f"User: {user_input}\nAI: {response}\n\n")
    except Exception as e:
        response_display.insert(tk.END, f"Error: {str(e)}\n")

# GUI
app = tk.Tk()
app.title("BeastGPT v0.1.2 - 15M Params")

# input box
tk.Label(app, text="Enter your prompt:").pack()
prompt_input = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=50, height=5)
prompt_input.pack(padx=10, pady=5)

# send button
send_button = tk.Button(app, text="Send", command=send_message)
send_button.pack(pady=5)

# display
tk.Label(app, text="Response:").pack()
response_display = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=50, height=15)
response_display.pack(padx=10, pady=5)

# app run
app.mainloop()
