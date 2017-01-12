import os.path

from slrc.crypto import sign_file, verify_file
from slrc.persist import check_pub_key, trust_pub_key, untrust_pub_key

import vim


def checked_source():
    if (
        os.path.isfile('.vimrc')
        and os.path.isfile('.vimrc.pub')
        and os.path.isfile('.vimrc.sig')
        ):
        if check_pub_key('.vimrc.pub'):
            if verify_file('.vimrc.pub', '.vimrc', '.vimrc.sig'):
                vim.command('source .vimrc')
            else:
                vim.command('echo "Slrc: invalid signature"')
        else:
            vim.command('echo "Slrc: .vimrc.pub not trusted"')


def sign_vimrc(priv_key_path):
    if os.path.isfile('.vimrc'):
        sign_file(priv_key_path, '.vimrc', '.vimrc.sig')
    else:
        vim.command('echo "Slrc: .vimrc does not exist"')
