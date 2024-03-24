# E2M

## Project 7
### Instructions for testing the database_input_form
These instructions are using VS Code as the IDE.
<ol>
  <li>Clone or sync the GitHub repository https://github.com/ITSC4155-E2M/Project5-8.git</li>
  <li>Open a terminal, then in bash install flask:  pip install flask</li>
  <li>In bash, install flask-mysqldb:  pip install flask flask-mysqldb</li>
  <li>Run the database.py application in the bash terminal:  python database.py</li>
  <li>In the bash terminal, find the line "* Running on http://127.0.0.1:5000", then ctrl_click the link.</li>
  <li>A browser window will open with the input form. Enter any first and last name to test with. (Don't worry, we'll delete it out later.)</li>
  <li>Select the "Submit" button.</li>
  <li>You should receive the message "Data inserted successfully."</li>
</ol>

### Instructions for viewing the database in MySQL Workbench
<ol>
  <li>Download MySQL Workbench on your computer.</li>
  <li>Create a new connection.</li>
    <ol>
      <li>Name the connection "E2M Database"</li>
      <li>Leave the default connection method.</li>
      <li>Hostname = ls-b640ee9303d25068be488588342687643e09a864.cte0si8k44ty.us-east-1.rds.amazonaws.com</li>
      <li>Port = 3306</li>
      <li>Username = dbmasteruser</li>
      <li>Username = dbmasteruser</li>
      <li>Password (use Store in Vault...) =3qu1tym3m0rym3m0r1al</li>
      <li>Test Connection, if good then select OK</li>
    </ol>
  <li>Open the E2M Database connection. See above if you need to create the connection.</li>
  <li>Navigate to the "Ancestry" database (aka schema)</li>
  <li>Open Tables, then open the "enslaved_person" table.</li>
  <li>Verifiy the name you entered as a code test is present.</li>
</ol>
<br>
Issues contact Nathan Schaaf at nschaaf@uncc.edu or 678-200-7438

