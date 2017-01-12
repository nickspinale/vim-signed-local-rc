# vim-signed-local-rc

Vim plugin for loading an RSA-signed project-local `.vimrc`.

## Usage

This plugin cares about the following files in `.`:

- `.vimrc`: Project-local configuration.
- `.vimrc.pub`: Public key of signer.
- `.vimrc.sig`: Signature of `.vimrc` by `.vimrc.pub`.

Commands:

- `SlrcSource`: Source `./.vimrc` if `./.vimrc.pub` is trusted and `./vimrc.sig` is valid.
- `SlrcTrust <pub_key>`: Trust `<pub_key>`.
- `SlrcUntrust <pub_key>`: Untrust `<pub_key>`.
- `SlrcSign <priv_key>`: Sign `./.vimrc` with `<priv_key>` and write to `./.vimrc.sig`

Options:

- `g:signed_local_rc_trusted_dir`: Directory for storing trusted keys (default `~/.signed_local_rc_trusted_dir`)

## Installation

There are many ways to install a vim plugin.
One of them is [pathogen.vim](https://github.com/tpope/vim-pathogen).
Once you have Pathogen installed, simply:

```
cd ~/.vim/bundle
git clone git://github.com/nickspinale/vim-signed-local-rc.git
```
