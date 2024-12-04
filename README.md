## Overview

This project is an example of using Azure DevOps for a Python project. It demonstrates how to set up a CI/CD pipeline for a Python application.  
We have multiple CI/CD Pipeline examples, one for running the SonarScanner and sending the results to SonarQube Server and the other for sending the results to SonarQube Cloud

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

## Important Links
Azure DevOps - SonarQube Server Integration > https://docs.sonarsource.com/sonarqube-server/latest/devops-platform-integration/azure-devops-integration/  
Azure DevOps Pipelines - SonarQube Cloud > https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/  
SonarScanner Analysis Scope > https://docs.sonarsource.com/sonarqube-server/latest/project-administration/analysis-scope/  
