python -m venv push_env
source push_env/bin/activate
pip install GitPython
export LATEST_TAG=$1
export BUMP_TYPE=$2
python tag_versioning.py
echo outside: $UPDATED_TAG
