python-dev:
  pkg:
    - installed

python-dev:
  pkg:
    - python-virtualenv

python-dev:
  pkg:
    - python-pip

/home/vagrant/vagrant-demo/flask-venv:
  virtualenv.managed:
    - system_site_packages: False
    - requirements: /vagrant/requirements.txt

start-flask:
  cmd.run:
    - name: /home/vagrant/vagrant-demo/flask-venv/bin/gunicorn server-application:app
        --daemon
        --bind {{ pillar['flask-variables']['bind_adress'] }}
        {% if pillar['flask-variables']['debug'] %}--debug{% endif %}
        {% if pillar['flask-variables']['reloader'] %}--reload{% endif %}
        --pid /home/vagrant/vagrant-demo/PIDFILE
        --access-logfile /home/vagrant/vagrant-demo/access.log
        --error-logfile /home/vagrant/vagrant-demo/error.log
    - cwd: /vagrant
    - creates: /home/vagrant/vagrant-demo/PIDFILE