# myGitActions
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/DaniaAlSafadi/myGitActions/BashScriptTests.yml?branch=main)
<span style="color:blue"><u><strong>🚀 CI Workflow: Check Your Bats Setup</strong></u></span>
🛠 GitHub Actions Workflow: **BashScriptTests.yml**
This repository includes a GitHub Actions workflow defined in **.github/workflows/BashScriptTests.yml.** <span style="color:blue"><u><strong>⚠️ Note: This workflow runs on every push to test with Bats.</strong></u></span>
<span style="color:blue">Workflow Name: learn-github-actions</span>
<span style="color:blue">Trigger: On every push</span>
<span style="color:blue">Purpose: Installs the Bash Automated Testing System (Bats) and displays its version.</span>
🔄 Workflow Steps
- **Checkout Code** – Retrieves the repository content using actions/checkout@v4.
- **Set Up Node.js** – Installs Node.js version 20 using actions/setup-node@v4.
- **Install Bats** – Installs the Bats testing framework globally using npm.
- **Verify Bats Installation** – Runs bats -v to confirm the version.

<u>The workflow diagram:</u>
