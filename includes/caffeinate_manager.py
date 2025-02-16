import subprocess
"""
    Never wake up with a terminated long-running process again !

    This module provides functions to start and stop the caffeinate process.
    The caffeinate process prevents the system from going to sleep, which is useful for long-running tasks.

    https://ss64.com/mac/caffeinate.html
"""

def start_caffeinate():
    """Starts the caffeinate process."""
    subprocess.Popen(["caffeinate", "-s"])

def stop_caffeinate():
    """Stops the caffeinate process."""
    subprocess.run(["pkill", "caffeinate"])

# Example usage:
# start_caffeinate()
# # Run your long-running task here
# stop_caffeinate()