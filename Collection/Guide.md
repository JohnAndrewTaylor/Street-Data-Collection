**To edit the form:**
- Sign in to the Epicollect5 website (https://five.epicollect.net) - you will need to request to be manually given permission to manage the current project. The project name is “Cavalier Manor Eco Districts” (the same name is used to search for the project in the application).
- You may use the "Form Builder" option to enter a graphical interface which allows you to click and drag questions or other features of your survey into the form. More information on Epicollect5 can be found here: https://epicollect5.gitbooks.io/epicollect5-user-guide/content.
- Your changes will affect the mapping of the exported .csv file, so any scripts will also need to be edited.
- You may also recreate the form in a new project by importing the provided .json file of the current form.

Searching for it in the app will bring it up, and from there data can be collected with it.

**To use the form:**
- Install the application Epicollect5 through the iOS or Android app stores.
- Search “Cavalier Manor Eco Districts” (or the name of the project you intend to use) to add the form to your phone
- Click "Add entry" in the top right
- Fill out all the required fields. The "No Issue" option is selected by default for any questions asking about potential problems.
- Click "Save entry" when you are done
- Select "Upload now" and then "Upload data" whenever you have Internet access to add your entry to the database.

**To view and export data:**
- Go to the project homepage and select "View Data" (The link for the provided form is: https://five.epicollect.net/project/cavalier-manor-eco-districts/data)
- Click "Download" in the upper right corner
- Select the CSV format and click "Download" in the left side of the screen.
- Rename the CSV file "input" after you unzip the zipped folder download.
- Run the sorting script in the same folder as the file. This should produce a sorted "output" file (your master CSV).
- To enable use with the GQIS visualization software, you must execute the additional provided filtering script or manually create a new filtered file.
- You may want to clear the online database and keep an offline master file if the entries become too crowded.

**To manually create a master CSV file**
- Open the downloaded CSV file in Microsoft Excel
- Delete the first four columns
- Select all the data except the first row
- On the Home tab, find and select "Sort & Filter"
- Select "Sort A to Z"
- The entries should be sorted by address now, so delete multiple entries for the same address, keeping only the most recent entry
- On the Home tab, find and select "Find & Select"
- Click "Replace..."
- Replace all values of "No Issue" with 0, all "Non-Severe Issue" with 1, and "Severe Issue" with 2

*Feel free to contact the team if you have any issues with these steps*
