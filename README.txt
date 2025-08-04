For the next steps for the uptime-monitor 


After downloading .PublishSettings file I need to add it to my Github.


Adding Secret to my Github repo.

Name it this - AZURE_WEBAPP_PUBLISH_PROFILE
paste all of the contents of .PublishSettings file in here and save it.


Creating Github actions for workflow file

In bash type this

.github.workflows/deploy.yml

Contents of the yaml file with be this

name: Build and Deploy to Azure App Service with Docker

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Deploy to Azure Web App
        uses: azure/webapps-deploy@v2
        with:
          app-name: uptime-monitor-app  
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
          package: .



And now in powershell in project folder do this

git add .github/workflows/deploy.yml
git commit -m "Add GitHub Actions workflow for Azure deployment"
git push


Go to azure app url and you should see uptime-monitor app running live

