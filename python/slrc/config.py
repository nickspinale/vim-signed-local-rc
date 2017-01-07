import vim

def get_trusted_dir():
    return vim.eval('expand(g:signed_local_rc_trusted_dir)')
