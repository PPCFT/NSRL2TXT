# NSRL2TXT
## Modify SQL Database to Text File

To convert your SQL database into a text file, you need to run the `main.py` script. This script is designed to extract data from your SQL database and save it in a plain text format. To execute the script, open your terminal or command prompt, navigate to the folder containing `main.py`, and run the following command:

```bash
python main.py
```

This process will create a text file containing the exported data from your SQL database. If you encounter any issues, make sure you have Python installed on your system and that all required dependencies for the script are available. The generated text file can be opened and edited with any standard text editor, such as Notepad or VS Code[^1][^2][^4].

## Sort and Remove Duplicates

To organize your data and ensure there are no duplicate entries, follow these steps:

1. First, create a new text file named `NISTWhiteList.txt` and add the header "MD5" to it by running:

```bash
echo "MD5" &gt; NISTWhiteList.txt
```

2. Next, sort the contents of your existing file (`NISTHashSet.txt`) and remove any duplicate lines. This is accomplished using the following command:

```bash
pv NISTHashSet.txt | sort --parallel=8 --buffer-size=16G | uniq &gt;&gt; NISTWhiteList.txt
```

    - `pv` is used to monitor the progress of the operation, which is helpful if you are working with large files.
    - `sort` organizes the lines in alphabetical order, making it easier to find duplicates.
    - `uniq` removes any duplicate lines, ensuring each MD5 hash appears only once.
    - The sorted and deduplicated data is then appended to `NISTWhiteList.txt`.

These commands are typically run in a Unix-like terminal (such as Linux or macOS). If you are using Windows, you may need to install additional tools or use the Windows Subsystem for Linux (WSL).

## Processing an XML File Containing Known Files and Extracting a List of MD5 Hashes

If you have an XML report file (for example, `Raport.xml`) that contains information about known files, you can extract all MD5 hash values using the following command:

```bash
pv Raport.xml | grep -oP '(?&lt;=)' &gt; /mnt/g/Hashsets/KnownFiles/Android_20250429.txt
```

- `pv` shows the progress of the operation.
- `grep -oP '(?&lt;=)'` searches for and extracts all 32-character MD5 hashes that are enclosed within `` tags in the XML file.
- The results are saved to a new text file, in this example: `/mnt/g/Hashsets/KnownFiles/Android_20250429.txt`.

This step is useful if you need a clean list of all MD5 hashes from a complex XML report, making it easier to process or compare against other datasets.

---

**Summary for Non-Technical Users:**

- You start by exporting your database to a text file using a Python script.
- Next, you clean up your data by sorting it and removing duplicates, ensuring you have a tidy list.
- Finally, you can extract specific information (like MD5 hashes) from an XML report and save it as a simple list for further use.

Each step uses command-line tools, which are standard utilities on most Unix-like systems. If you are new to the command line or working on Windows, you may need to install additional tools or seek help with the setup. The instructions provided are designed to automate repetitive tasks and ensure data accuracy throughout your workflow.

<div style="text-align: center"><img src="https://avatars.githubusercontent.com/u/118799273?v=4" class="logo" width="120"/></div>

[^1]: https://products.groupdocs.app/conversion/sql-to-txt

[^2]: https://stackoverflow.com/questions/57685647/convert-database-file-into-a-text-file

[^3]: https://www.edchart.com/free-online-converters/sql-to-text-converter.php

[^4]: https://www.sqlservercentral.com/articles/8-ways-to-export-sql-results-to-a-text-file

[^5]: https://www.withdata.com/blog/datafileconverter/sql-to-txt.html

[^6]: https://www.digitalocean.com/community/tutorials/how-to-use-python-markdown-with-flask-and-sqlite

[^7]: https://www.reddit.com/r/Database/comments/1ado2hn/best_way_to_convert_large_txt_files_into_a_sql/

[^8]: https://forum.obsidian.md/t/manipulate-all-md-files-at-once-with-python-giant-find-and-replace/27336

[^9]: https://docs.devart.com/querybuilder-for-sql-server/working-with-data/export-to-text.html

[^10]: https://pypi.org/project/MarkdownTools2/

[^11]: https://python-markdown.github.io/changelog/

[^12]: https://dev.to/minchulkim87/documenting-sql-with-markdown-and-diagrams-2lhp

[^13]: https://docs.readthedocs.io/en/stable/guides/migrate-rest-myst.html

[^14]: https://sqlmodel.tiangolo.com/contributing/

[^15]: https://gist.github.com/30nnax?direction=asc\&sort=updated

