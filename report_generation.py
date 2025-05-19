import pandas as pd
from jinja2 import Template
from datetime import datetime

# Load predictions.csv
df = pd.read_csv("predictions.csv")

# Basic stats
total_records = len(df)
attack_count = df["prediction"].value_counts().get(1, 0)
benign_count = df["prediction"].value_counts().get(0, 0)

# Extract hour if timestamp is available
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
else:
    df["hour"] = datetime.now().hour

attack_by_hour = df[df["prediction"] == 1]["hour"].value_counts().sort_index()
top_protocols = df[df["prediction"] == 1]["proto"].value_counts().head(5)

# HTML Template
template = Template("""
<h2>📄 Intrusion Detection Report</h2>
<p><strong>Date:</strong> {{ date }}</p>
<p><strong>Total Records:</strong> {{ total }}</p>
<p><strong>Attack Records:</strong> {{ attack }}</p>
<p><strong>Benign Records:</strong> {{ benign }}</p>

<h3>⏰ Attacks by Hour</h3>
<ul>
{% for hour, count in attack_by_hour.items() %}
  <li><strong>{{ hour }}:00</strong> → {{ count }} attacks</li>
{% endfor %}
</ul>

<h3>📡 Top Protocols Used in Attacks</h3>
<ul>
{% for proto, count in top_protocols.items() %}
  <li><strong>Protocol {{ proto }}</strong>: {{ count }} times</li>
{% endfor %}
</ul>
""")

# Render report
html_report = template.render(
    date=datetime.now().strftime("%Y-%m-%d"),
    total=total_records,
    attack=attack_count,
    benign=benign_count,
    attack_by_hour=attack_by_hour.to_dict(),
    top_protocols=top_protocols.to_dict()
)

# Save as HTML
with open("intrusion_report.html", "w") as f:
    f.write(html_report)

print("✅ Report generated: intrusion_report.html")
