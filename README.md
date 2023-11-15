# Algo-Starter

This project is an Algorand crowdfunding initiative, designed to empower creators and supporters within the Algorand ecosystem.

## Setup

### Initial Setup

1. Clone this repository locally.
2. Install prerequisites:
   - [Docker](https://www.docker.com/)
   - Install AlgoKit (minimum version: 1.1) - [Installation Link](https://github.com/algorandfoundation/algokit-cli#install)
   - Bootstrap your local environment by running `algokit bootstrap all` within this folder.
   - Run `algokit localnet start` to start a local Algorand network in Docker.

### Development

- **VS Code:**
  1. Open the repository root in VS Code.
  2. Install recommended extensions.
  3. Hit F5 to start running with breakpoint debugging.

- **JetBrains IDEs:**
  1. Open the repository root in the IDE.
  2. It should automatically detect it's a Poetry project and set up a Python interpreter and virtual environment.
  3. Hit Shift+F10|Ctrl+R to start running with breakpoint debugging.

- **Other Editors:**
  1. Open the repository root in your text editor.
  2. In a terminal, run `poetry shell`.
  3. Run `python -m smart_contracts` through your debugger of choice.

### Subsequent Use

1. If you update to the latest source code and there are new dependencies, run `algokit bootstrap all` again.
2. Follow the development steps above.

## Tools

This project utilizes Python, Algorand blockchain, AlgoKit, Beaker, PyTEAL, AlgoKit Utils, Poetry, Black, Ruff, mypy, pytest, and pip-audit.

- [Algorand](https://www.algorand.com/): Layer 1 Blockchain.
- [AlgoKit](https://github.com/algorandfoundation/algokit-cli): One-stop shop tool for Algorand developers.
- [Beaker](https://github.com/algorand-devrel/beaker): Smart contract development framework for PyTeal.
- [PyTEAL](https://github.com/algorand/pyteal): Python language binding for Algorand smart contracts.
- [AlgoKit Utils](https://github.com/algorandfoundation/algokit-utils-py): Core Algorand utilities.
- [Poetry](https://python-poetry.org/): Python packaging and dependency management.
- [Black](https://github.com/psf/black): Python code formatter.
- [Ruff](https://github.com/charliermarsh/ruff): Fast Python linter.
- [mypy](https://mypy-lang.org/): Static type checker.
- [pytest](https://docs.pytest.org/): Automated testing.
- [pip-audit](https://pypi.org/project/pip-audit/): Tool for scanning Python environments for packages with known vulnerabilities.

For a productive development experience in VS Code, check the [.vscode](./.vscode) folder.

## Inspiration

Algo-Starter is born from the ambition to make a positive impact on the Algorand network. As an initiative for the Impact track, we aim to revolutionize crowdfunding, offering a decentralized and transparent platform for global users.

## What's Next

Having laid the software foundation and product requirements, the next steps for Algo-Starter involve rigorous testing, campaign promotion, and further community engagement. The focus is on iterating, optimizing, and establishing Algo-Starter as a leading decentralized crowdfunding initiative on the Algorand network.

---

For guidance on the `smart_contracts` folder and adding new contracts to the project, refer to [README](smart_contracts/README.md).
