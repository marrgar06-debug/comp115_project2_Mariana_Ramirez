import matplotlib.pyplot as plt

hours = ["8am", "10am", "12pm", "2pm", "4pm", "6pm", "8pm", "10pm"]
focus_low_sleep = [4, 6, 5, 2, 3, 4, 3, 1] 
focus_high_sleep = [8, 9, 8, 7, 8, 7, 6, 5] #Feel free to perform an experiment, comparing days in which you slept 8 hours or more VS days you slept 5 hours or less. 

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
deep_sleep_minutes = [54, 55, 50, 40, 48, 92, 60] #Feel free to change this numbers and analyze your own sleep data!


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
plt.style.use('seaborn-v0_8-bright')


ax1.plot(hours, focus_high_sleep, marker='o', label='8 Hours Sleep', color='green', linewidth=3)
ax1.plot(hours, focus_low_sleep, marker='x', label='5 Hours Sleep', color='red', linestyle='--')
ax1.set_title("Daily Focus Level vs. Sleep Amount")
ax1.set_ylabel("Focus Score (1-10)")
ax1.set_ylim(0, 10)
ax1.legend()
ax1.grid(True, alpha=0.3)

colors = ['gray' if x < 60 else 'skyblue' for x in deep_sleep_minutes]
ax2.bar(days, deep_sleep_minutes, color=colors)
ax2.set_title("Deep Sleep Minutes per Night")
ax2.set_ylabel("Minutes")


ax2.axhline(y=60, color='orange', linestyle='-', label='Goal (60 min)')
ax2.legend()


plt.suptitle("Personal Health Metrics Analysis", fontsize=16)
plt.tight_layout()
plt.show()
