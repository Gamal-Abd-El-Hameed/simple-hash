import subprocess
import time
from hashHelper import *

calculate_hash_collision()
create_collision2()
calculate_hash_collision()
#time.sleep(20)

git_command = ['git', 'restore', 'test-files/5.txt']
subprocess.run(git_command)
