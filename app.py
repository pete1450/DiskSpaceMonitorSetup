from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip = request.form['ip']
        user = request.form['user']
        password = request.form['password']
        url = request.form['url']

        # Define the script content
        script_content = f"""#!/bin/bash

# Get the disk usage of a specified mount
disk_usage=$(df -h | grep '/dev/sda1' | awk '{{print $5}}' | sed 's/%//')

# Check if the disk usage is below 90%
if [ "$disk_usage" -lt 90 ]; then
  # Call the endpoint
  curl -X GET "{url}"
fi
"""

        # Save the script to a temporary file
        with open('/tmp/check_disk_space.sh', 'w') as script_file:
            script_file.write(script_content)

        os.chmod('/tmp/check_disk_space.sh', 0o755)

        # Transfer the script to the remote server
        os.system(f"sshpass -p '{password}' scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null /tmp/check_disk_space.sh {user}@{ip}:/home/{user}/check_disk_space.sh")

        # Add the cron job
        cron_job = f"0 */3 * * * /home/{user}/check_disk_space.sh"
        os.system(f"sshpass -p '{password}' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null {user}@{ip} '(crontab -l 2>/dev/null; echo \"{cron_job}\") | crontab -'")

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='192.168.1.234')
