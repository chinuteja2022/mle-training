import subprocess

# run ingest_data.py
subprocess.run(["python", "notebook/ingest_data.py"])

# run train.py
subprocess.run(["python", "notebook/train.py"])

# run score.py
subprocess.run(["python", "notebook/score.py"])
