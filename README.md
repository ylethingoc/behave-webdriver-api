# behave-webdriver-api
Behave framework for webdriver and rest-api testing using webdriver-manager to handle multi-browser.

### 🐋 Prerequisite 
You need an IntelliJ IDE Ultimate version to enable Behave run type and Gherkin language

### 🍰 IntelliJ Setup
1. Download Python plugin
2. Open project structure by pressing Ctrl + Alt + Shift + S, in Project -> Project SDK -> Add Python SDK
3. Open cmd prompt inside project folder then install all require packages in requirements.txt file by using cmd `install -r requirments.txt`

### ➡️ Note
* Spotify account is required and need to be added as Environment variables to run tests. For instance, select Run -> Edit Configurations 
-> Edit configuration templates -> Behave -> input `user=<your_user>;password=<your_password>` into Environment variables -> Apply -> OK
* The test in tests/web/features/spotify.feature should be executed first to get OAuth token.
