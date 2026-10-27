$ cat serajul_web.py                            from flask import Flask, render_template_string, request                                                                                              app = Flask(__name__)

# হোম পেজের ডিজাইন এবং ইনপুট ফর্ম
html_template = """
<!DOCTYPE html>
<html>                                            <head>                                                <meta charset="UTF-8">
    <title>Serajul AI Studio</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #0f172a; color: #fff; text-align: center; padding: 50px; }                                   .container { background: #1e293b; padding: 30px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
        input[type="text"] { width: 80%; padding: 10px; margin: 10px 0; border-radius: 5px; border: none; font-size: 16px; }                                  input[type="submit"] { background: #3b82f6; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; cursor: pointer; }
        input[type="submit"]:hover { background: #2563eb; }
        .result { margin-top: 20px; color: #38bdf8; font-size: 18px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🌟 Serajul AI Studio 🌟</h2>
        <p>প্রোপ্রাইটর / ক্রিয়েটর: সেরাজুল ইসলাম | কোচবিহার</p>
        <hr style="border: 0.5px solid #334155;">
        <form method="POST">
            <label>আপনার প্রম্পট বা আইডিয়া লিখুন:</label><br>
            <input type="text" name="prompt" placeholder="যেমন: A beautiful village in Cooch Behar" required><br>
            <input type="submit" value="জেনারেট করুন">
        </form>
        {% if user_prompt %}
            <div class="result">
                <p><strong>আপনার প্রম্পট:</strong> {{ user_prompt }}</p>
                <p>🎨 <em>স্ট্যাটাস: সফল! আপনার এআই প্রসেসিং কাজ করছে।</em></p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    user_prompt = None
    if request.method == 'POST':
        user_prompt = request.form.get('prompt')
    return render_template_string(html_template, user_prompt=user_prompt)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
~ $
