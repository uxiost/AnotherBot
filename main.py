# %%
import yaml

credentials = yaml.safe_load(open('./credentials.yml')) # .load(open('./credentials.yml'))
print(credentials)
