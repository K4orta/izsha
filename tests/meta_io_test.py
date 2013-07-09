import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import izsha, izsha_config

def open_meta_test():
	assert izsha.open_meta('tests/stubs/meta.yaml')['best_of'] == 3 

def format_meta_test():
	pass
