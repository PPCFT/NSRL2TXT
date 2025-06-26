# NSRL2TXT
## Modify SQL Database to Text File

To convert your SQL database into a text file, you need to run the `main.py` script. This script is designed to extract data from your SQL database and save it in a plain text format. To execute the script, open your terminal or command prompt, navigate to the folder containing `main.py`, and run the following command:
**Remember to change the PATH in `main.py` file!**
```bash
python main.py
```

This process will create a text file containing the exported data from your SQL database. If you encounter any issues, make sure you have Python installed on your system and that all required dependencies for the script are available. **The generated text file can't be opened and edited with any standard text editor due to its size!**

These commands are typically run in a Unix-like terminal (such as Linux or macOS). If you are using Windows, you may need to install additional tools or use the Windows Subsystem for Linux (WSL).

## Processing an XML File Containing Known Files and Extracting a List of MD5 Hashes

If you have an XML report file (for example, `Raport.xml`) that contains information about known files, you can extract all MD5 hash values using the following command:

```bash
pv Raport.xml | grep -oP '(?<=<!\[CDATA\[)[a-f0-9]{32}(?=\]\]>)'  > /mnt/g/Hashsets/KnownFiles/Android_20250429.txt
```

- `pv` shows the progress of the operation.
- `grep -oP '(?<=<!\[CDATA\[)[a-f0-9]{32}(?=\]\]>)' ` searches for and extracts all 32-character MD5 hashes that are enclosed within `` tags in the XML file.
- The results are saved to a new text file, in this example: `/mnt/g/Hashsets/KnownFiles/Android_20250429.txt`.

This step is useful if you need a clean list of all MD5 hashes from a complex XML report, making it easier to process or compare against other datasets.

---

**Summary for Non-Technical Users:**

- You start by exporting your database to a text file using a Python script.
- Finally, you can extract specific information (like MD5 hashes) from an XML report and save it as a simple list for further use.

Each step uses command-line tools, which are standard utilities on most Unix-like systems. If you are new to the command line or working on Windows, you may need to install additional tools or seek help with the setup. The instructions provided are designed to automate repetitive tasks and ensure data accuracy throughout your workflow.

<div style="text-align: center"><img src="https://avatars.githubusercontent.com/u/118799273?v=4" class="logo" width="120"/></div>

