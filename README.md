## Overview

This project is an example of using Azure DevOps for a Python project. It demonstrates how to set up a CI/CD pipeline for a Python application.  
We have multiple CI/CD Pipeline examples, one for running the SonarScanner and sending the results to SonarQube Server and the other for sending the results to SonarQube Cloud.  

PLEASE READ OUR SONARQUBE DOCUMENTATION FOR WORKING WITH AZURE DEVOPS PIPELINES  
Azure DevOps - SonarQube Server Integration > https://docs.sonarsource.com/sonarqube-server/latest/devops-platform-integration/azure-devops-integration/  
Azure DevOps Pipelines - SonarQube Cloud > https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/  

## Important Information in Pipelines
- triggers are set to only execute on changes to main branch and a specific directory in the project, this can be modified with whatever you would want to specify.
- they have shallow fetch set to 0. this is required for SonarScanner to properly analyze your project.  
- please remember to check the version available for the **cliScannerVersion** (https://github.com/SonarSource/sonar-scanner-cli/tags) parameter in the **SonarQubePrepare/SonarCloudPrepare** step.
- for more information on how to limit your analysis scope and parameters available, please check **SonarScanner Analysis Scope** and **SonarScanner Analysis Parameters** in the Important Links section.
- Please remember that there are different tasks for SonarQube Server and SonarQube Cloud. Examples for both are provided.
    - SonarQube Cloud Example: SonarQube-Cloud.yml  
    - SonarQube Server Example: SonarQube-Server.yml 

## Important Links
Azure DevOps - SonarQube Server Integration > https://docs.sonarsource.com/sonarqube-server/latest/devops-platform-integration/azure-devops-integration/  
Azure DevOps Pipelines - SonarQube Cloud > https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/  
SonarScanner Analysis Scope > https://docs.sonarsource.com/sonarqube-server/latest/project-administration/analysis-scope/  
SonarScanner Analysis Parameters > https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/analysis-parameters/  


## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your-repo/Onboarding-Pipeline-Examples.git
    cd Onboarding-Pipeline-Examples/Azure-DevOps/python-example
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running Tests

To run the tests, use the following command:
```sh
pytest
```