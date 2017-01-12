if exists('g:signed_local_rc_loaded')
  finish
endif

if !has('python')
  echom 'Error: signed-local-rc requires +python'
  finish
endif

python << EOF
import vim
import sys, os.path
this = vim.eval('expand("<sfile>")')
lib = os.path.join(os.path.dirname(this), '..', 'python')
sys.path.append(lib)
import slrc.vimsupport as slrc
EOF

let g:signed_local_rc_trusted_dir = '~/.signed_local_rc_trusted_dir'

command! SlrcSource py slrc.checked_source()
command! -nargs=1 SlrcTrust py slrc.trust_pub_key(<f-args>)
command! -nargs=1 SlrcUntrust py slrc.untrust_pub_key(<f-args>)
command! -nargs=1 SlrcSign py slrc.sign_vimrc(<f-args>)
