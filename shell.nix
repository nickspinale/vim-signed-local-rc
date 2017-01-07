with import <nixpkgs> {}; stdenv.mkDerivation {

  name = "env";

  shellHook = ''
    export VIMRUNTIME=${builtins.getEnv "VIMRUNTIME"}
  '';

  buildInputs = [
    python
    pythonPackages.pycrypto
    (vimUtils.makeCustomizable (callPackage <nixpkgs/pkgs/applications/editors/vim/configurable.nix> {
      inherit (darwin.apple_sdk.frameworks) CoreServices Cocoa Foundation CoreData;
      inherit (darwin) libobjc cf-private;
      features = "huge";
      lua = pkgs.lua5_1;
      gui = config.vim.gui or "auto";
      flags = [ "python" "X11" ];
      python = python.buildEnv.override {
        extraLibs = [ pythonPackages.pycrypto ];
      };
    }))
  ];

}
