# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
# # Define the tasks and weeks for each sprint
# data = [
#     # Sprint 1
#     ("Build basic frontend UI", 1, 2),
#     ("Implement REST API", 1, 2),
#     ("Select medical QnA dataset", 1, 2),
#     ("Test keyword extraction methods", 1, 2),
#     ("Structure dataset for T5 training", 2, 2),
#     # Sprint 2
#     ("Finalize keyword extraction strategy", 3, 4),
#     ("Generate full training dataset", 3, 4),
#     ("Polish REST API interactions", 3, 4),
#     ("Document system architecture", 3, 4),
#     ("Prepare midterm deliverables", 3, 4),
#     # Sprint 3
#     ("Train models on keyword dataset", 5, 6),
#     ("Create model inference pipeline", 5, 6),
#     ("Refactor backend for model integration", 5, 6),
#     ("Update frontend for model output", 5, 6),
#     ("Evaluate model performance", 5, 6),
#     # Sprint 4
#     ("Enhance frontend UI", 7, 8),
#     ("Conduct integration testing", 7, 8),
#     ("Finalize backend-model response format", 7, 8),
#     ("Write final project report", 7, 8),
#     ("Prepare final demo", 7, 8)
# ]

# # Create DataFrame
# df = pd.DataFrame(data, columns=["Task", "Start Week", "End Week"])
# df.head()




# # Setup plot
# fig, ax = plt.subplots(figsize=(12, 8))

# # Colors for different sprints
# colors = {1: "#6baed6", 2: "#9ecae1", 3: "#c6dbef", 4: "#deebf7"}

# # Plot each task as a horizontal bar
# for i, row in df.iterrows():
#     sprint = (row["Start Week"] - 1) // 2 + 1
#     ax.barh(y=i, width=row["End Week"] - row["Start Week"] + 1, left=row["Start Week"],
#             color=colors[sprint], edgecolor="black")
#     ax.text(row["Start Week"], i, row["Task"], va="center", ha="left", fontsize=9)

# # Set labels and grid
# ax.set_yticks(range(len(df)))
# ax.set_yticklabels([""] * len(df))
# ax.set_xticks(range(1, 9))
# ax.set_xticklabels([f"Week {i}" for i in range(1, 9)])
# ax.invert_yaxis()
# ax.set_title("Gantt Chart for Modular Query Refinement Project", fontsize=14)
# ax.set_xlabel("Timeline (Weeks)")

# # Add sprint legend
# legend_patches = [mpatches.Patch(color=color, label=f"Sprint {i}") for i, color in colors.items()]
# ax.legend(handles=legend_patches, loc="upper right")

# plt.tight_layout()
# plt.show()



import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
from datetime import datetime, timedelta

# Task data with week numbers (1-8)
task_data = [
    ("Build basic frontend UI", 1, 2),
    ("Implement REST API", 1, 2),
    ("Select medical QnA dataset", 1, 2),
    ("Test keyword extraction methods", 1, 2),
    ("Structure dataset", 1, 2),
    ("Finalize keyword extraction strategy", 3, 4),
    ("Generate full training dataset", 3, 4),
    ("Polish REST API interactions", 3, 4),
    ("Document system architecture", 3, 4),
    ("Prepare midterm deliverables", 3, 4),
    ("Train models on keyword dataset", 5, 6),
    ("Create model inference pipeline", 5, 6),
    ("Refactor backend for model integration", 5, 6),
    ("Update frontend for model output", 5, 6),
    ("Evaluate model performance", 5, 6),
    ("Enhance frontend UI", 7, 8),
    ("Conduct integration testing", 7, 8),
    ("Finalize backend-model response format", 7, 8),
    ("Write final project report", 7, 8),
    ("Prepare final demo", 7, 8)
]

df = pd.DataFrame(task_data, columns=["Task", "Start Week", "End Week"])

# Project start date (May 10, 2025)
project_start = datetime(2025, 5, 10)

# Map weeks to calendar dates
def week_to_date(week):
    return project_start + timedelta(weeks=week - 1)

df["Start Date"] = df["Start Week"].apply(week_to_date)
df["End Date"] = df["End Week"].apply(lambda w: week_to_date(w) + timedelta(days=6))

# Sprint color map
colors = {1: "#72d66b", 2: "#7650D6", 3: "#f70a0a", 4: "#a59d0c"}
df["Sprint"] = df["Start Week"].apply(lambda w: (w - 1) // 2 + 1)
df["Color"] = df["Sprint"].map(colors)

# Plot Gantt chart
fig, ax = plt.subplots(figsize=(14, 10))

for i, row in df.iterrows():
    ax.barh(i, (row["End Date"] - row["Start Date"]).days + 1,
            left=row["Start Date"], color=row["Color"], edgecolor='black')
    ax.text(row["Start Date"], i, row["Task"], va='center', ha='left', fontsize=9)

ax.set_yticks(range(len(df)))
ax.set_yticklabels([""] * len(df))
ax.invert_yaxis()
ax.set_xlabel("Date")
ax.set_title("📊 Gantt Chart: Modular Query Refinement Project (Real Dates)", fontsize=14)
ax.grid(True, which='major', axis='x', linestyle='--', alpha=0.5)

# Legend
legend_patches = [mpatches.Patch(color=color, label=f"Sprint {i}") for i, color in colors.items()]
ax.legend(handles=legend_patches, loc='upper right')

plt.tight_layout()
plt.show()
