# glma
## Background
Welcome to the glma repository! We created this for a hackathon, and the goal of our project is to create an ai agent that can help document codebases in a way that is easy to understand and navigate. This agent will be able to analyze code, generate documentation, and provide insights into the structure and functionality of the codebase. Ultimately this would help the process of migrating legacy codebases to modern frameworks and languages. For that reason, we are currently exploring the linux kernel codebase as a test case for our agent.

## Getting Started
This repo uses git submodules to include the linux kernel codebase. To get started, clone the repository and initialize the submodules:

If you would like a quick one line clone, you can use the following command:
```bash
git clone --recurse-submodules https://github.com/progressEdd/glma.git
```

If you have already cloned the repository, you can initialize the submodules with the following commands:
```bash
git pull
git submodule update --init --recursive
```

If you only need specific submodules, you can initialize them individually:
```bash
# For just the dev-onboarding submodule
git submodule update --init 01-dev-onboarding

# For just the Linux kernel submodule
git submodule update --init 00-supporting-files/data/linux-
```