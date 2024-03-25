import subprocess

from hashHelper import *

calculate_hash_collision()
create_collision()
calculate_hash_collision()


git_command = ['git', 'restore', 'test-files/5.txt']
subprocess.run(git_command)
