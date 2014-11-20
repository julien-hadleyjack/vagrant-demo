corepkgs:
   pkg.installed:
    - pkgs:
      - tmux
      - python-dev
      - python-virtualenv
      - python-pip

/home/vagrant/flask-venv:
  virtualenv.managed:
    - system_site_packages: False
    - requirements: /vagrant/requirements.txt

/vagrant/config.yaml:
  file.managed:
    - source: salt://flask-app/config.py
    - template: jinja

start-flask:
  cmd.run:
    - name: /home/vagrant/flask-venv/bin/python /vagrant/server-application.py