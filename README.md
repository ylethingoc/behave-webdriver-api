 # behave-webdriver-api
Behave for webdriver and rest-api testing using webdriver-manager to handle multi-browser 
and also including Docker 🐋 🐋 🐋

### 🔫 IntelliJ Setup
1. Download Python plugin
2. Open project structure by pressing Ctrl + Alt + Shift + S, in Project -> Project SDK -> 
Add Python SDK
3. Open cmd prompt inside project folder then install all require packages in requirements.txt file
by using cmd `install -r requirments.txt`

### 🕹️️ How to run test
* For IntelliJ, Select Build -> Edit Configurations -> Edit configuration templates 
-> Behave -> Use SDK of module
* Without IDE, open any terminal then use behave run command ```behave <path-to-suite>```, 
for example ```behave tests/web/features```
* For Docker, open any terminal then initial a container with 
```docker run behave-webdriver-api behave <path-to-suite>```, 
for example ```docker run behave-webdriver-api behave tests/web/features```

### 📌 Notice
* You need an IntelliJ IDE Ultimate version to enable Behave run type and Gherkin language.
* The test in tests/web/features/spotify.feature should be executed first to get OAuth token.
* Disable chrome option or using other browser by changing the configuration in setup.cfg
for UI visible.
* Multi-browser is not available for Docker, only Chrome at this time.

🍺🍺🍺
