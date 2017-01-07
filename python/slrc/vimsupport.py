import os.path

from slrc.crypto import sign_file, verify_file
from slrc.persist import check_pub_key, trust_pub_key

import vim


if (
    os.path.isfile('.vimrc.local')
    and os.path.isfile('.vimrc.local.pub')
    and os.path.isfile('.vimrc.local.sig')
    ):
    print 'hi'
