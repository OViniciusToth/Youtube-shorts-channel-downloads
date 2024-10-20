# YouTube Shorts Channel Downloader

This guide provides detailed instructions for downloading YouTube Shorts videos using the script from the **YouTube-Shorts-Channel-Downloads** repository.

## Step-by-Step Instructions

### 1. Clone the Repository
   - First, download the code from GitHub to your local machine. Open your terminal or command prompt and run:
     ```bash
     git clone https://github.com/OViniciusToth/Youtube-shorts-channel-downloads.git
     cd Youtube-shorts-channel-downloads
     ```

### 2. Install Required Dependencies
   - The script relies on several Python libraries, including `Selenium`, `yt-dlp`, and `Tkinter`. To install these dependencies, execute:
     ```bash
     pip install -r requirements.txt
     ```
   - This command installs all the necessary packages specified in the `requirements.txt` file.

### 3. Download and Set Up `chromedriver`
   - **Selenium** requires `chromedriver` to interact with the Chrome browser. Follow these steps:
     1. Visit the [ChromeDriver download page](https://chromedriver.chromium.org/downloads).
     2. Download the version that matches your installed Chrome browser.
     3. Place the `chromedriver` executable in the same directory as the script or ensure it is accessible in your system's PATH.

   - If you are using macOS or Linux, you might need to grant executable permissions:
     ```bash
     chmod +x chromedriver
     ```

### 4. Run the Script
   - Once the setup is complete, run the script by entering the following command:
     ```bash
     python download_shorts.py
     ```

### 5. Input the YouTube Shorts URL
   - After executing the script, you will be prompted to enter a **YouTube Shorts channel URL**. This should be the URL of the Shorts section (e.g., `https://www.youtube.com/@channel_name/shorts`).

### 6. Select the Download Folder
   - A file dialog will open (using `Tkinter`), allowing you to choose the folder where you want to save the downloaded videos. Select your desired folder and confirm.

### 7. Downloading the Videos
   - The script will start scraping the page, finding all available YouTube Shorts links, and downloading the videos to the selected folder.
   - You will see the progress of each video download in the terminal.

### 8. Check the Saved Videos
   - Once all downloads are complete, navigate to the folder you selected to find your downloaded Shorts videos.

---

This step-by-step guide will help users navigate through the process of downloading YouTube Shorts videos using your script effectively. Feel free to modify any details as necessary!
