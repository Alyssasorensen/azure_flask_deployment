### Deployed URL of my application: https://alyssa-504-flask.azurewebsites.net/

# **A Guide on How to Set Up and Deploy a Flask Application Using HTML and Azure App Service**

### *Overview: This guide will help you establish a Flask application, merging it with data handling using Pandas, and deploying the application on Azure App Service. Additionally, you will have the opportunity to enhance your skills in documenting the workflow and utilizing GitHub for project administration and management.*

#### **Step 1:** 
     Create a new repository in GitHub and name it "azure_flask_deployment." Then set up your Google Shell environment and open this repository using the "git clone" command.
    
#### **Step 2:**
     Create a "base.html" file and insert the code from Professor Williams GitHub, in week 2, under "flaskapp_0."

#### **Step 3:**
     Create a "about.html" file and insert the code from Professor Williams GitHub, in week 2, under "flaskapp_0."

#### **Step 4:**
     Create a "data.html" file and insert the code from Professor Williams GitHub, in week 2, under "flaskapp_0."

#### **Step 5**
     Create a "requirements.txt" file and insert, faker, pandas, flask.

#### **Step 6:**
     Once in the workspace, in Google Shell, you can add an "app.py" file. In this file you will need to import Flask and import Pandas. In your Google Shell environment, you can create a dataset folder where you can insert your CSV file. You can then push these changes to GitHub. 

#### **Step 7:**
     You can now update your data.html file by inserting the appropriate names of the columns, so that they display correctly when deploying the website. 

#### **Step 8:**
     In the app.py file on Google Shell, you will also need to insert your CSV file from your GitHub repository into the code, so that the website displays the dataset. You can do this by clicking on the datasets folder, that you just created and pushed to GitHub, and copy the raw data from that CSV file.  

#### **Step 9:**
     In your terminal, you can then type in "python app.py" to view the website and make changes. 

#### **Step 10:**
     After finalizing your website, you want to deploy your flask application to Azure App Service. In your terminal, insert "curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash." This will install the Azure CLI. 

#### **Step 11:** 
     In your terminal, type in "az." After this command, type in "az login --use-device-code." You are then going to click the URL and enter the code to authenticate. You are then going to press your Stony Brook account and press continue. You can then exit out of that tab and go back to Google Shell. You will see that you were successfully authenticated.  

#### **Step 12:** 
     You are then going to insert "az account list --output table" into your terminal. You are then going to change the subscription Id. This is done by inserting the code, "az account set --subscription subscriptionId." The subscription Id are numbers and letters and they signify the SubscriptionId next to "Azure for Students."

#### **Step 13:**
     You are now going to go in the Azure Web Portal and create a new resource group, give it a simple name, no white space and no special characters. When creating the resource group, ensure it is "Azure for Students." 

#### **Step 14:**
     In your terminal insert, "az group list."

#### **Step 15:**
     In your terminal insert, "az webapp up --name-insert resource group here-flask --runtime PYTHON:3.9 --sku B1." You have to insert "name" and right after that you insert what you named the resource group in Azure. 

#### **Step 16:**
     The terminal will then say that the webapp does not exist, and it will create the resource group and start the zip deployment. 

#### **Step 17:**
     After this finishes and your present working directory appears, type into the the terminal python app.py and the URL should appear where you can click on it and view your website. 

#### **Step 18:**
     Type into the terminal az webapp up and you will get the final URL to view your website. 