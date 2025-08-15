# main.py
# A simple log watcher

suspicious_keywords = ["hack", "malware","attack","intrusion"]

# simulate a log file
log_file = "sample_log.txt"

# create a sample log file (only once)
with open(log_file, "w") as f:
	f.write("User login successful\n")
	f.write("Possible malware detected\n")
	f.write("System running normally\n")

# read the log file and search for suspicious activity
with open(log_file, "r") as f:
	for line in f:
		if any(keyword in line.lower() for keyword in suspicious_keywords):
			print(f"[ALERT] Suspicious activity detected: {line.strip()}")
