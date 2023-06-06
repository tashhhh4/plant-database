#!/bin/sh

# modded_startup.sh

echo 'export APP_PATH="/app"' >> ~/.bashrc
echo 'cd $APP_PATH' >> ~/.bashrc

# Enter the source directory to make sure the script runs where the user expects
cd $APP_PATH

export APP_PATH="/app
if [ -z "$HOST" ]; then
                export HOST=0.0.0.0
fi

if [ -z "$PORT" ]; then
                export PORT=80
fi

export PATH="/opt/python/3.11.0/bin:${PATH}"
echo 'export VIRTUALENVIRONMENT_PATH="$APP_PATH/antenv"' >> ~/.bashrc
echo '. antenv/bin/activate' >> ~/.bashrc
PYTHON_VERSION=$(python -c "import sys; print(str(sys.version_info.major) + '.' + str(sys.version_info.minor))")
echo "Using packages from virtual environment 'antenv' located at '$APP_PATH/antenv'."
export PYTHONPATH="$PYTHONPATH:$APP_PATH/antenv/lib/python$PYTHON_VERSION/site-packages"
echo "Updated PYTHONPATH to '$PYTHONPATH'"
. antenv/bin/activate
GUNICORN_CMD_ARGS="--timeout 600 --access-logfile '-' --error-logfile '-' -c /opt/startup/gunicorn.conf.py --chdir=$APP_PATH" gunicorn config.wsgi