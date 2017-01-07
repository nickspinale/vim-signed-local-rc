if exists('g:signed_local_rc_loaded')
  finish
endif

if !has('python')
  echom 'Error: signed-local-rc requires +python'
  finish
endif

python << EOF
import vim
import sys, os, os.path
this = vim.eval('expand("<sfile>")')
lib = os.path.join(os.path.dirname(this), '..', 'python')
sys.path.append(lib)
import slrc.vimsupport
EOF

let g:signed_local_rc_trusted_dir = '~/.signed_local_rc_trusted_dir'
