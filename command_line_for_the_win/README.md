**Answer:**

I have successfully completed the task of uploading screenshots of completing the CMD Challenge using SFTP. Here is how I accomplished it:

1. **Take Screenshots**: I captured screenshots of my completion of the CMD Challenge, specifically the challenge available at [cmdchallenge.com](https://cmdchallenge.com/#/find_primes).

2. **Open Terminal/Command Prompt**: I launched a terminal or command prompt on my local machine.

3. **Establish Connection**: Utilizing the SFTP command-line tool, I established a connection to the sandbox environment. I utilized the provided hostname, username, and password for the sandbox environment.

   ```bash
   sftp username@hostname
   ```

4. **Navigate to Directory**: After connecting, I navigated to the directory where I intended to upload the screenshots.

   ```bash
   cd /root/alx-system_engineering-devops/command_line_for_the_win/
   ```

5. **Upload Screenshots**: Employing the SFTP put command, I uploaded the screenshots from my local machine to the sandbox environment.

   ```bash
   put local_screenshot.png
   ```

6. **Confirm Transfer**: I confirmed the successful transfer of the screenshots by checking the sandbox directory.

   ```bash
   ls
   ```

   ![Screenshot of Successful Transfer]([![image](https://github.com/ranaitsan123/alx-system_engineering-devops/assets/95276621/272ed67e-bc90-418f-9739-44e6a2850df3](https://github.com/ranaitsan123/alx-system_engineering-devops/blob/master/command_line_for_the_win/Capture%20d%E2%80%99%C3%A9cran%202024-04-28%20235944.png))
)

7. **Push to GitHub**: Following the successful transfer, I proceeded to push the screenshots to GitHub in line with the initial requirements.

**Note**: The screenshots of completed CMD Challenge tasks are located within the directory `/root/alx-system_engineering-devops/command_line_for_the_win/`.

I have documented these steps in the project’s README.md file to provide clear instructions on how I conducted the file transfer using SFTP.
