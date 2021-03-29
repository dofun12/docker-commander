#!/bin/bash


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
touch docker-commander.service
cat > $DIR/docker-commander.service <<EOL
[Unit]
Description=Simple docker dashboard server

[Service]
Restart=always
User=kevim
WorkingDirectory=${DIR}
ExecStart=pipenv run python main.py >> ${DIR}/log.txt 2>&1

[Install]
WantedBy=multi-user.target
EOL

sudo cp docker-commander.service /lib/systemd/system/
sudo systemctl daemon-reload
echo "USE: 'sudo service docker-commander' to Start"

