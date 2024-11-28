{
  description = "A simple Nix flake with a devshell including Python and OpenCV";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; 
  config = {
    permittedInsecurePackages = [
      "freeimage-unstable-2021-11-01"
    ];
  };
    };
    in {
      devShells.${system} = {
        default = pkgs.mkShell {
          buildInputs = with pkgs;[
            colmap
         (python3.withPackages (python-pkgs: [
              python-pkgs.opencv4
            ]))
          ];
        };
      };
    };
}
