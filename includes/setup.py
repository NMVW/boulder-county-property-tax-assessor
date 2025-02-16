import sys, os, datetime
from IPython import get_ipython
import json

environment = None
environment_initialized = False

environment_exception_message_template = '''{environment_name} is not yet supported.

To run on {environment_name} anyway:
- Pass `allow_{environment_token}=True` when calling `initialize_exercise()`
- Be prepared for problems
'''
colab_exception_message = environment_exception_message_template.format(environment_name='Google Colab', environment_token='colab')
kaggle_exception_message = environment_exception_message_template.format(environment_name='Kaggle', environment_token='kaggle')

unrecognized_environment_exception_message = '''Unrecognized Environment!

If you're attempting to run this notebook locally:
- Set up your Pipenv virtual environment
- Restart your editor
- Select the appropriate kernel
- Rerun this block.

To run on an unrecognized environment anyway:
- Pass `allow_unrecognized=True` when calling `initialize_exercise()`
- Be prepared for big problems!
'''

def initialize_environment(allow_colab=True, allow_kaggle=True, allow_unrecognized=False):
    global environment, environment_initialized

    if 'virtualenvs' in sys.executable:
        environment = 'VIRTUAL'
        print("🎉 Running in a Virtual environment")
    elif 'COLAB_GPU' in os.environ:
        environment = 'COLAB'
        print("🤔 Running on Google Colab")
        if not allow_colab:
            raise Exception(colab_exception_message)
    elif 'KAGGLE_KERNEL_RUN_TYPE' in os.environ:
        environment = 'KAGGLE'
        print("🤔 Running on Kaggle")
        if not allow_kaggle:
            raise Exception(kaggle_exception_message)
    elif allow_unrecognized:
        environment = 'UNRECOGNIZED'
        print("⚠️ Running in a unrecognized environment.")
    else:
        raise Exception(unrecognized_environment_exception_message)

    environment_initialized = True

def load_environment_variable(variable_name):
    if not environment_initialized:
        raise Exception("Environment not yet initialized. Run `setup.initialize_environment()` first.")
    if environment == 'VIRTUAL':
        # We shouldn't need to install packages in this environment, since Pipenv handles that for us
        from dotenv import load_dotenv
        load_dotenv()
        if variable_name not in os.environ:
            raise Exception(f"{variable_name} does not exist in os.environ")
        return os.environ[variable_name]
    elif environment == 'COLAB':
        from google.colab import userdata
        return userdata.get(variable_name)

def load_openai_api_key():
    return load_environment_variable('OPENAI_API_KEY')
