# %%
from distutils.command.config import config
import yaml

config = yaml.safe_load(open('./config.yml')) # .load(open('./config.yml'))
print(config)

# %%
url = config['url'].format(**config)
# %%
