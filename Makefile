install:
	python3 -m pip install --upgrade pip &&\
		python3 -m pip install -r ./config/requirements.txt &&\
			pip3 install -r ./config/requirements.txt

install_raspberrypi:
	python3 -m pip install -r ./config/requirements_raspberrypi.txt &&\
		pip3 install -r ./config/requirements_raspberrypi.txt

lint:
	find . -type f -name "*.py" | xargs pylint 

bandit:
	bandit -r . --configfile ./config/bandit.yaml -f html -o static/reports/bandit_report.html -v

flake8:
	flake8

check:
	flake8
	find . -type f -name "*.py" | xargs pylint 
	bandit -r . --configfile ./config/bandit.yaml
