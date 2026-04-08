# boot_dev_asteroids
A simple implementation of the Asteroids game in Python part of the boot dot dev course

## Setup and Running

This project uses [uv](https://github.com/astral-sh/uv) to manage dependencies and Python versions.

### 1. Prerequisites

Ensure you have `uv` installed. If not, you can find installation instructions [here](https://github.com/astral-sh/uv).

### 2. Install Dependencies

To create a virtual environment and install the required version of Pygame, run:

```sh
uv sync
```

### 3. Run the Game

You can run the main script directly through uv, which ensures the virtual environment is used:

```sh
uv run main.py
```

Alternatively, you can activate the virtual environment manually:

```sh
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

Then run:

```sh
python main.py
```

### Why these steps?

- **`uv sync`**: Uses the correct version provided with the repo lock file.
- **`uv run`**: Activates the environment behind the scenes
- **Python Version**: Python 3.13 is needed for pygame. `uv` will automatically try to find or download that specific version when the user runs the project based on the toml config.

### If you want to run this under nixos devshell (like I did)
Then forget about the Python venv completely, as it doesn't work well with Nixos' declarative nature. Instead you can create a flake with explicit definition of python packages to be used, thourgh the nix `withPackages`. Below is a sample flake with parts skipped. I do hope you use flakes. Why don't you use flakes? When are you going to switch to flakes? Please use flakes!

```nix
{
  description = "Flake with dev shell with Python with its packages";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-25.11";
  };

  outputs = { self, nixpkgs, ... } @ inputs:
  let
    system = "x86_64-linux";
  in {
    # ... add other parts of the flake setup you have

    devShells.${system}.default = let
      pkgs = import nixpkgs { system = system; };
      # Define python with packages included, because python doesn't like the nix way
      pythonWithPackages = pkgs.python3.withPackages (ps: [
        ps.pygame
      ]);
    in pkgs.mkShell {
      packages = [
        pythonWithPackages
        # ... other packages from your flake setup
      ];
    };
  };
}
```

If you aren't very advanced NixOS user like me, and just try copy pasting stuff from the Internet, you can find the complete flake and the other related files here: [NixOS dotfiles](https://github.com/luboganev/nixos/tree/gaming-pc).
