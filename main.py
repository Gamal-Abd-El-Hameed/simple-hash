import subprocess
from hashHelper import *

calculate_hash_collision()
create_collision()
print('-' * 50)
print('After creating collision:')
print('-' * 50)
calculate_hash_collision()

# restore the original file
git_command = ['git', 'restore', 'test-files/5.txt']
subprocess.run(git_command)
